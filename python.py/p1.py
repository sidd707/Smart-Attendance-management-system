"""with open("D:\\file.txt","r") as file:
    data=file.readlines()
    for line in data:
        word=line.split("-")
        print(word)
    """
def gcd(a, b):
    if a == 0:
        return b
 
    return gcd(b % a, a)
x=gcd(35,10)





"""f=open("D:\\file.txt",'r')
f.close()
print(f.closed)
"""