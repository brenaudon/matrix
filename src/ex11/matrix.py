from __future__ import annotations

from typing import TypeVar, Generic, Sequence, List
from numbers import Number

T = TypeVar('T', bound=Number)


class Matrix(Generic[T]):

    def __init__(self, rows: Sequence[Sequence[T]]) -> None:
        if not rows: # 0×0 not allowed
            raise ValueError("Matrix cannot be empty")
        row_lengths = {len(r) for r in rows}
        if len(row_lengths) != 1:
            raise ValueError("All rows must have the same length")
        self._m: List[List[T]] = [list(r) for r in rows]
        self._shape = (len(rows), len(rows[0])) # (rows, cols)


    # Helpers
    def __len__(self) -> int: return self._shape[0]  # nb rows

    def shape(self) -> tuple[int, int]: return self._shape

    def __getitem__(self, rc): # m[i][j] style access
        r, c = rc
        return self._m[r][c]

    def __setitem__(self, rc, value: T) -> None:
        r, c = rc
        self._m[r][c] = value

    def __repr__(self) -> str:
        return "Matrix([" + ",\n        ".join(map(str, self._m)) + "])"

    def _check_same_shape(self, other: "Matrix[T]") -> None:
        if self._shape != other._shape:
            raise ValueError("Matrix shape mismatch")

    def is_square(self) -> bool:
        """Return True if matrix is square."""
        rows, cols = self.shape()
        return rows == cols


    # Immutable operators
    def __add__(self, other: "Matrix[T]") -> "Matrix[T]":
        self._check_same_shape(other)
        return Matrix([[a + b for a, b in zip(r1, r2)]
                       for r1, r2 in zip(self._m, other._m)])

    def __sub__(self, other: "Matrix[T]") -> "Matrix[T]":
        self._check_same_shape(other)
        return Matrix([[a - b for a, b in zip(r1, r2)]
                       for r1, r2 in zip(self._m, other._m)])

    def __mul__(self, k: T) -> "Matrix[T]":
        return Matrix([[k * x for x in row] for row in self._m])
    __rmul__ = __mul__


    # Mutating operators
    def add(self, m: "Matrix[T]") -> None:
        self._check_same_shape(m)
        for i in range(self._shape[0]):
            for j in range(self._shape[1]):
                self._m[i][j] += m._m[i][j]

    def sub(self, m: "Matrix[T]") -> None:
        self._check_same_shape(m)
        for i in range(self._shape[0]):
            for j in range(self._shape[1]):
                self._m[i][j] -= m._m[i][j]

    def scl(self, k: T) -> None:
        for i in range(self._shape[0]):
            for j in range(self._shape[1]):
                self._m[i][j] *= k