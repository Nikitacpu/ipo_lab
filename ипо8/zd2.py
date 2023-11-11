import random
a= set(random.sample(range(1, 100), 5))
b = set(random.sample(range(1, 100), 5))
print("Первое множество: ", a)
print("Второе множество: ", b)
n = a.symmetric_difference(b)
print("Различные числа в этих множествах: ", list(n))
c = a.intersection(b)
print("Числа, которые входят как в первое, так и во второе множество: ", list(c))
