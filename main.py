velikost = 3
plan =  []
play = ""
play1 = ""
game_start = 0
kreten= False


for i in range(velikost):
    plan.append([])
    for j in range(velikost):
        plan[i].append("_")

while play != "End":
    if game_start == 0:
        print("Tady máš pole: ")
        for i in plan:
            print(i)
    print("Hraješ jako kolečko: ")
    play = int(input("Jaký řádek? "))
    play1 = int(input("Jaká pozice? "))
    play -=1
    play1 -=1
    if plan[play][play1]!="_":
        kreten = True
        while kreten == True:
            print("Si kretén tam už něco je, zkus to znovu!")
            for i in plan:
                print(i)
            play = int(input("Jaký řádek? "))
            play1 = int(input("Jaká pozice? "))
            play -= 1
            play1 -= 1
            if plan[play][play1] != "_":
                kreten = True
            else:
                kreten = False
                plan[play][play1] = "O"
                for i in plan:
                    print(i)

    else:
        plan[play][play1]= "O"
        for i in plan:
            print(i)
        game_start += 1

    print("Hraješ jako křížek: ")
    play = int(input("Jaký řádek? "))
    play1 = int(input("Jaká pozice? "))
    play -=1
    play1 -=1
    if plan[play][play1] != "_":
        kreten = True
        while kreten == True:
            print("Si kretén tam už něco je, zkus to znovu!")
            for i in plan:
                print(i)
            play = int(input("Jaký řádek? "))
            play1 = int(input("Jaká pozice? "))
            play -= 1
            play1 -= 1
            if plan[play][play1] != "_":
                kreten = True
            else:
                kreten = False
                plan[play][play1] = "X"
                for i in plan:
                    print(i)
    else:
        plan[play][play1] = "X"
        for i in plan:
            print(i)