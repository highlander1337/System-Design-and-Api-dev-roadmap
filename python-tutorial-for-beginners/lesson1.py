# This is a single-line comment.
# It explains what the following line of code is intended to do.

"""
This is a docstring.
Docstrings provide important information about the purpose, inputs, and outputs
of functions, methods, or classes.

See PEP 0257 for more information on docstrings:
https://peps.python.org/pep-0257/

Should be noticed that docstrings aren't comments, they are multiple line
strings that was not assigned to any variable. So it will be ignored at 
runtime.

According to the Python PEP 8 Style Guide, there are several things to keep in mind while writing comments:

1. Comments should always be complete and concise sentences.
2. It’s better to have no comment at all than one that’s difficult to understand or inaccurate.
3. Comments should be updated regularly to reflect changes in your code.
4. Too many comments can be distracting and reduce code quality. Comments aren’t needed where the code’s purpose is obvious.

Reference: https://peps.python.org/pep-0008/


Furthemore, comments can provide content for our documentation by using document generators like https://www.sphinx-doc.org/en/master/.

"""


# def print_hello_world():
#     """
#         This function prints the classic phrase "Hello, World!" to the console.
#         It does not return any value.
        
#         Arguments:
#         None
#     """
#     # Store the message "Hello, World!" in a variable
#     message = "Hello, World!"
#     # Print the message to the console
#     print(message)

# print_hello_world()


""" 
5 Simple rules, ref: https://kinsta.com/blog/python-comments/

1. Avoid the obvious

x1 = 0
# Bad comment
x1 = x1 + 4 # Increase x by 4

x2 = 0
# Good comment
x2 = x2 + 4 # Increase the border width

2. Keep it simple

# Bad comment
# return area by performing, Area of cylinder = (2*PI*r*h) + (2*PI*r*r)
def get_area(r,h):
    return (2*3.14*r*h) + (2*3.14*r*r)

# Good comment
# return area of cylinder
def get_area(r,h):
    return (2*3.14*r*h) + (2*3.14*r*r)
    
3. Use indentifiers carefully

# Bad comment
# return class() after modifying argument
def func(cls, arg):
    return cls(arg+5)
    
# Good comment
# return cls() after modifying arg
def func(cls, arg):
    return cls(arg+5)
    
4. DRY (Don't Repeat Yourself) and avoid WET (Write Everything Twice)

# Bad comment
# function to do x work
def do_something(y):
    # x work cannot be done if y is greater than max_limit
    if y < 400:
      print('doing x work')

# Good comment
# function to do x if arg:y is less than max_limit
def  do_something(y):
    if y in range(400):
        print('doing x work')

5. Consistent identation

# Bad comment
for i in range(2,20, 2):
# only even numbers
    if verify(i):
# i should be verified by verify()
        perform(x)
        
# Good comment
# only even numbers
for i in range(2,20, 2):
    # i should be verified by verify()
    if verify(i):
        perform(x)

"""


import pygame
import sys
from pygame.locals import *
import random

pygame.init()

FPS = 60
fpsClock = pygame.time.Clock()
WINDOW_WIDTH = 1280  # Width of the game window (HD resolution)
WINDOW_HEIGHT = 720  # Height of the game window (HD resolution)

LEFT_EDGE_MAX = 10
RIGHT_EDGE_MAX = WINDOW_WIDTH - 120
BOTTOM_EDGE_MAX = WINDOW_HEIGHT - 120
TOP_EDGE_MAX = 10

# This creates the game window where everything will be shown
DISPLAYSURF = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)
pygame.display.set_caption('Cat Catch Game with Lists')

WHITE = (255, 255, 255)  # RGB color for white

# Path where the image files are stored
RESOURCES_PATH = "D:/workspace/System-Design-and-Api-dev-roadmap/python-tutorial-for-beginners/resources/"

# Load the cat image that the player controls
catImg = pygame.image.load(RESOURCES_PATH + "cat.png")

# Randomly place the cat somewhere on the screen initially
catx = random.randint(LEFT_EDGE_MAX + 100, RIGHT_EDGE_MAX - 100)  # Integer position on X-axis
caty = random.randint(TOP_EDGE_MAX + 100, BOTTOM_EDGE_MAX - 100)  # Integer position on Y-axis

