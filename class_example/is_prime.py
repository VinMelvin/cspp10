num = 23

for i in range(2,int(20 ** 0.5)+1):
    if num % i == 0:
        print("not prime")
        break
else:
    print("is prime")