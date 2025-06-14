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
catx = random.randint(LEFT_EDGE_MAX + 100, RIGHT_EDGE_MAX - 100)
caty = random.randint(TOP_EDGE_MAX + 100, BOTTOM_EDGE_MAX - 100)

# -----------------------------------------
# What is a LIST? 
# A list is like a container or a collection that can hold multiple items, 
# and you can keep these items organized in a particular order. 
# Lists are useful to keep track of things, like points of a shape, images, or history of actions.
# You can think of a list as a numbered row of boxes, where each box holds one piece of information.
# -----------------------------------------

# This list stores the 4 corner points of the cat's hitbox (the area that detects collisions)
cat_hit_box = [[0, 0], [0, 0], [0, 0], [0, 0]]

CAT_HIT_BOX_X_SIZE = 80  # Width of cat hitbox
CAT_HIT_BOX_Y_SIZE = 80  # Height of cat hitbox
CAT_HIT_BOX_X_OFFSET = 40
CAT_HIT_BOX_Y_OFFSET = 40

# Here is a LIST of prey image paths
# This is a collection of different animals the cat can catch
PREYS = [
    RESOURCES_PATH + "rat.png",
    RESOURCES_PATH + "squirrel.png",
    RESOURCES_PATH + "spider.png",
    RESOURCES_PATH + "bird.png",
    RESOURCES_PATH + "lizard.png"
]  

# Another list to store hitbox points for the prey (same as the cat, but smaller)
prey_hit_box = [[0, 0], [0, 0], [0, 0], [0, 0]]

PREY_HIT_BOX_X_SIZE = 48
PREY_HIT_BOX_Y_SIZE = 48
PREY_HIT_BOX_X_OFFSET = 24
PREY_HIT_BOX_Y_OFFSET = 24

CAT_PREY_HIT_BOX_COLLISION_RATIO = 0.75  # How much overlap means the cat caught the prey

prey_is_not_selected = True  # Flag to know if we need to pick a new prey
score = 0  # Player's score

# Font to display text on screen
font = pygame.font.Font(None, 36)

# -----------------------------------------
# More LISTS in this game and their purpose:
# -----------------------------------------

# List to keep the last 3 caught prey names (history)
prey_history = []

# List to keep track of cat's previous positions for "undo" movement
movement_history = []

# List to keep scores of this game session (like a leaderboard)
score_log = []

# List to remember positions where prey were caught (for possible replay or stats)
caught_prey_positions = []

# List for special rewards earned during the game
special_rewards = []

# List to log frame timestamps (used to track time in the game)
frame_timeline = []

prey_name = None  # Keeps the current prey's name

