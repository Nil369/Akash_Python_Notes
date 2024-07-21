# Write a program to fill in a letter template given below with name and date taking input from user. 

letter = '''  
Dear <|Name|>,
\tYou are selected! 
<|Date|> 
''' 
name = input("Enter your name: ")
date = input("Enter a date: ")
print(letter.replace("<|Name|>", name).replace("<|Date|>", date))
