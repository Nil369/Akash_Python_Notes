# A spam comment is defined as a text containing following keywords: 
p1 = "Make a lot of money"
p2 = "buy now"  
p3 = "subscribe this"  
p4 = "click this"

# Write a program to detect these spams. 

message = input("Enter your comment: ")

if((p1 in message) or (p2 in message )or (p3 in message) or (p4 in message)):
    print("This comment is a spam")

else:
    print("This comment is not a spam")