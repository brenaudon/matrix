from __future__ import annotations

from typing import Sequence, TypeVar
from numbers import Number
import math

from vector import Vector

T = TypeVar("T", bound = Number)


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
