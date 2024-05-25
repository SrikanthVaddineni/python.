def calculate_total(exp):
    total = 0
    for item in exp:
        total=total+item
    return total
tom_exp_list = [2100,2345,2654]
joe_exp_list = [234,345,100]

toms_total=calculate_total(tom_exp_list)
joes_total=calculate_total(joe_exp_list)
print("Tom's total expenses:",toms_total)
print("joesntotal expenses:",joes_total)