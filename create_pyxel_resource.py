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

# New Forest Tile IDs (start after existing 0 and 1)
TILE_FOREST_GROUND_IDX = 2
TILE_TREE_TRUNK_IDX = 3
TILE_TREE_LEAVES_IDX = 4
TILE_SKY_IDX = 5

# Colors
COLOR_BACKGROUND = 1  # Dark Blue
COLOR_GROUND = 13     # Light Brown

# New Forest Tile Colors
COLOR_FOREST_GROUND_PRIMARY = 4  # Brown
COLOR_FOREST_GROUND_SECONDARY = 3  # Dark Green
COLOR_TREE_TRUNK = 4  # Brown
COLOR_TREE_LEAVES_PRIMARY = 11 # Light Green
COLOR_TREE_LEAVES_SECONDARY = 3  # Dark Green
COLOR_SKY = 12 # Light Blue

# Tile UV String Constants for tm.set()
# Format "UUVV" where UU is tile U-coord (in hex) and VV is tile V-coord (in hex)
# All current tiles are in the first row of the image bank (V=0)
TILE_UV_ORIGINAL_BACKGROUND = "0000" # TILE_BACKGROUND (0) -> u=0, v=0
TILE_UV_ORIGINAL_GROUND = "0100"     # TILE_GROUND (1) -> u=1, v=0
TILE_UV_FOREST_GROUND = "0200"       # TILE_FOREST_GROUND_IDX (2) -> u=2, v=0
TILE_UV_TREE_TRUNK = "0300"          # TILE_TREE_TRUNK_IDX (3) -> u=3, v=0
TILE_UV_TREE_LEAVES = "0400"         # TILE_TREE_LEAVES_IDX (4) -> u=4, v=0
TILE_UV_SKY = "0500"                 # TILE_SKY_IDX (5) -> u=5, v=0

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
    # Existing print statement for old tiles will be overwritten effectively by the new one if we replace it,
    # or we can have multiple print statements. Let's keep it simple and let the new print statement reflect the latest action.

    # TILE_FOREST_GROUND_IDX (index 2) at (16,0) - Mottled
    tile_x_start = 16
    for r in range(8):  # row
        for c in range(8):  # column
            color = COLOR_FOREST_GROUND_PRIMARY if (c + r) % 2 == 0 else COLOR_FOREST_GROUND_SECONDARY
            img_bank.pset(tile_x_start + c, 0 + r, color)

    # TILE_TREE_TRUNK_IDX (index 3) at (24,0) - Solid
    tile_x_start = 24
    img_bank.rect(tile_x_start, 0, 8, 8, COLOR_TREE_TRUNK)

    # TILE_TREE_LEAVES_IDX (index 4) at (32,0) - Mottled
    tile_x_start = 32
    for r in range(8):  # row
        for c in range(8):  # column
            color = COLOR_TREE_LEAVES_PRIMARY if (c + r) % 2 == 0 else COLOR_TREE_LEAVES_SECONDARY
            img_bank.pset(tile_x_start + c, 0 + r, color)

    # TILE_SKY_IDX (index 5) at (40,0) - Solid
    tile_x_start = 40
    img_bank.rect(tile_x_start, 0, 8, 8, COLOR_SKY)

    print("Defined new forest tile patterns in image bank 0.")

    # --- Set tiles in tilemap 0 ---
    # Get tilemap 0 - use pyxel.tilemaps[0] as per deprecation warning
    tm = pyxel.tilemaps[0]

    # tm is pyxel.tilemaps[0]
    # SCREEN_WIDTH_TILES and SCREEN_HEIGHT_TILES are 32 and 24

    # Fill with sky
    for y in range(SCREEN_HEIGHT_TILES): # Iterate all rows first
        for x in range(SCREEN_WIDTH_TILES):
            tm.set(x, y, [TILE_UV_SKY])
    print(f"Filled tilemap 0 with sky tile (UV: {TILE_UV_SKY}, Concept: {TILE_SKY_IDX}).")

    # Place Trees (example positions)
    tree_positions_x = [5, 15, 25]
    tree_trunk_height = 3
    tree_leaves_height = 3
    # ground_level_y is the first row of the ground, e.g. SCREEN_HEIGHT_TILES - 3
    # For calculations, let's use the y-coordinate of the tile *just above* the ground,
    # which is where the base of the trunk would sit.
    base_of_trunk_y = SCREEN_HEIGHT_TILES - 3 - 1 # e.g., 24 - 3 - 1 = 20

    for tree_x in tree_positions_x:
        # Place Trunks first, from bottom up
        for i in range(tree_trunk_height): # i = 0, 1, 2
            trunk_y = base_of_trunk_y - i  # y = 20, 19, 18
            if trunk_y >= 0:
                tm.set(tree_x, trunk_y, [TILE_UV_TREE_TRUNK])

        # Place Leaves above the trunk
        # Topmost trunk was at y = base_of_trunk_y - tree_trunk_height + 1
        top_trunk_y = base_of_trunk_y - tree_trunk_height + 1 # y = 20 - 3 + 1 = 18
        for i in range(tree_leaves_height): # i = 0, 1, 2
            leaf_y = top_trunk_y - 1 - i # y = 17, 16, 15
            if leaf_y >= 0:
                 tm.set(tree_x, leaf_y, [TILE_UV_TREE_LEAVES])
    print(f"Placed trees with distinct trunk/leaf layers in tilemap 0.")

    # Create forest ground platform (bottom 3 rows)
    for y_ground_offset in range(3): # 0, 1, 2
        for x in range(SCREEN_WIDTH_TILES):
            tm.set(x, SCREEN_HEIGHT_TILES - 1 - y_ground_offset, [TILE_UV_FOREST_GROUND])
    print(f"Created forest ground platform in tilemap 0 with tile (UV: {TILE_UV_FOREST_GROUND}, Concept: {TILE_FOREST_GROUND_IDX}).")

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
