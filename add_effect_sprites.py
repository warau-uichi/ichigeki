import pyxel
import os

RESOURCE_FILE = "assets/game.pyxres"
SCREEN_WIDTH_PIXELS = 32 * 8  # Consistent with previous scripts
SCREEN_HEIGHT_PIXELS = 24 * 8  # Consistent with previous scripts

# Sprite properties for Image Bank 2
EFFECT_SPRITE_WIDTH = 16
EFFECT_SPRITE_HEIGHT = 16

EFFECT_HIT_X = 0
EFFECT_HIT_Y = 0  # Top-left of image bank 2

EFFECT_ATTACK_X = 16  # Next to hit effect in image bank 2
EFFECT_ATTACK_Y = 0

EFFECT_PARRY_X = 32  # Next to attack effect in image bank 2
EFFECT_PARRY_Y = 0


COLOR_TRANSPARENT = 0
COLOR_BLACK = 1  # Added for consistency if outlines are needed
COLOR_DARK_BLUE = 2
COLOR_DARK_PURPLE = 3
COLOR_DARK_GREEN = 4
COLOR_BROWN = 5
COLOR_DARK_GRAY = 6  # For outlines or darker parts of effects
COLOR_WHITE = 7  # Standard White
COLOR_RED = 8  # Standard Red
COLOR_ORANGE = 9  # Standard Orange
COLOR_YELLOW = 10  # Standard Yellow
COLOR_LIGHT_GREEN = 11
COLOR_LIGHT_BLUE = 12  # Standard Light Blue
COLOR_LIGHT_PURPLE = 13
COLOR_PINK = 14
COLOR_PEACH = 15  # Or sometimes referred to as light pink/skin


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

    # Access image bank 2
    img_bank = pyxel.images[2]
    print("Targeting image bank 2 for effects.")

    # --- Enhanced Hit Effect (Spark) at (0,0) in Image Bank 2 ---
    # Clear area (16x16)
    img_bank.rect(
        EFFECT_HIT_X, EFFECT_HIT_Y, EFFECT_SPRITE_WIDTH, EFFECT_SPRITE_HEIGHT, COLOR_TRANSPARENT
    )

    # Central bright flash (white/yellow)
    center_x = EFFECT_HIT_X + EFFECT_SPRITE_WIDTH // 2
    center_y = EFFECT_HIT_Y + EFFECT_SPRITE_HEIGHT // 2

    img_bank.pset(center_x, center_y, COLOR_WHITE)
    img_bank.pset(center_x - 1, center_y, COLOR_YELLOW)
    img_bank.pset(center_x + 1, center_y, COLOR_YELLOW)
    img_bank.pset(center_x, center_y - 1, COLOR_YELLOW)
    img_bank.pset(center_x, center_y + 1, COLOR_YELLOW)
    img_bank.pset(center_x - 1, center_y - 1, COLOR_YELLOW)
    img_bank.pset(center_x + 1, center_y - 1, COLOR_YELLOW)
    img_bank.pset(center_x - 1, center_y + 1, COLOR_YELLOW)
    img_bank.pset(center_x + 1, center_y + 1, COLOR_YELLOW)

    # Radiating particles (orange/yellow)
    # Top-left
    img_bank.pset(center_x - 3, center_y - 3, COLOR_ORANGE)
    img_bank.pset(center_x - 4, center_y - 2, COLOR_YELLOW)
    img_bank.pset(center_x - 2, center_y - 4, COLOR_YELLOW)
    # Top-right
    img_bank.pset(center_x + 3, center_y - 3, COLOR_ORANGE)
    img_bank.pset(center_x + 4, center_y - 2, COLOR_YELLOW)
    img_bank.pset(center_x + 2, center_y - 4, COLOR_YELLOW)
    # Bottom-left
    img_bank.pset(center_x - 3, center_y + 3, COLOR_ORANGE)
    img_bank.pset(center_x - 4, center_y + 2, COLOR_YELLOW)
    img_bank.pset(center_x - 2, center_y + 4, COLOR_YELLOW)
    # Bottom-right
    img_bank.pset(center_x + 3, center_y + 3, COLOR_ORANGE)
    img_bank.pset(center_x + 4, center_y + 2, COLOR_YELLOW)
    img_bank.pset(center_x + 2, center_y + 4, COLOR_YELLOW)

    # Mid-radiants
    img_bank.pset(center_x - 5, center_y, COLOR_ORANGE)
    img_bank.pset(center_x + 5, center_y, COLOR_ORANGE)
    img_bank.pset(center_x, center_y - 5, COLOR_ORANGE)
    img_bank.pset(center_x, center_y + 5, COLOR_ORANGE)

    print(
        f"Created enhanced hit effect (spark) at ({EFFECT_HIT_X},{EFFECT_HIT_Y}) in image bank 2."
    )

    # --- Enhanced Attack Effect (Slash) at (16,0) in Image Bank 2 ---
    # A more dynamic and visible slash effect. Curved, sharp-looking.
    img_bank.rect(
        EFFECT_ATTACK_X,
        EFFECT_ATTACK_Y,
        EFFECT_SPRITE_WIDTH,
        EFFECT_SPRITE_HEIGHT,
        COLOR_TRANSPARENT,
    )

    # Main slash arc (thicker part - white)
    # Points: (2,13) -> (8,5) -> (13,2)
    x0, y0 = EFFECT_ATTACK_X + 2, EFFECT_ATTACK_Y + 13
    x1, y1 = EFFECT_ATTACK_X + 8, EFFECT_ATTACK_Y + 5
    x2, y2 = EFFECT_ATTACK_X + 13, EFFECT_ATTACK_Y + 2

    img_bank.line(x0, y0, x1, y1, COLOR_WHITE)
    img_bank.line(x1, y1, x2, y2, COLOR_WHITE)
    # Thicken it by shifting
    img_bank.line(x0 + 1, y0, x1 + 1, y1, COLOR_WHITE)
    img_bank.line(x1 + 1, y1, x2 + 1, y2, COLOR_WHITE)
    img_bank.line(x0, y0 - 1, x1, y1 - 1, COLOR_WHITE)  # for y-thickness
    img_bank.line(x1, y1 - 1, x2, y2 - 1, COLOR_WHITE)

    # Secondary arc (thinner part - light blue)
    # Points: (1,14) -> (7,6) -> (12,3) - slightly offset from white
    x0_lb, y0_lb = EFFECT_ATTACK_X + 1, EFFECT_ATTACK_Y + 14
    x1_lb, y1_lb = EFFECT_ATTACK_X + 7, EFFECT_ATTACK_Y + 6
    x2_lb, y2_lb = EFFECT_ATTACK_X + 12, EFFECT_ATTACK_Y + 3

    img_bank.line(x0_lb, y0_lb, x1_lb, y1_lb, COLOR_LIGHT_BLUE)
    img_bank.line(x1_lb, y1_lb, x2_lb, y2_lb, COLOR_LIGHT_BLUE)

    # Optional: a few fast-moving particles/lines
    img_bank.pset(EFFECT_ATTACK_X + 14, EFFECT_ATTACK_Y + 1, COLOR_WHITE)
    img_bank.pset(EFFECT_ATTACK_X + 15, EFFECT_ATTACK_Y + 0, COLOR_LIGHT_BLUE)
    img_bank.pset(EFFECT_ATTACK_X + 0, EFFECT_ATTACK_Y + 15, COLOR_LIGHT_BLUE)

    print(
        f"Created enhanced attack effect (slash) at "
        f"({EFFECT_ATTACK_X},{EFFECT_ATTACK_Y}) in image bank 2."
    )

    # --- New Parry Success Effect at (32,0) in Image Bank 2 ---
    # A brief, shield-like shimmer or a burst of sparks.
    img_bank.rect(
        EFFECT_PARRY_X,
        EFFECT_PARRY_Y,
        EFFECT_SPRITE_WIDTH,
        EFFECT_SPRITE_HEIGHT,
        COLOR_TRANSPARENT,
    )

    center_px = EFFECT_PARRY_X + EFFECT_SPRITE_WIDTH // 2
    center_py = EFFECT_PARRY_Y + EFFECT_SPRITE_HEIGHT // 2

    # Central shimmer/flash
    img_bank.rect(center_px - 2, center_py - 2, 5, 5, COLOR_WHITE)  # Central square
    img_bank.rectb(center_px - 3, center_py - 3, 7, 7, COLOR_LIGHT_BLUE)  # Outer border

    # Small radiating lines/sparks (more contained than hit spark)
    # Horizontal/Vertical emphasis
    img_bank.line(center_px - 5, center_py, center_px - 3, center_py, COLOR_YELLOW)
    img_bank.line(center_px + 3, center_py, center_px + 5, center_py, COLOR_YELLOW)
    img_bank.line(center_px, center_py - 5, center_px, center_py - 3, COLOR_YELLOW)
    img_bank.line(center_px, center_py + 3, center_px, center_py + 5, COLOR_YELLOW)

    # Diagonal small sparks
    img_bank.pset(center_px - 4, center_py - 4, COLOR_LIGHT_BLUE)
    img_bank.pset(center_px + 4, center_py - 4, COLOR_LIGHT_BLUE)
    img_bank.pset(center_px - 4, center_py + 4, COLOR_LIGHT_BLUE)
    img_bank.pset(center_px + 4, center_py + 4, COLOR_LIGHT_BLUE)

    img_bank.pset(center_px - 2, center_py - 2, COLOR_YELLOW)  # Inner corners of white sq
    img_bank.pset(center_px + 2, center_py - 2, COLOR_YELLOW)
    img_bank.pset(center_px - 2, center_py + 2, COLOR_YELLOW)
    img_bank.pset(center_px + 2, center_py + 2, COLOR_YELLOW)

    print(f"Created parry success effect at ({EFFECT_PARRY_X},{EFFECT_PARRY_Y}) in image bank 2.")

    # Save the changes
    pyxel.save(RESOURCE_FILE)
    print(f"Saved changes to resource file: {RESOURCE_FILE}")


if __name__ == "__main__":
    main()
