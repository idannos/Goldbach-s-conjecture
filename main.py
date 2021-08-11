import math
def prime(n):
    if n % 2 == 0:
        return False  # number is not prime
    iterations = int(math.sqrt(n)) + 1
    for i in range(3, iterations, 2):
        if n % i == 0:
            return False
    return True

zoogi = 2000
lst_up=[]
lst_down=[]
up= zoogi/2 + 1
down= zoogi/2 -1
for i in range(1,zoogi/4):
    if prime(up) and prime(down):
        lst_up.append(up)
        lst_down.append(down)
        # if we got here, golbach conjecture is right for this number
    up+=2
    down-=2

print lst_up
print lst_down
