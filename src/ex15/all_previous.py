from __future__ import annotations

from typing import TypeVar
from numbers import Number
import math

from vector import Vector
from matrix import Matrix

T = TypeVar("T", bound = Number)
_EPS = 1e-10 # pivot tolerance for float inputs
ROUND = 7 # digits to round floats in row_echelon post-processing

def linear_combination(
    vectors: Sequence[Vector[T]],
    coefs: Sequence[T],
) -> Vector[T]:
    """
    Return the linear combination of a sequence of vectors with given coefficients.
    The result is a new Vector instance containing the sum of each vector scaled by its coefficient.

    Complexity
    ----------
    Time  : Θ(k·n) — each coordinate visited once per vector
    Memory: Θ(n) — one accumulator vector, no extra copies
    """
    if len(vectors) != len(coefs):
        raise ValueError("vectors and coefs must have the same length")
    if not vectors:
        raise ValueError("Input sequences must not be empty")

    dim = len(vectors[0])
    if any(len(v) != dim for v in vectors):
        raise ValueError("All vectors must have the same dimension")

    # build an all-zeros accumulator of the right numeric type
    zero: T = coefs[0] - coefs[0] # zero of the same type as coefs
    acc = [zero] * dim

    # use fused multiply-add if available, otherwise do two separate ops
    # this is a CPython-specific optimization to reduce rounding errors
    # fma is a function that computes a * b + c in one step
    fma = getattr(math, "fma", None)  # fused multiply-add if CPython has it

    for a, u in zip(coefs, vectors):
        if fma is not None and isinstance(a, float):
            # fused multiply-add gives one rounding error instead of two
            for i in range(dim):
                acc[i] = fma(a, u[i], acc[i])
        else:
            for i in range(dim):
                acc[i] += a * u[i]

    return Vector(acc)


def lerp(u, v, t: float):
    """
    Linear interpolation between u and v with parameter t in [0,1].

    Time complexity  : Θ(n)   where n is the total number of coordinates
    Space complexity : Θ(n)   one new object of the same type as the inputs
    """
    if not (0.0 <= t <= 1.0):
        raise ValueError("t must be in the closed interval [0, 1]")
    if type(u) is not type(v):
        raise ValueError("u and v must be of the same type")

    # numbers
    if isinstance(u, Number):
        # fma when possible: (1 - t) * u + t * v  ==  u + t * (v - u)
        if isinstance(u, float) and hasattr(math, "fma"):
            return math.fma(t, v - u, u)
        return u + t * (v - u)

    # vector or matrix
    if isinstance(u, (Vector, Matrix)):
        return u + t * (v - u)

    # other types are not supported in this exercise
    raise TypeError(f"Unsupported type: {type(u).__name__}")


def dot(u: Vector[T], v: Vector[T]) -> T:
    """Return the dot product ⟨u|v⟩ of two same‑size vectors.

    Time complexity  : Θ(n)   (coordinates)
    Space complexity : Θ(1)   (single accumulator)
    """
    if len(u) != len(v):
        raise ValueError("Vector size mismatch in dot product")

    # Zero of the right numeric type
    zero: T = u[0] - u[0] if u else v[0] - v[0]

    total: T = zero
    fma = getattr(math, "fma", None)

    # Fused multiply‑add for floats
    if fma is not None and all(isinstance(x, float) for x in (*u, *v)):
        for a, b in zip(u, v):
            total = fma(a, b, total)
    else:
        for a, b in zip(u, v):
            a2 = a.conjugate() if hasattr(a, "conjugate") else a # handle complex numbers
            total += a2 * b

    return total


def norm1(v: Vector[T]) -> float:
    """Return the Manhattan norm (sum of |vi|) of v.

    Complexity: Θ(n) time, O(1) extra space.
    """
    return float(sum(abs(x) for x in v))


def norm2(v: Vector[T]) -> float:
    """Return the Euclidean norm (root of sum of squares) of v.

    Complexity: Θ(n) time, O(1) extra space.
    """
    total = 0.0
    fma = getattr(math, "fma", None)
    if fma is not None:
        for x in v:
            total = fma(x, x, total)
    else:
        for x in v:
            total += abs(x) ** 2
    return math.sqrt(total)


def norm_inf(v: Vector[T]) -> float:
    """Return the supremum norm (max of vi) of v.

    Complexity: Θ(n) time, O(1) extra space.
    """
    return float(max((abs(x) for x in v), default = 0.0))


def angle_cos(u: Vector[T], v: Vector[T]) -> float:
    """Return a real-valued cosine. Over ℂ, uses Re(⟨u|v⟩)/(‖u‖₂‖v‖₂).

    Time complexity: Θ(n) (coordinates)
    Space complexity: Θ(1) (single accumulator)
    """
    if len(u) != len(v):
        raise ValueError("Vectors must have identical dimensions")

    num = dot(u, v) # ⟨u|v⟩
    du = norm2(u) # ‖u‖₂
    dv = norm2(v) # ‖v‖₂

    if du == 0.0 or dv == 0.0:
        raise ValueError("Cosine undefined for zero‑length vector(s)")

    num_real = float(getattr(num, "real", num)) # handle complex numbers. getattr(object, attribute, default)
    return num_real / (du * dv)


