# Name : Hrant Babasyan
# UCID : 30224484
# Purpose of program: To create a simple pictionary game


from SimpleGraphics import * # Importing the main library


resize(800, 800) # Sizing the window to the desired size
colors = ['black', 'white', 'blue', 'green'] # Creating the desired list of colors


background_color = input(f'What color do you want the background to be? ({', '.join(colors)}):  ') # Asking for the background color
while background_color not in colors: # Checking to see if the user input is a part of the list of colors
    background_color = input(background_color+f' is not a valid option. Please pick one of the following ({', '.join(colors)}):  ') # Reprompting the user to enter a valid option
colors.remove(background_color) # Removing the chosen background color so that when asking for the foreground color,the user doesn't choose the same color


foreground_color = input(f'What color do you want the foreground to be? ({', '.join(colors)}):  ') # Asking for the foreground color
while foreground_color not in colors: # Checking to see if the user input is a part of the list of colors
    print('The foreground color must be a possible color, and cannot be the same as the background color.') # Giving a message to the user so that they understand to pick a color, and one other than the background color
    foreground_color = input(foreground_color+f' is not a valid option. Please pick one of the following ({', '.join(colors)}):  ') # Reprompting the user to enter a valid option


background(background_color) # Creating the background with the input color
setColor(foreground_color) # Setting the line color to the input color
shape = input('What shape are you going to draw:  ') # Asking the drawer for their shape
shape_guess = '' # Creating the variable to represent the guesser's guess of the shape. Will be used at the end of the program
points = [] # Creating the main list used in the program. This list represents the coordinate points given from the drawer.


def check_coordinate(coord, var): # Creating the function that checks whether the user inputted coordinate is valid or not. The coord parameter represents the value inputted from the user. The var parameter is used when asking for the coordinate point
    while True: # Loop to check the validity of the coordinate
        try: # Using this try statement to convert the inputted coordinate to an integer. In the case that this conversion results in a value error, the program will reprompt the user to enter a value that can be converted to an integer
            coord = int(coord) # Converting the coordinate into an integer
            if coord >= 0 and coord <= 800: # Checking if the coordinate is within 0-800
                return coord # Reaching the desired final destination, the coordinate point is now checked, and is returned to the variable
            else: # If the coordinate point is not within 0-800 this is what happens 
                print('Invalid input: Coordinates must be integers within 0 and 800.') # Tell the user the boundaries.
                if len(points) < 2: # Nesting an if statement within the else-if to determine the wording of the prompt. In the case that points list has less than two elements, that means that this is either the starting x or starting y coordinate
                    coord = input(f'What is the starting {var}-coordinate?: ')  # Asking the user to enter a valid number, and using the var parameter to remind them which direction the coordinate will be in
                    continue  # Continuing back through the loop
                elif len(points) >= 2: # Nesting an if statement within the else-if to determine the wording of the prompt. In the case that points list has 2 or more than two elements, that means that this is either the next x or next y coordinate
                    coord = input(f'What is the next {var}-coordinate?: ')  # Asking the user to enter a valid number, and using the var parameter to remind them which direction the coordinate will be in
                    continue  # Continuing back through the loop
        except ValueError: # This will occur in the case that the user enters a value other than an integer. This step was not necessary, however it only takes a few more lines and elevates the whole program
            print('Invalid input: Coordinates must be integers within 0 and 800.')  # Tell the user the boundaries.
            if len(points) < 2:  # Nesting an if statement within the else-if to determine the wording of the prompt. In the case that points list has less than two elements, that means that this is either the starting x or starting y coordinate
                coord = input(f'What is the starting {var}-coordinate?: ')  # Asking the user to enter a valid number, and using the var parameter to remind them which direction the coordinate will be in
                continue  # Continuing back through the loop
            elif len(points) >= 2:  # Nesting an if statement within the else-if to determine the wording of the prompt. In the case that points list has 2 or more than two elements, that means that this is either the next x or next y coordinate
                coord = input(f'What is the next {var}-coordinate?: ')  # Asking the user to enter a valid number, and using the var parameter to remind them which direction the coordinate will be in
                continue  # Continuing back through the loop


def add_point(): # Creating the function that adds the coordinate points to the points list, which is then drawn using the line() function
    global x # making the x coordinate point a global value, since it is referenced at the end of the program, and requires it to be a global variable
    x = check_coordinate(input('What is the next x-coordinate?: '), 'x') # Asking the user to give a coordinate point, which is then checked using the check_coordinate function
    points.append(x) # Adding the coordinate to the points list
    global y # making the x coordinate point a global value, since it is referenced at the end of the program, and requires it to be a global variable
    y = check_coordinate(input('What is the next y-coordinate?: '), 'y') # Asking the user to give a coordinate point, which is then checked using the check_coordinate function
    points.append(y) # Adding the coordinate to the points list
    line(points) # Drawing the points onto the window
    for i in range(len(points)): # The explanation of this loop is a bit complicated. You must subtact 1 from each element in the list of points, due to an oversight in the SimpleGraphics.py document. See line 625 in that document
        points[i] = points[i] - 1 # The line() function adds 1 to each element within any list that is its argument. To counteract this effect, we must subtract 1 from each element in the list.


x = check_coordinate(input('What is the starting x-coordinate?: '), 'x') # Asking the user to give a coordinate point, which is then checked using the check_coordinate function
points.append(x) # Adding the coordinate to the points list
y = check_coordinate(input('What is the starting y-coordinate?: '), 'y') # Asking the user to give a coordinate point, which is then checked using the check_coordinate function
points.append(y) # Adding the coordinate to the points list
print('\n'*50) # Printing 50 new lines so that the guesser doesn't know the shape


while True: # This is the main loop of the game, and when this ends the game ends
    guess_choice = input('Do you want to\n1: Get the next point\n2: Guess the shape\nEnter 1 or 2:  ') # Asking the guesser whether they want to see the next point or make their guess
    if guess_choice == '1': # If they choose 1 that means they want to see the next point
        add_point() # This calls the add_point() function which adds another point to the drawing
        if x == points[0] and y == points[1]: # This nested-if statement checks if the newly added points are the same as the original
            print(f'Game over. The shape was a {shape}.') # If they are the same, the game is over and the shape is revealed
            break # Ending the loop since the game is over
    elif guess_choice == '2': # If they choose 2 that means they want to make their guess
        shape_guess = input('What do you think the shape is?:  ') # Asking to see their guess of the shape
        if shape_guess == shape: # This if statement checks whether their guess was correct
            print(f'Correct! You guessed the shape after seeing {int(len(points)/2)} points!') # In this branch, their guess was correct, and the amount of points it took is revealed by halfing the length of the points list, since each point has 2 coordinates.
            break # Ending the loop since the game is over
        else: # This else branch means their guess would not be correct
            print(f'No, the answer is not {shape_guess}. Better luck next time!') # Tell them they are wrong, and not revealing the shape
            break  # Ending the loop since the game is over
    else: # This else branch is used in case the guesser enters a value other than 1 or 2
        print('Invalid input: Please pick either 1 or 2') # Reminding the guesser that they must pick options 1 or 2
        continue # Continuing back to the top of the loop to allow then to enter a correct input
