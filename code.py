# --------------
import pandas as pd
import numpy as np
import math
class complex_numbers:
    def __init__(self,x,y):
        self.real = x
        self.imag = y

    def __repr__(self):
        if self.real == 0.0 and self.imag == 0.0:
            return "0.00"
        if self.real == 0:
            return "%.2fi" % self.imag
        if self.imag == 0:
            return "%.2f" % self.real
        return "%.2f %s %.2fi" % (self.real, "+" if self.imag >= 0 else "-", abs(self.imag))
    def __add__(self,other):
        self.r = self.real + other.real
        self.i = self.imag + other.imag
        return complex_numbers(self.r,self.i)
    def __sub__(self,other):
        self.r = self.real - other.real
        self.i = self.imag - other.imag
        return complex_numbers(self.r,self.i)
    def __mul__(self,other):
        if(other.imag==0):
            self.r = (self.real * other.real)
            self.i = (self.imag * other.real)
            return complex_numbers(self.r,self.i)
        else:
            self.r = (self.real * other.real)-(self.imag * other.imag)
            self.i = (self.imag * other.real)+(self.real * other.imag)
            return complex_numbers(self.r,self.i)
        
    def __truediv__(self,other):
        self.r = ((self.real * other.real)+(self.imag * other.imag))/(math.pow(other.real,2)+math.pow(other.imag,2))
        self.i = ((self.imag * other.real)-(self.real * other.imag))/(math.pow(other.real,2)+math.pow(other.imag,2))
        return complex_numbers(self.r,self.i)

    def absolute(self):
        self.abb = math.sqrt(math.pow(self.real,2)+math.pow(self.imag,2))
        return self.abb
    
    def argument(self):
        self.arg = math.degrees(math.atan2(self.imag,self.real))
        return self.arg
    
    def conjugate(self):
        self.r = self.real
        self.i = -self.imag
        return complex_numbers(self.r,self.i)
comp_1 = complex_numbers(3,5)
comp_2 = complex_numbers(4,4)

comp_sum = complex_numbers.__add__(comp_1,comp_2)
comp_diff = complex_numbers.__sub__(comp_1,comp_2)
comp_prod = complex_numbers.__mul__(comp_1,comp_2)
comp_quot = complex_numbers.__truediv__(comp_1,comp_2)
comp_abs = complex_numbers.absolute(comp_1)
comp_conj = complex_numbers.conjugate(comp_1)
comp_arg = complex_numbers.argument(comp_1)

print(comp_1,comp_2,comp_sum,comp_diff,comp_prod,comp_quot,comp_abs,comp_conj,comp_arg,comp_arg)
print(comp_1)




