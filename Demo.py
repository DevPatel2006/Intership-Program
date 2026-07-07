user = []
for i in range(1,6):
    name = int(input(f"Enter the Values {i}: "))
    user.append(name)
print("Normal List is ",user)
max = 0
for i in user:
    if i > max:
        max = i
print("Maximum Values is ",max)
user1 = []
for i in range(len(user)):
    min = 0
    for i in user:
        if i > min:
            min = i 
        max = min
        if i in user:
            for i in user:
                if i == None:
                    break;
                elif i < max:
                    max = i
            user1.append(max)
            user.remove(max)    

print("Sorted Values are ",user1)
