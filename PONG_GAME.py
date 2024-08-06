import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = 'Первая игра для Ярика от папы'

class Ball(arcade.Sprite):
    def __init__(self):
        super().__init__('ball.png', 1.0)
class Bar(arcade.Sprite):
    def __init__(self):
        super().__init__('bar.png', 1.0)

class Game(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.bar = Bar()
        self.ball = Ball()
        self.setup()

    def setup(self):
        self.bar.center_x = SCREEN_WIDTH / 2
        self.bar.center_y = SCREEN_HEIGHT / 5
        self.ball.center_x = SCREEN_WIDTH / 2
        self.ball.center_y = SCREEN_HEIGHT / 5

    def on_draw(self):
        self.clear((130, 180, 215))
        self.ball.draw()
        self.bar.draw()

if __name__ == '__main__':
    window = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()