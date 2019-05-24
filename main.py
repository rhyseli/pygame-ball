import sys, pygame

black = 0, 0, 0
white = 255, 255, 255

size = width, height = 640, 480

pygame.init()

screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Pygame")

clock = pygame.time.Clock()

box = {
    "x": 300,
    "y": 200,
    "velocity": [3, 3]
}

while True:
    clock.tick(50)

    # Process events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # Clear the screen
    screen.fill(black)

    # Move the box
    box["x"] += box["velocity"][0]
    box["y"] += box["velocity"][1]

    if box["x"] >= width:
        box["velocity"][0] = -box["velocity"][0]

    if box["x"] <= 0:
        box["velocity"][0] = -box["velocity"][0]

    if box["y"] >= height:
        box[]


    # Draw the box
    pygame.draw.rect(screen, white, (box["x"], box["y"], 20, 20))

    # Update the screen
    pygame.display.flip()