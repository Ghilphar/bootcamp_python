from NumPyCreator import NumPyCreator
npc = NumPyCreator()
#import numpy as np

arr = npc.from_list([[],[]])

print(f'array({arr}, shape={arr.shape}, dtype={arr.dtype})')
arr2 = npc.from_list([[1,2,3],[6,3,4],[8,5,6]])
print(arr2)

arr3 = npc.from_tuple(("a","b","c"))
print(f"array({arr3}, dtype={arr3.dtype})")

arr4 = npc.from_iterable(range(5))
print(f"array({arr4})") 

#arr = np.array([0, 1, 2, 3, 4])
#print(arr)
#print("array(" + str(list(arr4)) + ")")

arr5 = npc.from_shape((0, 0))
print(f'array({arr5}, shape={arr5.shape}, dtype={arr5.dtype})')

arr6 = npc.from_shape((3, 5))
print(f"array({arr6})")

arr7 = npc.random((3, 5))
print(f"array({arr7})")


arr8 = npc.identity(4)
print(f"array({arr8})")

print(npc.from_list("toto"))
print(npc.from_list([[1,2,3],[6,3,4],[8,5,6,7]]))
print(npc.from_tuple(3.2))
print(npc.from_tuple(((1,5,8),(7,5))))
print(npc.from_shape((-1, -1)))
print(npc.identity(-1))