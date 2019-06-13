Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 23:09:28) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 5+9
14
>>> 2*2
4
>>> 25/5
5.0
>>> 40/9
4.444444444444445
.
>>> 70-56
14
>>> 70-103
-33
>>> 40//9
4
>>> 503/2
251.5
>>> 251/2
125.5
>>> 125/2
62.5
>>> 62/2
31.0
>>> 503%2
1
>>> 251%2
1
>>> 125%2
1
>>> 62%2
0
>>> 31/2
15.5
>>> 31%2
1
>>> 2**8
256
>>> 2**111
2596148429267413814265248164610048
>>> 2**11
2048
>>> 64**4
16777216
>>> 64**(1/2)
8.0
>>> 27**(1/3)
3.0
>>> v = 74.54
>>> v
74.54
>>> t = 11
>>> t
11
>>> d = v * t
>>> d
819.94
>>> 'La distancia es: ' + d
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    'La distancia es: ' + d
TypeError: can only concatenate str (not "float") to str
>>> 'La distancia es: ' + str(d)
'La distancia es: 819.94'
>>> v = 70
>>> d
819.94
>>> d = v * t
>>> d
770
>>>  t = 17
SyntaxError: unexpected indent
>>> t = 17
>>> t
17
>>> d
770
>>> d = v * t
>>> d
1190
>>> 'La distancia es ' + str(d) + ' Km'
'La distancia es 1190 Km'
>>> 'La distancia recorrida es ' + str(d) + ' Km'
'La distancia recorrida es 1190 Km'
>>> x1 = 4
>>> y1 = 2
>>> x2 = 6
>>> y2 = -8
>>> d = ((x2-x1)**2 + (y2-y1)**2)**(1/2)
>>> d
10.198039027185569
>>> 'La distancia medida es ' + str(d) + ' cm.'
'La distancia medida es 10.198039027185569 cm.'
>>> 'La distancia medida es ' + str(round(d,2)) + ' cm.'
'La distancia medida es 10.2 cm.'
>>> 'La distancia medida es ' + str(round(d,3)) + ' cm.'
'La distancia medida es 10.198 cm.'
>>> help(math)
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    help(math)
NameError: name 'math' is not defined
>>> help(math)
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    help(math)
NameError: name 'math' is not defined
>>> help(math)
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    help(math)
NameError: name 'math' is not defined
>>> help 'math'
SyntaxError: invalid syntax
>>> help math
SyntaxError: invalid syntax
>>> help(math)
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    help(math)
NameError: name 'math' is not defined
>>> math import
SyntaxError: invalid syntax
>>> help('math')
Help on built-in module math:

NAME
    math

DESCRIPTION
    This module is always available.  It provides access to the
    mathematical functions defined by the C standard.

