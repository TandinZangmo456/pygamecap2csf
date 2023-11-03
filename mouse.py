import pygame
import random

# Initialize Pygame
pygame.init()
# Game settings
WIDTH = 600
HEIGHT = 500 
PLAYER_COUNT = 1 # Set number of players

# Define font
font = pygame.font.Font(None, 32)

# Scoring
high_score = 0  # Initialize high_score variable
score = 0
score_text = font.render("Score: " + str(score), True, (255,255,255))

# Game Over 
game_over = False
game_started = False # Add this line

screen = pygame.display.set_mode((WIDTH, HEIGHT))
bg = pygame.image.load("/home/tandinzangmo/Desktop/PYGAME/space1.jpg").convert()
color = (0, 0, 0)
pygame.display.update()

# Define images
mouse_image = pygame.image.load("mouse.jpg").convert()
trash_image = pygame.image.load("trash.jpg").convert()
player_image = pygame.image.load("cat.jpg").convert()

# Resize images
mouse_image = pygame.transform.scale(mouse_image, (50, 50))  # Resize to 50x50
trash_image = pygame.transform.scale(trash_image, (50, 50)) # Resize to 50x50
player_image = pygame.transform.scale(player_image, (50, 50))  # Resize to 50x50

# Drawing function for images
def draw_image(surface, image, x, y):
   surface.blit(image, (x, y))

# Define start menu function
def draw_start_menu():
    screen.fill((0, 0, 0))  # Fill the screen with black
    title = font.render('My Game', True, (255, 255, 255))  # Render the title
    start_button = font.render('Press SPACE to start', True, (255, 255, 255))  # Render the start button
    high_score_text = font.render('High Score: ' + str(high_score), True, (255, 255, 255))  # Render the high score
    instructions = font.render('Press LEFT and RIGHT to move, UP to jump', True, (255, 255, 255))  # Render instructions
    screen.blit(title, (WIDTH//2 - title.get_width()//2, HEIGHT//2 - title.get_height()//2)) # Draw the title
    screen.blit(start_button, (WIDTH//2 - start_button.get_width()//2, HEIGHT//2 + 50)) # Draw the start button at a different position
    screen.blit(high_score_text, (WIDTH//2 - high_score_text.get_width()//2, HEIGHT//2 - 50)) # Draw the high score
    screen.blit(instructions, (WIDTH//2 - instructions.get_width()//2, HEIGHT//2 + title.get_height() + high_score_text.get_height() + 20)) # Draw instructions
    # Update the display
    pygame.display.update()

# Define Players 
players = []
for i in range(PLAYER_COUNT):
    players.append({
        "image": player_image,
        "x": WIDTH//2,       
        "y": HEIGHT - 100
    })

# Mouse  
mouseX = random.randint(0, WIDTH-100) 
mouseY = random.randint(0, HEIGHT-100) 

# Trash
trashX = random.randint(0, WIDTH-100) 
trashY = random.randint(0, HEIGHT-100) 

counter = 0

# Main game loop
running = True
start_menu = True

while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if start_menu:
                start_menu = False

    # Drawing
    if start_menu:
        draw_start_menu()
    else:
        # Update the game
        pass

    # Update the display
    pygame.display.flip()
        # Increment counter in every loop iteration
    counter += 1

        # If counter has reached 100, move the mouse to a new position
    if counter >= 100:
        mouseX = random.randint(0, WIDTH-100)
        mouseY = random.randint(0, HEIGHT-100)
        counter = 0  # Reset counter

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

        # Player movement    
        player_speed = 80
                        
        for i, player in enumerate(players):
            keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player["x"] > 0:
            player["x"] -= player_speed 
        if keys[pygame.K_RIGHT] and player["x"] < WIDTH - player_speed:
            player["x"] += player_speed
        if keys[pygame.K_UP] and player["y"] > 0:
            player["y"] -= player_speed  # Move up
        if keys[pygame.K_DOWN] and player["y"] < HEIGHT - player_speed:
            player["y"] += player_speed  # Move down

            # Set game over if player goes off screen
            if player["x"] < 0 or player["x"] > WIDTH:
                game_over = True

    # Clear the screen
    screen.fill((255, 0, 0))

    # Draw mouse
    draw_image(screen, mouse_image, mouseX, mouseY)

    # Draw trash
    draw_image(screen, trash_image, trashX, trashY)

    # Draw players
    for player in players:
        draw_image(screen, player["image"], player["x"], player["y"])


    # Check for collision
    for player in players:
        if player["x"] < mouseX < player["x"] + 100 and player["y"] < mouseY < player["y"] + 100:
            score += 1
            if score == 50: # Increase score required to win
                game_over = True
            mouseX = random.randint(0, WIDTH-100)
            mouseY = random.randint(0, HEIGHT-100)

    # Check for collision with trash
    for player in players:
        if player["x"] < trashX < player["x"] + 50 and player["y"] < trashY < player["y"] + 50:
            game_over = True        

    # Update score
    score_text = font.render("Score: " + str(score), True, (255,255,255))
    screen.blit(score_text, (10, 10))

    # Mouse and trash moves faster and diagonally
    mouseX += random.randint(0, 0)
    mouseY += random.randint(0, 0)
    trashX += random.randint(-10, 10)
    trashY += random.randint(-10, 10)

    # If mouse goes off screen, place it back on
    if mouseX < 0 or mouseX > WIDTH:
        mouseX = random.randint(0, WIDTH-100)
    if mouseY < 0 or mouseY > HEIGHT:
        mouseY = random.randint(0, HEIGHT-100)

    # If trash goes off screen, place it back on
    if trashX < 0 or trashX > WIDTH:
        trashX = random.randint(0, WIDTH-100)
    if trashY < 0 or trashY > HEIGHT:
        trashY = random.randint(0, HEIGHT-100)

    # Update the display
    pygame.display.flip()

# End game
pygame.quit()