from __future__ import annotations
from dataclasses import dataclass
from numbers import Complex as ABCComplex
import math

@dataclass(frozen=True)
class Complex:
    re: float
    im: float = 0.0


    @property
    def real(self) -> float: return self.re
    @property
    def imag(self) -> float: return self.im

    def conjugate(self) -> "Complex":
        return Complex(self.re, -self.im)

    # arithmetic
    def __add__(self, other):
        o = _coerce(other)
        return Complex(self.re + o.re, self.im + o.im)
    __radd__ = __add__

    def __sub__(self, other):
        o = _coerce(other)
        return Complex(self.re - o.re, self.im - o.im)
    def __rsub__(self, other):
        o = _coerce(other)
        return Complex(o.re - self.re, o.im - self.im)

    def __mul__(self, other):
        o = _coerce(other)
        return Complex(self.re * o.re - self.im * o.im, self.re * o.im + self.im * o.re)
    __rmul__ = __mul__

    def __truediv__(self, other):
        o = _coerce(other)
        denom = o.re * o.re + o.im * o.im
        if denom == 0.0:
            raise ZeroDivisionError("division by zero")
        return Complex((self.re * o.re + self.im * o.im) / denom,
                       (self.im * o.re - self.re * o.im) / denom)
    def __rtruediv__(self, other):
        return _coerce(other).__truediv__(self)

    def __neg__(self):
        return Complex(-self.re, -self.im)
    def __abs__(self):
        return (self.re ** 2 + self.im ** 2) ** 0.5

    def __repr__(self) -> str:
        sign = "+" if self.im >= 0 else "-"
        im_part = f"{abs(self.im)}" if abs(self.im) != 1 else ""
        return f"({self.re} {sign} {im_part}i)"

def _coerce(x) -> Complex:
    """
    Coerce x to Complex if possible.

    @param x: An int, float, complex, or Complex instance.
    @return: A Complex instance or NotImplemented.
    """
    if isinstance(x, Complex): return x
    if isinstance(x, (int, float)): return Complex(float(x), 0.0)
    if isinstance(x, complex): return Complex(x.real, x.imag)
    return NotImplemented

# Make isinstance(z, numbers.Number) true:
ABCComplex.register(Complex)
