print("wellcome to the game")
print("Here are the list if games :)")
print("							   1 )  Hunt Spellings Randomly (its a game related to english spellings)")
print("							   3 )  GOW (Game Of Words) ")
print("							   2 )  Lost In Nubers")
a=int(input())
# game :1
if (a==1):
	print("Hunt Spellings Randomly")
	print("Here are the rules:")
	print("                   **after completion of every instruction press enter**")
	print("                   a ) specify the Number of participants once you complete reading the instructions")
	print("                   b ) specify the names of participants in order")	
	print("                   c ) Then you have to answer question with a word specifed number of letters with and should start with the specified letter randomly gernerated within 9sec")
	print("                   d ) Then the oppertor should enter 1 if the player answered correctly, 0 if he didn't answered and -1 if he answered incorrect")
	print("                   e ) then if you want to continue game press o and if you want to end game press e ")
	from random import randint
	import string
	from timeit import default_timer as timer
	import random
	
	N=int(input("No of players : "))

	players1=[]
	players={}
	for i in range(N):
		players.update({i:0})
		players1.append(input("Enter name of player : "))
	m=0	
	r=0
	while True:
		r+=1
		print(randint(2,4),random.choice(string.ascii_letters))
		start =timer()
		while True:
			end= timer()
			if (end-start>1):
				print("pass: time up")
				break
		c=int(input("enter 1 or 0 or -1 accordingly : "))
		if (m<N):
			players[m]+=c
		else:
			m=m-N
			players[m]+=c
		k=input("  Do u wanna continue game if so then enter 1 else enter 2 : ")
		print("_____________","here we completed",r,"round(s) of game","_____________")
		if (k=="2"):
			for i in range(N):
				print(players1[i]+" : "+str(players[i]))
			break
		m+=1

if (a==2):
	print("Lost In Nubers")
	print("Here are the rules:")
	print("                   **after completion of every instruction press enter**")
	print("                   a ) specify the Number of participants once you complete reading the instructions")
	print("                   b ) specify the names of participants in order")	
	print("                   c ) Then you have to guess a randomly gernerated by compurt within 9sec")
	print("                   d ) Then the oppertor should enter 1 if the player answered correctly, 0 if he didn't answered and -1 if he answered")
	print("                   e ) then if you want to continue game press o and if you want to end game press e ")
	N=input("No of players : ")
	players1=[]
	players={}	
	for i in range(N):
		players.update({i,0})
		players1.append(input())
	m=0	






