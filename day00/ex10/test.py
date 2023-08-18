from loading import ft_progress
import time

# Test the function with the given example
listy = range(1000)
ret = 0
for elem in ft_progress(listy):
    time.sleep(0.02)

print(ret)

