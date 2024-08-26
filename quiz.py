def newGame():
    guesses=[]
    correct_guesses=0
    current_ques=1
    for key in question:
        print("---------------------------------------------")
        print(key)      
        for i in options[current_ques-1]:
            print(i)
        guess=input("Enter A,B,C or D: ")
        guess=guess.upper()
        guesses.append(guess)
        correct_guesses+=checkAnswer(question.get(key),guess)
        current_ques+=1
    viewScore(correct_guesses,guesses)
        
    
    
#--------------------------------------
def checkAnswer(answer,guess):
   if answer==guess:
       print("Correct!!")
       return 1 
   else:
       print("Wrong,try again!!")  
       return 0 
#--------------------------------------
def viewScore(correct_guesses,guesses):
    print("---------------------------------------------")
    print("Results: ")
    print("---------------------------------------------")
    print("Answers: ",end=" ")
    for i in question:
        print(question.get(i),end=" ")
    print()
    print("Guesses: ",end=" ")
    for i in guesses:
        print(i,end=" ")
    print()
    score=int((correct_guesses/len(question))*100)
    print("Your score is "+str(score)+"%")


      
#--------------------------------------
def resume():
    response=input("Do you want to play again?(yes or no): ")
    response=response.upper
    if response=="YES":
        return True
    else:
        return False

#--------------------------------------

question={
    "Who created python? : ":"A",
    "What is the capital of Canada? : ":"C",
    "Who landed on the moon first? : ":"D",
    "What is Galibs favourite color? : ":"D",
    "Choose your favourite classmate : ":"D"
}

options=[
    ["A. Van Rossum","B. Barak Obama","C. Sheikh Hasina","D.Dr. Jafar Iqbal"],
    ["A. Ottoa","B. Johannesburg","C. Montreal","D.Kualalampur"],
    ["A. Sheikh Hasina","B. Junaid Ahmed Palak","C. Yuri Gagarin","D.Neil Armstrong"],
    ["A. Violet","B. Purple","C. White","D. Black"],
    ["A. Smrity","B. Afsana Islam","C. Afsana","D. All of the options"],
]
newGame()


while resume():
    newGame()

print("Byeeeeeeeeeeeeeee!!!")





