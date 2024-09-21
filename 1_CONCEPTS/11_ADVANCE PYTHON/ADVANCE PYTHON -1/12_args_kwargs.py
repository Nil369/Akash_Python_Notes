# The special syntax *args in function definitions in Python is used to pass a variable number of arguments to a function.

def myFun(arg1, *args):
    print("First argument :", arg1)
    print("Rest values in *args:",end = "")
    for arg in args:
        print(" "+arg,end="")
    print("\n",type(args),end="\n\n")


myFun('Hello', 'This', 'is', 'Akash Halder')


# The special syntax **kwargs in function definitions in Python is used to pass a keyworded, variable-length argument list.

def func(**kwargs):
    print("*"*5,"Marks","*"*5)
    for key, value in kwargs.items():
        print(f'{key} -> {value}')

    print("\n",type(kwargs))

marklist = {"Akash":100, "Shruti":80, "Puchku":99}

func(**marklist)
