import random 

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTVUVWXYZ"
numbers = "0123456789"

# Name: Harsh Upadhyay 

all = lower + upper +numbers

length = 8

password = "".join(random.sample(all, length))
password2 = "".join(random.sample(all, length))
password3 = "".join(random.sample(all, length))
password4 = "".join(random.sample(all, length))
password5 = "".join(random.sample(all, length))


print(password)
print(password2)
print(password3)
print(password4)
print(password5)