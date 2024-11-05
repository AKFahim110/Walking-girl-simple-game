import pgzrun

# Set window dimensions
WIDTH = 1200
HEIGHT = 600

# Load all the walking images into an array
Anims = [Actor('1'), Actor('2'), Actor('3'),
         Actor('4'), Actor('5')]
numAnims = len(Anims)  # number of images
animIndex = 0  # index for animation
animSpeed = 0  # speed for animation update

# Initial position and direction
player_x = WIDTH / 2  # initial x position
player_y = HEIGHT / 2  # initial y position
direction = "right"  # initial direction of movement

# Set initial positions for each frame in the animation
for i in range(numAnims):
    Anims[i].x = player_x
    Anims[i].y = player_y

def draw():
    screen.fill('gray')  # background color
    Anims[animIndex].draw()  # draw the current frame of the animation

def update():
    global animIndex, player_x, animSpeed, direction

    # Move right
    if keyboard.right:
        direction = "right"
        player_x += 5  # move to the right
        for i in range(numAnims):
            Anims[i].x = player_x
            Anims[i].flip_x = False  # make character face right
        if player_x >= WIDTH:  # wrap around to the left side
            player_x = 0
        animate_character()

    # Move left
    elif keyboard.left:
        direction = "left"
        player_x -= 5  # move to the left
        for i in range(numAnims):
            Anims[i].x = player_x
            Anims[i].flip_x = True  # make character face left
        if player_x <= 0:  # wrap around to the right side
            player_x = WIDTH
        animate_character()

def animate_character():
    global animIndex, animSpeed
    animSpeed += 1
    if animSpeed % 5 == 0:  # controls animation speed
        animIndex += 1
        if animIndex >= numAnims:  # reset to the first frame
            animIndex = 0

pgzrun.go()
