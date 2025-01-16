# Q.Write a Python Program to input basic salary of an employee and calculate its Gross salary
# according to following: Basic Salary <= 10000 : HRA = 20%, DA = 80% Basic Salary <= 20000
# : HRA = 25%, DA = 90% Basic Salary > 20000 : HRA = 30%, DA = 95%.

basic_sal = float(input('Enter the basic salary of an employee : '))

hr = 0
da = 0

if basic_sal <= 10000:
    hr = 0.20 * basic_sal
    da = 0.80 * basic_sal
elif basic_sal <= 20000:
    hr = 0.25 * basic_sal
    da = 0.90 * basic_sal
else:
    hr = 0.30 * basic_sal
    da = 0.95 * basic_sal

gross_sal = basic_sal + hr + da

print(f'Basic Salary : {basic_sal:.2f}')
print(f'HRA : {hr:.2f}')
print(f'DA : {da:.2f}')
print(f'Gross Salary : {gross_sal:.2f}')