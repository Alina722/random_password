import random
import string
user = int(input("input password len: "))

seed = 'ABCDEFGHIJKLMNOPQRSTIVWXYZabcdefghijklmnopqrstivwxyz1234567890!@#()_+P][\/.,'
bu = []
for i in range(user):
    bu.append(random.choice(seed))
    salt = ''.join(bu)
print(salt)