FUNCTIONS
    acos(x, /)
        Return the arc cosine (measured in radians) of x.
    
    acosh(x, /)
        Return the inverse hyperbolic cosine of x.
    
    asin(x, /)
        Return the arc sine (measured in radians) of x.
    
    asinh(x, /)
        Return the inverse hyperbolic sine of x.
    
    atan(x, /)
        Return the arc tangent (measured in radians) of x.
    
    atan2(y, x, /)
        Return the arc tangent (measured in radians) of y/x.
        
        Unlike atan(y/x), the signs of both x and y are considered.
    
    atanh(x, /)
        Return the inverse hyperbolic tangent of x.
    
    ceil(x, /)
        Return the ceiling of x as an Integral.
        
        This is the smallest integer >= x.
    
    copysign(x, y, /)
        Return a float with the magnitude (absolute value) of x but the sign of y.
        
        On platforms that support signed zeros, copysign(1.0, -0.0)
        returns -1.0.
    
    cos(x, /)
        Return the cosine of x (measured in radians).
    
    cosh(x, /)
        Return the hyperbolic cosine of x.
    
    degrees(x, /)
        Convert angle x from radians to degrees.
    
    erf(x, /)
        Error function at x.
    
    erfc(x, /)
        Complementary error function at x.
    
    exp(x, /)
        Return e raised to the power of x.
    
    expm1(x, /)
        Return exp(x)-1.
        
        This function avoids the loss of precision involved in the direct evaluation of exp(x)-1 for small x.
    
    fabs(x, /)
        Return the absolute value of the float x.
    
    factorial(x, /)
        Find x!.
        
        Raise a ValueError if x is negative or non-integral.
    
    floor(x, /)
        Return the floor of x as an Integral.
        
        This is the largest integer <= x.
    
    fmod(x, y, /)
        Return fmod(x, y), according to platform C.
        
        x % y may differ.
    
    frexp(x, /)
        Return the mantissa and exponent of x, as pair (m, e).
        
        m is a float and e is an int, such that x = m * 2.**e.
        If x is 0, m and e are both 0.  Else 0.5 <= abs(m) < 1.0.
    
    fsum(seq, /)
        Return an accurate floating point sum of values in the iterable seq.
        
        Assumes IEEE-754 floating point arithmetic.
    
    gamma(x, /)
        Gamma function at x.
    
    gcd(x, y, /)
        greatest common divisor of x and y
    
    hypot(x, y, /)
        Return the Euclidean distance, sqrt(x*x + y*y).
    
    isclose(a, b, *, rel_tol=1e-09, abs_tol=0.0)
        Determine whether two floating point numbers are close in value.
        
          rel_tol
            maximum difference for being considered "close", relative to the
            magnitude of the input values
          abs_tol
            maximum difference for being considered "close", regardless of the
            magnitude of the input values
        
        Return True if a is close in value to b, and False otherwise.
        
        For the values to be considered close, the difference between them
        must be smaller than at least one of the tolerances.
        
        -inf, inf and NaN behave similarly to the IEEE 754 Standard.  That
        is, NaN is not close to anything, even itself.  inf and -inf are
        only close to themselves.
    
    isfinite(x, /)
        Return True if x is neither an infinity nor a NaN, and False otherwise.
    
    isinf(x, /)
        Return True if x is a positive or negative infinity, and False otherwise.
    
    isnan(x, /)
        Return True if x is a NaN (not a number), and False otherwise.
    
    ldexp(x, i, /)
        Return x * (2**i).
        
        This is essentially the inverse of frexp().
    
    lgamma(x, /)
        Natural logarithm of absolute value of Gamma function at x.
    
    log(...)
        log(x, [base=math.e])
        Return the logarithm of x to the given base.
        
        If the base not specified, returns the natural logarithm (base e) of x.
    
    log10(x, /)
        Return the base 10 logarithm of x.
    
    log1p(x, /)
        Return the natural logarithm of 1+x (base e).
        
        The result is computed in a way which is accurate for x near zero.
    
    log2(x, /)
        Return the base 2 logarithm of x.
    
    modf(x, /)
        Return the fractional and integer parts of x.
        
        Both results carry the sign of x and are floats.
    
    pow(x, y, /)
        Return x**y (x to the power of y).
    
    radians(x, /)
        Convert angle x from degrees to radians.
    
    remainder(x, y, /)
        Difference between x and the closest integer multiple of y.
        
        Return x - n*y where n*y is the closest integer multiple of y.
        In the case where x is exactly halfway between two multiples of
        y, the nearest even value of n is used. The result is always exact.
    
    sin(x, /)
        Return the sine of x (measured in radians).
    
    sinh(x, /)
        Return the hyperbolic sine of x.
    
    sqrt(x, /)
        Return the square root of x.
    
    tan(x, /)
        Return the tangent of x (measured in radians).
    
    tanh(x, /)
        Return the hyperbolic tangent of x.
    
    trunc(x, /)
        Truncates the Real x to the nearest Integral toward 0.
        
        Uses the __trunc__ magic method.

DATA
    e = 2.718281828459045
    inf = inf
    nan = nan
    pi = 3.141592653589793
    tau = 6.283185307179586

FILE
    (built-in)


