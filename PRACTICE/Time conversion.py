time=int(input("Enter the time in seconds:-"))
min=time//60
sec=time%60
if sec==0:
    print(time,"seconds=",min,"minutes")
else:
    print(time,"seconds=",min,"minutes",sec,"seconds")