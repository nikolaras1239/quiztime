print("Welcome to my Quiz game")
player1=input("First Player,give me your name:  ")
player2=input("Second Player,give me your name:  ")
pl=[player1,player2]
points=[0,0]
i=1
question=["1. What is the fastest land animal?   a)wolf  b)cheetah","2. Which of these is the fastest fish? a)sailfish   b)flying fish","3. What is the fastest bird?  a)stork  b)Peregrine Falcon","4. Which of these is the shortest time span?  a)decade b)century","5. Which of these is the shortest measurement of length?  a)inch b)centimetre","6. Which of these things most likely takes up the least time?  a)Taking a shower  b)Reading a 300page novel","7.What Percentage Of Canada Is Forest?  a)21  b)31","Where Is The Coldest Place On Earth? a)Antarctica b)North Pole"]
answers=["b","a","b","a","b","a","a","a"]
q=0
i=0
while i<8:
    print(pl[q])
    print(question[i])
    ans=input("give me the answer: ")
    if ans==answers[i]:
        print("Congratulations,you are right")
        points[q-1]=points[q-1]+1
    else:
        print("Wrong")
    if i%2==0:
        q=0
    else:
        q=1
    i=i+1

print("Lets move to the last two questions")
print(player1)
q1=input("Give us a question for you opponent: ")
a1=input("give us the answer: ")
print(player2)
print(q1)
a2=input("give me the answer: ")
if a1==a2:
    points[1]+=1
print(player2)
q2=input(" Give us a question for you opponent: ")
a3=input("give us the answer: ")
print(player1)
print(q1)
a4=input("give me the answer: ")
if a3==a4:
    points[0]+=1




if points[0]>points[1]:
    print("The winner is")
    print(player1)
elif points[0]<points[1]:
    print("The winner is")
    print(player2)
else:
    print("Its a tie")
