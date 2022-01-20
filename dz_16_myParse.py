import ast
with open("HW_44.txt","r") as file:
    str_1 = file.readline()
    while str_1:
     str_1 = str_1[0:len(str_1) - 1]
     str_1 = str_1.replace("+"," + ").replace("-"," - ").replace("/"," / ").replace("*"," * ")
     list_1=str_1.split(" ")
     result = 0
     operation = "+"
     i = 0
     while i < len(list_1):
        #пропускаем пустые элементы и выбираем первое слагаемое
        while (i < len(list_1)) and (list_1[i] == ""):
          i = i + 1
        #выполняем операцию
        if operation == "+":
            result = result + float(list_1[i])
        if operation == "-":
            result = result - float(list_1[i])
        if operation == "*":
            result = result * float(list_1[i])
        if operation == "/":
            result = result / float(list_1[i])
        i = i + 1
        #пропускаем пустые элементы и выбираем операцию
        while (i < len(list_1)) and (list_1[i] == ""):
          i = i + 1
        if (i < len(list_1)):
          operation = list_1[i]
          i = i + 1
     print(result)
     str_1 = file.readline()
file.close
