import random
list=[1,2,3,4,5]
def shuffle(list):
    for i in range(len(list)):
        values=random.randint(0,i)
        if values==i:
            list[i],list[values]=list[values],list[i]
    return list

print(list)

