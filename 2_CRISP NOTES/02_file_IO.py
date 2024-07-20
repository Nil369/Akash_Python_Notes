"""====================================Writing a file=========================="""
s = "Akash is a good boy"

with open("Akash.txt","w") as f:
    f.write(s)

fp = open("Akash.txt","w")
fp.write(s)
fp.close()

"""====================================Reading a file================================"""
s = "Akash is a good boy"

with open("Akash.txt","r") as f:
   s = f.read()
   print(s)

f = open("Akash.txt","r")
s= f.read()
print(s)
f.close()
"""=================================Appending a file=========================="""
s = "Akash is a good boy"

with open("Akash.txt","a") as f:
    f.write("He is a 18 yrs old boy")
# This add string to the exsisting file..But if you write a file it will erase the old content and add the new content written in<f.write()>