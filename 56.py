n = int(input("Введіть кількість рядків: "))



for i in range(n):
    l = input("Введіть рядок ")
    if len(l) % 2 == 0:
        mid = len(l) // 2
       
        p = l[:mid - 1]+l[mid-1].upper()+l[mid].upper()+ l[mid + 1:]
        print(p)
    else:
     print("не парний рядок ")

  