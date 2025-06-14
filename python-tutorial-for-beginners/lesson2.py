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
# What is the print() function and why is it important here?
# -----------------------------------------
# The print() function is a fundamental Python command that displays information in the console.
# It helps programmers see the internal state of the game while it runs.
#
# Why use print() in this code?
# - Debugging: Print statements let you check variables like cat positions, scores, and lists at any moment.
# - Tracking game events: For example, when the player quits, we print the leaderboard and special rewards.
# - Understanding flow: You can verify if certain parts of the code are reached or if some conditions happen.
#
# Without print(), it's hard to know what the program is doing inside while it runs,
# especially when working with complex data or multiple events.
# Using print() statements during development makes finding and fixing bugs easier.
# -----------------------------------------

# Hitbox coordinates for the cat (used for collision detection)
cat_hit_box = [[0, 0], [0, 0], [0, 0], [0, 0]]

CAT_HIT_BOX_X_SIZE = 80
CAT_HIT_BOX_Y_SIZE = 80
CAT_HIT_BOX_X_OFFSET = 40
CAT_HIT_BOX_Y_OFFSET = 40

# List of prey image paths - different animals the cat can catch
PREYS = [
    RESOURCES_PATH + "rat.png",
    RESOURCES_PATH + "squirrel.png",
    RESOURCES_PATH + "spider.png",
    RESOURCES_PATH + "bird.png",
    RESOURCES_PATH + "lizard.png"
]

# Hitbox coordinates for the prey
prey_hit_box = [[0, 0], [0, 0], [0, 0], [0, 0]]

PREY_HIT_BOX_X_SIZE = 48
PREY_HIT_BOX_Y_SIZE = 48
PREY_HIT_BOX_X_OFFSET = 24
PREY_HIT_BOX_Y_OFFSET = 24

CAT_PREY_HIT_BOX_COLLISION_RATIO = 0.75

prey_is_not_selected = True
score = 0

font = pygame.font.Font(None, 36)

prey_history = []
movement_history = []
score_log = []
caught_prey_positions = []
special_rewards = []
frame_timeline = []

prey_name = None

