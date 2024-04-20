import turtle
import random

# Constants
CELL_SIZE = 20
GRID_WIDTH = 20
GRID_HEIGHT = 15

# Directions
UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

# Colors
SNAKE_COLOR = "green"
FRUIT_COLOR = "red"
GRID_COLOR = "black"

class SnakeGame:
    def __init__(self):
        self.window = turtle.Screen()
        self.window.title("Snake Game")
        self.window.setup(GRID_WIDTH * CELL_SIZE, GRID_HEIGHT * CELL_SIZE)
        self.window.bgcolor("white")
        self.window.tracer(0)  # Turn off animation

        self.snake = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        self.direction = RIGHT
        self.fruit = self.generate_fruit()
        self.score = 0

        self.pen = turtle.Turtle()
        self.pen.penup()
        self.pen.hideturtle()
        self.pen.goto(0, GRID_HEIGHT * CELL_SIZE // 2 - 20)
        self.pen.write("Score: {}".format(self.score), align="center", font=("Courier", 24, "normal"))

        self.window.listen()
        self.window.onkeypress(self.go_up, "Up")
        self.window.onkeypress(self.go_down, "Down")
        self.window.onkeypress(self.go_left, "Left")
        self.window.onkeypress(self.go_right, "Right")

        self.update()

    def generate_fruit(self):
        while True:
            x = random.randint(0, GRID_WIDTH - 1)
            y = random.randint(0, GRID_HEIGHT - 1)
            if (x, y) not in self.snake:
                return (x, y)

    def draw_cell(self, x, y, color):
        self.pen.goto(x * CELL_SIZE - GRID_WIDTH * CELL_SIZE // 2, y * CELL_SIZE - GRID_HEIGHT * CELL_SIZE // 2)
        self.pen.pendown()
        self.pen.begin_fill()
        for _ in range(4):
            self.pen.forward(CELL_SIZE)
            self.pen.right(90)
        self.pen.end_fill()
        self.pen.penup()

    def draw_snake(self):
        for x, y in self.snake:
            self.draw_cell(x, y, SNAKE_COLOR)

    def draw_fruit(self):
        self.draw_cell(*self.fruit, FRUIT_COLOR)

    def draw_grid(self):
        self.pen.color(GRID_COLOR)
        for x in range(-GRID_WIDTH // 2, GRID_WIDTH // 2 + 1):
            self.pen.goto(x * CELL_SIZE, -GRID_HEIGHT * CELL_SIZE // 2)
            self.pen.pendown()
            self.pen.goto(x * CELL_SIZE, GRID_HEIGHT * CELL_SIZE // 2)
            self.pen.penup()
        for y in range(-GRID_HEIGHT // 2, GRID_HEIGHT // 2 + 1):
            self.pen.goto(-GRID_WIDTH * CELL_SIZE // 2, y * CELL_SIZE)
            self.pen.pendown()
            self.pen.goto(GRID_WIDTH * CELL_SIZE // 2, y * CELL_SIZE)
            self.pen.penup()

    def go_up(self):
        if self.direction != DOWN:
            self.direction = UP

    def go_down(self):
        if self.direction != UP:
            self.direction = DOWN

    def go_left(self):
        if self.direction != RIGHT:
            self.direction = LEFT

    def go_right(self):
        if self.direction != LEFT:
            self.direction = RIGHT

    def update(self):
        # Move the snake
        head = self.snake[0]
        if self.direction == UP:
            new_head = (head[0], head[1] + 1)
        elif self.direction == DOWN:
            new_head = (head[0], head[1] - 1)
        elif self.direction == LEFT:
            new_head = (head[0] - 1, head[1])
        elif self.direction == RIGHT:
            new_head = (head[0] + 1, head[1])

        # Check for collision
        if (
            new_head[0] < 0
            or new_head[0] >= GRID_WIDTH
            or new_head[1] < 0
            or new_head[1] >= GRID_HEIGHT
            or new_head in self.snake
        ):
            self.game_over()

        # Check if the snake eats the fruit
        if new_head == self.fruit:
            self.score += 1
            self.pen.clear()
            self.pen.write("Score: {}".format(self.score), align="center", font=("Courier", 24, "normal"))
            self.snake.insert(0, new_head)
            self.fruit = self.generate_fruit()
        else:
            self.snake.insert(0, new_head)
            self.snake.pop()

        self.pen.clear()
        self.draw_grid()
        self.draw_snake()
        self.draw_fruit()
        self.window.update()

        # Update again in 100 milliseconds
        self.window.ontimer(self.update, 100)

    def game_over(self):
        self.pen.goto(0, 0)
        self.pen.write("Game Over", align="center", font=("Courier", 24, "normal"))
        self.window.update()
        self.window.mainloop()

# Run the game
game = SnakeGame()
game.window.mainloop()
