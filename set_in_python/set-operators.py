#use of set operators in python
s={"a","b","c"}
s1={"b","c","d"}

#use of union operator
union=s.union(s1)
print(union)

#use of intersection operator
intersection=s.intersection(s1)
print(intersection)

#use of difference operator
difference=s.difference(s1)
print(difference)

#use of symmetric difference operator
sym_diff=s.symmetric_difference(s1)
print(sym_diff)