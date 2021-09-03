
import tensorflow as tf
import keras
import sympy
from sympy import *

x = Symbol('x')
f = x**2 + x**3 + 1
f = f.diff(x)
print(f) 
