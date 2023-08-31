import numpy as np
from ScrapBooker import ScrapBooker
spb = ScrapBooker()
arr1 = np.arange(0,25).reshape(5,5)
#print(arr1)
print(spb.crop(arr1, (3,1),(1,0)))

arr2 = np.array("A B C D E F G H I".split() * 6).reshape(-1,9)
#print(arr2)
print(f"array({spb.thin(arr2,3,0)}, {arr2.dtype})")

arr3 = np.array([[var] * 10 for var in "ABCDEFG"])
#print(arr3)
print(f"{spb.thin(arr3,3,1)}, dtype={arr3.dtype}")

arr4 = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])
print(f"array({spb.juxtapose(arr4, 2, 0)})")


not_numpy_arr = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
print(spb.crop(not_numpy_arr, (1,2)))
print(spb.juxtapose(arr4, -2, 0))
print(spb.mosaic(arr4, (1, 2, 3)))