>>> x1
4
>>> x2
6
>>> y1
2
>>> y2
-8
>>> sqrt(16)
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    sqrt(16)
NameError: name 'sqrt' is not defined
>>> for math import sqrt
SyntaxError: invalid syntax
>>> from math import sqrt
>>> sqrt(16)
4.0
>>> pow(2,3)
8
>>> d = sqrt(pow(x2+x1)+pow(y2-y1))
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    d = sqrt(pow(x2+x1)+pow(y2-y1))
TypeError: pow expected at least 2 arguments, got 1
>>> d = sqrt(pow((x2+x1),2)+pow((y2-y1),2))
>>> d
14.142135623730951
>>> d = sqrt(pow((x2-x1),2)+pow((y2-y1),2))
>>> d
10.198039027185569
>>> 'La distancia medida es ' + str(round(d,2)) + ' cm.'
'La distancia medida es 10.2 cm.'
>>> angulo = 22
>>> c = 90
>>> a = c * sin(angulo)
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    a = c * sin(angulo)
NameError: name 'sin' is not defined
>>> from math import sin
>>> a = c * sin(angulo)
>>> a
-0.7966178361363488
>>> a = c * sin(radians(angulo))
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    a = c * sin(radians(angulo))
NameError: name 'radians' is not defined
>>> from math import radians
>>> a = c * sin(radians(angulo))
>>> a
33.71459340743208
>>> agl = degrees(asin(a/c))
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    agl = degrees(asin(a/c))
NameError: name 'degrees' is not defined
>>> from math import degrees
>>> agl = degrees(asin(a/c))
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    agl = degrees(asin(a/c))
NameError: name 'asin' is not defined
>>> from math import asin
>>> agl = degrees(asin(a/c))
>>> agl
22.0
>>> b
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    b
NameError: name 'b' is not defined
>>> c
90
>>> b = c * cos(radians(angulo))
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    b = c * cos(radians(angulo))
NameError: name 'cos' is not defined
>>> from math import cos
>>> b = c * cos(radians(angulo))
>>> b
83.44654691101087
>>> round(d,2)
10.2
>>> round(b,2)
83.45
>>> print('El valor de b es ', b)
El valor de b es  83.44654691101087
>>> print('El valor de b es ', str(b))
El valor de b es  83.44654691101087
>>> print('El valor de b es ', str(round(b,2)))
El valor de b es  83.45
>>> print('El valor de b es ', str(round(b,2))), ' cm.'
El valor de b es  83.45
(None, ' cm.')
>>> print('El valor de b es ' + str(round(b,2)) + ' cm.')
El valor de b es 83.45 cm.
>>> rint('El valor de b es ', str(round(b,2)), ' cm.')
Traceback (most recent call last):
  File "<pyshell#104>", line 1, in <module>
    rint('El valor de b es ', str(round(b,2)), ' cm.')
NameError: name 'rint' is not defined
>>> print('El valor de b es ', str(round(b,2)), ' cm.')
El valor de b es  83.45  cm.
>>> nombre = 'Beymar'
>>> ap = 'Jiménez'
>>> am = 'Ruiz'
>>> nombre
'Beymar'
>>> ap
'Jiménez'
>>> am
'Ruiz'
>>> nombre, ap, am
('Beymar', 'Jiménez', 'Ruiz')
>>> nombre + ap + am
'BeymarJiménezRuiz'
>>> nombre + ' ' + ap + ' ' + am
'Beymar Jiménez Ruiz'
>>> print(nombre + ' ' + ap + ' ' + am)
Beymar Jiménez Ruiz
>>> nombre[0]
'B'
>>> nombre[1]
'e'
>>> len(nombre)
6
>>> nombre[6]
Traceback (most recent call last):
  File "<pyshell#119>", line 1, in <module>
    nombre[6]
IndexError: string index out of range
>>> nombre[5]
'r'
>>> nombre[len(nombre)-1]
'r'
>>> nombre[-1]
'r'
>>> nombre[-2]
'a'
>>> nombre[-4]
'y'
>>> nombre[:3]
'Bey'
>>> nombre[3:]
'mar'
>>> nombre[2:4]
'ym'
>>> nombre[2:5]
'yma'
>>> help('arrays')
No Python documentation found for 'arrays'.
Use help() to get the interactive help utility.
Use help(str) for help on the str class.

>>> help('array')
Help on built-in module array:

NAME
    array

DESCRIPTION
    This module defines an object type which can efficiently represent
    an array of basic values: characters, integers, floating point
    numbers.  Arrays are sequence types and behave very much like lists,
    except that the type of objects stored in them is constrained.

