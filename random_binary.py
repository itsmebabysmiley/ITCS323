import random

def random_bin(size, n):
    for i in range(n):
        binary = ''
        for i in range(0,size):
            binary += str(random.randint(0,1))
        print(f'"{binary}"')

        
def random_bin_randomly(min_size,max_size,n):
    for i in range(n):
        length = random.randrange(min_size,max_size+1)
        binary = ''
        for i in range(0,length):
            binary += str(random.randint(0,1))
        print(f'"{binary}"')

        
#random_bin(10,10)
#random_bin_randomly(5,8,10)
mode = int(input('choose mode...\n[1] random binary fix size\n[2] random binary flexible size\n:'))
if mode == 1:
    print('---Random binary Fix size---')
    size = int(input('length of binary:'))
    n = int(input('Required amount:'))
    random_bin(size,n)
elif mode == 2:
    print('---Random binary Flexible size---')
    min_len = int(input('minimum length of binary:'))
    max_len = int(input('maximum length of binary:'))
    n = int(input('Required amount:'))
    random_bin_randomly(min_len, max_len,n)