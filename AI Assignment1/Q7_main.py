# Q. (i) Write a function which takes principal amount, interest rate and time. This function returns
# compound interest. Call this function to print the output.
# (ii) Save this function (as a module) in a python file and call it in another python file.

# (i)
def cal_compound_interest(principal,rate,time):
    amount = principal * (1 + rate / 100) ** time
    compound_interest = amount - principal
    return compound_interest

# principal = 1000
# rate = 7.5
# time = 3
# ci = cal_compound_interest(principal,rate,time)
# print(f'\nPrincipal = {principal},\nRate = {rate},\nTime = {time}\n\nCompound interest = {ci:.3f}')
