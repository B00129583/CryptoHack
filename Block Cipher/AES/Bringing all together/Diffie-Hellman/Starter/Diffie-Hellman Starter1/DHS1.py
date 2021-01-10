p = 991
g = 209

##find d such that g * d mod 991 = 1.

for d in range (991):
    if (d*g) % p ==1:
        print(d)
        break