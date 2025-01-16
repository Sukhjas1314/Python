import Q7_main

principal = 1000
rate = 7.5
time = 3
ci = Q7_main.cal_compound_interest(principal,rate,time)
print(f'\nPrincipal = {principal},\nRate = {rate},\nTime = {time}\n\nCompound interest = {ci:.3f}')
