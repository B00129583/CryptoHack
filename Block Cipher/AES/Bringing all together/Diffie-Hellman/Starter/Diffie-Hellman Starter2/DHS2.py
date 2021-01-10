p = 28151

# g^x mod p
g=2
found = False

while not found:
    for x in range(2,p):
        if pow(g,x,p) == g:
            break
        if x ==p-1:
           found = true
           print(g)
    if found:
         
        break
    g=g+1