# -------------------
# Main game loop starts here
# -------------------
while True:
    DISPLAYSURF.fill(WHITE)  # Clear screen with white

    # Keep track of time frames, add current time in milliseconds to the list
    frame_timeline.append(pygame.time.get_ticks())
    if len(frame_timeline) > 100:  # Keep only the last 100 timestamps to save memory
        frame_timeline.pop(0)  # Remove the oldest timestamp

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

            # When the player moves, save the current position in movement_history list
            if keys[K_RIGHT]:
                movement_history.append((catx, caty))  # Save previous position
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
            elif keys[K_u]:  # If 'u' is pressed, undo last movement
                if movement_history:
                    catx, caty = movement_history.pop()  # Go back to previous position
            elif keys[K_c]:
                print(cat_hit_box)  # Debug print hitbox coordinates

    # Update the cat's hitbox coordinates based on the current cat position
    cat_hit_box[0][0] = catx - CAT_HIT_BOX_X_SIZE / 2 + CAT_HIT_BOX_X_OFFSET
    cat_hit_box[0][1] = caty - CAT_HIT_BOX_Y_SIZE / 2 + CAT_HIT_BOX_Y_OFFSET
    cat_hit_box[1][0] = catx + CAT_HIT_BOX_X_SIZE / 2 + CAT_HIT_BOX_X_OFFSET
    cat_hit_box[1][1] = caty - CAT_HIT_BOX_Y_SIZE / 2 + CAT_HIT_BOX_Y_OFFSET
    cat_hit_box[2][0] = catx + CAT_HIT_BOX_X_SIZE / 2 + CAT_HIT_BOX_X_OFFSET
    cat_hit_box[2][1] = caty + CAT_HIT_BOX_Y_SIZE / 2 + CAT_HIT_BOX_Y_OFFSET
    cat_hit_box[3][0] = catx - CAT_HIT_BOX_X_SIZE / 2 + CAT_HIT_BOX_X_OFFSET
    cat_hit_box[3][1] = caty + CAT_HIT_BOX_Y_SIZE / 2 + CAT_HIT_BOX_Y_OFFSET

    # Draw the cat image on the screen at the current position
    DISPLAYSURF.blit(catImg, (catx, caty))
    # You can also draw the hitbox polygon for debugging:
    # pygame.draw.polygon(DISPLAYSURF, (0, 255, 255), cat_hit_box)

    # If no prey selected, choose one randomly from the PREYS list
    if prey_is_not_selected:
        # Pick a random prey image path from the list
        prey_path = PREYS[random.randint(0, len(PREYS)-1)]

        # Extract the prey name from the path (like "rat" or "spider")
        prey_name = prey_path.split("/")[-1].split(".")[0]

        # Load the prey image
        prey = pygame.image.load(prey_path)

        # Randomly place prey somewhere on the screen
        prey_x = random.randint(LEFT_EDGE_MAX + 100, RIGHT_EDGE_MAX - 100)
        prey_y = random.randint(TOP_EDGE_MAX + 100, BOTTOM_EDGE_MAX - 100)

        # Update the prey hitbox coordinates in the same way as the cat
        prey_hit_box[0][0] = prey_x - PREY_HIT_BOX_X_SIZE / 2 + PREY_HIT_BOX_X_OFFSET
        prey_hit_box[0][1] = prey_y - PREY_HIT_BOX_Y_SIZE / 2 + PREY_HIT_BOX_Y_OFFSET
        prey_hit_box[1][0] = prey_x + PREY_HIT_BOX_X_SIZE / 2 + PREY_HIT_BOX_X_OFFSET
        prey_hit_box[1][1] = prey_y - PREY_HIT_BOX_Y_SIZE / 2 + PREY_HIT_BOX_Y_OFFSET
        prey_hit_box[2][0] = prey_x + PREY_HIT_BOX_X_SIZE / 2 + PREY_HIT_BOX_X_OFFSET
        prey_hit_box[2][1] = prey_y + PREY_HIT_BOX_Y_SIZE / 2 + PREY_HIT_BOX_Y_OFFSET
        prey_hit_box[3][0] = prey_x - PREY_HIT_BOX_X_SIZE / 2 + PREY_HIT_BOX_X_OFFSET
        prey_hit_box[3][1] = prey_y + PREY_HIT_BOX_Y_SIZE / 2 + PREY_HIT_BOX_Y_OFFSET

        prey_is_not_selected = False  # We now have a prey on screen

    # Draw the prey image on the screen
    DISPLAYSURF.blit(prey, (prey_x, prey_y))
    # Draw the prey hitbox polygon for debugging:
    # pygame.draw.polygon(DISPLAYSURF, (255, 0, 255), prey_hit_box)

    # ----------- Collision detection -----------
    # Extract all x and y coordinates from cat's hitbox points
    cat_x_vals = [pt[0] for pt in cat_hit_box]
    cat_y_vals = [pt[1] for pt in cat_hit_box]

    # Extract all x and y coordinates from prey's hitbox points
    prey_x_vals = [pt[0] for pt in prey_hit_box]
    prey_y_vals = [pt[1] for pt in prey_hit_box]

    # Determine edges of cat hitbox rectangle
    cat_left, cat_right = min(cat_x_vals), max(cat_x_vals)
    cat_top, cat_bottom = min(cat_y_vals), max(cat_y_vals)

    # Determine edges of prey hitbox rectangle
    prey_left, prey_right = min(prey_x_vals), max(prey_x_vals)
    prey_top, prey_bottom = min(prey_y_vals), max(prey_y_vals)

    # Calculate overlap (intersection) between cat and prey hitboxes
    inter_left = max(cat_left, prey_left)
    inter_right = min(cat_right, prey_right)
    inter_top = max(cat_top, prey_top)
    inter_bottom = min(cat_bottom, prey_bottom)

    inter_width = inter_right - inter_left
    inter_height = inter_bottom - inter_top

    # Calculate intersection area, only if they overlap
    inter_area = inter_width * inter_height if inter_width > 0 and inter_height > 0 else 0

    # Calculate prey area (hitbox size)
    prey_area = (prey_right - prey_left) * (prey_bottom - prey_top)

    # Calculate ratio of overlap area to prey area
    cat_prey_hit_box_ratio = inter_area / prey_area if prey_area > 0 else 0

    # Check if the cat caught the prey (overlap ratio is enough)
    cat_catch_the_prey = cat_prey_hit_box_ratio >= CAT_PREY_HIT_BOX_COLLISION_RATIO
    if cat_catch_the_prey:
        prey_is_not_selected = True  # Need to select a new prey
        score += 1  # Increase score

        # Add the caught prey's name to the prey_history list
        prey_history.append(prey_name)

        # Keep only the last 3 caught prey in history
        if len(prey_history) > 3:
            prey_history.pop(0)  # Remove oldest caught prey

        # Save the position where the prey was caught
        caught_prey_positions.append((prey_x, prey_y))

        # Special reward example: if cat caught a lizard, add bonus points
        if prey_name == "lizard":
            special_rewards.append("+5 bonus points")

    # ----------- UI rendering -----------

    # Display score on screen
    score_surf = font.render(f"Score: {score}", True, (0, 0, 0))
    DISPLAYSURF.blit(score_surf, (10, 10))

    # Display last 3 caught prey names on screen
    for i, name in enumerate(prey_history):
        label = font.render(f"Prey {i+1}: {name}", True, (100, 100, 100))
        DISPLAYSURF.blit(label, (10, 50 + i * 30))

    # Display info about active lists (collections) on the right side of screen
    list_labels = [
        f"Active Lists:",
        f"- PREYS: {len(PREYS)} items",  # Number of prey types available
        f"- prey_history: {prey_history}",  # Names of last caught prey
        f"- movement_history: {len(movement_history)} steps",  # Number of moves stored
        f"- score_log: {score_log}",  # Scores recorded this session
        f"- caught_prey_positions: {len(caught_prey_positions)}",  # Positions saved
        f"- special_rewards: {special_rewards}",  # Rewards earned
        f"- frame_timeline (len): {len(frame_timeline)}"  # Time stamps stored
    ]
    for i, text in enumerate(list_labels):
        label = font.render(text, True, (50, 50, 50))
        DISPLAYSURF.blit(label, (WINDOW_WIDTH - 500, 10 + i * 28))

    # Update the screen and keep FPS stable
    pygame.display.update()
    fpsClock.tick(FPS)

# -----------------------------------------
# What is a LIST and why do we use it here?
# -----------------------------------------
# A list in Python is a way to store multiple items together in an ordered collection.
# Think of a list as a row of boxes, each holding one item, and you can access these items by their position.
# Lists help organize data that belongs together, like images, positions, scores, or history of actions.
# 
# In this game, lists are used for several purposes:
# - PREYS: Holds different types of animals the cat can catch.
# - prey_history: Keeps track of the last few prey caught, so the player can see recent catches.
# - movement_history: Stores past cat positions, allowing the player to undo moves.
# - score_log: Keeps track of scores across multiple rounds or sessions.
# - caught_prey_positions: Remembers where prey were caught for possible replay or stats.
# - special_rewards: Logs any bonus rewards earned during play.
# - frame_timeline: Tracks game time frame by frame, useful for timing events.
#
# Using lists allows the game to dynamically manage multiple pieces of related data,
# making it easier to update, display, and analyze as the game runs.
# -----------------------------------------
