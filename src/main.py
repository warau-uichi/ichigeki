import sys

import pyxel

# Game constants
SCREEN_WIDTH = 256
SCREEN_HEIGHT = 192
PLAYER_WIDTH = 16
PLAYER_HEIGHT = 16
PLAYER_COLOR = 7  # White
PLAYER_SPEED = 2


class Game:
    def __init__(self):
        # Get the current module to access global player_x
        main_module = sys.modules.get(__name__)

        # Use the global player_x if it exists, otherwise initialize to center
        if hasattr(main_module, "player_x"):
            self.player_x = main_module.player_x
        else:
            self.player_x = SCREEN_WIDTH / 2 - PLAYER_WIDTH / 2

        if hasattr(main_module, "player_y"):
            self.player_y = main_module.player_y
        else:
            self.player_y = SCREEN_HEIGHT / 2 - PLAYER_HEIGHT / 2

        # Pyxel初期化処理
        pyxel.init(SCREEN_WIDTH, SCREEN_HEIGHT, title="イチゲキーン", fps=30)
        pyxel.load("assets/game.pyxres")  # Note: This file is empty for now

        # Expose properties for testing
        self.setup_globals()

    def setup_globals(self):
        # Make properties accessible globally for testing
        # This approach avoids global statements inside methods
        # pylint: disable=global-statement
        global player_x, player_y, player_width, player_height, player_speed
        player_x = self.player_x
        player_y = self.player_y
        player_width = PLAYER_WIDTH
        player_height = PLAYER_HEIGHT
        player_speed = PLAYER_SPEED

    def update(self):
        if pyxel.btn(pyxel.KEY_A):
            self.player_x -= PLAYER_SPEED
        if pyxel.btn(pyxel.KEY_D):
            self.player_x += PLAYER_SPEED

        # Clamp player_x to screen boundaries
        self.player_x = max(0, min(self.player_x, pyxel.width - PLAYER_WIDTH))

        # Update globals for testing without using global statement inside methods
        self._update_globals()

    def _update_globals(self):
        # pylint: disable=global-statement
        global player_x
        player_x = self.player_x

    def draw(self):
        pyxel.cls(0)  # Clear screen with black
        # Draw player
        pyxel.rect(
            self.player_x,
            self.player_y,
            PLAYER_WIDTH,
            PLAYER_HEIGHT,
            PLAYER_COLOR,
        )

    def run(self):
        pyxel.run(self.update, self.draw)


# Initialize globals for testing
player_x = 0
player_y = 0
player_width = PLAYER_WIDTH
player_height = PLAYER_HEIGHT
player_speed = PLAYER_SPEED


# For compatibility with tests
def update():
    # pylint: disable=global-statement
    global game_instance
    if "game_instance" not in globals():
        game_instance = Game()

    # Get the main module dynamically to access the player_x that tests modify
    main_module = __import__(__name__)

    # Synchronize from main module to game instance
    game_instance.player_x = main_module.player_x

    # Update the game
    game_instance.update()

    # Synchronize back from game instance to main module
    main_module.player_x = game_instance.player_x


# Create and run game when this module is executed directly
if __name__ == "__main__":
    game = Game()
    game.run()
