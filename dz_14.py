from random import randint
def part_sort(list_1, start, finish):
    if start < finish and start > 0 and finish < 10:
     part = list_1[start : finish]
     part.sort()
     list_1 = list_1[:start] + part + list_1[finish:]
     return list_1
    else:
         return None

lister = [randint(1,10) for i in range(10)]
print(lister)
print(part_sort(lister, 3, 8))

