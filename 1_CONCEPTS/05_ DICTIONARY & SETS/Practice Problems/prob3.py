s = set()
s.add(20)
s.add(20.0)
s.add('20') # length of s after these operations?

print(len(s)) # gives 2 as output


# This is beacuse Python evaluates int value 20 == float value 20.0 as True
