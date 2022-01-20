with open("HW_44.txt","r") as file:
    str_1 = file.readline()
    new_file = []
    while str_1:
     str_1 = str_1.replace("\n", "")
     result = eval(str_1)
     # print(result)
     new_file.append(str_1 + " = " + str(result)+"\n")
     str_1 = file.readline()
file.close
with open("HW_44.txt", "w") as file:
    file.writelines(new_file)
file.close
