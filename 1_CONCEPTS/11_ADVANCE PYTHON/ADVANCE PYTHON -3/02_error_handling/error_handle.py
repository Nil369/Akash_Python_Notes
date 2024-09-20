file = open('akash.txt', 'w')

try:
    file.write('Akash is a good boy')
finally:
    file.close()

with open('akash1.txt', 'w') as file:
    file.write('Akash is a very very good boy :)')