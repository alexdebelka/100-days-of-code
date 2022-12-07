print('''                 _
                ;`',
                `,  `,
                 ',   ;   ,,-""==..,
                  \    ','          \
          ,-""'-., ;    '    __.-="-.;
        ," ,,_    "V      _."
       ;,'   ''-,          "=--,_
              ,-''    _  _       `,
             /   ,.-+(_)(_)�--.,   ;
            ,'  /   ; (_)       `\ ,
            ; ,/    ;._.;         ;
            !,'     ;   ;
            V'      ;   ;
                    ;._.;
                    ;   ;
                    ;   ;        ~
     ~              ;._.;
               ~    ;   ;
                   .�   `.                ~
             __,.--;.___.;--.,___
       _,,-""      ;     ;       ""-,,_
   .-��            ;     ;             ``-.
  ",              �       `               ,"        ~
    "-_                                _-"
~       ``----..,_          __,,..bmw-�
                  ```''''���                  ~''')
print("Welcome to Treasure Island. Your mission is to find the treasure")
print("Let's start")
option1=input("Where do you want to go? Left or Right?\n").lower()
if option1=="left":
    option2=input("You arrived at the magical lake. Do you want to swim or wait for a boat? Type 'swim' or 'wait' \n").lower()
    if option2=="wait":
        option3=input("You just passed the lake and arrived at 3 mythical doors! Choose between the blue, yellow and green door only by typing the color\n").lower()
        if option3=="yellow":
            print("You have won!!! You got 1000 gold")
        elif option3=="red":
            print("You burned by fire. Game over")
        elif option3=="blue":
            print("You got eaten by beasts. Game over.")
        else:
            print("Game over.")
    else:
        print("You have been attacked by invisible sharks")
else:
    print("You fall into a hole. Game Over")