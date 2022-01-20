from random import randint

with open("Task_HW_6.txt") as file:
    list_word = file.read().split()

    print(*list_word, sep="\n")

for i in range(len(list_word)):
    for el in list_word[i]:
        if not el.isalpha() and el != "-":
             list_word[i] = list_word[i].replace(el, '')

for el in list_word:
    if not el:
        list_word.remove(el)

print(list_word)