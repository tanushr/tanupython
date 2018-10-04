import random
print("welcome to rock paper scissor")
c={1:'rock',2:'paper',3:'scissor'}
r=random.randint(1,3)
print(r,"=",c[r])
s1=0
s2=0
p=input("enter 'k' for rock,'a' for paper,'s' for scissor")
if(p=='k'):
	if(r==2):
		print("c wins")
		s1=1
	else:
		if(r==3):
			print("p wins")
			s2=1
elif(p=='a'):
	if(r==1):
		print("p wins")
		s2=2
	else:
		if(r==3):
			print("c wins")
			s1=2
elif(p=='s'):
	if(r==1):
		print("c wins")
		s1=3
	else:
		if(r==2):
			print("p wins")
			s2=3

	if(s1==3):
		print("computer wins")
	else:
		print("player wins")
else:
	print("bye")							

			

		