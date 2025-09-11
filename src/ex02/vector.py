from __future__ import annotations

from typing import TypeVar, Generic, Sequence, List, Iterable, TYPE_CHECKING
from numbers import Number

if TYPE_CHECKING:
    from matrix import Matrix

T = TypeVar('T', bound = Number)

class Vector(Generic[T]):
    def __init__(self, data: Sequence[T]) -> None:
        self._data: List[T] = list(data)

    # Helpers
    def __len__(self) -> int: return len(self._data)

    def __iter__(self) -> Iterable[T]: return iter(self._data)

    def __getitem__(self, i: int) -> T: return self._data[i]

    def __setitem__(self, i: int, value: T) -> None: self._data[i] = value

    def __repr__(self) -> str: return f"Vector({self._data})"

    def _check_same_size(self, other: "Vector[T]") -> None:
        if len(self) != len(other):
            raise ValueError("Vector size mismatch")

    def vector_to_matrix(self, rows: int, cols: int) -> Matrix[T]:
        """Reshape a 1‑D Vector into a `rows × cols` Matrix.

        Complexity: O(n) where *n=len(vec).
        """
        if rows * cols != len(self):
            raise ValueError("Total element count mismatch in reshape.")

        it = iter(self)
        return Matrix([[next(it) for _ in range(cols)] for _ in range(rows)])


    # Immutable operators
    def __add__(self, other: "Vector[T]") -> "Vector[T]":
        self._check_same_size(other)
        return Vector(a + b for a, b in zip(self, other))

    def __sub__(self, other: "Vector[T]") -> "Vector[T]":
        self._check_same_size(other)
        return Vector(a - b for a, b in zip(self, other))

    def __mul__(self, k: T) -> "Vector[T]":
        return Vector(k * x for x in self)
    __rmul__ = __mul__


    # Mutating operators
    def add(self, v: "Vector[T]") -> None:
        self._check_same_size(v)
        for i in range(len(self)): self[i] += v[i]

    def sub(self, v: "Vector[T]") -> None:
        self._check_same_size(v)
        for i in range(len(self)): self[i] -= v[i]

    def scl(self, k: T) -> None:
        for i in range(len(self)): self[i] *= k
