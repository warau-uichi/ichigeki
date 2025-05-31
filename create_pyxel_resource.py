import pyxel
import os

# Define the resource file path
RESOURCE_FILE = "assets/game.pyxres"
ASSETS_DIR = "assets"

# Screen dimensions (in tiles)
SCREEN_WIDTH_TILES = 32
SCREEN_HEIGHT_TILES = 24

# Tile IDs
TILE_BACKGROUND = 0
TILE_GROUND = 1

# Colors
COLOR_BACKGROUND = 1  # Dark Blue
COLOR_GROUND = 13     # Light Brown

def main():
    # Create assets directory if it doesn't exist
    if not os.path.exists(ASSETS_DIR):
        os.makedirs(ASSETS_DIR)

    # Initialize Pyxel
    # Screen size here is in pixels, tilemap size is 256x256 by default
    pyxel.init(
        SCREEN_WIDTH_TILES * 8,
        SCREEN_HEIGHT_TILES * 8,
        title="Pyxel Resource Creator"
    )
    print("Initialized Pyxel.")

    # Load existing resource file if it exists, otherwise Pyxel starts fresh
    if os.path.exists(RESOURCE_FILE):
        pyxel.load(RESOURCE_FILE)
        print(f"Loaded existing resource file: {RESOURCE_FILE}")
    else:
        print("No existing resource file found.")
        print(f"A new one will be created at: {RESOURCE_FILE}")

    # --- Create tile patterns in image bank 0 ---
    # Tile 0: Background (dark blue)
    # Get the image bank (image 0) - use pyxel.images[0] as per deprecation warning
    img_bank = pyxel.images[0]

    # Fill an 8x8 area for the background tile (tile 0)
    # img_bank.rect(x, y, w, h, col)
    # Tile 0 will be at (0,0) in the image bank
    img_bank.rect(0, 0, 8, 8, COLOR_BACKGROUND)

    # Tile 1: Ground (light brown)
    # Tile 1 will be at (8,0) in the image bank
    img_bank.rect(8, 0, 8, 8, COLOR_GROUND)
    print("Defined tile patterns in image bank 0.")

    # --- Set tiles in tilemap 0 ---
    # Get tilemap 0 - use pyxel.tilemaps[0] as per deprecation warning
    tm = pyxel.tilemaps[0]

    # Fill the entire tilemap with the background tile (tile 0)
    # Modifying to pass tile_id as a list, e.g., [TILE_BACKGROUND]
    for y in range(SCREEN_HEIGHT_TILES):
        for x in range(SCREEN_WIDTH_TILES):
            # tm.set(tile_x, tile_y, tile_id_in_image_bank)
            # Note: pyxel tilemaps store tile IDs as strings "ttxxii" where
            # tt is tilemap, xx is tile_x, ii is tile_y.
            # However, the API tm.set() uses integer tile IDs from the image bank.
            # The actual tile ID in the image bank is what we use here.
            # We defined tile 0 (background) at (0,0) and tile 1 (ground) at (8,0).
            # Pyxel internally maps these to tile indices.
            # For simplicity, let's assume the tile at (0,0) in image bank is tile index 0,
            # and tile at (8,0) is tile index 1 if the image bank was laid out linearly.
            # More accurately, pyxel.tilemap(0).set(x,y,0) refers to the 8x8 pixels
            # starting at (0,0) in image bank 0 and pyxel.tilemap(0).set(x,y,1) refers
            # to the 8x8 pixels starting at (8,0) in image bank 0
            tm.set(x, y, [str(TILE_BACKGROUND)])
    print(f"Filled tilemap 0 with background tile ({TILE_BACKGROUND}).")

    # Create a ground platform at the bottom (last 2 rows)
    # Modifying to pass tile_id as a list of strings, e.g., [str(TILE_GROUND)]
    for y in range(SCREEN_HEIGHT_TILES - 2, SCREEN_HEIGHT_TILES):
        for x in range(SCREEN_WIDTH_TILES):
            tm.set(x, y, [str(TILE_GROUND)])
    print(f"Created ground platform in tilemap 0 with ground tile ({TILE_GROUND}).")

    # --- Save the resource file ---
    # The pyxel.save() function automatically saves to the path used in pyxel.load()
    # or if not loaded, to a path derived from the script name if init was used
    # without a specific save path.
    # To ensure it saves to our desired location:
    pyxel.save(RESOURCE_FILE)
    print(f"Saved resource file to: {RESOURCE_FILE}")

    # Pyxel usually runs an event loop with pyxel.run(update, draw)
    # Since this is a script to generate resources, we don't need an active loop.
    # We can quit pyxel if it was initialized for graphics.
    # However, pyxel.init() in resource-only mode (no display) might not
    # require pyxel.quit().
    # For safety, let's assume it might have opened a window if not run
    # in a headless environment.
    # pyxel.quit() # This might not be necessary or could error if no window was opened.

if __name__ == "__main__":
    main()
