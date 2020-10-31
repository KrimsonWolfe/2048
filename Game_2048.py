import arcade
from PIL import Image, ImageDraw, ImageFont
from arcade.arcade_types import RGB
from funcs_2048 import new_merge_right, new_merge_left, new_merge_up, new_merge_down, print_board
import random as rand

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = "2048 Knockoff"
SQUARE_SIZE = int(SCREEN_WIDTH / 4)
FONT_SIZE = 50

def create_texture(size, color):
    texture_list = []
    name_list = ["0","2", "4", "8", "16", "32", "64", "128", "256", "512", "1024", "2048"]
    font = ImageFont.truetype("arial.ttf", FONT_SIZE)
    for i in range(12):
        temp = Image.new("RGB", size, color[i])
        draw = ImageDraw.Draw(temp)
        width, height = draw.textsize(name_list[i], font)
        xy = ((SQUARE_SIZE/2-width/2), (SQUARE_SIZE/2-height/2))
        # Uncomment if text is wanted
        draw.text(xy, f"{name_list[i]}",fill= (0, 0, 0), font = font)
        texture = arcade.Texture(f"{name_list[i]}", temp)
        temp.save(name_list[i]+".png")
        texture_list.append(texture)
        # temp.show()
    return texture_list

def create_board() -> arcade.SpriteList:
    out = arcade.SpriteList()
    # Create Sprites and assign their center_x and center_y values
    for y in range(3, -1, -1):
        for x in range(4):
            x_pos = 100 + (x * 200)
            y_pos = 100 + (y * 200)
            temp = arcade.Sprite()
            temp.position = (x_pos,y_pos)
            out.append(temp)
    return out


def assign_sprite(board:list, texture_list: list, sprite_list: arcade.SpriteList):
    # updating the board
    numbs = ["0", "2", "4", "8", "16", "32", "64", "128", "256", "512", "1024", "2048"]
    i = 0
    zipped = dict(zip(numbs, texture_list))
    for row in board:
        for square in row:
            sprite_list[i].texture = zipped[str(square)]
            i += 1

class Game(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        self.board_list = None
        self.number_sprite = None
        self.score = 0
        # yellow, peach, orange, pink, red, lavender, purple, blue, green, brown, black
        self.color_list = [(255, 255, 255), (253, 253, 151), (255, 218, 185), (255, 178, 102), (255, 204, 229),
                            (255, 105, 97), (229, 204, 255), (178,102, 255), (119, 158, 203),
                            (119, 221, 119), (178, 137, 102), (174, 174, 174)]
        self.number_board = None
        self.texture_list = create_texture((SQUARE_SIZE, SQUARE_SIZE), self.color_list)

    def setup(self):
        self.board_list = create_board()
        self.number_board = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        for _ in range(2):
            self.random_spawn()
        """inner = [0 for _ in range(4)]
        for _ in range(4):
            self.number_board.append(inner)"""
        assign_sprite(self.number_board, self.texture_list, self.board_list)
    
    # randomly spawn a new 90% 2 or 10% 4
    def random_spawn(self):
        zero_locations = []
        for i,row in enumerate(self.number_board):
            for j, item in enumerate(row):
                if item == 0:
                    zero_locations.append((i,j))
        if zero_locations == []:
            return
        choice = rand.choice(zero_locations)
        self.number_board[choice[0]][choice[1]] = rand.choices([2,4], [0.9, 0.1], k=1)[0]

    def on_key_press(self, key: int, modifiers: int):
        if key in [arcade.key.LEFT, arcade.key.A]:
            print("Before: ", end="")
            print_board(self.number_board)
            new_merge_left(self.number_board)
            self.random_spawn()
            print("After: ", end="")
            print_board(self.number_board)
        if key in [arcade.key.RIGHT, arcade.key.D]:
            print("Before: ", end="")
            print_board(self.number_board)
            new_merge_right(self.number_board)
            self.random_spawn()
            print("After: ", end="")
            print_board(self.number_board)
        if key in [arcade.key.UP, arcade.key.W]:
            print("Before: ", end="")
            print_board(self.number_board)
            new_merge_up(self.number_board)
            self.random_spawn()
            print("After: ", end="")
            print_board(self.number_board)
        if key in [arcade.key.DOWN, arcade.key.S]:
            print("Before: ", end="")
            print_board(self.number_board)
            new_merge_down(self.number_board)
            self.random_spawn()
            print("After: ", end="")
            print_board(self.number_board)

        assign_sprite(self.number_board, self.texture_list, self.board_list)
    
    def on_draw(self):
        arcade.start_render()
        self.board_list.draw()

def main():
    window = Game()
    window.setup()
    arcade.run()

if __name__ == '__main__':
    main()
