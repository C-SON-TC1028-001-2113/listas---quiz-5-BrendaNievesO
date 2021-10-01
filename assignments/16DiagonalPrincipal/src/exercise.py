
def main():
    a=int(input(''))
    b=int(input(''))
    c=a*b
    i=0
    f=0
    l1=[]
    l2=[]
    if a==b:
        while i<c:
            i=i+1
            n=int(input(''))
            l1.append(n)
        while f<c:
            v=l1[f]
            l2.append(v)
            f=f+(a+1)
        print(l2)
    else:
        print('La matriz no es cuadrada')

if __name__=='__main__':
    main()
