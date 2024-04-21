import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Pong")
screen.bgcolor("black")
screen.setup(width=600, height=400)
screen.tracer(0)  # Turn off animation

# Paddle A (controlled by mouse)
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-250, 0)

# Paddle B (controlled by AI)
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(250, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.1
ball.dy = 0.1

# Functions to move paddles
def paddle_a_move(y):
    paddle_a.sety(y)

def paddle_b_ai():
    if ball.ycor() < paddle_b.ycor() and abs(ball.ycor() - paddle_b.ycor()) > 20:
        paddle_b.sety(paddle_b.ycor() - 0.1)
    elif ball.ycor() > paddle_b.ycor() and abs(ball.ycor() - paddle_b.ycor()) > 20:
        paddle_b.sety(paddle_b.ycor() + 0.1)

# Function to update paddle_a position based on mouse click
def update_paddle_a(x, y):
    paddle_a_move(y)

# Keyboard bindings (for exiting the game)
screen.listen()
screen.onkeypress(screen.bye, "Escape")

# Bind update_paddle_a to mouse clicks within the window


# Main game loop
while True:
    screen.update()
    screen.onscreenclick(update_paddle_a)
    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 190:
        ball.sety(190)
        ball.dy *= -1

    if ball.ycor() < -190:
        ball.sety(-190)
        ball.dy *= -1

    if ball.xcor() > 290:
        ball.goto(0, 0)
        ball.dx *= -1

    if ball.xcor() < -290:
        ball.goto(0, 0)
        ball.dx *= -1

    # Paddle B (AI control)
    paddle_b_ai()

    # Paddle and ball collisions
    if (ball.xcor() > 240 and ball.xcor() < 250) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(240)
        ball.dx *= -1

    if (ball.xcor() < -240 and ball.xcor() > -250) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-240)
        ball.dx *= -1
