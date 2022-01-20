from random import randint as rn

list_1 = [rn(1, 100) for i in range(rn(5, 30))]

print(list_1)

n_file = "Exercise_17.txt"

# with open(n_file, 'w') as file:
#     file.write(str(list_1))
#
# with open(n_file) as file:
    #Удаление всех знаков кроме цифр
    #list_2 = file.read().replace("[","").replace("]","").replace(",","").split()
    #Удаление только скобок
#     list_2 = file.read().replace("[","").replace("]","").replace(", ").split()
#
#     for i in range(len(list_2)):
#         list_2[i] = int(list_2[i])
#
print(list_2)
print(f"list_2[0] = {list_2[0]}", type(list_2))
print(f"list_1[0] = {list_1[0]}", type(list_1))

# with open(n_file,"w") as fl:
#     print(f"fl.writable() = {fl.writable()}")
#     fl.writable([str(el) + " " for l in list_1])
#
#
# with open(n_file) as fl:
#     sum_dig = 0
#     for chislo_str in fl.read().split():
#         for dig_str in chislo_str:
#             sum_dig += int(dig_str)
# print(sum_dig)
#
# with open(n_file) as fl:
#     sum_dig = 0
#     for symb in fl.read():
#         if symb_isdigit():
#             sum_dig += int(symb)
# print(sum_dig)


# def sum_dig(heap):
#     return sum ([int(el) for el in heap if el.isdigit()])
#
# with open("File_1.txt") as fl:
#     sum_ddd = sum_dig(fl.read())
# print(sum_ddd)