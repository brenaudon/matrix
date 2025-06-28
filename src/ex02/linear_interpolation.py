from __future__ import annotations

from typing import TypeVar
from numbers import Number
import math

from vector import Vector
from matrix import Matrix

T = TypeVar("T", bound=Number)

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

    # plain numbers
    if isinstance(u, Number):
        # use fma when possible: (1-t)*u + t*v  ==  u + t*(v-u)
        if isinstance(u, float) and hasattr(math, "fma"):
            return math.fma(t, v - u, u)
        return u + t * (v - u)

    # vector or matrix
    if isinstance(u, (Vector, Matrix)):
        return u + t * (v - u)

    # other types are not supported in this exercise
    raise TypeError(f"Unsupported type: {type(u).__name__}")