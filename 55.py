txt = input()

a=txt.split()

d=len(a)
print(d)    
for q in a:
        if len(q)>len(a):
            a=q
          
print(a)