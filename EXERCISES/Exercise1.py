'''Write a Python program to create a dictionary similar to the real-world dictionary.
The user will give the word as input. Suppose that the word is present in your dictionary
along with its definition or meaning.The program will print the meaning or definition of that word.'''


marks ={"Akash": 99,"Subham":69,"Anshuman":88,"Shruti":89,"Habibi":69,
        "set":"collection of well defined elements","variables":"A container which stores a number,string,etc",
        "Programmer":"A person who writes program in oder to make other peoples lives easy"}
while(True):
    try:
        name = input("Enter a name: ")
        print(marks[name])
    except:
        print("Opps!! We think the person marks/ meaning is not presnt in our dictonary")