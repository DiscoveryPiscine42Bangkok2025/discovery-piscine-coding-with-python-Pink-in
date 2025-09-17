import sys
para= []
n=0
for x in sys.argv:
    if n!=0:
        para.append(x)
    n += 1
print(f"Number of parameters: {len(para)}.")
