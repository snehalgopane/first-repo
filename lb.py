li=[1,2,3,4,5,6,7,89]
print(tuple(filter(lambda x:x%2==0,li)))

li=[10,20,30,4,50]
x=list(map(lambda x:x*2,li))
print(x)

x=lambda a,b:a*b
print(x(5,6))

a=5
b=6
c=a*b
print(c)