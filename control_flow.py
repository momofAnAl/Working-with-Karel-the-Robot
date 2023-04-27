from karel.stanfordkarel import *

"""
File: main.py
--------------------
When you finish writing this file, Karel should have repaired 
each of the columns in the temple
"""

def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    #square of 5 units high
    for i in range(2):
        ascend_hurdle()
        move_to_wall()
        descend_hurdle()
        move_to_wall()
    
#ascend_hurdle
def ascend_hurdle():
    turn_left()
    put_beeper()
    for i in range(4):
        move()
        put_beeper()
    turn_right()
    
#descend_hurdle
def descend_hurdle():
    turn_right()
    for i in range(4):
        put_beeper()
        move()
    put_beeper()
    turn_left()

#move to the next arches       
def move_to_wall():
    for i in range(4):
        if front_is_clear():
            move()
            
#Turn_right            
def turn_right():
    for i in range(3):
        turn_left()
if __name__ == '__main__':
    main()