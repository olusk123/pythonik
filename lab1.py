
def imienzawisko(x,y):
    return x + "."+y
print(imienzawisko("J","Kowalski"))


def imienzawisko2(x,y):
    return x[0].upper() + "."+ y[0].upper() + y[1:]
print(imienzawisko2("j","kowalski"))

def c(a,b,c):
    return a*100+b-c
print(c(20,22,21))

def d(a,b,c):
    return c(a,b)
print(imienzawisko("jan","kowalski"))

def f(a,b):
    if a and b > 0 and b!=0:
        return a/b
print(f(8,4))
i=0
while i <100:
    i += int(input())
    print(i)
def zad7(lista):
    return tuple(lista)
lista =[1,2,3,"jan",12]
print(zad7(lista))

lista1 =[]
for x in range(3):
    lista1.append(input())
print(zad7(lista1))