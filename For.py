exp = [2340,2400, 3450, 2980]
total =0
for i in range (len(exp)):
    print('Month:',(i+1),'Expense:',exp[i])
    total = total + exp[i]

print('Total expense os :',total)
