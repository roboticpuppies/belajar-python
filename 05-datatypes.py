"""
Text Type           :	str
Numeric Types       :	int, float, complex
Sequence Types      :	list, tuple, range
Mapping Type        :	dict
Set Types           :	set, frozenset
Boolean Type        :	bool
Binary Types        :	bytes, bytearray, memoryview
None Type           :	NoneType
"""

x = "Hello World"                               # str
x = 20                                          # int
x = 20.5                                        # float
x = 1j                                          # complex
x = ["apple", "banana", "cherry"]               # List
x = ("apple", "banana", "cherry")               # Tuple
x = range(6)                                    # Range
x = {"name" : "John", "age" : 36}               # Dict
x = {"apple", "banana", "cherry"}               # Set
x = frozenset({"apple", "banana", "cherry"})    # frozenset
x = True                                        # bool	
x = b"Hello"                                    # bytes	
x = bytearray(5)                                # bytearray	
x = memoryview(bytes(5))                        # memoryview	
x = None                                        # NoneType

# Conversion
x = 1    # int
y = 2.8  # float

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

# You cannot convert complex numbers into another number type