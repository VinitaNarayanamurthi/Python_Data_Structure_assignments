__author__ = 'Steven Carnovale and Vinita Narayanamurthi'

"""
CSCI-603: Lab 2 Assignment

 This is a program which shows the image of the forest during the day and night. 
 The night scene consists of trees, house(optional) and a star. 
 During the day time, the lumber from the tree trunks are used to 
 renovate the house and make it bigger. 
"""

import turtle
import math
import random

# global constants for window dimensions
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 1000
tree_list = ['Pine', 'Maple', 'Cedar']
Dist_btw_obj = 100
trunk_ht = []
no_of_trees = input("How many trees in your forest ? ")
print(no_of_trees)
house_exists = input("Is there a house in the forest (y/n) ? ")

#def initial_setup():  #To get the required input from the user such as number of trees and if there is any house existing.

def init():
    """
    Initialize for drawing.  (-400, -400) is in the lower left and
    (400, 400) is in the upper right.
    :pre: pos (0,0), heading (east), up
    :post: pos (0,0), heading (east), up
    :return: None
    """
    turtle.setworldcoordinates(-WINDOW_WIDTH/2, -WINDOW_WIDTH/2,
        WINDOW_WIDTH/2, WINDOW_HEIGHT/2)
    turtle.up()
    turtle.setheading(0)
    # turtle.hideturtle()
    turtle.title('Forest')
    turtle.speed(0)
    turtle.back(320)
    house_wall_ht = 100

    if(int(no_of_trees) == 0 and house_exists == 'n'):
        turtle.up()
        turtle.forward(Dist_btw_obj)
        turtle.down()
        # star_tracking(10)
    elif (int(no_of_trees) == 0 and house_exists == 'y'):
        create_house(house_wall_ht)
        turtle.up()
        turtle.left(90)
        turtle.forward(house_wall_ht + 20)
        turtle.right(90)
        turtle.down()


    elif (int(no_of_trees) == 1 and house_exists == 'n'):

        tree_type = random.choice(tree_list)
        create_tree(tree_type)
    elif (int(no_of_trees) == 1 and house_exists == 'y'):
        tree_type = random.choice(tree_list)
        create_tree(tree_type)
        create_house(house_wall_ht)

    #if(house_exists == 'y') and int(no_of_trees)>0:


       # create_house(house_wall_ht)
    # if(int(no_of_trees)==0 and house_exists == 'y'):
    #         house_wall_ht = 100
    #         create_house(house_wall_ht)
    #
    else:
        house_loc = random.randint(1, (int(no_of_trees)))
        for i in range(0,(int(no_of_trees))):
            tree_type = random.choice(tree_list)
            create_tree(tree_type)
            if (house_exists == 'y'):
                if (i == ((house_loc)-1)):

                    create_house(house_wall_ht)



def create_tree(Tree_type):
    turtle.color('brown')
    if(no_of_trees == 0):
       trunk_height = 0

    elif(Tree_type == 'Pine'):
        trunk_height = random.randint(50, 200)
    elif (Tree_type == 'Maple'):
        trunk_height = random.randint(50, 150)
    else:
        trunk_height = random.randint(50, 180)


    trunk_ht.append(trunk_height)

    turtle.down()
    turtle.left(90)
    turtle.forward(trunk_height)
    turtle.right(90)

    if(trunk_ht == 0):
        return
    else:
        create_treeTop(Tree_type, trunk_height)





def create_treeTop(Tree_type, trunk_height):
    turtle.color('green')

    if (Tree_type == 'Pine'):
        turtle.back(15)
        for i in range(0,3):
            turtle.forward(30)
            turtle.left(120)

        turtle.forward(15)
        turtle.up()
        turtle.right(90)
        turtle.forward(trunk_height)
        turtle.left(90)
        turtle.forward(Dist_btw_obj)
        turtle.down()


    elif (Tree_type == 'Maple'):
        turtle.circle(15)
        turtle.up()
        turtle.right(90)
        turtle.forward(trunk_height)
        turtle.left(90)
        turtle.forward(Dist_btw_obj)
        turtle.down()




    else:
        turtle.begin_fill()
        turtle.forward(15)
        turtle.left(90)
        turtle.circle(15,180)
        turtle.left(90)
        turtle.forward(15)
        turtle.end_fill()
        # turtle.left(180)
        turtle.up()
        turtle.right(90)
        turtle.forward(trunk_height)
        turtle.left(90)
        turtle.forward(Dist_btw_obj)
        turtle.down()







def create_house(wall_ht):

    turtle.down()
    for i in range(0,4):
        if i==2:
            turtle.up()
            turtle.forward(wall_ht)
            turtle.left(90)
        else:
            turtle.down()
            turtle.forward(wall_ht)
            turtle.left(90)
    turtle.left(90)
    turtle.forward(wall_ht)
    turtle.right(45)
    turtle.forward(math.sqrt(2)*(wall_ht/2))
    turtle.right(90)
    turtle.forward(math.sqrt(2)*(wall_ht/2))
    turtle.right(45)
    turtle.forward(wall_ht)
    turtle.left(90)
    # turtle.forward(100)
    # turtle.left(90)
    #




    turtle.up()
    turtle.forward(Dist_btw_obj)
    turtle.down()

    # turtle.left(90)
    # turtle.up()
    # turtle.forward(130)
    # turtle.down()

def star_tracking(max_ht):
    des_str_ht = max_ht+30+20
    turtle.up()
    turtle.left(90)
    turtle.forward(des_str_ht)
    # print('final star ht', des_ht)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(180)
    turtle.down()


def star():
    turtle.left(90)
    for i in range(0,8):
        turtle.forward(10)
        turtle.back(10)
        turtle.right(360/8)
        turtle.hideturtle()




def drawforest(no_of_trees):
    init()

    if (int(no_of_trees) < 1):
        max_ht = 10
    else:
        max_ht = max(trunk_ht)
    star_tracking(max_ht)
    star()



def main():
    """
    The main function.
    :pre: pos (0,0), heading (east), up
    :post: pos (0,0), heading (east), up
    :return: None
    """

    drawforest(no_of_trees)
    # print("Tree trunk height", trunk_ht)
    #print("We have " + str(sum(trunk_ht)) + " units of lumber for building")
    #
    input("Night is done, press enter for day")

    if(house_exists == 'n' and int(no_of_trees)==0  ):
        alpha = 0

    elif(house_exists == 'n' and int(no_of_trees) > 0 ):
        total_wood = sum(trunk_ht)
        alpha = total_wood / (2 + math.sqrt(2))
    else:
        total_wood = sum(trunk_ht) + (200 + (2 * (math.sqrt(2))))
        alpha = total_wood / (2 + math.sqrt(2))

    print("We have " + str(sum(trunk_ht)) + " units of lumber for building")
    print("We have built a house with walls" + str(alpha)+ "tall")
    turtle.reset()
    create_house(alpha)
    turtle.up()
    turtle.left(90)
    turtle.forward(200)
    turtle.right(90)
    turtle.down()

    turtle.circle(30)






    turtle.mainloop()

if __name__ == '__main__':
    main()
