import random
print("welcome to snake and ladder")
p=0
while(p<=100):
	a=input("enter r to roll the dice")
	if(a=='r'):
		r=random.randint(1,6)
		print("dice value is ",r)
		p=p+r
		print("score is",p)
		if(p==8):
			p=37
			print("climbed ladder")
		elif(p==13):
			p=34
			print(" climbed ladder")
		elif(p==40):
			p=68
			print("climbed ladder")
		elif(p==52):
			p==81
			print("climbed ladder")
		elif(p==76):
			p==97
			print("climbed ladder")
		elif(p==11):
			p=2
			print("snake bite")
		elif(p==25):
			p=4
			print("snake bite")
		elif(p==38):
			p=9
			print("snake bite")
		elif(p==65):		
			p=46
			print("snake bite")
		elif(p==89):
			p=70
			print("snake bite")
		elif(p==93):
			p=64
			print("snake bite")
		elif(p==100):
			print("winner")
		else:
			print("try again")
	else:
		print("bye")
		break	 