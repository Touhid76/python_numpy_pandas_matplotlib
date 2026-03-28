#random numbers in python
import random
random.seed(10)
x=random.random()
print(x)  

#use   of randint() function
y=random.randint(1,10)
print(y)

#use of uniform() function:floating num generate
z=random.uniform(1,10)
print(z)

#use of choice() function:randomly select an element from a sequence
s=["apple","banana","cherry"]
print(random.choice(s))

#use of choices() function:randomly select multiple elements from a sequence
print(random.choices(s,weights=[10,2,3]))

#use of shuffle() function:randomly shuffle a sequence
random.shuffle(s)
print(s)

#use of sample() function:randomly select a specified number of elements from a sequence
print(random.sample(s,k=2))
