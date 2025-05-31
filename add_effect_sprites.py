import pyxel
import os

RESOURCE_FILE = "assets/game.pyxres"
SCREEN_WIDTH_PIXELS = 32 * 8  # Consistent with previous scripts
SCREEN_HEIGHT_PIXELS = 24 * 8 # Consistent with previous scripts

# Sprite properties
EFFECT_HIT_X = 0
EFFECT_HIT_Y = 32   # Below player sprites (0,16) and (16,16)
EFFECT_HIT_WIDTH = 8
EFFECT_HIT_HEIGHT = 8

EFFECT_ATTACK_X = 8 # Next to hit effect
EFFECT_ATTACK_Y = 32
EFFECT_ATTACK_WIDTH = 16
EFFECT_ATTACK_HEIGHT = 8

COLOR_TRANSPARENT = 0
COLOR_YELLOW = 10
COLOR_ORANGE = 9
COLOR_LIGHT_BLUE = 12
COLOR_WHITE = 7

def main():
    if not os.path.exists(RESOURCE_FILE):
        print(f"Error: Resource file {RESOURCE_FILE} not found.")
        print("Please run previous scripts first.")
        return

    # Initialize Pyxel.
    pyxel.init(SCREEN_WIDTH_PIXELS, SCREEN_HEIGHT_PIXELS, title="Effect Sprite Adder")
    print("Initialized Pyxel.")

    # Load the existing resource file
    pyxel.load(RESOURCE_FILE)
    print(f"Loaded resource file: {RESOURCE_FILE}")

    # Access image bank 0
    img_bank = pyxel.images[0]

    # --- Create Hit Effect (Spark) at (0,32) ---
    # Clear area
    img_bank.rect(
        EFFECT_HIT_X, EFFECT_HIT_Y, EFFECT_HIT_WIDTH, EFFECT_HIT_HEIGHT,
        COLOR_TRANSPARENT
    )
    # Spark: a few pixels
    # Central pixel
    img_bank.pset(EFFECT_HIT_X + 3, EFFECT_HIT_Y + 3, COLOR_YELLOW)
    img_bank.pset(EFFECT_HIT_X + 4, EFFECT_HIT_Y + 3, COLOR_YELLOW)
    img_bank.pset(EFFECT_HIT_X + 3, EFFECT_HIT_Y + 4, COLOR_YELLOW)
    img_bank.pset(EFFECT_HIT_X + 4, EFFECT_HIT_Y + 4, COLOR_YELLOW)
    # Outer sparks
    img_bank.pset(EFFECT_HIT_X + 1, EFFECT_HIT_Y + 3, COLOR_ORANGE)
    img_bank.pset(EFFECT_HIT_X + 6, EFFECT_HIT_Y + 4, COLOR_ORANGE)
    img_bank.pset(EFFECT_HIT_X + 3, EFFECT_HIT_Y + 1, COLOR_ORANGE)
    img_bank.pset(EFFECT_HIT_X + 4, EFFECT_HIT_Y + 6, COLOR_ORANGE)
    print(f"Created hit effect (spark) at ({EFFECT_HIT_X},{EFFECT_HIT_Y}) in image bank 0.")

    # --- Create Attack Effect (Slash) at (8,32) ---
    # Clear area
    img_bank.rect(
        EFFECT_ATTACK_X, EFFECT_ATTACK_Y, EFFECT_ATTACK_WIDTH, EFFECT_ATTACK_HEIGHT,
        COLOR_TRANSPARENT
    )
    # Slash: a simple arc. Using line segments for simplicity.
    # For a 16x8 area.
    # Start (EFFECT_ATTACK_X, EFFECT_ATTACK_Y)
    # Points for a small arc: (2,5) to (6,1) to (13,1) to (15,3)
    # relative to sprite top-left
    img_bank.line(
        EFFECT_ATTACK_X + 2, EFFECT_ATTACK_Y + 6, EFFECT_ATTACK_X + 5,
        EFFECT_ATTACK_Y + 2, COLOR_LIGHT_BLUE
    )
    img_bank.line(
        EFFECT_ATTACK_X + 5, EFFECT_ATTACK_Y + 2, EFFECT_ATTACK_X + 10,
        EFFECT_ATTACK_Y + 1, COLOR_WHITE
    )
    img_bank.line(
        EFFECT_ATTACK_X + 10, EFFECT_ATTACK_Y + 1, EFFECT_ATTACK_X + 13,
        EFFECT_ATTACK_Y + 3, COLOR_LIGHT_BLUE
    )
    # Thicken it slightly
    img_bank.line(
        EFFECT_ATTACK_X + 3, EFFECT_ATTACK_Y + 6, EFFECT_ATTACK_X + 6,
        EFFECT_ATTACK_Y + 2, COLOR_LIGHT_BLUE
    )

    print_msg = (
        f"Created attack effect (slash) sprite at "
        f"({EFFECT_ATTACK_X},{EFFECT_ATTACK_Y}) in image bank 0."
    )
    print(print_msg)

    # Save the changes
    pyxel.save(RESOURCE_FILE)
    print(f"Saved changes to resource file: {RESOURCE_FILE}")

if __name__ == "__main__":
    main()
