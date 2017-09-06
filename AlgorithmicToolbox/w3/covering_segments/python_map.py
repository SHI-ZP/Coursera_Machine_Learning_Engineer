from collections import namedtuple

segment = namedtuple('segment', 'start end')

a1, b1 = list(range(10)), list(range(10))
print(map(lambda x: segment(x[0], x[1]), zip(a1[::2]), b1[1::2]))
c = map(lambda x: segment(x[0], x[1]), zip(a1[::2], b1[1::2]))
# print(list(c))
# print(list(c))
print(c)
d = list(c)
print(d)
for i in d:
    print(i)
