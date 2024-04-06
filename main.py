import image
from game import SLEEP
from time import sleep
from survivor import Death
from game import game
from random import randint

#Angeline Vu, CS302-001, 03/20/2024
#This file contains the main function

LOOT = 3        #Number of times loot during a day
EVENTS = 3      #Loot and mob spawns
SLEEP = 0.5     #Sleep seconds

#Main
def main():
    image.title()   #Title & description
    app = game()    
    loot = 0
    #for x in range(0, 100):
    #    app.spawn_loot(x)
    try:
        while True:
            try: 
                select1 = app.safe_menu()           #Safe Zone    
                if select1 == '1':                  #Leave safe zone
                    loot += 1
                    if loot > LOOT:
                        print("\nYou are too Fatigued to loot.")
                    else:
                        print("\nLeaving Safe Zone...")
                        image.line()
                        for i in range(0, EVENTS):
                            app.spawn_loot(randint(1,100))
                            sleep(SLEEP)
                            mob = app.spawn_mob(randint(1,100))
                            if mob is not None:
                                app.mob_menu(mob, app.weapon_menu())
                            sleep(SLEEP)
                        print("\nYou are fatigued. You make your way\nback to a safe zone.")

                elif select1 == '2':                #Open inventory
                    select2 = app.inventory_menu()
                    if select2 == '1':
                        app.consume_item()

                else:
                    app.sleep()
                    loot = 0

            #except KeyboardInterrupt:
            #    exit()

            except TypeError as e:          #Non-int
                print(e)


    except Death as e:      #Death
        print(e) 
        image.line()
        app.game_over()

    except KeyboardInterrupt:
        return

if __name__ == "__main__":
    main()