import random 
#Been a while since any python projects, lets see how this goes...
money = 100
isRunning = True
list = ["APPLE", "BANANA", "CHERRY", "DURIAN"]
mult = 1.0
while isRunning:
    print("\n"*5 +"-"*50)
    start = input('''Welcome to slots! If you know how to play, just press enter.
          If you need help, type options. If you would like to end, type q or end. or mult to spend 20 to increase the mult''')
    if(start.lower() == "options"):
        print("You can roll for whatever amount of money you like can have. Gambling is bad but also fun.")
    elif(start.lower() == "q" or start == "end"):
        isRunning = False
        break
    elif(start.lower() == "mult"):
        money -= 20
        mult += 0.1
        input("Mult is now " + str(mult))
    def roll():
        global money 
        bettingAmount = int(input("Betting amount: "))
        if(bettingAmount > money):
            print("not enough. Your Balance: " + str(money))
            return
        money -= bettingAmount
        o1 = random.choice(list)
        o2 = random.choice(list)
        o3 = random.choice(list)
        o4 = random.choice(list)
        print(o1 + " " + o2 + " " + o3 + " " + o4)
        if(o1 == o2 == o3 == o4):
            money += bettingAmount*10
        elif(o1==o2==o3):
            money += bettingAmount*2
        elif(o1==o2==o4):
            money += bettingAmount*2
        elif(o3==o2==o4):
            money += bettingAmount*2
        print("Balance: " + str(money))
        cont = input("enter \'q\' to quit, anything else to continue.")
        if(cont == "q"):
            return 
        else:
            roll()
    roll()

    def advancedroll():
        list2 = [["A", "B", "C", "D"], ["A", "B", "C", "D"], ["A", "B", "C", "D"], ["A", "B", "C", "D"]]
        random.shuffle(list2)
        print(list2[0], list2[1], list2[2], list[3])
        
    advancedroll()


