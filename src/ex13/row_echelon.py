from __future__ import annotations

from typing import TypeVar
from numbers import Number

from matrix import Matrix

T = TypeVar("T", bound = Number)


# small helper to decide zero
_EPS = 1e-10
ROUND = 7

def _is_zero(x: T) -> bool:
    try:
        return abs(x) < _EPS
    except TypeError:
        return x == 0


def row_echelon(mat: Matrix[T], decimals: int = ROUND) -> Matrix[T]:
    """
    Return the reduced row‑echelon of the matrix.

    Time complexity is O(m * n^2), where m is the number of rows and n is the number of columns.
    Memory complexity is O(m * n) for the output matrix.
    """
    m, n = mat.shape()

    # deep copy of the data so the input is left intact
    A = [row.copy() for row in (mat._m if hasattr(mat, "_m") else [[mat[r, c] for c in range(n)] for r in range(m)])]

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

    # Post‑processing: eliminate −0.0 and trim floating garbage
    if decimals is not None:
        fmt = lambda v: 0.0 if _is_zero(v) else round(float(v), decimals)
        for r in range(m):
            A[r] = [fmt(x) for x in A[r]]

    return Matrix(A)
