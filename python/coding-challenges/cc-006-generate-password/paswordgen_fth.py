import random
name = input ("Please enter your full name without any space :")
result=""
while len(result)< 3:
    result+=name[random.randint(0,len(name))].lower()
result+=str(random.randint(1000,9999))
print(result)