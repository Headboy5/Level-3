class snakes_and_ladders:
    def __init__(self, position=0):
        self.position = position
    def move(self, roll):
        self.position += roll
        if self.position > 100:
            self.position = 100 - (self.position - 100)
        print(f"Player moved to position {self.position}")
        return self.position
    def add_snake(self, snake):
        self.snake = snake
    def add_ladder(self, ladder):
        self.ladder = ladder

class Snake:
    def __init__(self, start, end):
        self.start = start
        self.end = end
    def move(self, position):
        if position == self.start:
            print("Oh no! Landed on a snake!")
            return self.end
        return position

class Ladder:
    def __init__(self, start, end):
        self.start = start
        self.end = end
    def move(self, position):
        if position == self.start:
            print("Yay! Climbed a ladder!")
            return self.end
        return position
def test_snakes_and_ladders():
    game = snakes_and_ladders()
    snake1 = Snake(16, 6)
    snake2 = Snake(47, 26)
    snake3 = Snake(49, 11)
    snake4 = Snake(56, 53)
    game.add_snake(snake1)
    game.add_snake(snake2)
    game.add_snake(snake3)
    game.add_snake(snake4)
    ladder1 = Ladder(2, 15)
    game.add_ladder(ladder1)
    game.move(1)
    game.move(1)
    # game.move(3)
    # game.move(4)
    # game.move(5)
    # game.move(6)
    # game.move(7)
    # game.move(8)
    # game.move(9)
    # game.move(10)

test_snakes_and_ladders()