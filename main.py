velikost = 3
plan =  []
play = ""
play1 = ""
game_start = 0
kreten= False
game_loop = True


#Vytváří pole a dává do listu prázdné pole
def create_plan():
    for i in range(velikost):
        plan.append([])
        for j in range(velikost):
            plan[i].append("_")

#Zobrazuje aktuální pole
def show_plan():
    for i in plan:
        print(i)

def assign_kolečko():
    plan[play][play1] = "O"

def assign_křížek():
    plan[play][play1] = "X"
def win_kolečko():
    count = 0
    general_count = 0
    line_count = 0
    kolečko_count = 0
    pos_1 = 0
    pos_2 = 0
    pos_3 = 0
    for line in plan:
        general_count+=1
        line_count += 1
        for symbol in line:
            count+=1
            if symbol == "O":
                kolečko_count += 1
            else:
                pass
            if general_count == kolečko_count:
                pos_1 += 1
            if general_count + 1 == kolečko_count:
                pos_2 += 1
            if general_count + 2 == kolečko_count:
                pos_3 += 1
            else:
                pass
    if pos_1 == 1 and pos_2 == 1 and pos_3 == 1:
        print("Kolečko vyhrálo!")
        game_loop = False
    else:
        general_count = 0
        count = 0
        line_count = 0
        kolečko_count = 0
        pos_1 = 0
        pos_2 = 0
        pos_3 = 0




























create_plan()


while game_loop == True:
    if game_start == 0:
        print("Tady máš pole: ")
        show_plan()
    print("Hraješ jako kolečko: ")
    play = int(input("Jaký řádek? "))
    play1 = int(input("Jaká pozice? "))
    play -=1
    play1 -=1
    if plan[play][play1]!="_":
        kreten = True
        while kreten == True:
            print("Si kretén tam už něco je, zkus to znovu!")
            show_plan()
            play = int(input("Jaký řádek? "))
            play1 = int(input("Jaká pozice? "))
            play -= 1
            play1 -= 1
            if plan[play][play1] != "_":
                kreten = True
            else:
                kreten = False
                assign_kolečko()
                show_plan()
                win_kolečko()


    else:
        assign_kolečko()
        show_plan()
        win_kolečko()
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
            show_plan()
            play = int(input("Jaký řádek? "))
            play1 = int(input("Jaká pozice? "))
            play -= 1
            play1 -= 1
            if plan[play][play1] != "_":
                kreten = True
            else:
                kreten = False
                assign_křížek()
                show_plan()
    else:
        assign_křížek()
        show_plan()