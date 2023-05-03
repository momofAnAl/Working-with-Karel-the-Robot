from karel.stanfordkarel import *

"""
Karel should fill the whole world with beepers.
"""


def main():
    """
    pre: Karel is facing East
    post: Karel is facing east for the next row
    """
    #while right_is_blocked():
    for i in range(4):
        safe_put()
        return_to_first_col()
        change_to_next_row()
    safe_put()
    put_beeper()
        
    
        
#safe put function so Karen can put beeper 
def safe_put():
    #put_beeper()
    while front_is_clear():
       put_beeper()
       move()
       
       
# return to first column:      
            
def return_to_first_col():
    turn_opposite()
    put_beeper()
    while facing_west() and front_is_clear():
        move()
        
        
#change to next row:
def change_to_next_row():
    while facing_west():
        if front_is_blocked():
            turn_right()
            move()
            turn_right()
        
# turn to face the opposite direction
def turn_opposite():
    for i in range(2):
        turn_left()
        
def turn_right():
    for i in range(3):
        turn_left()


# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()