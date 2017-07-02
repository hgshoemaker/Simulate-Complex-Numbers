# hiding info
# encapsulation
# inheritance
# polymorphism

# class: a collection of attributes that are defined for any object
# data members, methods

# mehods are
import math


def set_real(val):
    if type(val) not in (int, float):
        raise Exception('real part must be a number')


def set_image(val):
    if type(val) not in (int, float):
        raise Exception('imag part must be a number')


class Complex:
    """ this call simulates complex numbers"""

    def __init__(self, real=0, imag=0):
        self.__real = real
        self.__imag = imag
        if (type(real) not in (int, float)) or type(imag) not in (int, float):
            raise Exception('Args are not numbers')
        set_real(real)
        set_image(imag)

    def get_real(self):
        return self.__real

    def get_imag(self):
        return self.__imag

    def get_modulus(self):
        return math.sqrt(self.get_real() * self.get_real() + self.get_imag() * self.get_imag())

    def get_phi(self):
        return math.atan2(self.get_imag(), self.get_real())

    def __str__(self):
        return str(self.get_real()) + '+' + str(self.get_imag()) + 'i'

    def __add__(self, other):
        return Complex(self.get_real() + other.get_real(), self.get_imag() + other.get_imag())

    def __mul__(self, other):
        if type(other) in (int, float):
            return Complex(self.get_real() * other, self.get_imag() * other)
        else:
            return Complex(self.get_real() * self.get_real() - self.get_imag() * other.get_imag(),
                           self.get_imag() * other.get_imag() + self.get_real() * other.get_real())

    def __truediv__(self, other):
        if type(other) in (int, float):
            return Complex (self.get_real() / float(other), self.get_imag() / float(other))
        else:
            a, b, c, d = self.get_real(), self.get_imag(), other.get_real(), other.get_imag()
            nominator = c * c + d * d
            return Complex((a * c + b * d) / nominator, (b * c - a * d) / nominator)


aa = Complex(5, 0.3)
bb = Complex(-3, 4)
print(aa + bb)
print(aa * bb)
print(bb / 2)
