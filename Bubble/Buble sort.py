from Data import data
print([data])
print(f'кол-во элементов:{len(data)}')
lenn=len(data)-1
iteration=0
for i in range (0,len(data)):
    for b in range(0,((lenn)-i)):

        if data[b] > data[b+1]:
            data[b],data[b+1]=data[b+1],data[b]
            iteration+=1
        else:
            iteration += 1
print(f'{iteration} операций')
print(data)