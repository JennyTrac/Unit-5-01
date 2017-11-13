# created by Jenny Trac
# created on Nov 13 2017
# program generates 10 random numbers and calculates their average

import ui
from numpy import random

# create array
random_numbers = []

def generate_touch_up_inside(sender):
    # generates 10 random numbers
    
    global random_numbers
    
    # clears the labels and textfields
    random_numbers = []
    view['randomnumbers_textview'].text = " "
    view['average_label'].text = " "
    
    for new_random_number in range(0, 10):
        new_random_number = random.randint(1, 100+1)
        random_numbers.append(new_random_number)
        view['randomnumbers_textview'].text = view['randomnumbers_textview'].text + '\r' + str(new_random_number)
    

def calculate_average_touch_up_inside(sender):
    
    total = 0
    for new_random_number in random_numbers:
        total = total + new_random_number
    average = total / len(random_numbers)
    view['average_label'].text = "The average is: " + str(average)


view = ui.load_view()
view.present('sheet')
