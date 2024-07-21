# Write a program using functions to find greatest of three numbers. 

def greatest(a,b,c):
    if(a>b and a>c):
        print(f"{a} is Greatest")
    elif(b>a and b>c):
        print(f"{b} is Greatest")
    elif(c>a and c>b):
        print(f"{b} is Greatest")

a = int(input(f"Enter 1st number: "))
b = int(input(f"Enter 2nd number: "))
c = int(input(f"Enter 3rd number: "))

greatest(a,b,c)