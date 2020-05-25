import random

sum = 0

while sum <=980:
    data = []
    #     # if sum <=980:
    for i in range(1,19):

        id = random.randint(1,9)
        data.append(str(id))
        bat = ''.join(data)
    print(bat)
    sum +=1
