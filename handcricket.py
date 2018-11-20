import random
a=int(input("enter value for the toss "))
if(a%2==0):
	print("player start playing")
else:
	print("computer start playing")


computer=0
score=0
while True:
	b=input("enter a character")
	if(b=='t'):
		c=int(input("enter value"))
		score=score+c
		print(" player score is",score)
	else:
		r=random.randint(1,10)
		computer=computer+r
		print("computer hits",r)
		print("computer score is",computer)

		
	
		