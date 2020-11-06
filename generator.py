""" Demonstrate the functionality of Generators in Python """

""" Below is an example of simple generator, which is a function that acts as an iterator 
    The value of previous invocation is remembered and only next value is returned ---> "ON DEMAND"
    The use of "yield" instead of "return" makes below function a generator
"""


def abc_generator():
    yield 'a'
    yield 'b'
    yield 'c'


for char in abc_generator():
    print(char)
print("-"*40)


def num_generator(nums=1):
    while nums:
        yield nums
        nums += 1


for num in num_generator():
    print(num)
    if num == 4:
        break
print("-"*40)


def doubles(stop=10):
    return (2 * n for n in range(stop))


d_gen = doubles(5)
print(type(d_gen))
print("First d_gen num is: ", next(d_gen))
print("Next d_gen num is: ", d_gen.__next__())
print("Next d_gen num is: ", d_gen.__next__())
print("Next d_gen num is: ", d_gen.__next__())
print("Next d_gen num is: ", d_gen.__next__())
# print("Next d_gen num is: ", d_gen.__next__())  # StopIteration error

triples = (3 * n for n in range(10))
print(type(triples))
print(next(triples))
print(triples.__next__())
