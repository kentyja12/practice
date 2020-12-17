#Monte Carlo Method.

import random

def check():
    N = input("How many times do you want to hit? n*thousand,million,billion,trillion>> ")
    unit = [(1000,"thousand"),(1000000,"million"),(1000000000,"billion"),(1000000000000,"trillion")]

    if "*" in list(N):
        N = N.split("*")
        for num,name in unit:
            if N[1] == name:
                return int(N[0])*num
        else:
            print("Oops. You don't know units?")
            check()
    else:
        return int(N)
        exit()

n_in = 0 #count stings x^2+y^2<=1
n_out = 0 #count stings x^2+y^2>1
N_re = check()

for i in range(N_re):
    x = random.random()
    y = random.random()
    
    if x**2+y**2 <= 1:
        n_in += 1
    else:
        n_out += 1
    
    pi = 4*(n_in/(n_out+n_in))

print("Number of trials:",N_re)
print("pi =",pi)