CLASSES
    builtins.object
        array
    
    ArrayType = class array(builtins.object)
     |  array(typecode [, initializer]) -> array
     |  
     |  Return a new array whose items are restricted by typecode, and
     |  initialized from the optional initializer value, which must be a list,
     |  string or iterable over elements of the appropriate type.
     |  
     |  Arrays represent basic values and behave very much like lists, except
     |  the type of objects stored in them is constrained. The type is specified
     |  at object creation time by using a type code, which is a single character.
     |  The following type codes are defined:
     |  
     |      Type code   C Type             Minimum size in bytes 
     |      'b'         signed integer     1 
     |      'B'         unsigned integer   1 
     |      'u'         Unicode character  2 (see note) 
     |      'h'         signed integer     2 
     |      'H'         unsigned integer   2 
     |      'i'         signed integer     2 
     |      'I'         unsigned integer   2 
     |      'l'         signed integer     4 
     |      'L'         unsigned integer   4 
     |      'q'         signed integer     8 (see note) 
     |      'Q'         unsigned integer   8 (see note) 
     |      'f'         floating point     4 
     |      'd'         floating point     8 
     |  
     |  NOTE: The 'u' typecode corresponds to Python's unicode character. On 
     |  narrow builds this is 2-bytes on wide builds this is 4-bytes.
     |  
     |  NOTE: The 'q' and 'Q' type codes are only available if the platform 
     |  C compiler used to build Python supports 'long long', or, on Windows, 
     |  '__int64'.
     |  
     |  Methods:
     |  
     |  append() -- append a new item to the end of the array
     |  buffer_info() -- return information giving the current memory info
     |  byteswap() -- byteswap all the items of the array
     |  count() -- return number of occurrences of an object
     |  extend() -- extend array by appending multiple elements from an iterable
     |  fromfile() -- read items from a file object
     |  fromlist() -- append items from the list
     |  frombytes() -- append items from the string
     |  index() -- return index of first occurrence of an object
     |  insert() -- insert a new item into the array at a provided position
     |  pop() -- remove and return item (default last)
     |  remove() -- remove first occurrence of an object
     |  reverse() -- reverse the order of the items in the array
     |  tofile() -- write all items to a file object
     |  tolist() -- return the array converted to an ordinary list
     |  tobytes() -- return the array converted to a string
     |  
     |  Attributes:
     |  
     |  typecode -- the typecode character used to create the array
     |  itemsize -- the length in bytes of one array item
     |  
     |  Methods defined here:
     |  
     |  __add__(self, value, /)
     |      Return self+value.
     |  
     |  __contains__(self, key, /)
     |      Return key in self.
     |  
     |  __copy__(self, /)
     |      Return a copy of the array.
     |  
     |  __deepcopy__(self, unused, /)
     |      Return a copy of the array.
     |  
     |  __delitem__(self, key, /)
     |      Delete self[key].
     |  
     |  __eq__(self, value, /)
     |      Return self==value.
     |  
     |  __ge__(self, value, /)
     |      Return self>=value.
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __getitem__(self, key, /)
     |      Return self[key].
     |  
     |  __gt__(self, value, /)
     |      Return self>value.
     |  
     |  __iadd__(self, value, /)
     |      Implement self+=value.
     |  
     |  __imul__(self, value, /)
     |      Implement self*=value.
     |  
     |  __iter__(self, /)
     |      Implement iter(self).
     |  
     |  __le__(self, value, /)
     |      Return self<=value.
     |  
     |  __len__(self, /)
     |      Return len(self).
     |  
     |  __lt__(self, value, /)
     |      Return self<value.
     |  
     |  __mul__(self, value, /)
     |      Return self*value.
     |  
     |  __ne__(self, value, /)
     |      Return self!=value.
     |  
     |  __reduce_ex__(self, value, /)
     |      Return state information for pickling.
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __rmul__(self, value, /)
     |      Return value*self.
     |  
     |  __setitem__(self, key, value, /)
     |      Set self[key] to value.
     |  
     |  __sizeof__(self, /)
     |      Size of the array in memory, in bytes.
     |  
     |  append(self, v, /)
     |      Append new value v to the end of the array.
     |  
     |  buffer_info(self, /)
     |      Return a tuple (address, length) giving the current memory address and the length in items of the buffer used to hold array's contents.
     |      
     |      The length should be multiplied by the itemsize attribute to calculate
     |      the buffer length in bytes.
     |  
     |  byteswap(self, /)
     |      Byteswap all items of the array.
     |      
     |      If the items in the array are not 1, 2, 4, or 8 bytes in size, RuntimeError is
     |      raised.
     |  
     |  count(self, v, /)
     |      Return number of occurrences of v in the array.
     |  
     |  extend(self, bb, /)
     |      Append items to the end of the array.
     |  
     |  frombytes(self, buffer, /)
     |      Appends items from the string, interpreting it as an array of machine values, as if it had been read from a file using the fromfile() method).
     |  
     |  fromfile(self, f, n, /)
     |      Read n objects from the file object f and append them to the end of the array.
     |  
     |  fromlist(self, list, /)
     |      Append items to array from list.
     |  
     |  fromstring(self, buffer, /)
     |      Appends items from the string, interpreting it as an array of machine values, as if it had been read from a file using the fromfile() method).
     |      
     |      This method is deprecated. Use frombytes instead.
     |  
     |  fromunicode(self, ustr, /)
     |      Extends this array with data from the unicode string ustr.
     |      
     |      The array must be a unicode type array; otherwise a ValueError is raised.
     |      Use array.frombytes(ustr.encode(...)) to append Unicode data to an array of
     |      some other type.
     |  
     |  index(self, v, /)
     |      Return index of first occurrence of v in the array.
     |  
     |  insert(self, i, v, /)
     |      Insert a new item v into the array before position i.
     |  
     |  pop(self, i=-1, /)
     |      Return the i-th element and delete it from the array.
     |      
     |      i defaults to -1.
     |  
     |  remove(self, v, /)
     |      Remove the first occurrence of v in the array.
     |  
     |  reverse(self, /)
     |      Reverse the order of the items in the array.
     |  
     |  tobytes(self, /)
     |      Convert the array to an array of machine values and return the bytes representation.
     |  
     |  tofile(self, f, /)
     |      Write all items (as machine values) to the file object f.
     |  
     |  tolist(self, /)
     |      Convert array to an ordinary list with the same items.
     |  
     |  tostring(self, /)
     |      Convert the array to an array of machine values and return the bytes representation.
     |      
     |      This method is deprecated. Use tobytes instead.
     |  
     |  tounicode(self, /)
     |      Extends this array with data from the unicode string ustr.
     |      
     |      Convert the array to a unicode string.  The array must be a unicode type array;
     |      otherwise a ValueError is raised.  Use array.tobytes().decode() to obtain a
     |      unicode string from an array of some other type.
     |  
     |  ----------------------------------------------------------------------
     |  Static methods defined here:
     |  
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  itemsize
     |      the size, in bytes, of one array item
     |  
     |  typecode
     |      the typecode character used to create the array
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  __hash__ = None
    
    class array(builtins.object)
     |  array(typecode [, initializer]) -> array
     |  
     |  Return a new array whose items are restricted by typecode, and
     |  initialized from the optional initializer value, which must be a list,
     |  string or iterable over elements of the appropriate type.
     |  
     |  Arrays represent basic values and behave very much like lists, except
     |  the type of objects stored in them is constrained. The type is specified
     |  at object creation time by using a type code, which is a single character.
     |  The following type codes are defined:
     |  
     |      Type code   C Type             Minimum size in bytes 
     |      'b'         signed integer     1 
     |      'B'         unsigned integer   1 
     |      'u'         Unicode character  2 (see note) 
     |      'h'         signed integer     2 
     |      'H'         unsigned integer   2 
     |      'i'         signed integer     2 
     |      'I'         unsigned integer   2 
     |      'l'         signed integer     4 
     |      'L'         unsigned integer   4 
     |      'q'         signed integer     8 (see note) 
     |      'Q'         unsigned integer   8 (see note) 
     |      'f'         floating point     4 
     |      'd'         floating point     8 
     |  
     |  NOTE: The 'u' typecode corresponds to Python's unicode character. On 
     |  narrow builds this is 2-bytes on wide builds this is 4-bytes.
     |  
     |  NOTE: The 'q' and 'Q' type codes are only available if the platform 
     |  C compiler used to build Python supports 'long long', or, on Windows, 
     |  '__int64'.
     |  
     |  Methods:
     |  
     |  append() -- append a new item to the end of the array
     |  buffer_info() -- return information giving the current memory info
     |  byteswap() -- byteswap all the items of the array
     |  count() -- return number of occurrences of an object
     |  extend() -- extend array by appending multiple elements from an iterable
     |  fromfile() -- read items from a file object
     |  fromlist() -- append items from the list
     |  frombytes() -- append items from the string
     |  index() -- return index of first occurrence of an object
     |  insert() -- insert a new item into the array at a provided position
     |  pop() -- remove and return item (default last)
     |  remove() -- remove first occurrence of an object
     |  reverse() -- reverse the order of the items in the array
     |  tofile() -- write all items to a file object
     |  tolist() -- return the array converted to an ordinary list
     |  tobytes() -- return the array converted to a string
     |  
     |  Attributes:
     |  
     |  typecode -- the typecode character used to create the array
     |  itemsize -- the length in bytes of one array item
     |  
     |  Methods defined here:
     |  
     |  __add__(self, value, /)
     |      Return self+value.
     |  
     |  __contains__(self, key, /)
     |      Return key in self.
     |  
     |  __copy__(self, /)
     |      Return a copy of the array.
     |  
     |  __deepcopy__(self, unused, /)
     |      Return a copy of the array.
     |  
     |  __delitem__(self, key, /)
     |      Delete self[key].
     |  
     |  __eq__(self, value, /)
     |      Return self==value.
     |  
     |  __ge__(self, value, /)
     |      Return self>=value.
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __getitem__(self, key, /)
     |      Return self[key].
     |  
     |  __gt__(self, value, /)
     |      Return self>value.
     |  
     |  __iadd__(self, value, /)
     |      Implement self+=value.
     |  
     |  __imul__(self, value, /)
     |      Implement self*=value.
     |  
     |  __iter__(self, /)
     |      Implement iter(self).
     |  
     |  __le__(self, value, /)
     |      Return self<=value.
     |  
     |  __len__(self, /)
     |      Return len(self).
     |  
     |  __lt__(self, value, /)
     |      Return self<value.
     |  
     |  __mul__(self, value, /)
     |      Return self*value.
     |  
     |  __ne__(self, value, /)
     |      Return self!=value.
     |  
     |  __reduce_ex__(self, value, /)
     |      Return state information for pickling.
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __rmul__(self, value, /)
     |      Return value*self.
     |  
     |  __setitem__(self, key, value, /)
     |      Set self[key] to value.
     |  
     |  __sizeof__(self, /)
     |      Size of the array in memory, in bytes.
     |  
     |  append(self, v, /)
     |      Append new value v to the end of the array.
     |  
     |  buffer_info(self, /)
     |      Return a tuple (address, length) giving the current memory address and the length in items of the buffer used to hold array's contents.
     |      
     |      The length should be multiplied by the itemsize attribute to calculate
     |      the buffer length in bytes.
     |  
     |  byteswap(self, /)
     |      Byteswap all items of the array.
     |      
     |      If the items in the array are not 1, 2, 4, or 8 bytes in size, RuntimeError is
     |      raised.
     |  
     |  count(self, v, /)
     |      Return number of occurrences of v in the array.
     |  
     |  extend(self, bb, /)
     |      Append items to the end of the array.
     |  
     |  frombytes(self, buffer, /)
     |      Appends items from the string, interpreting it as an array of machine values, as if it had been read from a file using the fromfile() method).
     |  
     |  fromfile(self, f, n, /)
     |      Read n objects from the file object f and append them to the end of the array.
     |  
     |  fromlist(self, list, /)
     |      Append items to array from list.
     |  
     |  fromstring(self, buffer, /)
     |      Appends items from the string, interpreting it as an array of machine values, as if it had been read from a file using the fromfile() method).
     |      
     |      This method is deprecated. Use frombytes instead.
     |  
     |  fromunicode(self, ustr, /)
     |      Extends this array with data from the unicode string ustr.
     |      
     |      The array must be a unicode type array; otherwise a ValueError is raised.
     |      Use array.frombytes(ustr.encode(...)) to append Unicode data to an array of
     |      some other type.
     |  
     |  index(self, v, /)
     |      Return index of first occurrence of v in the array.
     |  
     |  insert(self, i, v, /)
     |      Insert a new item v into the array before position i.
     |  
     |  pop(self, i=-1, /)
     |      Return the i-th element and delete it from the array.
     |      
     |      i defaults to -1.
     |  
     |  remove(self, v, /)
     |      Remove the first occurrence of v in the array.
     |  
     |  reverse(self, /)
     |      Reverse the order of the items in the array.
     |  
     |  tobytes(self, /)
     |      Convert the array to an array of machine values and return the bytes representation.
     |  
     |  tofile(self, f, /)
     |      Write all items (as machine values) to the file object f.
     |  
     |  tolist(self, /)
     |      Convert array to an ordinary list with the same items.
     |  
     |  tostring(self, /)
     |      Convert the array to an array of machine values and return the bytes representation.
     |      
     |      This method is deprecated. Use tobytes instead.
     |  
     |  tounicode(self, /)
     |      Extends this array with data from the unicode string ustr.
     |      
     |      Convert the array to a unicode string.  The array must be a unicode type array;
     |      otherwise a ValueError is raised.  Use array.tobytes().decode() to obtain a
     |      unicode string from an array of some other type.
     |  
     |  ----------------------------------------------------------------------
     |  Static methods defined here:
     |  
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  itemsize
     |      the size, in bytes, of one array item
     |  
     |  typecode
     |      the typecode character used to create the array
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  __hash__ = None

DATA
    typecodes = 'bBuhHiIlLqQfd'

FILE
    (built-in)


>>> 
