from __future__ import annotations

from typing import TypeVar
from numbers import Number
import math

from vector import Vector
from matrix import Matrix
from dot_product import dot

T = TypeVar("T", bound=Number)


def mat_vec_mul(mat: Matrix[T], u: Vector[T]) -> Vector[T]:
    """Return the matrix–vector product A·u.

    Time complexity  : O(nm)   (n=rows, m=cols)
    Space complexity : O(m)    (m=rows, result vector)
    """
    m, n = mat.shape()
    if len(u) != n:
        raise ValueError("Dimension mismatch in matrix–vector product")

    fma = getattr(math, "fma", None)
    out = []

    for row in mat._m:  # direct row access, no column cache
        if fma is not None and all(isinstance(x, float) for x in (*row, *u)):
            acc = 0.0
            for a, b in zip(row, u):
                acc = fma(a, b, acc)
        else:
            acc = 0
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
    if n != n2:
        raise ValueError("Inner dimensions do not match for A·B")

    fma = getattr(math, "fma", None)
    result = [[None] * p for _ in range(m)]

    # No column cache so no extra memory; just indexed access.
    for i, rowA in enumerate(mat1._m):
        for j in range(p):
            if fma is not None and all(isinstance(x, float) for x in (*rowA, *(mat2._m[k][j] for k in range(n)))):
                acc = 0.0
                for k, a in enumerate(rowA):
                    acc = fma(a, mat2._m[k][j], acc)
            else:
                acc = 0
                for k, a in enumerate(rowA):
                    acc += a * mat2._m[k][j]
            result[i][j] = acc

    return Matrix(result)