
from random import shuffle
# append
my_list = [1]

my_list.append(2)
my_list.append(3)

print("my_list: append", my_list)

# remove
my_list.remove(2)

print("my_list: remove", my_list)


# pop
my_list.pop()

print("my_list: pop", my_list)


# extend
my_list.extend([4, 5, 6, 0, -1, 1, 2])

print("my_list: extend", my_list)


# insert
my_list.insert(1, 2)
my_list.insert(2, 3)

print("my_list: insert", my_list)


# copy

my_list_copy = my_list.copy()

print("my_list: copy", my_list_copy)

del my_list[0]

print("my_list: del", my_list)

my = my_list.sort()

print("my_list: sort", my_list)



# print("my_list: count", )
# sh = shuffle(my_list)
# print("my_list: shuffle", my_list)


x_y = [x for x in my_list if x > 2]
print(x_y)