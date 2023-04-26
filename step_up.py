# This tells PyCharm who Karel is
# Every Karel file has a line just like it
from karel.stanfordkarel import *

# this program executes in a special function called main
def main():
    move()
    pick_beeper()
    turn_left()
    move()
    #turn right
    turn_right()
    move()
    move()
    put_beeper()
    move()
    
def turn_right():
    turn_left()
    turn_left()
    turn_left()


# This is "boilerplate" code which launches your code
# when you hit the run button
if __name__ == '__main__':
    main()
