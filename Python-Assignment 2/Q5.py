# Q.Write a program to rename a key city to location in the following dictionary:
# data = {"city": "New York","population": 8419600,"area": 468.9}.

data = {
    'city' : 'New York',
    'population' : 8419600,
    'area' : 468.9 }

if 'city' in data:
    data['location'] = data.pop('city')

print('\nAfter updating the dictionary :',data)
print('\n')