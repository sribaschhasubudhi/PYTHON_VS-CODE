d={1:10,2:20,3:30,4:40}
#print(d.get(5,"not found"))
#print(d.keys())
e={'jack':11,'jill':12}
#print(e.clear())
#print(d.items())
#print(e.values())
#d.update(e)
#print(d)
#print(e.pop('jack'))
#q=d.setdefault(4,60)   #4 already has a value;40
#print(q)       #So,output will be 40
r=d.fromkeys([89],20)
print(r)
print(d)