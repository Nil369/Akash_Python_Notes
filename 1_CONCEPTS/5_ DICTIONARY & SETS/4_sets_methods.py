s = {1, 5, 32, 54,5, 5, 5, "AKASH"}

print(s, type(s))

s.add(566)
print(s)
s.remove(1)
print(s)


# UNION & INTERSECTION:

s1 = {1, 45, 6, 78}  
s2 = {7, 8, 1, 78}

print(s1.union(s2))
print(s1.intersection(s2))