import pyxel

# Player properties
player_x = 256 / 2 - 8
player_y = 192 / 2 - 8
player_width = 16
player_height = 16
player_color = 7  # White
player_speed = 2

# Pyxel初期化処理
pyxel.init(256, 192, title="イチゲキーン", fps=30)
pyxel.load("assets/game.pyxres") # Note: This file is empty for now

def update():
    global player_x # Declare player_x as global to modify it
    if pyxel.btn(pyxel.KEY_A):
        player_x -= player_speed
    if pyxel.btn(pyxel.KEY_D):
        player_x += player_speed

    # Clamp player_x to screen boundaries
    player_x = max(0, min(player_x, pyxel.width - player_width))

def draw():
    pyxel.cls(0)  # Clear screen with black
    # Draw player
    pyxel.rect(player_x, player_y, player_width, player_height, player_color)

pyxel.run(update, draw)
