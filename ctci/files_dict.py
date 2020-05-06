# #!/usr/bin/env python3
# # Square code !!
# import turtle
#
# # --- functions ---
#
# def s(n, l):
#
#     if n == 0: # stop conditions
#
#         # draw filled rectangle
#
#
#         for _ in range (4):
#             turtle.forward(l)
#             turtle.left(90)
#
#
#     else: # recursion
#
#         # around center point create 8 smalles rectangles.
#         # create two rectangles on every side
#         # so you have to repeat it four times
#
#         for _ in range(1):
#             # first rectangle
#             s(n-1, l/3)
#             turtle.forward(l)
#             turtle.left(90)
#             turtle.forward(l)
#             turtle.left(90)
#             s(n-1, l/3)
#             turtle.forward(l)
#             turtle.left(90)
#             turtle.forward(l)
#             turtle.left(90)
#
#
#         # update screen
#         turtle.update()
#
# # --- main ---
#
# # stop updating screen (to make it faster)
# # turtle.tracer(0)
#
# # start
# s(3, 200)
#
# # event loop
# turtle.done()


## Triangle code:

# !/usr/bin/env python3
#
# import turtle
#
#
# # --- functions ---
#
# def s(n, l):
#     if n == 0:  # stop conditions
#
#         # draw filled rectangle
#
#         for _ in range(3):
#             turtle.forward(l)
#             turtle.left(120)
#
#
#     else:  # recursion
#
#         # around center point create 8 smalles rectangles.
#         # create two rectangles on every side
#         # so you have to repeat it four times
#
#         for _ in range(3):
#             # first rectangle
#
#             turtle.forward(l)
#             s(n-1, l/2)
#             turtle.left(120)
#         # update screen
#         turtle.update()
#
#
# # --- main ---
#
# # stop updating screen (to make it faster)
# # turtle.tracer(0)
#
# # start
# s(3, 200)
#
# # event loop
# turtle.done()


## Sierpinski triangle


# import turtle
#
#
# # --- functions ---
#
# def s(n, l):
#     if n == 0:  # stop conditions
#
#         # draw filled rectangle
#
#         for _ in range(3):
#             turtle.forward(l)
#             turtle.left(120)
#
#
#     else:  # recursion
#
#         # around center point create 8 smalles rectangles.
#         # create two rectangles on every side
#         # so you have to repeat it four times
#
#         for _ in range(1):
#             # first rectangle
#
#             s(n - 1, l / 2)
#             turtle.forward(l/2)
#             s(n-1, l/2)
#             turtle.forward(l/2)
#             turtle.left(120)
#             turtle.forward(l/2)
#             s(n-1, l/2)
#             turtle.left(60)
#             turtle.forward(l/2)
#             turtle.left(60)
#             turtle.forward(l/2)
#             turtle.left(120)
#         # update screen
#         turtle.update()
#
#
# # --- main ---
#
# # stop updating screen (to make it faster)
# # turtle.tracer(0)
#
# # start
# s(2, 200)
#
# # event loop
# turtle.done()


## Star:

import turtle


# --- functions ---

def s(n, l):
    if n == 0:  # stop conditions

        # draw filled rectangle

       pass

    else:  # recursion

        # around center point create 8 smalles rectangles.
        # create two rectangles on every side
        # so you have to repeat it four times
        #
        for _ in range(5):


            turtle.forward(l)
            s(n-1, l/3)

            turtle.left(180)

            turtle.left(36)

        # update screen
        turtle.update()


# --- main ---

# stop updating screen (to make it faster)
# turtle.tracer(0)

# start
s(2, 200)

# event loop
turtle.done()