while True:
    DISPLAYSURF.fill(WHITE)

    frame_timeline.append(pygame.time.get_ticks())
    if len(frame_timeline) > 100:
        frame_timeline.pop(0)

    for event in pygame.event.get():
        if event.type == QUIT:
            # When quitting, print leaderboard and rewards for review/debug
            print("Leaderboard (this session):", sorted(score_log, reverse=True))
            print("Special Rewards Earned:", special_rewards)

            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:
            keys = pygame.key.get_pressed()

            if keys[K_RIGHT]:
                movement_history.append((catx, caty))
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
            elif keys[K_u]:  # Undo last move
                if movement_history:
                    catx, caty = movement_history.pop()
            elif keys[K_c]:
                # Print cat hitbox for debugging
                print("Cat hitbox coordinates:", cat_hit_box)

    cat_hit_box[0][0] = catx - CAT_HIT_BOX_X_SIZE / 2 + CAT_HIT_BOX_X_OFFSET
    cat_hit_box[0][1] = caty - CAT_HIT_BOX_Y_SIZE / 2 + CAT_HIT_BOX_Y_OFFSET
    cat_hit_box[1][0] = catx + CAT_HIT_BOX_X_SIZE / 2 + CAT_HIT_BOX_X_OFFSET
    cat_hit_box[1][1] = caty - CAT_HIT_BOX_Y_SIZE / 2 + CAT_HIT_BOX_Y_OFFSET
    cat_hit_box[2][0] = catx + CAT_HIT_BOX_X_SIZE / 2 + CAT_HIT_BOX_X_OFFSET
    cat_hit_box[2][1] = caty + CAT_HIT_BOX_Y_SIZE / 2 + CAT_HIT_BOX_Y_OFFSET
    cat_hit_box[3][0] = catx - CAT_HIT_BOX_X_SIZE / 2 + CAT_HIT_BOX_X_OFFSET
    cat_hit_box[3][1] = caty + CAT_HIT_BOX_Y_SIZE / 2 + CAT_HIT_BOX_Y_OFFSET

    DISPLAYSURF.blit(catImg, (catx, caty))

    if prey_is_not_selected:
        prey_path = PREYS[random.randint(0, len(PREYS)-1)]
        prey_name = prey_path.split("/")[-1].split(".")[0]
        prey = pygame.image.load(prey_path)
        prey_x = random.randint(LEFT_EDGE_MAX + 100, RIGHT_EDGE_MAX - 100)
        prey_y = random.randint(TOP_EDGE_MAX + 100, BOTTOM_EDGE_MAX - 100)

        prey_hit_box[0][0] = prey_x - PREY_HIT_BOX_X_SIZE / 2 + PREY_HIT_BOX_X_OFFSET
        prey_hit_box[0][1] = prey_y - PREY_HIT_BOX_Y_SIZE / 2 + PREY_HIT_BOX_Y_OFFSET
        prey_hit_box[1][0] = prey_x + PREY_HIT_BOX_X_SIZE / 2 + PREY_HIT_BOX_X_OFFSET
        prey_hit_box[1][1] = prey_y - PREY_HIT_BOX_Y_SIZE / 2 + PREY_HIT_BOX_Y_OFFSET
        prey_hit_box[2][0] = prey_x + PREY_HIT_BOX_X_SIZE / 2 + PREY_HIT_BOX_X_OFFSET
        prey_hit_box[2][1] = prey_y + PREY_HIT_BOX_Y_SIZE / 2 + PREY_HIT_BOX_Y_OFFSET
        prey_hit_box[3][0] = prey_x - PREY_HIT_BOX_X_SIZE / 2 + PREY_HIT_BOX_X_OFFSET
        prey_hit_box[3][1] = prey_y + PREY_HIT_BOX_Y_SIZE / 2 + PREY_HIT_BOX_Y_OFFSET

        prey_is_not_selected = False

    DISPLAYSURF.blit(prey, (prey_x, prey_y))

    cat_x_vals = [pt[0] for pt in cat_hit_box]
    cat_y_vals = [pt[1] for pt in cat_hit_box]

    prey_x_vals = [pt[0] for pt in prey_hit_box]
    prey_y_vals = [pt[1] for pt in prey_hit_box]

    cat_left, cat_right = min(cat_x_vals), max(cat_x_vals)
    cat_top, cat_bottom = min(cat_y_vals), max(cat_y_vals)

    prey_left, prey_right = min(prey_x_vals), max(prey_x_vals)
    prey_top, prey_bottom = min(prey_y_vals), max(prey_y_vals)

    inter_left = max(cat_left, prey_left)
    inter_right = min(cat_right, prey_right)
    inter_top = max(cat_top, prey_top)
    inter_bottom = min(cat_bottom, prey_bottom)

    inter_width = inter_right - inter_left
    inter_height = inter_bottom - inter_top

    inter_area = inter_width * inter_height if inter_width > 0 and inter_height > 0 else 0
    prey_area = (prey_right - prey_left) * (prey_bottom - prey_top)

    cat_prey_hit_box_ratio = inter_area / prey_area if prey_area > 0 else 0

    cat_catch_the_prey = cat_prey_hit_box_ratio >= CAT_PREY_HIT_BOX_COLLISION_RATIO
    if cat_catch_the_prey:
        prey_is_not_selected = True
        score += 1
        prey_history.append(prey_name)
        if len(prey_history) > 3:
            prey_history.pop(0)
        caught_prey_positions.append((prey_x, prey_y))
        if prey_name == "lizard":
            special_rewards.append("+5 bonus points")

    score_surf = font.render(f"Score: {score}", True, (0, 0, 0))
    DISPLAYSURF.blit(score_surf, (10, 10))

    for i, name in enumerate(prey_history):
        label = font.render(f"Prey {i+1}: {name}", True, (100, 100, 100))
        DISPLAYSURF.blit(label, (10, 50 + i * 30))

    list_labels = [
        f"Active Lists:",
        f"- PREYS: {len(PREYS)} items",
        f"- prey_history: {prey_history}",
        f"- movement_history: {len(movement_history)} steps",
        f"- score_log: {score_log}",
        f"- caught_prey_positions: {len(caught_prey_positions)}",
        f"- special_rewards: {special_rewards}",
        f"- frame_timeline (len): {len(frame_timeline)}"
    ]
    for i, text in enumerate(list_labels):
        label = font.render(text, True, (50, 50, 50))
        DISPLAYSURF.blit(label, (WINDOW_WIDTH - 500, 10 + i * 28))

    pygame.display.update()
    fpsClock.tick(FPS)


# -----------------------------------------
# Summary about print()
# -----------------------------------------
# The print() function is used to display information to the console.
# It helps developers see what is happening inside the program during execution.
# In this code, print() statements help debug by showing positions, scores, and game events.
# This makes it easier to find and fix bugs and understand the game's flow.
