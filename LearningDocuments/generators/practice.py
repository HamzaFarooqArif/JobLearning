def square(number_range):
    for i in range(1, number_range):
        yield(i*i)
num_list = square(5)
print(next(num_list))
print(next(num_list))
print(next(num_list))
print(next(num_list))

num_list_2 = (x*x for x in range(1, 5))
print(next(num_list_2))
print(next(num_list_2))
print(next(num_list_2))
print(next(num_list_2))