def cross_product(u: Vector[T], v: Vector[T]) -> Vector[T]:
    """Return the 3‑D cross product u × v.

    Time complexity: Θ(1)   (a constant 9 multiplies/adds)
    Space complexity: Θ(1)   (one new 3‑element Vector)
    """
    if len(u) != 3 or len(v) != 3:
        raise ValueError("Cross product is only defined for 3‑D vectors")

    ux, uy, uz = u[0], u[1], u[2]
    vx, vy, vz = v[0], v[1], v[2]

    fma = getattr(math, "fma", None)

    if fma is not None and all(isinstance(x, float) for x in (ux, uy, uz, vx, vy, vz)):
        cx = fma(uy, vz, -uz * vy)   # uy*vz − uz*vy
        cy = fma(uz, vx, -ux * vz)   # uz*vx − ux*vz
        cz = fma(ux, vy, -uy * vx)   # ux*vy − uy*vx
    else:
        cx = uy * vz - uz * vy
        cy = uz * vx - ux * vz
        cz = ux * vy - uy * vx

    return Vector([cx, cy, cz])


def mat_vec_mul(mat: Matrix[T], u: Vector[T]) -> Vector[T]:
    """Return the matrix–vector product A·u.

    Time complexity  : O(nm)   (n=rows, m=cols)
    Space complexity : O(m)    (m=rows, result vector)
    """
    m, n = mat.shape()
    if m == 0 or n == 0:
        raise ValueError("Matrix cannot be empty")
    if len(u) != n:
        raise ValueError("Dimension mismatch in matrix–vector product")

    fma = getattr(math, "fma", None)
    zero: T = u[0] - u[0]
    out = []

    for row in mat._m:  # direct row access, no column cache
        if fma is not None and all(isinstance(x, float) for x in (*row, *u)):
            acc = 0.0
            for a, b in zip(row, u):
                acc = fma(a, b, acc)
        else:
            acc = zero
            for a, b in zip(row, u):
                acc += a * b
        out.append(acc)

    return Vector(out)


def mat_mat_mul(mat1: Matrix[T], mat2: Matrix[T]) -> Matrix[T]:
    """Return the matrix–matrix product A·B.

    Time complexity  : O(nmp)   (n=rows, m=cols, p=cols2)
    Space complexity : O(mp)    (m=rows, p=cols2, result matrix)
    """
    m, n = mat1.shape()
    n2, p = mat2.shape()
    if m == 0 or n == 0 or n2 == 0 or p == 0:
        raise ValueError("Matrices cannot be empty")
    if n != n2:
        raise ValueError("Inner dimensions do not match for A·B")

    fma = getattr(math, "fma", None)
    zero: T = mat1[0][0] - mat1[0][0]
    result = [[None] * p for _ in range(m)]

    # No column cache for no extra memory, just indexed access.
    for i, rowA in enumerate(mat1._m):
        for j in range(p):
            if fma is not None and all(isinstance(x, float) for x in (*rowA, *(mat2._m[k][j] for k in range(n)))):
                acc = 0.0
                for k, a in enumerate(rowA):
                    acc = fma(a, mat2._m[k][j], acc)
            else:
                acc = zero
                for k, a in enumerate(rowA):
                    acc += a * mat2._m[k][j]
            result[i][j] = acc

    return Matrix(result)


def trace(mat: Matrix[T]) -> T:
    """Return trace(mat) = sum of the diagonal elements.

    Time complexity: Θ(n), where n is the number of rows (or columns).
    Space complexity: Θ(1) extra space.
    """
    if not mat.is_square():
        raise ValueError("Matrix must be square")

    # Additive identity of the correct numeric type
    acc: T = mat[0][0] - mat[0][0]

    rows, _ = mat.shape()

    for i in range(rows):
        acc += mat[i][i]

    return acc


def transpose(mat: Matrix[T]) -> Matrix[T]:
    """Return the transpose matrix B = Aᵀ.

    Time complexity: Θ(n·m) (one assignment per entry)
    Space complexity: Θ(n·m) (the returned matrix)
    """
    rows, cols = mat.shape()

    data_t = [[mat[r, c] for r in range(rows)] for c in range(cols)]

    return Matrix(data_t)


def _is_zero(x: T) -> bool:
    try:
        return abs(x) < _EPS
    except TypeError:
        return x == 0


