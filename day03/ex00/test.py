from NumPyCreator import NumPyCreator
import numpy as np

npc = NumPyCreator()

print("test 1")
assert np.array_equal(npc.from_list([[1,2,3],[6,3,4]]), np.array([[1, 2, 3],[6, 3, 4]]))
print(npc.from_list([[1,2,3],[6,3,4]]))
print("test 2")
print(npc.from_list([[1,2,3],[6,4]]))
assert npc.from_list([[1,2,3],[6,4]]) is None
print("test 3")
arr = npc.from_list([[1,2,3],['a','b','c'],[6,4,7]])
print(arr)
print("dtype:", arr.dtype)
assert np.array_equal(npc.from_list([[1,2,3],['a','b','c'],[6,4,7]]), np.array([['1','2','3'],['a','b','c'],['6','4','7']], dtype='<U21'))
print("test 4")
print(npc.from_list(((1,2),(3,4))))
assert npc.from_list(((1,2),(3,4))) is None
print("test 5")
print(npc.from_tuple(("a", "b", "c")))
assert np.array_equal(npc.from_tuple(("a", "b", "c")), np.array(['a', 'b', 'c']))
print("test 6")
print(npc.from_tuple(["a", "b", "c"]))
assert npc.from_tuple(["a", "b", "c"]) is None
print("test 7")
print(npc.from_iterable(range(5)))
assert np.array_equal(npc.from_iterable(range(5)), np.array([0, 1, 2, 3, 4]))
print("test 8")
shape=(3,5)
print(npc.from_shape(shape))
assert np.array_equal(npc.from_shape(shape), np.array([[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0]]))
print("Test random")
print(npc.random(shape))
# Commenting out the random test as it would generate different values each time
# assert np.array_equal(npc.random(shape), ...)
print("test 9")
print(npc.identity(4))
assert np.array_equal(npc.identity(4), np.array([[1., 0., 0., 0.],[0., 1., 0., 0.],[0., 0., 1., 0.],[0., 0., 0., 1.]]))

print('end')