import os
import sys

import pyxel

# Game constants
SCREEN_WIDTH = 256
SCREEN_HEIGHT = 192
PLAYER_WIDTH = 16  # Width of the player sprite
PLAYER_HEIGHT = 16  # Height of the player sprite
# PLAYER_COLOR = 7  # White - No longer needed for rect drawing
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
            # Position player near the bottom, a bit above the ground tiles
            # Ground tiles are at rows 22, 23. Tile height is 8.
            # So ground starts at y = 22 * 8 = 176.
            # Player height is 16. So player_y = 176 - 16 = 160 for on-ground.
            self.player_y = 160
            # If player_y was also global for tests, update it:
            if hasattr(main_module, "player_y"):
                main_module.player_y = self.player_y

        # Pyxel初期化処理
        pyxel.init(SCREEN_WIDTH, SCREEN_HEIGHT, title="イチゲキーン", fps=30)
        # Determine the absolute path to the assets directory
        script_path = os.path.abspath(__file__)  # Abs path to this script.
        script_dir = os.path.dirname(script_path)  # Abs path to script's dir.
        project_root = os.path.dirname(script_dir)  # Abs path to project root.
        # Construct path to assets file, e.g., /path/to/project/assets/game.pyxres
        asset_path = os.path.join(project_root, "assets", "game.pyxres")
        pyxel.load(asset_path)
        # --- Start Tilemap Debug Inspection ---
        print("DEBUG: Inspecting loaded tilemap 0 data...")
        tm = pyxel.tilemaps[0]
        # Sample points: expected sky, tree, ground
        coords_to_check = {
            "Top-left sky (0,0)": (0, 0),
            "Mid-sky (15,10)": (15, 10),
            "Tree top (5,15)": (5, 15),  # Expected: TILE_TREE_LEAVES_IDX (4)
            "Tree trunk (5,18)": (5, 18),  # Expected: TILE_TREE_TRUNK_IDX (3)
            "Ground (0,23)": (0, 23),  # Expected: TILE_FOREST_GROUND_IDX (2)
            "Ground (15,22)": (15, 22),  # Expected: TILE_FOREST_GROUND_IDX (2)
        }
        for desc, (tx, ty) in coords_to_check.items():
            tile_val = tm.pget(tx, ty)
            print(f"DEBUG: Tile at ({tx},{ty}) ({desc}): {tile_val}")
        print("DEBUG: --- End Tilemap Debug Inspection ---")
        # --- Start Image Bank Debug Inspection ---
        print("DEBUG: Inspecting loaded image bank 0 pixel data...")
        img_bank = pyxel.images[0]
        # Coordinates for new tiles in image bank 0:
        # TILE_FOREST_GROUND_IDX = 2 (at 16,0) -> Expected colors: 4 (Brown) or 3 (Dark Green)
        # TILE_TREE_TRUNK_IDX = 3 (at 24,0) -> Expected color: 4 (Brown)
        # TILE_TREE_LEAVES_IDX = 4 (at 32,0) -> Expected colors: 11 (Light Green) or 3 (Dark Green)
        # TILE_SKY_IDX = 5 (at 40,0) -> Expected color: 12 (Light Blue)

        coords_to_check_img = {
            "Sky tile pixel (40,0)": (40, 0),  # Expected: COLOR_SKY (12)
            "Sky tile pixel (43,3)": (43, 3),  # Expected: COLOR_SKY (12)
            "Forest ground pixel (16,0)": (
                16,
                0,
            ),  # Expected: COLOR_FOREST_GROUND_PRIMARY/SECONDARY (4 or 3)
            "Tree trunk pixel (24,0)": (24, 0),  # Expected: COLOR_TREE_TRUNK (4)
        }
        for desc, (px, py) in coords_to_check_img.items():
            pixel_val = img_bank.pget(px, py)
            print(f"DEBUG: Image bank 0 pixel at ({px},{py}) ({desc}): {pixel_val}")
        print("DEBUG: --- End Image Bank Debug Inspection ---")

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
        if pyxel.btn(pyxel.KEY_A) or pyxel.btn(pyxel.KEY_LEFT):
            self.player_x -= PLAYER_SPEED
        if pyxel.btn(pyxel.KEY_D) or pyxel.btn(pyxel.KEY_RIGHT):
            self.player_x += PLAYER_SPEED

        # Clamp player_x to screen boundaries
        self.player_x = max(0, min(self.player_x, pyxel.width - PLAYER_WIDTH))

        # Add sound effect on 'F' key press
        if pyxel.btnp(pyxel.KEY_F):
            pyxel.play(0, 0)  # Play sound 0 (attack) on channel 0

        # Update globals for testing without using global statement inside methods
        self._update_globals()

    def _update_globals(self):
        # pylint: disable=global-statement
        global player_x
        player_x = self.player_x

    def draw(self):
        pyxel.cls(0)  # Clear screen with black (optional if tilemap covers all)

        # Draw the stage tilemap (tilemap 0)
        # bltm(x, y, tm, u, v, w, h, [colkey])
        # x, y: screen coordinates to draw at
        # tm: tilemap index (0)
        # u, v: tilemap source coordinates (top-left tile to start drawing from)
        # w, h: width and height in terms of number of tiles to draw
        #       pyxel.width and pyxel.height are in pixels.
        #       Since tiles are 8x8, pyxel.width/8 and pyxel.height/8 for full screen.
        # Don't use color 0 for transparency as our tiles may contain it
        # 問題を解決するための別のアプローチを試す
        # タイルマップの表示をデバッグするためのコード
        for y in range(pyxel.height // 8):
            for x in range(pyxel.width // 8):
                tile_val = pyxel.tilemaps[0].pget(x, y)
                if tile_val:
                    # tile_valが(tile_index, rotation)のタプルなので最初の値を使用
                    tile_idx = tile_val[0]
                    # タイルインデックスに基づいて、イメージバンク0から対応する8x8タイルを描画
                    u = (tile_idx * 8) % pyxel.width
                    v = ((tile_idx * 8) // pyxel.width) * 8
                    pyxel.blt(x * 8, y * 8, 0, u, v, 8, 8, 0)

        # Draw player sprite
        # blt(x, y, img, u, v, w, h, [colkey])
        # x, y: screen coordinates
        # img: image bank index (0)
        # u, v: image bank source coordinates (top-left of sprite)
        # w, h: width and height of sprite
        # colkey: transparency color (0 for black, typically)
        pyxel.blt(
            self.player_x,
            self.player_y,
            0,  # Image bank 0
            0,  # u (sprite sheet x for idle)
            16,  # v (sprite sheet y for idle)
            PLAYER_WIDTH,
            PLAYER_HEIGHT,
            0,  # Color key for transparency
        )

        # Old player drawing (rectangle) - commented out
        # pyxel.rect(
        #     self.player_x,
        #     self.player_y,
        #     PLAYER_WIDTH,
        #     PLAYER_HEIGHT,
        #     PLAYER_COLOR, # PLAYER_COLOR was defined as 7 (white)
        # )

    def run(self):
        pyxel.run(self.update, self.draw)


# Initialize globals for testing
# These values will be overwritten by Game.__init__ if game is run directly,
# but tests might rely on them being here.
player_x = SCREEN_WIDTH / 2 - PLAYER_WIDTH / 2
player_y = 160  # Consistent with Game.__init__ initial position
player_width = PLAYER_WIDTH
player_height = PLAYER_HEIGHT
player_speed = PLAYER_SPEED


# For compatibility with tests
def update():
    # pylint: disable=global-statement
    global game_instance
    if "game_instance" not in globals():
        # Initialize game_instance using the global player_x and player_y
        # that tests might have set before calling this update function.
        # This ensures that test-set values are picked up by Game constructor.
        game_instance = Game()

    # Get the main module dynamically to access the player_x that tests modify
    main_module = __import__(__name__)

    # Synchronize from main module to game instance for x (tests might change global player_x)
    # (player_y is not typically changed by current tests in the same way)
    game_instance.player_x = main_module.player_x

    # Update the game
    game_instance.update()

    # Synchronize back from game instance to main module
    main_module.player_x = game_instance.player_x


# Create and run game when this module is executed directly
if __name__ == "__main__":
    game = Game()
    game.run()
