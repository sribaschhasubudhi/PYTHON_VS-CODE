month_day={"January": 31,"February": 28,"March": 31,"April": 30,"May": 31,"June": 30,"July": 31,"August": 31,"September": 30,"October": 31,"November": 30,"December": 31}
'''1.
mname=input("Enter the month:-")
print(mname,"has",month_day[mname],"days")'''
#print(sorted(month_day.keys()))
'''
for i in month_day:
    if month_day[i]==31:
        print(i)'''
print(sorted(month_day.items()))