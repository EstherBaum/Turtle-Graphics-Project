# Creating Christmas Turtle Graphcis Program

import turtle
import random

# grab user input

while True :
    size = input("What size tree would you like? [small, medium, or large]: ")
    size = size.lower()
    if size == "small" :
        x = 1
        y = 1
        break
    elif size == "medium" :
        x = 2
        y = 2
        break
    elif size == "large" :
        x = 2.75
        y = 2.75
        break
    else :
        print("Sorry, that entry is invalid. Please try again")

# collect coordinates for bottom of trunk

x_coord_bottom_trunk = x*(0)
y_coord_bottom_trunk = y*(-62.5)

# Ask user for number of presents they would like under the tree.
while True :
    try :
        num_presents = int(input("How many presents would you like under the tree?: "))
        break
    except:
        print("Sorry, that input was invalid. Please try again")
        continue

# Make a list of coordinates for back and front presents

present_coord_back = []
present_coord_front = []
for i in range(num_presents) :
    if size == "small"  :
        x_pres_cor = random.randint(-4,3)*10 # multiply by 10 to space out presents
        y_pres_cor = random.randint(-9, -5)*10
        if y_pres_cor > -70 :
            present_coord_back.append((x_pres_cor,y_pres_cor))
        else :
            present_coord_front.append((x_pres_cor, y_pres_cor))
    elif size == "medium"  :
        x_pres_cor = random.randint(-85,85)
        y_pres_cor = random.randint(-195, -98)
        if y_pres_cor > -150 :
            present_coord_back.append((x_pres_cor,y_pres_cor))
        else :
            present_coord_front.append((x_pres_cor, y_pres_cor))
    else :
        x_pres_cor = random.randint(-131,131)
        y_pres_cor = random.randint(-272, -130)
        if y_pres_cor > -208 :
            present_coord_back.append((x_pres_cor,y_pres_cor))
        else :
            present_coord_front.append((x_pres_cor, y_pres_cor))

    # Sort both lists of tuples by y_pres_cord
    # this was you can add presents from back to front

    #
    present_coord_back = sorted(present_coord_back, key=lambda x: x[1], reverse=True)
    present_coord_front = sorted(present_coord_front, key=lambda x: x[1], reverse=True)




# create turtle object and screen
screen = turtle.Screen()

# create turtle, set speed, and hide it

t = turtle.Turtle()
t.speed(10)
t.hideturtle()

def scatter_presents_back(pres_coord) :
    for coord in present_coord_back :
        presents(coord[0],coord[1])

def scatter_presents_front(pres_coord) :
    for coord in present_coord_front :
        presents(coord[0],coord[1])


def presents (a,b):

    # create list of colors for presents and ribbon
    # randomly select color for present and ribbon
    # if colors are the same, choose a new color for ribbon_color
    # until it is nothte same as present_color
    color_list = ["light blue", "white", "yellow", "red", "green"]
    present_color = random.choice(color_list)
    ribbon_color = random.choice(color_list)
    if ribbon_color == present_color :
        while ribbon_color == present_color :
            ribbon_color = random.choice(color_list)

    # create range of locations for presents this needs to be done before functions are called

    # move turtle to location and set present side_length
    t.penup()
    t.goto(a,b)

    random_side = random.uniform(1,2)
    if size == "small" :
        side_length = 20*random_side
    elif size == "medium" :
        side_length = 30*random_side
    else :
        side_length = 50*random_side

    # draw and fill outside box
    t.pendown()
    t.begin_fill()
    t.goto(a+(side_length*.5), b)
    t.goto(a+(side_length * .5), b+side_length)
    t.goto(a-(side_length * .5), b+side_length)
    t.goto(a-(side_length * .5), b)
    t.goto(a,b)

    # fill box with color
    t.fillcolor(present_color)
    t.end_fill()
    t.penup()

    # draw ribbon on presents
    # set ribbon size
    r_size = random.uniform(1/9, 3/9)*side_length

    # set beginning coordinates for horizontal ribbon
    t.goto(a+(side_length*.5),b+(side_length*.5)-(1/2)*r_size)

    # start fill
    t.begin_fill()
    t.pendown()

    #draw horizontal ribbon
    t.goto(a-(side_length * .5), b+(side_length*.5)-(1/2)*r_size)
    t.goto(a-(side_length * .5), b+(side_length*.5)+(1/2)*r_size)
    t.goto(a+(side_length * .5), b+(side_length*.5)+(1/2)*r_size)
    t.goto(a+(side_length * .5), b+(side_length*.5)-(1/2)*r_size)

    # end fill with green
    t.fillcolor(ribbon_color)
    t.end_fill()
    t.penup()

    # start coordinates for vertical ribbon
    t.goto(a+((1/2)*(r_size)),b)

    # start fill
    t.begin_fill()
    t.pendown()

    # draw vertical ribbon
    t.goto(a+((1/2)*(r_size)),b+(side_length))
    t.goto(a-((1/2)*(r_size)),b+(side_length))
    t.goto(a-((1/2)*(r_size)),b)
    t.goto(a+((1/2)*(r_size)),b)

    # end fill with ribbon color
    t.fillcolor(ribbon_color)
    t.end_fill()
    t.penup()

