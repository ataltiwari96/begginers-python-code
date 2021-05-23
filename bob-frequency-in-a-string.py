#This code finds out the frequency of 'bob' in a given string

s='azcbobobgghakalbobobboboob'
a=''
b=''
c=''
d=''
f=0
for char in s:
   #Swapping Technique with using third variable
    a=b
    b=c
    c=char
    d=a+b+c
    if(d=='bob'):
     f+=1
    else:
     f+=0
print("Number of times bob occurs:",+f)
