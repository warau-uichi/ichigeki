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

    # TILE_FOREST_GROUND_IDX (index 2) at (16,0)
    # Mottled brown/dark green
    tile_x_start = 16
    for y_offset in range(8):
        for x_offset in range(8):
            col = COLOR_FOREST_GROUND_PRIMARY if (x_offset + y_offset) % 2 == 0 else COLOR_FOREST_GROUND_SECONDARY
            img_bank.pset(tile_x_start + x_offset, 0 + y_offset, col)

    # TILE_TREE_TRUNK_IDX (index 3) at (24,0)
    # Solid dark brown
    tile_x_start = 24
    for y_offset in range(8):
        for x_offset in range(8):
            img_bank.pset(tile_x_start + x_offset, 0 + y_offset, COLOR_TREE_TRUNK)

    # TILE_TREE_LEAVES_IDX (index 4) at (32,0)
    # Mottled light/dark green
    tile_x_start = 32
    for y_offset in range(8):
        for x_offset in range(8):
            col = COLOR_TREE_LEAVES_PRIMARY if (x_offset + y_offset) % 2 == 0 else COLOR_TREE_LEAVES_SECONDARY
            img_bank.pset(tile_x_start + x_offset, 0 + y_offset, col)

    # TILE_SKY_IDX (index 5) at (40,0)
    # Solid light blue
    tile_x_start = 40
    for y_offset in range(8):
        for x_offset in range(8):
            img_bank.pset(tile_x_start + x_offset, 0 + y_offset, COLOR_SKY)

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
    ground_level_y = SCREEN_HEIGHT_TILES - 3 # Top Y of ground layer

    for tree_x in tree_positions_x:
        # Leaves
        for i in range(tree_leaves_height):
            # Ensure y is not negative if trees are very tall
            leaf_y = ground_level_y - tree_trunk_height - i
            if leaf_y >= 0:
                 tm.set(tree_x, leaf_y, [TILE_UV_TREE_LEAVES])
        # Trunk
        for i in range(tree_trunk_height):
            trunk_y = ground_level_y - 1 - i
            if trunk_y >=0:
                tm.set(tree_x, trunk_y, [TILE_UV_TREE_TRUNK])
    print(f"Placed trees in tilemap 0 (Leaves UV: {TILE_UV_TREE_LEAVES}, Trunk UV: {TILE_UV_TREE_TRUNK}).")

    # Create forest ground platform (bottom 3 rows)
    for y_ground_offset in range(3): # 0, 1, 2
        for x in range(SCREEN_WIDTH_TILES):
            tm.set(x, SCREEN_HEIGHT_TILES - 1 - y_ground_offset, [TILE_UV_FOREST_GROUND])
    print(f"Created forest ground platform in tilemap 0 with tile (UV: {TILE_UV_FOREST_GROUND}, Concept: {TILE_FOREST_GROUND_IDX}).")

    # --- Start Internal Tilemap Debug Inspection ---
    print("DEBUG: Internally inspecting tilemap 0 data BEFORE saving...")
    # Ensure tm is the correct tilemap object, it should be pyxel.tilemaps[0]
    # If tm was a local variable in a previous scope, re-get it:
    # tm_debug = pyxel.tilemaps[0]
    # However, tm should still be in scope if defined earlier in main()
    # Assuming 'tm' (pyxel.tilemaps[0]) is still in scope and correctly modified:
    try:
        # tm was defined as: tm = pyxel.tilemaps[0]
        debug_tile_val_0_0 = tm.pget(0, 0) # Expected TILE_SKY_IDX (5), which is tile at (40,0) in image bank
        print(f"DEBUG: Internal pget(0,0) (sky): {debug_tile_val_0_0}")

        debug_tile_val_0_23 = tm.pget(0, 23) # Expected TILE_FOREST_GROUND_IDX (2), which is tile at (16,0)
        print(f"DEBUG: Internal pget(0,23) (ground): {debug_tile_val_0_23}")

        debug_tile_val_5_18 = tm.pget(5, 18) # Expected TILE_TREE_TRUNK_IDX (3), which is tile at (24,0)
        print(f"DEBUG: Internal pget(5,18) (tree trunk): {debug_tile_val_5_18}")

    except Exception as e:
        print(f"DEBUG: Error during internal pget: {e}")
    print("DEBUG: --- End Internal Tilemap Debug Inspection ---")
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
