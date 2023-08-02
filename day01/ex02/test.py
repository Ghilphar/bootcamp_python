import numpy as np
from vector import Vector


# Column vector of shape (n, 1)
print("\nMy result")

print(Vector([[0.0], [1.0], [2.0], [3.0]]).shape)
print("Expected output")
print("(4, 1)")
print("\nMy result")

print(Vector([[0.0], [1.0], [2.0], [3.0]]).values)
print("Expected output")
print("[[0.0], [1.0], [2.0], [3.0]]")
# Row vector of shape (1, n)
print("\nMy result")

print(Vector([[0.0, 1.0, 2.0, 3.0]]).shape)
print("Expected output")
print("(1, 4)")
print("\nMy result")

print(Vector([[0.0, 1.0, 2.0, 3.0]]).values)
print("Expected output")
print("[[0.0, 1.0, 2.0, 3.0]]")

print("Example 1:") 

# Example 1:
v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
print("\nMy result")

print(v1.shape)
print("Expected output")
print("(4, 1)")
print("\nMy result")

print(v1.T())
print("Expected output")
print("Vector([[0.0, 1.0, 2.0, 3.0]])")
print("\nMy result")

print(v1.T().shape)
print("Expected output")
print("(1,4)")

print("\nExample 2:") 
# Example 2:
v2 = Vector([[0.0, 1.0, 2.0, 3.0]])
print("\nMy result")

print(v2.shape)
print("Expected output")
print("(1,4)")
print("\nMy result")

print(v2.T())
print("Expected output")
print("Vector([[0.0], [1.0], [2.0], [3.0]])")
print("\nMy result")

print(v2.T().shape)
print("Expected output")
print("(4,1)")


print("\nExample 3:")

# Example 3:
v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
v2 = Vector([[2.0], [1.5], [2.25], [4.0]])

print("\nMy result :")
print(v1.dot(v2))
print("Expected output: 18.0")
v3 = Vector([[1.0, 3.0]])
v4 = Vector([[2.0, 4.0]])
print("\nMy result :")
print(v3.dot(v4))
print("Expected output: 14.0")

print("The dot function is the sum of multiplication of each element of vector A" \
      + " by each element of vector B : " \
      + "A ⋅ B = A1B1 + A2B2 + A3B3" \
      + "\n1 * 2 + 3 * 4 = 2 + 12 = 14")

v1 = Vector([[0.0, 1.0, 2.0, 3.0]])

print("\nMy result")
v1
print("Expected output")
# Expected output: to see what __repr__() should do
print("[[0.0, 1.0, 2.0, 3.0]]")

print("\nMy result")
print(v1)
# Expected output: to see what __str__() should do
print("[[0.0, 1.0, 2.0, 3.0]]")
print("\n")
print("\nMy tests\n")

vn3 = Vector(3)
print(vn3)

vrange = Vector((10,16)) 
print(vrange)

# Vector initialization
v1 = Vector([[1.0], [2.0], [3.0]])
np_v1 = np.array([1.0, 2.0, 3.0]).reshape(-1, 1)

assert v1.values == np_v1.tolist()

# Scalar multiplication
v2 = v1 * 5
np_v2 = np_v1 * 5

assert v2.values == np_v2.tolist()

# Scalar division
v3 = v1 / 2.0
np_v3 = np_v1 / 2.0

assert v3.values == np_v3.tolist()

# Transpose
v4 = v1.T()
np_v4 = np_v1.T

assert v4.values == np_v4.tolist()

# Dot product
v5 = Vector([[1.0, 2.0, 3.0]])
np_v5 = np.array([1.0, 2.0, 3.0])

assert v5.dot(v5) == np_v5.dot(np_v5)

print("All tests passed!")
