from functools import reduce

#  lambda - inline functions stored in variables

# dble = lambda x, y : 2 * x * y
# print(dble(10, 2))

#  map - inline loop which aplies some code to every item of a list

n = [1, 2, 3, 4, 5, 6]
m = [7, 11, 13]
o = ['I','Love','You']
p = [["ab"], ["cd"], ["ef"]]
# print(list(map(lambda x : x ** 2, n)))
# print([x > 1 for x in n])

#  filter - loop for a condition to remove those elements which return false
# print(list(filter(lambda x : x > 2, m)))

# reduce - apply a function to an iterable reducing it to a cumulative value. pute recursion is reduction

# factorial = reduce(lambda x, y : x + ' ' + y, o)
# print(factorial)

# for i in range(p.length):
#     print(p[i])

