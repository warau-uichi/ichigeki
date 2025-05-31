import pyxel
import os

RESOURCE_FILE = "assets/game.pyxres"
SCREEN_WIDTH_PIXELS = 32 * 8  # Matching the init from previous script
SCREEN_HEIGHT_PIXELS = 24 * 8 # Matching the init from previous script

# Sprite properties
PLAYER_IDLE_X = 0
# Below the 8x8 tiles which occupy y=0..7 (or y=0..15 if two rows of tiles)
PLAYER_IDLE_Y = 16
PLAYER_MOVE_X = 16
PLAYER_MOVE_Y = 16
SPRITE_WIDTH = 16
SPRITE_HEIGHT = 16

COLOR_TRANSPARENT = 0
COLOR_PLAYER_BODY = 7  # White
COLOR_PLAYER_EYE = 3   # Dark Red/Brownish

def main():
    if not os.path.exists(RESOURCE_FILE):
        print(f"Error: Resource file {RESOURCE_FILE} not found.")
        print("Please run the previous script first.")
        return

    # Initialize Pyxel. This is needed before load.
    # Using simple init, assuming headless works if no pyxel.run() is called.
    pyxel.init(SCREEN_WIDTH_PIXELS, SCREEN_HEIGHT_PIXELS, title="Sprite Adder")
    print("Initialized Pyxel.") # Fixed by ruff (was f-string)

    # Load the existing resource file
    pyxel.load(RESOURCE_FILE)
    print(f"Loaded resource file: {RESOURCE_FILE}")

    # Access image bank 0
    img_bank = pyxel.images[0] # Use new API as per previous findings

    # --- Create Idle Sprite at (0,16) ---
    # Clear area for sprite with transparency
    img_bank.rect(
        PLAYER_IDLE_X, PLAYER_IDLE_Y, SPRITE_WIDTH, SPRITE_HEIGHT,
        COLOR_TRANSPARENT
    )
    # Simple body (e.g., a 12x12 box centered in the 16x16 area)
    body_x_offset = (SPRITE_WIDTH - 12) // 2  # 2
    body_y_offset = (SPRITE_HEIGHT - 12) // 2 # 2
    img_bank.rect(
        PLAYER_IDLE_X + body_x_offset, PLAYER_IDLE_Y + body_y_offset,
        12, 12, COLOR_PLAYER_BODY
    )
    # Simple eye (e.g., a 2x2 box)
    eye_x_offset = body_x_offset + 7 # Relative to sprite origin (0,16)
    eye_y_offset = body_y_offset + 3 # Relative to sprite origin (0,16)
    img_bank.rect(
        PLAYER_IDLE_X + eye_x_offset, PLAYER_IDLE_Y + eye_y_offset,
        2, 2, COLOR_PLAYER_EYE
    )
    print(f"Created idle player sprite at ({PLAYER_IDLE_X},{PLAYER_IDLE_Y}) in image bank 0.")

    # --- Create Movement Sprite at (16,16) ---
    # Clear area for sprite with transparency
    img_bank.rect(
        PLAYER_MOVE_X, PLAYER_MOVE_Y, SPRITE_WIDTH, SPRITE_HEIGHT,
        COLOR_TRANSPARENT
    )
    # Simple body (same as idle)
    img_bank.rect(
        PLAYER_MOVE_X + body_x_offset, PLAYER_MOVE_Y + body_y_offset,
        12, 12, COLOR_PLAYER_BODY
    )
    # Simple eye, shifted for movement indication (e.g., shifted right by 2 pixels)
    move_eye_x_offset = eye_x_offset + 2
    img_bank.rect(
        PLAYER_MOVE_X + move_eye_x_offset, PLAYER_MOVE_Y + eye_y_offset,
        2, 2, COLOR_PLAYER_EYE
    )
    # Add a small "trail" or "blur" line
    trail_x_offset = body_x_offset - 2 # To the left of the body
    trail_y_offset = body_y_offset + 5
    # A small vertical line
    img_bank.rect(
        PLAYER_MOVE_X + trail_x_offset, PLAYER_MOVE_Y + trail_y_offset,
        2, 4, COLOR_PLAYER_BODY
    )
    print_msg = (
        f"Created movement player sprite at "
        f"({PLAYER_MOVE_X},{PLAYER_MOVE_Y}) in image bank 0."
    )
    print(print_msg)

    # Save the changes
    pyxel.save(RESOURCE_FILE)
    print(f"Saved changes to resource file: {RESOURCE_FILE}")

if __name__ == "__main__":
    main()
