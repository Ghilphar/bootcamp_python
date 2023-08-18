from ScrapBooker import ScrapBooker
import numpy as np

spb = ScrapBooker()

arr1 = np.arange(0, 25).reshape(5, 5)
print(arr1)
arr1_transform = spb.crop(arr1, (3, 1), (1, 0))
print("Transform")

print(arr1_transform)

arr2 = np.array("A B C D E F G H I".split() * 6).reshape(-1, 9)
#print("A B C D E F G H I".split() * 6)
print(arr2)
arr2_transform = spb.thin(arr2, 3, 0)

print(arr2_transform, (arr2_transform.dtype))


arr3 = np.array([[1, 2, 3],[1, 2, 3],[1, 2, 3]])

arr3_tyransform = spb.juxtapose(arr3, 3, 1)
print(arr3)
print(arr3_tyransform)

