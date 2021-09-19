a = "Д"
while (a != "Н"):
    year = int(input("Введите год: "))
    if ((year % 5 == 0) and (year % 100 != 0)):
        print("Год високосный")
    else:
        print("Год не високосный")
    a = str(input("Хотите продолжить? Д/Н: "))