def row_echelon(mat: Matrix[T]) -> Matrix[T]:
    """
    Return the reduced row‑echelon of the matrix.

    Time complexity is O(m * n^2), where m is the number of rows and n is the number of columns.
    Memory complexity is O(m * n) for the output matrix.
    """
    m, n = mat.shape()

    # Deep copy
    A = [[mat[r, c] for c in range(n)] for r in range(m)]

    pivot_row = 0
    for col in range(n):
        # pivot search (first non‑zero at/below current row)
        pivot = next((r for r in range(pivot_row, m) if not _is_zero(A[r][col])), None)
        if pivot is None:
            continue # full column of zeros: skip

        # move pivot row up if needed
        if pivot != pivot_row:
            A[pivot_row], A[pivot] = A[pivot], A[pivot_row]

        # scale pivot row so leading entry is exactly 1
        pv = A[pivot_row][col]
        A[pivot_row] = [x / pv for x in A[pivot_row]]

        # eliminate ALL other rows
        for r in range(m):
            if r == pivot_row:
                continue
            factor = A[r][col]
            if _is_zero(factor):
                continue
            A[r] = [x - factor * y for x, y in zip(A[r], A[pivot_row])]

        pivot_row += 1
        if pivot_row == m:
            break

    return Matrix(A)


def determinant(mat: Matrix[T]) -> T:
    """Return det(mat) via Gaussian elimination with partial pivoting (make matrix upper triangular).

    Time complexity is O(n^3) for an n×n matrix.
    Memory complexity is O(n^2) for the matrix copy.
    """
    n_rows, n_cols = mat.shape()
    if n_rows != n_cols:
        raise ValueError("Determinant is defined only for square matrices")
    n = n_rows

    # Deep copy
    A = [[mat[r, c] for c in range(n)] for r in range(n)]

    det: T = 1 # multiplicative identity of generic type T
    sign = 1 # track row swaps
    zero: T = mat[0][0] - mat[0][0]  # zero of generic type T

    for col in range(n):
        # Partial pivot: find row with largest |pivot|
        pivot_row = max(range(col, n), key=lambda r: abs(A[r][col]))
        pivot_val = A[pivot_row][col]

        # If pivot is ‘zero’, determinant is zero
        try:
            is_zero = abs(pivot_val) < _EPS
        except TypeError:  # non-float
            is_zero = pivot_val == 0
        if is_zero:
            return det * zero  # correct zero of type T

        # Row swap if needed
        if pivot_row != col:
            A[col], A[pivot_row] = A[pivot_row], A[col]
            sign *= -1

        # Eliminate entries below the pivot
        for r in range(col + 1, n):
            factor = A[r][col] / pivot_val
            A[r][col] = zero
            for c in range(col + 1, n):
                A[r][c] -= factor * A[col][c]

        det *= pivot_val  # The determinant of an upper triangular matrix is the product of the diagonal elements.

    return det * sign


def inverse(mat: Matrix[T]) -> Matrix[T]:
    """Return the inverse of matrix.

    Time complexity: O(n^3) where n is the number of rows/columns in the matrix.
    Space complexity: O(n^2) for the augmented matrix.
    """
    n_rows, n_cols = mat.shape()
    if n_rows != n_cols:
        raise ValueError("Inverse exists only for square matrices")
    n = n_rows

    # Build the augmented matrix [A | I]
    A = [[mat[r, c] for c in range(n)] for r in range(n)]
    I = [[mat[0, 0] - mat[0, 0] for _ in range(n)] for _ in range(n)]  # zero matrix of type T
    for i in range(n):
        I[i][i] = I[i][i] + 1
    aug = [A[i] + I[i] for i in range(n)]  # each row: A | I

    # Gauss–Jordan elimination
    pivot_row = 0
    for col in range(n):
        # pivot search
        pivot = next((r for r in range(pivot_row, n) if not _is_zero(aug[r][col])), None)
        if pivot is None:
            raise ValueError("Matrix is singular (zero pivot)")
        # swap
        if pivot != pivot_row:
            aug[pivot_row], aug[pivot] = aug[pivot], aug[pivot_row]
        # scale pivot row
        pv = aug[pivot_row][col]
        scale = [x / pv for x in aug[pivot_row]]
        aug[pivot_row] = scale
        # eliminate other rows
        for r in range(n):
            if r == pivot_row:
                continue
            factor = aug[r][col]
            if _is_zero(factor):
                continue
            aug[r] = [x - factor * y for x, y in zip(aug[r], aug[pivot_row])]
        pivot_row += 1
    # Extract inverse from right half
    inv_data = [row[n:] for row in aug]

    return Matrix(inv_data)

def _is_zero_scalar(x: T) -> bool:
    """Zero‑test"""
    try:
        return abs(x) < _EPS
    except TypeError:  # non‑abs‑supporting types (e.g. Fractions)
        return x == 0

def rank(mat: Matrix[T]) -> int:
    """Return the rank of matrix. Rank is the number of non‑zero rows in the row‑echelon form.

    Time complexity: O(n^3) for an n x n matrix.
    Space complexity: O(n^2) for an n x n matrix.
    """
    ref = row_echelon(mat)
    rows, cols = ref.shape()

    def is_zero_row(r: int) -> bool:
        return all(_is_zero_scalar(ref[r, c]) for c in range(cols))

    return sum(not is_zero_row(r) for r in range(rows))