import numpy as np
from vector import Vector
#
#
## Column vector of shape (n, 1)
#
#print("START Test shape (n,1) comuln vector:")
#print("\nMy result")
#
#print(Vector([[0.0], [1.0], [2.0], [3.0]]).shape)
#print("Expected output")
#print("(4, 1)")
#
#print("START Test values (n,1) comuln vector:")
#print("\nMy result")
#print(Vector([[0.0], [1.0], [2.0], [3.0]]).values)
#print("Expected output")
#print("[[0.0], [1.0], [2.0], [3.0]]")
#
## Row vector of shape (1, n)
#print("START Test shapes (1, n) row vector:")
#print("\nMy result")
#print(Vector([[0.0, 1.0, 2.0, 3.0]]).shape)
#print("Expected output")
#print("(1, 4)")
#
#print("START Test values (1, n) row vector:")
#print("\nMy result")
#print(Vector([[0.0, 1.0, 2.0, 3.0]]).values)
#print("Expected output")
#print("[[0.0, 1.0, 2.0, 3.0]]")
#
#print("END Preliminars")
#
#print("START Example 1:") 
## Example 1:
#print("Vector([[0.0], [1.0], [2.0], [3.0]])")
#v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
#print("Shape")
#print("\nMy result")
#print(v1.shape)
#print("Expected output")
#print("(4, 1)")
#
#print("Print Transpose vector")
#print("before Transpose : " )
#print(v1.values)
#print("\nMy result after transpose")
#print(v1.T())
#print("Expected output")
#print("Vector([[0.0, 1.0, 2.0, 3.0]])")
#
#print("new shape")
#print("\nMy result")
#print(v1.T().shape)
#print("Expected output")
#print("(1,4)")
#
## Example 2:
#print("\nSTART Example 2:") 
#
#print("Shape vector 1, n:")
#v2 = Vector([[0.0, 1.0, 2.0, 3.0]])
#print("\n Print shape vector 2v. My result")
#print(v2.shape)
#print("Expected output")
#print("(1,4)")
#
#print("Start test: .T() , transpose vector.")
#print("before ", v2.values)
#print("\nMy result after transpose of vector v2")
#print(v2.T())
#print("Expected output")
#print("Vector([[0.0], [1.0], [2.0], [3.0]])")
#print("\nMy result shape v2 after transpose")
#print(v2.T().shape)
#print("Expected output")
#print("(4,1)")
#
#
#
#print("\nExample 3 : (dot operation: multiplication des valeurs de deux vecteurs de meme shape (1,n = row) (n,1 = column))")
#
## Example 3:
#v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
#v2 = Vector([[2.0], [1.5], [2.25], [4.0]])
#print("vector v1 = ", v1.values)
#print("vector v2 = ", v2.values)
#print("\nMy result after dot function :")
#print(v1.dot(v2))
#print("Expected output: 18.0")
#
##v3 = Vector([[1.0, 3.0]])
##v4 = Vector([[2.0, 4.0]])
##print("\nMy result :")
##print(v3.dot(v4))
##print("Expected output: 14.0")
##
##print("The dot function is the sum of multiplication of each element of vector A" \
##      + " by each element of vector B : " \
##      + "A ⋅ B = A1B1 + A2B2 + A3B3" \
##      + "\n1 * 2 + 3 * 4 = 2 + 12 = 14")
#
#v1 = Vector([[0.0, 1.0, 2.0, 3.0]])
#
#print("\nMy result for print vector (__repr__(v1))")
#print(v1.__repr__())
#print("Expected output")
## Expected output: to see what __repr__() should do
#print("[[0.0, 1.0, 2.0, 3.0]]")
#
#print("\nMy result for print(v1)")
#print(v1)
## Expected output: to see what __str__() should do
#print("[[0.0, 1.0, 2.0, 3.0]]")
#print("\n")
#print("\nMy tests\n")
#
#vn3 = Vector(3)
#print(vn3)
#
#vrange = Vector((10,16)) 
#print(vrange)

# Vector initialization

print("Initialize vector one with my class one with numpy")
v1 = Vector([[1.0], [2.0], [3.0]])
np_v1 = np.array([[1.0], [2.0], [3.0]])
#np_v1 = np.array([1.0, 2.0, 3.0]).reshape(-1, 1)


print("Test .tolist() vs values")
assert v1.values == np_v1.tolist()
print("PASS")

# Scalar multiplication
print("Test scalar multiplication (vector and scalar).")
v2 = v1 * 5
np_v2 = np_v1 * 5

assert v2.values == np_v2.tolist()
print("PASS")

print("Test scalar multiplication (scalar and vector).")
v2 = 5 * v1
np_v2 = 5 * np_v1

assert v2.values == np_v2.tolist()
print("PASS")

# Scalar division

print("Test scalar division (vector and scalar).")

v3 = v1 / 2.0
np_v3 = np_v1 / 2.0

assert v3.values == np_v3.tolist()
print("PASS")


# print("Test scalar division (scalar and vector).")
# 
# v3 = 2.0 / v1
# np_v3 = 2.0 / np_v1
# 
# assert v3.values == np_v3.tolist()
# print("PASS")

# Transpose

v4 = v1.T()
np_v4 = np_v1.T

print("TEST transpose")
assert v4.values == np_v4.tolist()
print("PASS")

# Dot product
v5 = Vector([[1.0, 2.0, 3.0]])
np_v5 = np.array([1.0, 2.0, 3.0])

print("TEST Dot product")
assert v5.dot(v5) == np_v5.dot(np_v5)
print("PASS")
print("All tests passed!")