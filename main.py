# 1 for Rock s
# -1 for Paper w
# 0 for scissors g
computer = -1
youstr = input("Enter your choice: ")
youdict = {"s":1, "w":-1, "g":0}
reversedict = {1: "Rock", -1: "Paper", 0: "Scissors"}
you = youdict[youstr]

print(f"You chose {reversedict[you]}\nComputer chose {reversedict[computer]}")

if(computer == you):
    print("Its draw")

else:
    if(computer ==-1 and you ==1):
        print("You win!")
        
    elif(computer ==-1 and you ==0):
        print("You win!")
        
    elif(computer ==1 and you ==-1):
        print("You lose!")
        
    elif(computer ==1 and you ==0):
        print("You win!")
        
    elif(computer ==0 and you ==-1):
        print("You win!")                         
        
    elif(computer ==0 and you ==1):
        print("You lose!")     
        
    else:
        print("Something went wrong!")     