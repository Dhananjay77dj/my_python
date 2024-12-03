import time
from functools import lru_cache as lc

@lc(maxsize=None)
def fx(n):
    time.sleep(2)
    return n*5


print(fx(12))
print(fx(13))
print(fx(45))



print(fx(12))
print(fx(13))
print(fx(45))
