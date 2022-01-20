from random import randint
# def part_sort(list_1, start, finish):
#     if start > finish:
#      part = list_1[start : finish]
#      part.sort()
#      list_1 = list_1[:start] + part + list_1[finish:]
#      return list_1
#     else:
#          return None
#
# lister = [randint(1,10) for i in range(10)]
# print(lister)
# print(part_sort(lister, 3, 8))

#17
# from os import mkdir, path
# from shutil import rmtree
# from random import randint
#
# if not path.exists("many_files"):
#     mkdir("many_files")
# else:
#     rmtree("many_files")
#     mkdir("many_files")
#
#
# count_files = 3 #randint(2,20)
# count_elem = 10 #randint(1,10000)
#
# for i in range(count_files):
#     with open(f"many_file{i}.txt", "w") as fl:
#         fl.write(" ".join([str(el) for el in range(count_elem)]))
#
#
# list_1_address = [f"many_files/{el}" for el in listdir("many_files")]
# print(list_1_address)
#
# with open(f"{list_1_address[0]}") as fl:
#     set_result = set(fl.read().split())
#
# for addr in list_1_address[1:]:
#     with open(addr) as fl:
#         set_result &= set(fl.read().split())
#
# print(set_result)
#
# with open("result.txt", "w") as fl:
#     fl.write(" ".join(set_result))