# The cat's position on the screen is stored using integers because positions are whole numbers
# We use floats when calculating sizes or coordinates involving division for precision
CAT_HIT_BOX_X_SIZE = 80.0  # Width of the cat's hitbox (float)
CAT_HIT_BOX_Y_SIZE = 80.0  # Height of the cat's hitbox (float)
CAT_HIT_BOX_X_OFFSET = 40  # Offset for hitbox positioning (integer)
CAT_HIT_BOX_Y_OFFSET = 40

prey_name = None  # Current prey's name (string or None if no prey)
cat_image_path = RESOURCES_PATH + "cat.png"  # File path stored as string

prey_is_not_selected = True  # Flag to check if prey is currently selected or not
CAT_PREY_HIT_BOX_COLLISION_RATIO = 0.75  # Float ratio for collision check

# List of all available prey image paths so the game can pick one randomly
PREYS = [
    RESOURCES_PATH + "rat.png",
    RESOURCES_PATH + "squirrel.png",
    RESOURCES_PATH + "spider.png",
    RESOURCES_PATH + "bird.png",
    RESOURCES_PATH + "lizard.png"
]

# List of the cat's hitbox corner points (each point is [x, y])
cat_hit_box = [[0, 0], [0, 0], [0, 0], [0, 0]]

PREY_HIT_BOX_X_SIZE = 48.0
PREY_HIT_BOX_Y_SIZE = 48.0
PREY_HIT_BOX_X_OFFSET = 24
PREY_HIT_BOX_Y_OFFSET = 24

# List to keep the last 3 caught prey names (history)
prey_history = []

# List to keep track of cat's previous positions for undo feature
movement_history = []

# List to keep scores of this game session (like a leaderboard)
score_log = []

# List to remember positions where prey were caught (for possible replay or stats)
caught_prey_positions = []

# List for special rewards earned during the game
special_rewards = []

# List to log frame timestamps (used to track time in the game)
frame_timeline = []

score = 0  # Player's score (integer)

# Font to display text on screen
font = pygame.font.Font(None, 36)

