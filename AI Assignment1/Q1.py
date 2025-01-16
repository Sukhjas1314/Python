# Q.A class with 10 students wants to produce some information from the results of the four standard
# tests in Maths, Science, English and IT. Each test is out of 100 marks. The information output
# should be the highest, lowest and average mark for each test and the highest, lowest and average
# mark overall. Write a program in Python to complete this task.

students = [
    [85, 90, 78, 88],
    [92, 81, 76, 85],
    [75, 88, 89, 90],
    [80, 85, 84, 82],
    [95, 92, 91, 87],
    [78, 84, 80, 76],
    [88, 79, 77, 81],
    [84, 86, 82, 83],
    [90, 87, 88, 89],
    [91, 93, 94, 92]
]

subjects = ['Maths','Science','English','IT']

for idx in range(4):
    subject_scores = []
    for i in students:
        subject_scores.append(i[idx])

    highest = max(subject_scores)
    lowest = min(subject_scores)
    average = sum(subject_scores)/len(subject_scores)

    print(f'{subjects[idx]} : \n\tHighest : {highest}\tLowest : {lowest}\tAverage : {average:.2f}')

total = []
for i in students:
    total.append(sum(i))

overall_highest = max(total)
overall_lowest = min(total)
overall_average = sum(total)/len(total)

print('\nOverall Score : ')
print(f'\tHighest : {overall_highest}\tLowest : {overall_lowest}\tAverage : {overall_average:.2f}')

