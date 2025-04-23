import turtle as t
import random

# Setup screen
screen = t.Screen()
screen.setup(600, 600)
screen.title("Super Swap!")
screen.bgcolor("skyblue")
screen.register_shape("src/assets/flight.gif")
screen.register_shape("src/assets/speed.gif")
screen.register_shape("src/assets/invis.gif")

"""
# Setup background (optional, now hidden turtle)
bg = t.Turtle()
bg.shape("square")
bg.color("skyblue")
bg.shapesize(1000)
bg.penup()
bg.goto(0, 0)
bg.hideturtle()
"""

scoreNum = 0
obstSpeed = 10
playertype = 3

# Score display
score_display = t.Turtle()
score_display.speed(0)
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 225)
score_display.write("Score: " + str(scoreNum), align="center", font=("Courier", 16, "normal"))

# Setup player
player = t.Turtle()
player.speed(0)
player.penup()
player.shape("triangle")
player.setheading(90)
player.goto(-200, 0)
player.color("blue")

# List to keep track of (obstacle, type) tuples
obstacles = []

# Obstacle types
def create_obstacle(color):
    obs = t.Turtle()
    obs.speed(0)
    obs.penup()
    obs.shape("circle")
    obs.color(color)
    obs.goto(250, 0)

    # Determine type based on color
    if color == "white":
        obs_type = 1
    elif color == "red":
        obs_type = 2
    elif color == "blue":
        obs_type = 3

    obstacles.append((obs, obs_type))

def spawn_obstacle():
    color = random.choice(['blue', 'white', 'red'])
    create_obstacle(color)
    screen.ontimer(spawn_obstacle, 1500)

# Move obstacles
def move_obstacles():
    global scoreNum, obstSpeed
    to_remove = []

    for obs, obs_type in obstacles:
        obs.setx(obs.xcor() - obstSpeed)

        # Check collision range (near player)
        if -210 < obs.xcor() < -190:
            if obs_type != playertype:
                score_display.clear()
                score_display.write("Game Over! Score: " + str(scoreNum), align="center", font=("Courier", 16, "normal"))
                return  # Stop the loop

        # Off screen
        if obs.xcor() < -300:
            obs.hideturtle()
            to_remove.append((obs, obs_type))
            scoreNum += 1
            obstSpeed += 1
            score_display.clear()
            score_display.write("Score: " + str(scoreNum), align="center", font=("Courier", 16, "normal"))

    for obs_tuple in to_remove:
        obstacles.remove(obs_tuple)

    screen.ontimer(move_obstacles, 50)

# Controls
def setinvis():
    global playertype
    playertype = 1
    player.shape("src/assets/invis.gif")
    player.color("white")

def setStrength():
    global playertype
    playertype = 2
    player.shape("src/assets/flight.gif")
    player.color("red")

def setSpeed():
    global playertype
    playertype = 3
    player.shape("src/assets/speed.gif")
    player.color("blue")

def quit():
    screen.bye()

# Key bindings
screen.listen()
screen.onkey(setinvis, "a")
screen.onkey(setStrength, "s")
screen.onkey(setSpeed, "d")
screen.onkey(quit, "q")

# Start the game
spawn_obstacle()
move_obstacles()
screen.mainloop()
