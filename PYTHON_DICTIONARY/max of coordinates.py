my_points={'a':(4,3),'b':(1,2),'c':(5,1)}
val_l=[]
va_l=[]
for i in my_points:
    l=list(my_points[i])
    val_l.append(l[0])
print("Maximum Value at index(my_points,0)=",max(val_l))
for j in my_points:
    ls=list(my_points[j])
    va_l.append(ls[1])
print("Maximum Value at index(my_points,1)=",max(va_l))
