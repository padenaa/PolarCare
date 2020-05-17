#imports:
from graphics import *
import random
import math
import os
import time
import webbrowser

#creating window
win=GraphWin("PolarCare",350,600)
win.setBackground("white")

polar_image= Image(Point(350/2,200), "polarbike.png")
polar_image.draw(win)

title= Text(Point(350/2,50), "POLAR CARE")
title.setFill("light blue")
title.setSize(36)
title.setStyle("bold")
title.draw(win)

file = open("coins.txt")
coins = int(file.read());#THIS IS SET AT 75 FOR DEMO PURPOSES ONLY
file.close()
timer = 0;

#start timer:
start = Rectangle (Point(100,350),Point(250, 400))
start.setFill("light blue")
start.setOutline("cyan3")
start.setWidth(5)

start_text=Text(Point(175,375), "START TIMER")#must be updated everytime coin value changes
start_text.setFill("cyan3")
start_text.setStyle("bold")

#store:
store = Rectangle (Point(100,425),Point(250, 475))
store.setFill("light blue")
store.setOutline("cyan3")
store.setWidth(5)

store_text=Text(Point(175,450), "STORE")#must be updated everytime coin value changes
store_text.setFill("cyan3")
store_text.setStyle("bold")

#home:
home = Rectangle (Point(0,570),Point(70, 600))
home.setFill("light blue")
home.setOutline("cyan3")
home.setWidth(2)

home_text=Text(Point(35,585), "HOME")#must be updated everytime coin value changes
home_text.setFill("cyan3")
home_text.setStyle("bold")

#coins
money = Rectangle (Point(280,570),Point(350, 600))
money.setFill("light blue")
money.setOutline("cyan3")
money.setWidth(2)


money_text=Text(Point(305,585), ("$" + str(coins)))#must be updated everytime coin value changes
money_text.setFill("cyan3")
money_text.setStyle("bold")

#TIMER
time_display= Text(Point(175, 450), "time (mins): " + str(timer))
time_display.setFill("light blue")
time_display.setSize(25)

end_text=Text(Point(175,375), "END TIMER")#must be updated everytime coin value changes
end_text.setFill("cyan3")
end_text.setStyle("bold")

######SHOP######
#donate:
donate_text=Text(Point(175,375), "DONATE (free)")#must be updated everytime coin value changes
donate_text.setFill("cyan3")
donate_text.setStyle("bold")

#fact:
fact_text=Text(Point(175,450), "BEAR FACT ($5)")#must be updated everytime coin value changes
fact_text.setFill("cyan3")
fact_text.setStyle("bold")

fact_arr = ["there are only around 31,000 polar bears left in the world", "there are approximately 16,000 polar bears in Canada", "By 2050, there’ll be approx. a one-third decline in polar bear population", "sea ice is melting at 13% per decade leading to many starving polar bears", "polar bears are losing weight which decreases chances of surviving summer"]
pic_arr = ["1.gif", "2.gif", "3.gif", "4.gif", "5.gif"]

fact_counter = 0;

#mini-game: --> open a new window for this
game = Rectangle (Point(100,500),Point(250, 550))
game.setFill("light blue")
game.setOutline("cyan3")
game.setWidth(5)

game_text=Text(Point(175,525), "MINI GAME ($50)")#must be updated everytime coin value changes
game_text.setFill("cyan3")
game_text.setStyle("bold")

