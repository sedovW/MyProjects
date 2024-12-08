fibanachi_file=open('Fibanachi_file','w+')
fibanachi=[1,1]
n=int(input("Для сброса файла введиите \'0\'\nВведите количество чисел Фибоначчи: "))
n=n-2
first=1
second=1
next_num=None
for I in range(0,n):
    next_num=first+second
    fibanachi.append(next_num)
    first=second
    second=next_num
    next_num=0
n=n+2
print(n)
if n != 0:
    fibanachi = str(fibanachi)
    fibanachi_file.write(fibanachi[1:-1])
    print(fibanachi[1:-1])


