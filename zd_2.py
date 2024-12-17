input_str = input("Введите строку символов, разделенных пробелами: ")

razd = input_str.split()

rez = []

for i in razd:
    if i not in rez:
        rez.append(i)

print(rez)