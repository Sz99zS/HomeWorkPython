from random import randint

#3

# list_1 = [randint(1,10) for i in range(10)]
# list_2 = [randint(1,10) for i in range(10)]
#
# print(sorted(set(list_1) & set(list_2)))
#
# print(list_1 )
# print(list_2)

#1

#list_1 = [randint(1,10) for i in range(10)]

# list_1 = sorted(list_1)
# pop = 0
# result = 0
# for i in range(10):
#     if list_1[i] != pop:
#         result = result + 1
#         pop = list_1[i]
# print(result)
# print(list_1)

#2

list_1 = [randint(1,10) for i in range(10)]
list_2 = [randint(1,10) for i in range(10)]

list_1 = sorted(list_1)
list_2 = sorted(list_2)

result = 0
for u in range(len(list_1)):
    j = 0
    pop_1 = list_1[u]
    while j <= len(list_2)-1 and pop_1 != list_2[j]:
        j = j + 1
    if j > len(list_2)-1:
        result = result + 1
print(result)
print(list_1)
print(list_2)

