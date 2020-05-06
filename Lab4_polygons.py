


import turtle
tur=turtle.Turtle()
tur.speed(1000)

# def init_turtle():
#
#
#     turtle.setworldcoordinates(-1000/2, -1000/2,
#         1000/2,1000/2)
#     turtle.up()
#     turtle.setheading(0)
#
#     turtle.title('Polygon')
#     size = 100
#     segment = input("Enter the Depth value: ")
#
#     if segment.isdecimal():
#         drawstar1(int(segment), size, turtle)
#     else:
#         print("Error .. Program Terminating ")
#         exit()
#







def polygons(no_of_side, size, turtle ):
    color = ["red", "orange", "yellow", "green", "blue", "blueviolet", "violet", "bluegreen"]
    sum = 0
    total = 0

    if no_of_side <=2:
        pass

    else:

        for i in range(no_of_side):
            sum += size
            turtle.pencolor(color[no_of_side-1])
            # turtle.color([no_of_side-1])
            turtle.begin_fill()
            turtle.forward(size)
            turtle.back((3/4)*size)
            polygons(no_of_side-1, size/2,  turtle)
            turtle.pencolor(color[no_of_side - 1])
            # turtle.color([no_of_side - 1])
            turtle.begin_fill()

            turtle.forward((3/4)*size)
            turtle.left(360 / no_of_side)
            turtle.end_fill()
        total += sum
        print(sum)
        print(total)




    # turtle.speed(0)
    # color = ["blue", "red", "green"]
    #
    # if segment == 0:
    #     pass
    # else:
    #     for i in range(0,6):
    #         turtle.down()
    #         if segment % 2 == 0:
    #             turtle.pencolor(color[1])
    #         elif segment == 1:
    #             turtle.pencolor(color[0])
    #         else:
    #             turtle.pencolor(color[2])
    #         turtle.forward(size)
    #
    #         drawstar1(segment-1, size/3, turtle)
    #         if segment % 2 == 0:
    #             turtle.pencolor(color[1])
    #         elif segment == 1:
    #             turtle.pencolor(color[0])
    #         else:
    #             turtle.pencolor(color[2])
    #         turtle.up()

    #         turtle.back(size)
    #         turtle.right(60)
            # print ("The current segment is "+str(segment-1))

polygons(4, 200,  tur)
turtle.mainloop()


#
#
# def main():
#     init_turtle()
#     turtle.mainloop()
#
#
# if __name__ == '__main__':
#         main()