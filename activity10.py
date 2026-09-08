j = 19
e = 25
m = 8

print(j > e) 
print(j > m and m < e)
print(e > j or j < m)
print(e > m or j < m)

print(j > e or m < j and m == e)
print(m < j and m == e)

print( not(j > e or m < j and m == e))