def tree_skirt(x,a,b) :  # x is tree_size, a and b are x and y coordinates for bottom of tree skirt
    # put turtle a bit below the tree trunk
    t.penup()
    t.goto(a,b)
    t.pendown()
    # fill color of skirt with red
    t.begin_fill()

    # draw a flattened circle
    t.setheading(0)
    # rug_bottom = t.pos()
    t.circle(x*120, 25)
    t.circle(x*20,65)
    # rug_right = t.pos()
    t.circle(x*20,65)
    t.circle(x*120, 25)
    # rug_top = t.pos()
    t.circle(x*120, 25)
    t.circle(x*20,65)
    # rug_left = t.pos()
    t.circle(x*20,65)
    t.circle(x*120, 25)

    t.fillcolor("#D2042D")
    t.end_fill()

def draw_tree(x,y) :

    # Draw left side
    t.penup()
    t.setposition(0,y*(100))
    t.begin_fill()

    # prepare to draw left side
    t.pendown()
    t.begin_fill()

    # draw left side
    t.goto(x*(22.5),y*(60))
    t.goto(x*(12.5),y*(60))
    t.goto(x*(37.5),y*(10))
    t.goto(x*(25),y*(10))
    t.goto(x*(60),y*(-55))
    t.goto(x*(0),y*(-55))

    # prepare to draw right side
    t.penup()
    t.setposition(0, y*(100))
    t.pendown()

    #draw right side
    x = -x
    t.goto(x*(22.5),y*(60))
    t.goto(x*(12.5),y*(60))
    t.goto(x*(37.5),y*(10))
    t.goto(x*(25),y*(10))
    t.goto(x*(60),y*(-55))
    t.goto(x*(0),y*(-55))
    t.penup()

    # end fill with dark green
    t.fillcolor("dark green")
    t.end_fill()

    # draw trunk
    # beginning trunk location
    t.goto(x*(7.5),y*(-55))

    # begin trunk fill
    t.begin_fill()

    # draw trunk
    t.goto(x*(7.5), y*(-70))
    t.goto(x*(-7.5), y*(-70))
    t.goto(x*(-7.5), y*(-55))
    t.goto(x*(7.5), y*(-55))

    # fill with brown
    t.fillcolor("brown")
    t.end_fill()

def star_circle(tree_top_x, tree_top_y) :
    t.penup()
    t.goto(tree_top_x,tree_top_y)

    # invisible star to collect coordinates

    outer_star_point_1 = t.pos()
    t.circle(20,72)
    outer_star_point_2 = t.pos()
    t.circle(20, 72)
    outer_star_point_3 = t.pos()
    t.circle(20, 72)
    outer_star_point_4 = t.pos()
    t.circle(20, 72)
    outer_star_point_5 = t.pos()
    t.circle(20, 72)
    t.left(90)
    t.forward(10)
    t.right(90)
    t.circle(10,36)
    inner_star_point_1 = t.pos()
    t.circle(10,72)
    inner_star_point_2 = t.pos()
    t.circle(10, 72)
    inner_star_point_3 = t.pos()
    t.circle(10, 72)
    inner_star_point_4 = t.pos()
    t.circle(10, 72)
    inner_star_point_5 = t.pos()
    t.circle(10,36)

    # make star with coordinates
    t.goto(outer_star_point_1)
    t.pendown()
    t.begin_fill()

    # start drawing star
    t.goto(inner_star_point_1)
    t.goto(outer_star_point_2)
    t.goto(inner_star_point_2)
    t.goto(outer_star_point_3)
    t.goto(inner_star_point_3)
    t.goto(outer_star_point_4)
    t.goto(inner_star_point_4)
    t.goto(outer_star_point_5)
    t.goto(inner_star_point_5)
    t.goto(outer_star_point_1)

    # color star yellow
    t.fillcolor("yellow")
    t.end_fill()



def main() :
    tree_skirt(x, x_coord_bottom_trunk, y_coord_bottom_trunk - y * 40)
    scatter_presents_back(present_coord_back)
    draw_tree(x,y)
    star_circle(x-2,(y*100)-1)
    scatter_presents_front(present_coord_front)

main()

# exit screen
screen.exitonclick()