# -----------------------------------------
# Main game loop starts here
# -----------------------------------------
while True:
    DISPLAYSURF.fill(WHITE)  # Clear screen with white color (tuple)

    # Keep track of frame timestamps using pygame's get_ticks (returns int milliseconds)
    frame_timeline.append(pygame.time.get_ticks())
    if len(frame_timeline) > 100:  # Keep only the last 100 timestamps to save memory
        frame_timeline.pop(0)  # Remove the oldest timestamp from the list

    for event in pygame.event.get():
        if event.type == QUIT:
            # When quitting, save the score in the score log list and print leaderboard
            score_log.append(score)
            print("Leaderboard (this session):", sorted(score_log, reverse=True))
            print("Special Rewards Earned:", special_rewards)
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:
            keys = pygame.key.get_pressed()

            # Movement keys: store previous position in a list before moving (undo feature)
            if keys[K_RIGHT]:
                movement_history.append((catx, caty))  # Save previous position (tuple)
                catx += 10
                if catx >= RIGHT_EDGE_MAX:
                    catx -= 10
            elif keys[K_DOWN]:
                movement_history.append((catx, caty))
                caty += 10
                if caty >= BOTTOM_EDGE_MAX:
                    caty -= 10
            elif keys[K_LEFT]:
                movement_history.append((catx, caty))
                catx -= 10
                if catx <= LEFT_EDGE_MAX:
                    catx += 10
            elif keys[K_UP]:
                movement_history.append((catx, caty))
                caty -= 10
                if caty <= TOP_EDGE_MAX:
                    caty += 10
            elif keys[K_u]:  # Undo last movement if possible
                if movement_history:
                    catx, caty = movement_history.pop()  # Pop last position tuple from list
            elif keys[K_c]:
                print(cat_hit_box)  # Debug print hitbox coordinates

    # Update the cat's hitbox coordinates based on the current cat position (using floats)
    cat_hit_box[0][0] = catx - CAT_HIT_BOX_X_SIZE / 2 + CAT_HIT_BOX_X_OFFSET
    cat_hit_box[0][1] = caty - CAT_HIT_BOX_Y_SIZE / 2 + CAT_HIT_BOX_Y_OFFSET
    cat_hit_box[1][0] = catx + CAT_HIT_BOX_X_SIZE / 2 + CAT_HIT_BOX_X_OFFSET
    cat_hit_box[1][1] = caty - CAT_HIT_BOX_Y_SIZE / 2 + CAT_HIT_BOX_Y_OFFSET
    cat_hit_box[2][0] = catx + CAT_HIT_BOX_X_SIZE / 2 + CAT_HIT_BOX_X_OFFSET
    cat_hit_box[2][1] = caty + CAT_HIT_BOX_Y_SIZE / 2 + CAT_HIT_BOX_Y_OFFSET
    cat_hit_box[3][0] = catx - CAT_HIT_BOX_X_SIZE / 2 + CAT_HIT_BOX_X_OFFSET
    cat_hit_box[3][1] = caty + CAT_HIT_BOX_Y_SIZE / 2 + CAT_HIT_BOX_Y_OFFSET

    # Draw the cat image on the screen at the current position (catx, caty are integers)
    DISPLAYSURF.blit(catImg, (catx, caty))
    # You can also draw the hitbox polygon for debugging:
    # pygame.draw.polygon(DISPLAYSURF, (0, 255, 255), cat_hit_box)

    # If no prey selected, choose one randomly from the PREYS list
    if prey_is_not_selected:
        prey_path = PREYS[random.randint(0, len(PREYS) - 1)]  # Pick a random string from list

        # Extract the prey name from the file path string
        prey_name = prey_path.split("/")[-1].split(".")[0]

        # Load the prey image (surface object)
        prey = pygame.image.load(prey_path)

        # Randomly place prey somewhere on the screen (integers)
        prey_x = random.randint(LEFT_EDGE_MAX + 100, RIGHT_EDGE_MAX - 100)
        prey_y = random.randint(TOP_EDGE_MAX + 100, BOTTOM_EDGE_MAX - 100)

        # Update prey hitbox (list of lists of floats)
        prey_hit_box = [[0, 0], [0, 0], [0, 0], [0, 0]]
        prey_hit_box[0][0] = prey_x - PREY_HIT_BOX_X_SIZE / 2 + PREY_HIT_BOX_X_OFFSET
        prey_hit_box[0][1] = prey_y - PREY_HIT_BOX_Y_SIZE / 2 + PREY_HIT_BOX_Y_OFFSET
        prey_hit_box[1][0] = prey_x + PREY_HIT_BOX_X_SIZE / 2 + PREY_HIT_BOX_X_OFFSET
        prey_hit_box[1][1] = prey_y - PREY_HIT_BOX_Y_SIZE / 2 + PREY_HIT_BOX_Y_OFFSET
        prey_hit_box[2][0] = prey_x + PREY_HIT_BOX_X_SIZE / 2 + PREY_HIT_BOX_X_OFFSET
        prey_hit_box[2][1] = prey_y + PREY_HIT_BOX_Y_SIZE / 2 + PREY_HIT_BOX_Y_OFFSET
        prey_hit_box[3][0] = prey_x - PREY_HIT_BOX_X_SIZE / 2 + PREY_HIT_BOX_X_OFFSET
        prey_hit_box[3][1] = prey_y + PREY_HIT_BOX_Y_SIZE / 2 + PREY_HIT_BOX_Y_OFFSET

        prey_is_not_selected = False  # Now prey is selected

    # Draw the prey image at its position (prey_x, prey_y are integers)
    DISPLAYSURF.blit(prey, (prey_x, prey_y))
    # Debug draw prey hitbox:
    # pygame.draw.polygon(DISPLAYSURF, (255, 0, 255), prey_hit_box)

    # ----------- Collision detection -----------

    # Extract x and y coordinates from hitboxes using list comprehensions
    cat_x_vals = [pt[0] for pt in cat_hit_box]
    cat_y_vals = [pt[1] for pt in cat_hit_box]

    prey_x_vals = [pt[0] for pt in prey_hit_box]
    prey_y_vals = [pt[1] for pt in prey_hit_box]

    # Determine edges of rectangles (min and max of coordinate lists)
    cat_left, cat_right = min(cat_x_vals), max(cat_x_vals)
    cat_top, cat_bottom = min(cat_y_vals), max(cat_y_vals)

    prey_left, prey_right = min(prey_x_vals), max(prey_x_vals)
    prey_top, prey_bottom = min(prey_y_vals), max(prey_y_vals)

    # Calculate overlap edges by comparing edges of cat and prey hitboxes
    inter_left = max(cat_left, prey_left)
    inter_right = min(cat_right, prey_right)
    inter_top = max(cat_top, prey_top)
    inter_bottom = min(cat_bottom, prey_bottom)

    # Calculate overlap width and height (floats)
    inter_width = inter_right - inter_left
    inter_height = inter_bottom - inter_top

    # Calculate intersection area if overlap exists (positive width and height)
    inter_area = inter_width * inter_height if inter_width > 0 and inter_height > 0 else 0

    # Calculate prey hitbox area
    prey_area = (prey_right - prey_left) * (prey_bottom - prey_top)

    # Calculate overlap ratio (float)
    cat_prey_hit_box_ratio = inter_area / prey_area if prey_area > 0 else 0

    # Check if the cat caught the prey based on collision ratio (boolean)
    cat_catch_the_prey = cat_prey_hit_box_ratio >= CAT_PREY_HIT_BOX_COLLISION_RATIO

    if cat_catch_the_prey:
        prey_is_not_selected = True  # Need to select new prey

        score += 1  # Increase player's score (integer)

        # Add caught prey's name to the prey_history list (list of strings)
        prey_history.append(prey_name)

        # Keep only last 3 prey caught to limit history size
        if len(prey_history) > 3:
            prey_history.pop(0)  # Remove oldest item from list

        # Save position where prey was caught as a tuple (immutable pair of integers)
        caught_prey_positions.append((prey_x, prey_y))

        # Special rewards example using string labels
        if prey_name == "lizard":
            special_rewards.append("+5 bonus points")

    # ----------- UI Rendering -----------

    # Render the score on screen using font (score is int converted to string)
    score_surf = font.render(f"Score: {score}", True, (0, 0, 0))
    DISPLAYSURF.blit(score_surf, (10, 10))

    # Render last 3 caught prey names on screen (iterate over list of strings)
    for i, name in enumerate(prey_history):
        label = font.render(f"Prey {i + 1}: {name}", True, (100, 100, 100))
        DISPLAYSURF.blit(label, (10, 50 + i * 30))

    # Show info about active lists (demonstrates length, contents, etc.)
    list_labels = [
        f"Active Lists:",
        f"- PREYS: {len(PREYS)} items",  # Number of prey types (int)
        f"- prey_history: {prey_history}",  # List of strings
        f"- movement_history: {len(movement_history)} steps",  # List length (int)
        f"- score_log: {score_log}",  # List of scores (ints)
        f"- caught_prey_positions: {len(caught_prey_positions)}",  # List length
        f"- special_rewards: {special_rewards}",  # List of reward strings
        f"- frame_timeline (len): {len(frame_timeline)}"  # List length of timestamps
    ]

    for i, text in enumerate(list_labels):
        label = font.render(text, True, (50, 50, 50))
        DISPLAYSURF.blit(label, (WINDOW_WIDTH - 500, 10 + i * 28))

    # Update the screen and keep the FPS stable
    pygame.display.update()
    fpsClock.tick(FPS)
    
# ---------------------------
# Explanation about Comments
# ---------------------------

# Comments are essential in programming because they help explain what the code does,
# making it easier to understand, maintain, and debug — especially when returning
# to code after some time or when working in a team.

# In this code, comments:
# - Clarify the purpose of variables and constants (e.g., what each hitbox size represents).
# - Explain why certain values or choices are made (like screen edges or collision ratio).
# - Describe the flow of logic (e.g., what happens when a key is pressed or a collision occurs).
# - Indicate sections of the program for easier navigation (like "Main game loop" or "Collision detection").
# - Provide debugging aids (e.g., printing hitbox coordinates or drawing polygons).

# Good commenting practices help prevent confusion, save time debugging,
# and improve collaboration with others.

# Summary:
# Use comments to communicate intent and logic clearly without repeating obvious code.
# Keep comments concise, relevant, and up-to-date.
# Comments are not only for others but also for your future self to quickly understand
# how and why the code works the way it does.