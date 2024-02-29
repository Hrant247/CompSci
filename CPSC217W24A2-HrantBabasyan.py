# Name : Hrant Babasyan
# UCID : 30224484
# Purpose of program: sjdbljdacsacaljbd

from SimpleGraphics import *


# resize(800, 800)
# colors = ['black', 'white', 'blue', 'green']
#
#
# background_color = input(f'What color do you want the background to be? ({', '.join(colors)}):  ')
# while background_color not in colors:
#     background_color = input(background_color+f' is not a valid option. Please pick one of the following ({', '.join(colors)}):  ')
# colors.remove(background_color)
#
#
# foreground_color = input(f'What color do you want the foreground to be? ({', '.join(colors)}):  ')
# while foreground_color not in colors:
#     print('The foreground color must be a possible color, and cannot be the same as the background color.')
#     foreground_color = input(foreground_color+f' is not a valid option. Please pick one of the following ({', '.join(colors)}):  ')
#
#
# background(background_color)
# setColor(foreground_color)
#
# shape = input('What shape are you going to draw:  ')
# print('\n'*50)
background('black')
setColor('blue')
points = []
def check_coordinate(var, var_name):
    while True:
        try:
            var = int(var)
            if var >= 0 and var <= 800:
                var_name = var
                return var_name
            else:
                print('Invalid input: Coordinates must be integers between 0 and 800.')
                var = input(f'What is the starting {var_name}-coordinate?: ')
                continue
        except ValueError:
            print('Invalid input: Coordinates must be integers between 0 and 800.')
            var = input(f'What is the starting {var_name}-coordinate?: ')
            continue
def add_point():
    global x
    x = check_coordinate(input('What is the next x-coordinate?: '), 'x')
    points.append(x)
    global y
    y = check_coordinate(input('What is the next y-coordinate?: '), 'y')
    points.append(y)
    if x == points[0] and y == points[1]:
        print("works")


x = check_coordinate(input('What is the starting x-coordinate?: '), 'x')
points.append(x)
y = check_coordinate(input('What is the starting y-coordinate?: '), 'y')
points.append(y)
print(points, x, y)
add_point()
line(points)
add_point()
line(points)
add_point()
line(points)
add_point()
print(points, x, y)
line(points)
print(points, x, y)
