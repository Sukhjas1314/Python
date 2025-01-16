# Q. A = {34, 56, 78, 90} and B = {78, 45, 90, 23} . Perform the following operations:
# i. Find the unique scores achieved by both teams (union).
# ii. Identify the scores that are common to both teams (intersection).
# iii. Find the scores that are exclusive to each team (symmetric difference).
# iv. Check if the scores of team A are a subset of team B, and if team B's scores are a superset of team A.
# v. Remove a specific score X (input by the user) from set A if it exists. If not, print a message saying it is not present.

A = {34,56,78,90}
B = {78,45,90,23}

print('\nUnion of both sets :',A.union(B))

print('\nIntersection of the sets :',A.intersection(B))

print('\nSymmetric difference :',A.symmetric_difference(B))

is_subset = A.issubset(B)
print('\nScores of team A are a subset of team B :',is_subset)

is_superset = B.issuperset(A)
print('\nScores of team B are a superset of team A.',is_superset)

x = int(input('\nEnter a score to be removed : '))
if x in A:
    print(f'{x} is present in the set A')
    A.remove(x)
    print(f'After removing {x} from set A : {A}')
else:
    print(f'{x} is not present in the set A')

print('\n')