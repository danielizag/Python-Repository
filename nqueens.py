
import random
n = int(input("Give a value for N for the NxN board: "))

nq = list(range(n))

def board(arg0):
        print ("\n".join('O' * i + 'X' + 'O' * (n-i-1) for i in arg0) + "\n")
    
def conflicts(list):
        conflicts = 0
        for x in range(len(list)):
                for y in range(x+1, len(list)):
                        if list[x] == list[y]:
                                conflicts += 1
                        if abs(list[x]+list[y])==abs(x-y):
                                conflicts += 1
        return conflicts

iters = 0 

while conflicts(nq) > 0:
        iters += 1
        random.shuffle(nq)
        
	
print("After", iters, "iterations, NQ",nq,"has",conflicts(nq),"conflicts.")
if conflicts(nq) == 0:
                board(nq)