#######################################################
#back end
in_home = True
while True: #repeat the program
    #update the number of coins in text file:
    file = open("coins.txt", "w")
    file.write(str(int(coins)))
    file.close()
    
    in_home = True
    in_store = True
    start.undraw()
    start_text.undraw()
    store.undraw()
    store_text.undraw()
    money.undraw()
    money_text.undraw()
    time_display.undraw()
    donate_text.undraw()
    game.undraw()
    game_text.undraw()
    fact_text.undraw()
    
    start.draw(win)
    start_text.draw(win)
    store.draw(win)
    store_text.draw(win)
    money.draw(win)
    money_text.draw(win)
    while (in_home): #home page
        time_display.undraw()
        end_text.undraw()
        click = win.getMouse()
        #timer
        if 100 < click.getX() < 250 and 350 < click.getY() < 400:
            start_time = time.time()
            in_home = False
            start_text.undraw()
            store_text.undraw()
            store.undraw()
            home.undraw()
            home_text.undraw()
            end_text.draw(win)
            
            in_timer = True;
            while in_timer:
                click2 = win.getMouse()                
                if 100 < click2.getX() < 250 and 350 < click.getY() < 400: #if end timer was clicked
                    end_time = time.time()
                    timer= end_time - start_time
                    timer = timer/60
                    timer = round(timer, 0) #calcular the time and round it
                    time_display= Text(Point(175, 450), "time (mins): " + str(timer))
                    time_display.setFill("light blue")
                    time_display.setSize(25)
                    time_display.draw(win)

                    in_timer = False
                    time.sleep(2)

                    #update coins:
                    coins = coins + timer
                    money_text=Text(Point(305,585), ("$" + str(coins)))#must be updated everytime coin value changes
                    money_text.setFill("cyan3")
                    money_text.setStyle("bold")
                    money_text.draw(win)
                    

        #store
        if 100 < click.getX() < 250 and 425 < click.getY() < 475: 
            
            in_home = False
            in_store = True;
            start_text.undraw()
            store_text.undraw()
            
            home.draw(win)
            home_text.draw(win)
            donate_text.draw(win)
            fact_text.draw(win)
            if (fact_counter >= 5):
                fact_text.undraw()
                store.undraw()
            game.draw(win)
            game_text.draw(win)
            
            while in_store:
                click2 = win.getMouse()
                if 0 < click2.getX() < 70 and 570 < click2.getY() < 600: #home button
                    in_store = False
                elif 100 < click2.getX() < 250 and 350 < click2.getY() < 400 :#donate button
                    #INSERT LINK TO DONATE
                    webbrowser.open("https://polarbearsinternational.org/donate/ca/")
                elif 100 < click2.getX() < 250 and 425 < click2.getY()< 475 and coins >= 5 and fact_counter < 5:#fact button
                    #Give random fact and check that they have correct $ and subtract
                    win_fact=GraphWin("Random Fact",350,600) #make a new window
                    win_fact.setBackground("light blue")
                    #display the fact:
                    random_picture = Image(Point(175, 250), str(pic_arr[fact_counter]))
                    random_fact = Text(Point(175, 400), str(fact_arr[fact_counter]))
                    random_fact.setSize(7)
                    random_fact.setStyle("bold")
                    random_picture.draw(win_fact)
                    random_fact.draw(win_fact)
                    time.sleep(5)
                    win_fact.close()
                    fact_counter = fact_counter+1
                    coins = coins - 5
                    money_text.undraw()
                    money_text=Text(Point(305,585), ("$" + str(coins)))#must be updated everytime coin value changes
                    money_text.setFill("cyan3")
                    money_text.setStyle("bold")
                    money_text.draw(win)
                    
                elif 100 < click2.getX() < 250 and 500 < click2.getY() < 550 and coins >= 20: #game button
                    win_game = GraphWin("Mini Game",350,600) #make a new window
                    win_game.setBackground("light blue")
                    won=False
                    instructions = Text(Point(175, 500), "catch 10 seals before all the ice melts!")
                    instructions.setSize(15)
                    instructions.draw(win_game)
                    ice = Circle (Point(175, 300), 125)
                    ice.setFill("white")
                    ice.setOutline("white")
                    ice.draw(win_game)
                    polar_bear = Image(Point(175,300), "bear.png")
                    polar_bear.draw(win_game)
                    #drop some seals: collect them
                    items = 0;
                    x = 0
                    y = 0
                    k = 1
                    time.sleep(2)
                    for i in range (13):
                        x=random.randint(50,300)
                        y=0
                        seal = Image(Point(x,y), "seal.png")
                        for j in range(120):
                            j+j+1
                            seal.move(0,5)
                            seal.draw(win_game)
                            time.sleep(.04)
                            seal.undraw()
                            y=y+5
                            click3 = win_game.checkMouse()
                            #caught or not?
                            if  click3 != None and x-50 < click3.getX() < x+50 and y-41 < click3.getY() < y+41:
                                items = items +1
                                instructions.undraw()
                                instructions = Text(Point(175, 500), "items caught: " + str(items))
                                instructions.draw(win_game)
                                break
                            elif click3 != None:
                                break
                        if items >= 10: #condition for winning
                            won = True
                            break
                        ice.undraw()
                        ice = Circle (Point(175, 300), 125-(5*k))
                        ice.setFill("white")
                        ice.setOutline("white")
                        ice.draw(win_game)
                        polar_bear = Image(Point(175,300), "bear.png")
                        polar_bear.draw(win_game)
                        k=k+1
                        i+i+1

                    #say whether they won or not: 
                    if won:
                        instructions.undraw()
                        instructions = Text(Point(175, 500), "You won!")
                        instructions.draw(win_game)
                    else:
                        instructions.undraw()
                        instructions = Text(Point(175, 500), "You lost!")
                        instructions.draw(win_game)
                    
                    time.sleep(2)
                    win_game.close()
                    coins = coins - 50
                    money_text.undraw()
                    money_text=Text(Point(305,585), ("$" + str(coins)))#must be updated everytime coin value changes
                    money_text.setFill("cyan3")
                    money_text.setStyle("bold")
                    money_text.draw(win)
