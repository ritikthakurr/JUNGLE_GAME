#jungle game

print("welcome to jungle game")
print("a man want to go to the fort from the bus stand in the hill station you are required to give him directions and help him to successfully reach to destination")
z=int(input("press 1 for left and press 2 for right"))

if(z==1):
    print("reached gol chowk")
    a=int(input("press 1 for taking left from the gol chowk and press 2 for taking right from the gol chowk"))
    if(a==1):
        print("game over:-reached forest area")
    elif(a==2):
        print("game over:-reached unidentified location")
elif(z==2):
    print("reched village xyz")
    b=int(input("press 1 for taking left from village xyz & press 2 for taking right from village xyz"))
    if(b==1):
        print("GAME OVER:- road block due to falling of tree")
    elif(b==2):
        print("you are going in the road and after some time you met with the stranger")
        c=int(input("press 1 for taking help from the stranger and press 2 for nat taking help from the stranger"))
        if(c==1):
            print("YOU WON:- reached the fort")
        elif(c==2):
            print("YOU LOSE:- game over")


