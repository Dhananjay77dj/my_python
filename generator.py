def generator():  # the mai differnece between the return and yield is return store the value but the yield generate it on mauke pe !
# isse memory nahi bharti jab jab value chahiye tab tab value generate karte jaao
    for i in range(5545):
        yield i
x = generator()
print(next(x))
print(next(x))
print(next(x))

print(next(x))



