import pyxel
import os

RESOURCE_FILE = "assets/game.pyxres"
SCREEN_WIDTH_PIXELS = 32 * 8  # Matching the init from previous script
SCREEN_HEIGHT_PIXELS = 24 * 8  # Matching the init from previous script

# Sprite properties
PLAYER_IDLE_X = 0
PLAYER_IDLE_Y = 16  # Y-coordinate for idle, move, and other animations
PLAYER_MOVE_X = 16
PLAYER_MOVE_Y = PLAYER_IDLE_Y
SPRITE_WIDTH = 16
SPRITE_HEIGHT = 16

# New animation sprite coordinates
PLAYER_ANIM_Y = PLAYER_IDLE_Y  # All player sprites on the same row
PLAYER_ATTACK1_X = 48
PLAYER_ATTACK2_X = 64
PLAYER_ATTACK3_X = 80
PLAYER_PARRY_X = 96
PLAYER_DAMAGE_X = 112
PLAYER_VICTORY_X = 128


# Pyxel default color palette mapping for the Samurai character
COLOR_TRANSPARENT = 0
COLOR_BLACK = 1
COLOR_DARK_BLUE = 2  # Not used directly, preferring greys
COLOR_DARK_PURPLE = 3  # Potential for belt or accents
COLOR_DARK_GREEN = 4  # Not used
COLOR_BROWN = 5  # For sword hilt/sheath, skin tone accents
COLOR_DARK_GRAY = 6  # For hair, hakama
COLOR_LIGHT_GRAY = 7  # For lighter parts of uwagi, blade reflection
COLOR_WHITE = 8  # For uwagi (main body), eyes
COLOR_RED = 9  # For belt accent or details
COLOR_ORANGE = 10  # Not used
COLOR_YELLOW = 11  # For details, sword guard
COLOR_LIGHT_GREEN = 12  # Not used
COLOR_LIGHT_BLUE = 13  # Not used
COLOR_LIGHT_PURPLE = 14  # Not used
COLOR_PINK = 15  # Skin tone for face/hands

# Define semantic colors for the player sprite
COLOR_PLAYER_HAIR = COLOR_BLACK
COLOR_PLAYER_HAKAMA = COLOR_DARK_GRAY
COLOR_PLAYER_UWAGI = COLOR_WHITE
COLOR_PLAYER_SKIN = COLOR_PINK
COLOR_PLAYER_BELT = COLOR_RED
COLOR_PLAYER_SWORD_HILT = COLOR_BROWN
COLOR_PLAYER_SWORD_SHEATH = COLOR_BLACK
COLOR_PLAYER_SWORD_GUARD = COLOR_YELLOW
COLOR_PLAYER_SWORD_BLADE = COLOR_LIGHT_GRAY  # For the sword's blade
COLOR_PLAYER_EYE = COLOR_BLACK  # Simple black dot for eyes
COLOR_PLAYER_OUTLINE = COLOR_BLACK


def main():
    if not os.path.exists(RESOURCE_FILE):
        print(f"Error: Resource file {RESOURCE_FILE} not found.")
        print("Please run the previous script first.")
        return

    # Initialize Pyxel. This is needed before load.
    # Using simple init, assuming headless works if no pyxel.run() is called.
    pyxel.init(SCREEN_WIDTH_PIXELS, SCREEN_HEIGHT_PIXELS, title="Sprite Adder")
    print("Initialized Pyxel.")  # Fixed by ruff (was f-string)

    # Load the existing resource file
    pyxel.load(RESOURCE_FILE)
    print(f"Loaded resource file: {RESOURCE_FILE}")

    # Access image bank 0
    img_bank = pyxel.images[0]

    # --- Create Idle Sprite at (0,16) ---
    # Clear area for sprite with transparency
    img_bank.rect(PLAYER_IDLE_X, PLAYER_IDLE_Y, SPRITE_WIDTH, SPRITE_HEIGHT, COLOR_TRANSPARENT)

    # Head (approx. 5x4 pixels, centered horizontally)
    head_x = PLAYER_IDLE_X + 5
    head_y = PLAYER_IDLE_Y + 2
    img_bank.rect(head_x, head_y, 6, 1, COLOR_PLAYER_HAIR)  # Hair top
    img_bank.rect(head_x - 1, head_y + 1, 8, 1, COLOR_PLAYER_HAIR)  # Hair main
    img_bank.pset(head_x + 2, head_y + 1, COLOR_PLAYER_SKIN)  # Forehead part
    img_bank.pset(head_x + 3, head_y + 1, COLOR_PLAYER_SKIN)
    img_bank.rect(head_x, head_y + 2, 6, 2, COLOR_PLAYER_SKIN)  # Face
    img_bank.rect(head_x + 1, head_y + 2, 1, 1, COLOR_PLAYER_EYE)  # Left Eye
    img_bank.rect(head_x + 4, head_y + 2, 1, 1, COLOR_PLAYER_EYE)  # Right Eye
    img_bank.rect(head_x, head_y + 4, 6, 1, COLOR_PLAYER_HAIR)  # Hair bottom

    # Body (Uwagi - White/Light Gray) - Torso with wider shoulders
    # Shoulders
    img_bank.rect(PLAYER_IDLE_X + 2, PLAYER_IDLE_Y + 5, 12, 1, COLOR_PLAYER_UWAGI)
    img_bank.rect(PLAYER_IDLE_X + 3, PLAYER_IDLE_Y + 6, 10, 1, COLOR_PLAYER_UWAGI)
    # Torso
    img_bank.rect(PLAYER_IDLE_X + 4, PLAYER_IDLE_Y + 7, 8, 3, COLOR_PLAYER_UWAGI)

    # Belt (Red)
    img_bank.rect(PLAYER_IDLE_X + 4, PLAYER_IDLE_Y + 9, 8, 1, COLOR_PLAYER_BELT)
    img_bank.pset(PLAYER_IDLE_X + 3, PLAYER_IDLE_Y + 9, COLOR_PLAYER_BELT)  # Tie part
    img_bank.pset(PLAYER_IDLE_X + 12, PLAYER_IDLE_Y + 9, COLOR_PLAYER_BELT)  # Tie part

    # Legs (Hakama - Dark Gray) - Feet slightly apart
    # Upper part of Hakama (connected to Uwagi/Belt)
    img_bank.rect(PLAYER_IDLE_X + 4, PLAYER_IDLE_Y + 10, 8, 2, COLOR_PLAYER_HAKAMA)
    # Left Leg
    img_bank.rect(PLAYER_IDLE_X + 3, PLAYER_IDLE_Y + 12, 4, 3, COLOR_PLAYER_HAKAMA)
    img_bank.pset(PLAYER_IDLE_X + 2, PLAYER_IDLE_Y + 12, COLOR_PLAYER_HAKAMA)  # Wider stance
    img_bank.pset(PLAYER_IDLE_X + 3, PLAYER_IDLE_Y + 15, COLOR_BLACK)  # Foot outline
    img_bank.pset(PLAYER_IDLE_X + 4, PLAYER_IDLE_Y + 15, COLOR_BLACK)
    # Right Leg
    img_bank.rect(PLAYER_IDLE_X + 9, PLAYER_IDLE_Y + 12, 4, 3, COLOR_PLAYER_HAKAMA)
    img_bank.pset(PLAYER_IDLE_X + 11, PLAYER_IDLE_Y + 12, COLOR_PLAYER_HAKAMA)  # Wider stance
    img_bank.pset(PLAYER_IDLE_X + 10, PLAYER_IDLE_Y + 15, COLOR_BLACK)  # Foot outline
    img_bank.pset(PLAYER_IDLE_X + 11, PLAYER_IDLE_Y + 15, COLOR_BLACK)

    # Arms (Close to body or one hand on sword hilt)
    # Left Arm (slightly bent, close to body)
    img_bank.rect(PLAYER_IDLE_X + 2, PLAYER_IDLE_Y + 6, 2, 3, COLOR_PLAYER_UWAGI)
    img_bank.pset(PLAYER_IDLE_X + 2, PLAYER_IDLE_Y + 9, COLOR_PLAYER_SKIN)  # Hand
    img_bank.pset(PLAYER_IDLE_X + 3, PLAYER_IDLE_Y + 9, COLOR_PLAYER_SKIN)  # Hand

    # Right Arm (potentially resting on sword hilt)
    # Sheathed sword on left hip (player's left, screen right for viewer).
    # Char faces viewer: sword on player's left (screen left).
    # Char faces right: sword on player's left (still screen left).
    sword_sheath_x = PLAYER_IDLE_X + 2
    sword_sheath_y = PLAYER_IDLE_Y + 8
    img_bank.rect(sword_sheath_x, sword_sheath_y, 1, 5, COLOR_PLAYER_SWORD_SHEATH)  # Sheath
    img_bank.pset(sword_sheath_x, sword_sheath_y - 1, COLOR_PLAYER_SWORD_HILT)  # Hilt top
    img_bank.pset(sword_sheath_x + 1, sword_sheath_y - 1, COLOR_PLAYER_SWORD_GUARD)  # Guard part
    img_bank.pset(sword_sheath_x - 1, sword_sheath_y - 1, COLOR_PLAYER_SWORD_GUARD)  # Guard part

    # Right arm resting on hilt
    img_bank.rect(
        PLAYER_IDLE_X + 12, PLAYER_IDLE_Y + 6, 2, 2, COLOR_PLAYER_UWAGI
    )  # Shoulder/Upper arm
    img_bank.pset(PLAYER_IDLE_X + 11, PLAYER_IDLE_Y + 7, COLOR_PLAYER_UWAGI)
    img_bank.pset(PLAYER_IDLE_X + 10, PLAYER_IDLE_Y + 8, COLOR_PLAYER_SKIN)  # Hand on hilt
    img_bank.pset(PLAYER_IDLE_X + 11, PLAYER_IDLE_Y + 8, COLOR_PLAYER_SKIN)  # Hand on hilt

    # Outline (optional, but can help define the sprite)
    # Example: Hair outline already part of hair drawing.
    # Body outline
    # img_bank.rect_border(PLAYER_IDLE_X + 2, PLAYER_IDLE_Y + 5, 12, 8, COLOR_PLAYER_OUTLINE) #Uwg
    # img_bank.rect_border(PLAYER_IDLE_X + 3, PLAYER_IDLE_Y + 10, 10, 5, COLOR_PLAYER_OUTLINE) #Hkm
    # Pixel art outlines are often integrated or selectively applied.
    # Current drawing implies outlines with darker edge colors.

    print(f"Created idle player sprite at ({PLAYER_IDLE_X},{PLAYER_IDLE_Y}) in image bank 0.")

    # --- Create Movement Sprite Frame 1 at (16,16) ---
    # Desc: Player's R leg forward, L leg back. Slight body lean/arm movement.
    img_bank.rect(PLAYER_MOVE_X, PLAYER_MOVE_Y, SPRITE_WIDTH, SPRITE_HEIGHT, COLOR_TRANSPARENT)

    # Head (similar to idle, maybe slight tilt or different hair flow if possible in 16x16)
    head_x = PLAYER_MOVE_X + 5
    head_y = PLAYER_MOVE_Y + 2
    img_bank.rect(head_x, head_y, 6, 1, COLOR_PLAYER_HAIR)
    img_bank.rect(head_x - 1, head_y + 1, 8, 1, COLOR_PLAYER_HAIR)
    img_bank.pset(head_x + 2, head_y + 1, COLOR_PLAYER_SKIN)
    img_bank.pset(head_x + 3, head_y + 1, COLOR_PLAYER_SKIN)
    img_bank.rect(head_x, head_y + 2, 6, 2, COLOR_PLAYER_SKIN)
    img_bank.rect(head_x + 1, head_y + 2, 1, 1, COLOR_PLAYER_EYE)
    img_bank.rect(head_x + 4, head_y + 2, 1, 1, COLOR_PLAYER_EYE)
    img_bank.rect(head_x, head_y + 4, 6, 1, COLOR_PLAYER_HAIR)

    # Body (Uwagi) - Slight lean if possible, or arm swing can imply this
    # Shoulders
    img_bank.rect(PLAYER_MOVE_X + 2, PLAYER_MOVE_Y + 5, 12, 1, COLOR_PLAYER_UWAGI)
    img_bank.rect(PLAYER_MOVE_X + 3, PLAYER_MOVE_Y + 6, 10, 1, COLOR_PLAYER_UWAGI)
    # Torso
    img_bank.rect(PLAYER_MOVE_X + 4, PLAYER_MOVE_Y + 7, 8, 3, COLOR_PLAYER_UWAGI)

    # Belt
    img_bank.rect(PLAYER_MOVE_X + 4, PLAYER_MOVE_Y + 9, 8, 1, COLOR_PLAYER_BELT)
    img_bank.pset(PLAYER_MOVE_X + 3, PLAYER_MOVE_Y + 9, COLOR_PLAYER_BELT)
    img_bank.pset(PLAYER_MOVE_X + 12, PLAYER_MOVE_Y + 9, COLOR_PLAYER_BELT)

    # Legs (Hakama) - Player's Right leg forward (screen right), Left leg back
    # Upper part of Hakama
    img_bank.rect(PLAYER_MOVE_X + 4, PLAYER_MOVE_Y + 10, 8, 2, COLOR_PLAYER_HAKAMA)

    # Right Leg (Forward) - Appears slightly longer/more prominent
    img_bank.rect(
        PLAYER_MOVE_X + 8, PLAYER_MOVE_Y + 12, 4, 3, COLOR_PLAYER_HAKAMA
    )  # Shifted right
    img_bank.pset(PLAYER_MOVE_X + 9, PLAYER_MOVE_Y + 15, COLOR_BLACK)  # Foot
    img_bank.pset(PLAYER_MOVE_X + 10, PLAYER_MOVE_Y + 15, COLOR_BLACK)

    # Left Leg (Back) - Appears slightly shorter/less prominent
    img_bank.rect(PLAYER_MOVE_X + 3, PLAYER_MOVE_Y + 12, 3, 2, COLOR_PLAYER_HAKAMA)  # Shorter
    img_bank.pset(PLAYER_MOVE_X + 4, PLAYER_MOVE_Y + 14, COLOR_BLACK)  # Foot back
    img_bank.pset(PLAYER_MOVE_X + 5, PLAYER_MOVE_Y + 14, COLOR_BLACK)

    # Arms - Suggest movement. E.g. Left arm forward, Right arm back.
    # Left Arm (Swinging forward)
    img_bank.rect(PLAYER_MOVE_X + 2, PLAYER_MOVE_Y + 6, 2, 1, COLOR_PLAYER_UWAGI)  # Shoulder part
    img_bank.rect(
        PLAYER_MOVE_X + 3, PLAYER_MOVE_Y + 7, 2, 2, COLOR_PLAYER_UWAGI
    )  # Arm extended slightly
    img_bank.pset(PLAYER_MOVE_X + 4, PLAYER_MOVE_Y + 9, COLOR_PLAYER_SKIN)  # Hand

    # Right Arm (Swinging back)
    img_bank.rect(
        PLAYER_MOVE_X + 12, PLAYER_MOVE_Y + 6, 2, 2, COLOR_PLAYER_UWAGI
    )  # Shoulder part (mostly hidden)
    img_bank.pset(PLAYER_MOVE_X + 11, PLAYER_MOVE_Y + 7, COLOR_PLAYER_UWAGI)  # Arm back
    img_bank.pset(PLAYER_MOVE_X + 10, PLAYER_MOVE_Y + 8, COLOR_PLAYER_SKIN)  # Hand back

    # Sword (Stays on left hip, might shift slightly with body)
    sword_sheath_x = PLAYER_MOVE_X + 3  # Adjusted for body movement
    sword_sheath_y = PLAYER_MOVE_Y + 8
    img_bank.rect(sword_sheath_x, sword_sheath_y, 1, 5, COLOR_PLAYER_SWORD_SHEATH)
    img_bank.pset(sword_sheath_x, sword_sheath_y - 1, COLOR_PLAYER_SWORD_HILT)
    img_bank.pset(sword_sheath_x + 1, sword_sheath_y - 1, COLOR_PLAYER_SWORD_GUARD)
    img_bank.pset(sword_sheath_x - 1, sword_sheath_y - 1, COLOR_PLAYER_SWORD_GUARD)

    print(
        f"Created move sprite Frame 1 at ({PLAYER_MOVE_X},{PLAYER_MOVE_Y}) in bank 0."
    )

    # --- Create Movement Sprite Frame 2 at (32,16) ---
    # Desc: Player's L leg forward, R leg back. Complementary arm movement.
    PLAYER_MOVE_FRAME2_X = PLAYER_MOVE_X + SPRITE_WIDTH
    PLAYER_MOVE_FRAME2_Y = PLAYER_MOVE_Y
    img_bank.rect(
        PLAYER_MOVE_FRAME2_X, PLAYER_MOVE_FRAME2_Y, SPRITE_WIDTH, SPRITE_HEIGHT, COLOR_TRANSPARENT
    )

    # Head (similar to Frame 1)
    head_x = PLAYER_MOVE_FRAME2_X + 5
    head_y = PLAYER_MOVE_FRAME2_Y + 2
    img_bank.rect(head_x, head_y, 6, 1, COLOR_PLAYER_HAIR)
    img_bank.rect(head_x - 1, head_y + 1, 8, 1, COLOR_PLAYER_HAIR)
    img_bank.pset(head_x + 2, head_y + 1, COLOR_PLAYER_SKIN)
    img_bank.pset(head_x + 3, head_y + 1, COLOR_PLAYER_SKIN)
    img_bank.rect(head_x, head_y + 2, 6, 2, COLOR_PLAYER_SKIN)
    img_bank.rect(head_x + 1, head_y + 2, 1, 1, COLOR_PLAYER_EYE)
    img_bank.rect(head_x + 4, head_y + 2, 1, 1, COLOR_PLAYER_EYE)
    img_bank.rect(head_x, head_y + 4, 6, 1, COLOR_PLAYER_HAIR)

    # Body (Uwagi) - Consistent with Frame 1
    img_bank.rect(PLAYER_MOVE_FRAME2_X + 2, PLAYER_MOVE_FRAME2_Y + 5, 12, 1, COLOR_PLAYER_UWAGI)
    img_bank.rect(PLAYER_MOVE_FRAME2_X + 3, PLAYER_MOVE_FRAME2_Y + 6, 10, 1, COLOR_PLAYER_UWAGI)
    img_bank.rect(PLAYER_MOVE_FRAME2_X + 4, PLAYER_MOVE_FRAME2_Y + 7, 8, 3, COLOR_PLAYER_UWAGI)

    # Belt
    img_bank.rect(PLAYER_MOVE_FRAME2_X + 4, PLAYER_MOVE_FRAME2_Y + 9, 8, 1, COLOR_PLAYER_BELT)
    img_bank.pset(PLAYER_MOVE_FRAME2_X + 3, PLAYER_MOVE_FRAME2_Y + 9, COLOR_PLAYER_BELT)
    img_bank.pset(PLAYER_MOVE_FRAME2_X + 12, PLAYER_MOVE_FRAME2_Y + 9, COLOR_PLAYER_BELT)

    # Legs (Hakama) - Player's Left leg forward (screen left), Right leg back
    img_bank.rect(PLAYER_MOVE_FRAME2_X + 4, PLAYER_MOVE_FRAME2_Y + 10, 8, 2, COLOR_PLAYER_HAKAMA)

    # Left Leg (Forward)
    img_bank.rect(
        PLAYER_MOVE_FRAME2_X + 3, PLAYER_MOVE_FRAME2_Y + 12, 4, 3, COLOR_PLAYER_HAKAMA
    )  # Shifted left
    img_bank.pset(PLAYER_MOVE_FRAME2_X + 4, PLAYER_MOVE_FRAME2_Y + 15, COLOR_BLACK)  # Foot
    img_bank.pset(PLAYER_MOVE_FRAME2_X + 5, PLAYER_MOVE_FRAME2_Y + 15, COLOR_BLACK)

    # Right Leg (Back)
    img_bank.rect(
        PLAYER_MOVE_FRAME2_X + 9, PLAYER_MOVE_FRAME2_Y + 12, 3, 2, COLOR_PLAYER_HAKAMA
    )  # Shorter
    img_bank.pset(PLAYER_MOVE_FRAME2_X + 10, PLAYER_MOVE_FRAME2_Y + 14, COLOR_BLACK)  # Foot back
    img_bank.pset(PLAYER_MOVE_FRAME2_X + 11, PLAYER_MOVE_FRAME2_Y + 14, COLOR_BLACK)

    # Arms - Complementary to Frame 1. Right arm forward, Left arm back.
    # Right Arm (Swinging forward)
    img_bank.rect(
        PLAYER_MOVE_FRAME2_X + 12, PLAYER_MOVE_FRAME2_Y + 6, 2, 1, COLOR_PLAYER_UWAGI
    )  # Shoulder part
    img_bank.rect(
        PLAYER_MOVE_FRAME2_X + 11, PLAYER_MOVE_FRAME2_Y + 7, 2, 2, COLOR_PLAYER_UWAGI
    )  # Arm extended slightly
    img_bank.pset(PLAYER_MOVE_FRAME2_X + 10, PLAYER_MOVE_FRAME2_Y + 9, COLOR_PLAYER_SKIN)  # Hand

    # Left Arm (Swinging back)
    img_bank.rect(
        PLAYER_MOVE_FRAME2_X + 2, PLAYER_MOVE_FRAME2_Y + 6, 2, 2, COLOR_PLAYER_UWAGI
    )  # Shoulder part
    img_bank.pset(
        PLAYER_MOVE_FRAME2_X + 3, PLAYER_MOVE_FRAME2_Y + 7, COLOR_PLAYER_UWAGI
    )  # Arm back
    img_bank.pset(
        PLAYER_MOVE_FRAME2_X + 4, PLAYER_MOVE_FRAME2_Y + 8, COLOR_PLAYER_SKIN
    )  # Hand back

    # Sword (Stays on left hip, might shift slightly with body)
    sword_sheath_x = PLAYER_MOVE_FRAME2_X + 2  # Adjusted for body movement
    sword_sheath_y = PLAYER_MOVE_FRAME2_Y + 8
    img_bank.rect(sword_sheath_x, sword_sheath_y, 1, 5, COLOR_PLAYER_SWORD_SHEATH)
    img_bank.pset(sword_sheath_x, sword_sheath_y - 1, COLOR_PLAYER_SWORD_HILT)
    img_bank.pset(sword_sheath_x + 1, sword_sheath_y - 1, COLOR_PLAYER_SWORD_GUARD)
    img_bank.pset(sword_sheath_x - 1, sword_sheath_y - 1, COLOR_PLAYER_SWORD_GUARD)

    print(
        f"Created move sprite Frame 2 at ({PLAYER_MOVE_FRAME2_X},{PLAYER_MOVE_FRAME2_Y}) in b0."
    )

    print_msg = (
        f"Created movement sprites at ({PLAYER_MOVE_X},{PLAYER_MOVE_Y}) "
        f"and ({PLAYER_MOVE_FRAME2_X},{PLAYER_MOVE_FRAME2_Y}) in bank 0."
    )
    print(print_msg)

    # --- Create Attack Animation Sprites ---
    # Frame 1: Startup (48,16) - Hand moving to sword, slight crouch/lean.
    img_bank.rect(PLAYER_ATTACK1_X, PLAYER_ANIM_Y, SPRITE_WIDTH, SPRITE_HEIGHT, COLOR_TRANSPARENT)
    # Body slightly lower than idle
    head_x = PLAYER_ATTACK1_X + 5
    head_y = PLAYER_ANIM_Y + 3  # Lowered head
    img_bank.rect(head_x, head_y, 6, 1, COLOR_PLAYER_HAIR)
    img_bank.rect(head_x - 1, head_y + 1, 8, 1, COLOR_PLAYER_HAIR)
    img_bank.pset(head_x + 2, head_y + 1, COLOR_PLAYER_SKIN)
    img_bank.pset(head_x + 3, head_y + 1, COLOR_PLAYER_SKIN)
    img_bank.rect(head_x, head_y + 2, 6, 2, COLOR_PLAYER_SKIN)
    img_bank.rect(head_x + 1, head_y + 2, 1, 1, COLOR_PLAYER_EYE)
    img_bank.rect(head_x + 4, head_y + 2, 1, 1, COLOR_PLAYER_EYE)
    img_bank.rect(head_x, head_y + 4, 6, 1, COLOR_PLAYER_HAIR)

    # Uwagi - slightly compressed for crouch
    img_bank.rect(PLAYER_ATTACK1_X + 2, PLAYER_ANIM_Y + 6, 12, 1, COLOR_PLAYER_UWAGI)  # Shoulders
    img_bank.rect(
        PLAYER_ATTACK1_X + 3, PLAYER_ANIM_Y + 7, 10, 3, COLOR_PLAYER_UWAGI
    )  # Torso a bit lower
    # Belt
    img_bank.rect(PLAYER_ATTACK1_X + 4, PLAYER_ANIM_Y + 10, 8, 1, COLOR_PLAYER_BELT)
    img_bank.pset(PLAYER_ATTACK1_X + 3, PLAYER_ANIM_Y + 10, COLOR_PLAYER_BELT)
    img_bank.pset(PLAYER_ATTACK1_X + 12, PLAYER_ANIM_Y + 10, COLOR_PLAYER_BELT)

    # Legs (Hakama) - Crouched
    img_bank.rect(
        PLAYER_ATTACK1_X + 3, PLAYER_ANIM_Y + 11, 10, 1, COLOR_PLAYER_HAKAMA
    )  # Upper part
    img_bank.rect(
        PLAYER_ATTACK1_X + 2, PLAYER_ANIM_Y + 12, 5, 3, COLOR_PLAYER_HAKAMA
    )  # Left leg bent
    img_bank.rect(
        PLAYER_ATTACK1_X + 9, PLAYER_ANIM_Y + 12, 5, 3, COLOR_PLAYER_HAKAMA
    )  # Right leg bent
    img_bank.pset(PLAYER_ATTACK1_X + 3, PLAYER_ANIM_Y + 15, COLOR_BLACK)  # Foot
    img_bank.pset(PLAYER_ATTACK1_X + 4, PLAYER_ANIM_Y + 15, COLOR_BLACK)
    img_bank.pset(PLAYER_ATTACK1_X + 11, PLAYER_ANIM_Y + 15, COLOR_BLACK)  # Foot
    img_bank.pset(PLAYER_ATTACK1_X + 12, PLAYER_ANIM_Y + 15, COLOR_BLACK)

    # Arms - Right hand moving to sword hilt (on player's left)
    # Left arm may be slightly back for balance
    img_bank.rect(PLAYER_ATTACK1_X + 12, PLAYER_ANIM_Y + 7, 2, 3, COLOR_PLAYER_UWAGI)  # Left arm
    img_bank.pset(PLAYER_ATTACK1_X + 12, PLAYER_ANIM_Y + 10, COLOR_PLAYER_SKIN)  # Left hand

    # Sword hilt access
    sword_sheath_x = PLAYER_ATTACK1_X + 1  # Sword shifted slightly forward due to body turn/crouch
    sword_sheath_y = PLAYER_ANIM_Y + 9
    img_bank.rect(sword_sheath_x, sword_sheath_y, 1, 5, COLOR_PLAYER_SWORD_SHEATH)
    img_bank.pset(sword_sheath_x, sword_sheath_y - 1, COLOR_PLAYER_SWORD_HILT)
    img_bank.pset(sword_sheath_x + 1, sword_sheath_y - 1, COLOR_PLAYER_SWORD_GUARD)
    img_bank.pset(sword_sheath_x - 1, sword_sheath_y - 1, COLOR_PLAYER_SWORD_GUARD)

    # Right arm reaching for hilt
    img_bank.rect(
        PLAYER_ATTACK1_X + 3, PLAYER_ANIM_Y + 7, 2, 2, COLOR_PLAYER_UWAGI
    )  # Right shoulder/upper arm
    img_bank.line(
        PLAYER_ATTACK1_X + 4,
        PLAYER_ANIM_Y + 8,
        PLAYER_ATTACK1_X + 2,
        PLAYER_ANIM_Y + 9,
        COLOR_PLAYER_UWAGI,
    )  # Forearm
    img_bank.pset(
        PLAYER_ATTACK1_X + 2, PLAYER_ANIM_Y + 9, COLOR_PLAYER_SKIN
    )  # Right hand near hilt
    img_bank.pset(PLAYER_ATTACK1_X + 1, PLAYER_ANIM_Y + 9, COLOR_PLAYER_SKIN)
    print(f"Created Attack Startup sprite at ({PLAYER_ATTACK1_X},{PLAYER_ANIM_Y}).")

    # Frame 2: Active (64,16) - Sword drawn and extended.
    img_bank.rect(PLAYER_ATTACK2_X, PLAYER_ANIM_Y, SPRITE_WIDTH, SPRITE_HEIGHT, COLOR_TRANSPARENT)
    # Body lunging forward, character may be slightly to the left of the cell
    head_x = PLAYER_ATTACK2_X + 2  # Head shifted left due to lunge
    head_y = PLAYER_ANIM_Y + 3
    img_bank.rect(head_x, head_y, 6, 1, COLOR_PLAYER_HAIR)
    img_bank.rect(head_x - 1, head_y + 1, 8, 1, COLOR_PLAYER_HAIR)
    img_bank.pset(head_x + 2, head_y + 1, COLOR_PLAYER_SKIN)
    img_bank.pset(head_x + 3, head_y + 1, COLOR_PLAYER_SKIN)
    img_bank.rect(head_x, head_y + 2, 6, 2, COLOR_PLAYER_SKIN)  # Face
    img_bank.rect(head_x + 1, head_y + 2, 1, 1, COLOR_PLAYER_EYE)  # Eyes focused
    img_bank.rect(head_x + 4, head_y + 2, 1, 1, COLOR_PLAYER_EYE)
    img_bank.rect(head_x, head_y + 4, 6, 1, COLOR_PLAYER_HAIR)

    # Body - Torso extended
    img_bank.rect(PLAYER_ATTACK2_X + 1, PLAYER_ANIM_Y + 6, 10, 1, COLOR_PLAYER_UWAGI)  # Shoulders
    img_bank.rect(PLAYER_ATTACK2_X + 2, PLAYER_ANIM_Y + 7, 8, 3, COLOR_PLAYER_UWAGI)  # Torso
    # Belt
    img_bank.rect(PLAYER_ATTACK2_X + 2, PLAYER_ANIM_Y + 10, 8, 1, COLOR_PLAYER_BELT)

    # Legs - Lunging stance, right leg forward
    img_bank.rect(
        PLAYER_ATTACK2_X + 2, PLAYER_ANIM_Y + 11, 8, 1, COLOR_PLAYER_HAKAMA
    )  # Hakama top
    img_bank.rect(
        PLAYER_ATTACK2_X + 0, PLAYER_ANIM_Y + 12, 4, 2, COLOR_PLAYER_HAKAMA
    )  # Left leg back, bent
    img_bank.pset(PLAYER_ATTACK2_X + 1, PLAYER_ANIM_Y + 14, COLOR_BLACK)  # Left foot
    img_bank.rect(
        PLAYER_ATTACK2_X + 5, PLAYER_ANIM_Y + 12, 4, 3, COLOR_PLAYER_HAKAMA
    )  # Right leg extended
    img_bank.pset(PLAYER_ATTACK2_X + 8, PLAYER_ANIM_Y + 15, COLOR_BLACK)  # Right foot
    img_bank.pset(PLAYER_ATTACK2_X + 9, PLAYER_ANIM_Y + 15, COLOR_BLACK)

    # Arms and Sword
    # Right arm extended with sword
    img_bank.rect(
        PLAYER_ATTACK2_X + 4, PLAYER_ANIM_Y + 7, 3, 2, COLOR_PLAYER_UWAGI
    )  # Right shoulder/upper arm
    img_bank.line(
        PLAYER_ATTACK2_X + 6,
        PLAYER_ANIM_Y + 8,
        PLAYER_ATTACK2_X + 8,
        PLAYER_ANIM_Y + 9,
        COLOR_PLAYER_SKIN,
    )  # Right hand

    # Sword Blade - extends to the right
    sword_hilt_attach_x = PLAYER_ATTACK2_X + 9
    sword_hilt_attach_y = PLAYER_ANIM_Y + 9
    img_bank.pset(sword_hilt_attach_x - 1, sword_hilt_attach_y, COLOR_PLAYER_SWORD_GUARD)  # Guard
    img_bank.pset(sword_hilt_attach_x, sword_hilt_attach_y, COLOR_PLAYER_SWORD_HILT)
    img_bank.line(
        sword_hilt_attach_x + 1,
        sword_hilt_attach_y,
        PLAYER_ATTACK2_X + 15,
        sword_hilt_attach_y,
        COLOR_PLAYER_SWORD_BLADE,
    )  # Blade
    img_bank.pset(PLAYER_ATTACK2_X + 14, sword_hilt_attach_y - 1, COLOR_PLAYER_SWORD_BLADE)  # Tip

    # Left arm back for balance or off-screen
    img_bank.rect(PLAYER_ATTACK2_X + 1, PLAYER_ANIM_Y + 7, 2, 3, COLOR_PLAYER_UWAGI)
    img_bank.pset(PLAYER_ATTACK2_X + 1, PLAYER_ANIM_Y + 10, COLOR_PLAYER_SKIN)
    print(f"Created Attack Active sprite at ({PLAYER_ATTACK2_X},{PLAYER_ANIM_Y}).")

    # Frame 3: Recovery (80,16) - Sword being sheathed or returning to ready.
    img_bank.rect(PLAYER_ATTACK3_X, PLAYER_ANIM_Y, SPRITE_WIDTH, SPRITE_HEIGHT, COLOR_TRANSPARENT)
    # Similar to idle or startup, but perhaps sword still visible or body settling.
    # For simplicity, let's make it similar to idle but with sword visible and being put away.
    head_x = PLAYER_ATTACK3_X + 5
    head_y = PLAYER_ANIM_Y + 2
    img_bank.rect(head_x, head_y, 6, 1, COLOR_PLAYER_HAIR)
    img_bank.rect(head_x - 1, head_y + 1, 8, 1, COLOR_PLAYER_HAIR)
    img_bank.pset(head_x + 2, head_y + 1, COLOR_PLAYER_SKIN)
    img_bank.pset(head_x + 3, head_y + 1, COLOR_PLAYER_SKIN)
    img_bank.rect(head_x, head_y + 2, 6, 2, COLOR_PLAYER_SKIN)
    img_bank.rect(head_x + 1, head_y + 2, 1, 1, COLOR_PLAYER_EYE)
    img_bank.rect(head_x + 4, head_y + 2, 1, 1, COLOR_PLAYER_EYE)
    img_bank.rect(head_x, head_y + 4, 6, 1, COLOR_PLAYER_HAIR)

    img_bank.rect(PLAYER_ATTACK3_X + 2, PLAYER_ANIM_Y + 5, 12, 1, COLOR_PLAYER_UWAGI)
    img_bank.rect(PLAYER_ATTACK3_X + 3, PLAYER_ANIM_Y + 6, 10, 1, COLOR_PLAYER_UWAGI)
    img_bank.rect(PLAYER_ATTACK3_X + 4, PLAYER_ANIM_Y + 7, 8, 3, COLOR_PLAYER_UWAGI)
    img_bank.rect(PLAYER_ATTACK3_X + 4, PLAYER_ANIM_Y + 9, 8, 1, COLOR_PLAYER_BELT)
    img_bank.pset(PLAYER_ATTACK3_X + 3, PLAYER_ANIM_Y + 9, COLOR_PLAYER_BELT)
    img_bank.pset(PLAYER_ATTACK3_X + 12, PLAYER_ANIM_Y + 9, COLOR_PLAYER_BELT)

    img_bank.rect(PLAYER_ATTACK3_X + 4, PLAYER_ANIM_Y + 10, 8, 2, COLOR_PLAYER_HAKAMA)
    img_bank.rect(PLAYER_ATTACK3_X + 3, PLAYER_ANIM_Y + 12, 4, 3, COLOR_PLAYER_HAKAMA)
    img_bank.pset(PLAYER_ATTACK3_X + 2, PLAYER_ANIM_Y + 12, COLOR_PLAYER_HAKAMA)
    img_bank.pset(PLAYER_ATTACK3_X + 3, PLAYER_ANIM_Y + 15, COLOR_BLACK)
    img_bank.pset(PLAYER_ATTACK3_X + 4, PLAYER_ANIM_Y + 15, COLOR_BLACK)
    img_bank.rect(PLAYER_ATTACK3_X + 9, PLAYER_ANIM_Y + 12, 4, 3, COLOR_PLAYER_HAKAMA)
    img_bank.pset(PLAYER_ATTACK3_X + 11, PLAYER_ANIM_Y + 12, COLOR_PLAYER_HAKAMA)
    img_bank.pset(PLAYER_ATTACK3_X + 10, PLAYER_ANIM_Y + 15, COLOR_BLACK)
    img_bank.pset(PLAYER_ATTACK3_X + 11, PLAYER_ANIM_Y + 15, COLOR_BLACK)

    # Arms - Sword being sheathed. Right hand guiding sword, left hand near sheath.
    # Sword (mostly sheathed or blade pointing down/back)
    sword_sheath_x = PLAYER_ATTACK3_X + 2
    sword_sheath_y = PLAYER_ANIM_Y + 8
    img_bank.rect(sword_sheath_x, sword_sheath_y, 1, 5, COLOR_PLAYER_SWORD_SHEATH)  # Sheath
    img_bank.line(
        sword_sheath_x,
        sword_sheath_y - 1,
        sword_sheath_x,
        sword_sheath_y - 3,
        COLOR_PLAYER_SWORD_BLADE,
    )  # Tip of blade visible
    img_bank.pset(sword_sheath_x, sword_sheath_y - 4, COLOR_PLAYER_SWORD_HILT)  # Hilt
    img_bank.pset(sword_sheath_x + 1, sword_sheath_y - 4, COLOR_PLAYER_SWORD_GUARD)
    img_bank.pset(sword_sheath_x - 1, sword_sheath_y - 4, COLOR_PLAYER_SWORD_GUARD)

    # Right arm
    img_bank.rect(PLAYER_ATTACK3_X + 12, PLAYER_ANIM_Y + 6, 2, 2, COLOR_PLAYER_UWAGI)
    img_bank.pset(PLAYER_ATTACK3_X + 11, PLAYER_ANIM_Y + 7, COLOR_PLAYER_UWAGI)
    img_bank.pset(
        PLAYER_ATTACK3_X + 10, PLAYER_ANIM_Y + 8, COLOR_PLAYER_SKIN
    )  # Hand near where hilt would be if fully sheathed

    # Left arm
    img_bank.rect(
        PLAYER_ATTACK3_X + 2, PLAYER_ANIM_Y + 6, 2, 3, COLOR_PLAYER_UWAGI
    )  # Left arm guiding
    img_bank.pset(
        PLAYER_ATTACK3_X + 3, PLAYER_ANIM_Y + 8, COLOR_PLAYER_SKIN
    )  # Left hand on sheath
    print(f"Created Attack Recovery sprite at ({PLAYER_ATTACK3_X},{PLAYER_ANIM_Y}).")

    # --- Create Parry Animation Sprite (96,16) ---
    img_bank.rect(PLAYER_PARRY_X, PLAYER_ANIM_Y, SPRITE_WIDTH, SPRITE_HEIGHT, COLOR_TRANSPARENT)
    # Defensive posture, sword held horizontally or vertically in front.
    # Body slightly braced.
    head_x = PLAYER_PARRY_X + 5
    head_y = PLAYER_ANIM_Y + 2
    img_bank.rect(head_x, head_y, 6, 1, COLOR_PLAYER_HAIR)
    img_bank.rect(head_x - 1, head_y + 1, 8, 1, COLOR_PLAYER_HAIR)
    img_bank.pset(head_x + 2, head_y + 1, COLOR_PLAYER_SKIN)
    img_bank.pset(head_x + 3, head_y + 1, COLOR_PLAYER_SKIN)
    img_bank.rect(head_x, head_y + 2, 6, 2, COLOR_PLAYER_SKIN)
    img_bank.rect(head_x + 1, head_y + 2, 1, 1, COLOR_PLAYER_EYE)  # Determined eyes
    img_bank.rect(head_x + 4, head_y + 2, 1, 1, COLOR_PLAYER_EYE)
    img_bank.rect(head_x, head_y + 4, 6, 1, COLOR_PLAYER_HAIR)

    img_bank.rect(PLAYER_PARRY_X + 2, PLAYER_ANIM_Y + 5, 12, 1, COLOR_PLAYER_UWAGI)
    img_bank.rect(PLAYER_PARRY_X + 3, PLAYER_ANIM_Y + 6, 10, 1, COLOR_PLAYER_UWAGI)
    img_bank.rect(PLAYER_PARRY_X + 4, PLAYER_ANIM_Y + 7, 8, 3, COLOR_PLAYER_UWAGI)
    img_bank.rect(PLAYER_PARRY_X + 4, PLAYER_ANIM_Y + 9, 8, 1, COLOR_PLAYER_BELT)
    img_bank.pset(PLAYER_PARRY_X + 3, PLAYER_ANIM_Y + 9, COLOR_PLAYER_BELT)
    img_bank.pset(PLAYER_PARRY_X + 12, PLAYER_ANIM_Y + 9, COLOR_PLAYER_BELT)

    img_bank.rect(PLAYER_PARRY_X + 4, PLAYER_ANIM_Y + 10, 8, 2, COLOR_PLAYER_HAKAMA)
    img_bank.rect(PLAYER_PARRY_X + 3, PLAYER_ANIM_Y + 12, 4, 3, COLOR_PLAYER_HAKAMA)  # Legs solid
    img_bank.pset(PLAYER_PARRY_X + 2, PLAYER_ANIM_Y + 12, COLOR_PLAYER_HAKAMA)
    img_bank.pset(PLAYER_PARRY_X + 3, PLAYER_ANIM_Y + 15, COLOR_BLACK)
    img_bank.pset(PLAYER_PARRY_X + 4, PLAYER_ANIM_Y + 15, COLOR_BLACK)
    img_bank.rect(PLAYER_PARRY_X + 9, PLAYER_ANIM_Y + 12, 4, 3, COLOR_PLAYER_HAKAMA)
    img_bank.pset(PLAYER_PARRY_X + 11, PLAYER_ANIM_Y + 12, COLOR_PLAYER_HAKAMA)
    img_bank.pset(PLAYER_PARRY_X + 10, PLAYER_ANIM_Y + 15, COLOR_BLACK)
    img_bank.pset(PLAYER_PARRY_X + 11, PLAYER_ANIM_Y + 15, COLOR_BLACK)

    # Arms holding sword defensively (e.g. horizontally in front)
    # Left arm
    img_bank.rect(PLAYER_PARRY_X + 2, PLAYER_ANIM_Y + 6, 2, 3, COLOR_PLAYER_UWAGI)
    img_bank.pset(PLAYER_PARRY_X + 3, PLAYER_ANIM_Y + 8, COLOR_PLAYER_SKIN)  # Left hand
    # Right arm
    img_bank.rect(PLAYER_PARRY_X + 12, PLAYER_ANIM_Y + 6, 2, 3, COLOR_PLAYER_UWAGI)
    img_bank.pset(PLAYER_PARRY_X + 11, PLAYER_ANIM_Y + 8, COLOR_PLAYER_SKIN)  # Right hand

    # Sword held horizontally
    sword_y_parry = PLAYER_ANIM_Y + 8
    img_bank.line(
        PLAYER_PARRY_X + 4,
        sword_y_parry,
        PLAYER_PARRY_X + 10,
        sword_y_parry,
        COLOR_PLAYER_SWORD_HILT,
    )  # Hilt part
    img_bank.line(
        PLAYER_PARRY_X + 2,
        sword_y_parry,
        PLAYER_PARRY_X + 4,
        sword_y_parry,
        COLOR_PLAYER_SWORD_BLADE,
    )  # Left part of blade
    img_bank.line(
        PLAYER_PARRY_X + 10,
        sword_y_parry,
        PLAYER_PARRY_X + 13,
        sword_y_parry,
        COLOR_PLAYER_SWORD_BLADE,
    )  # Right part of blade
    img_bank.pset(PLAYER_PARRY_X + 6, sword_y_parry, COLOR_PLAYER_SWORD_GUARD)  # Center guard
    print(f"Created Parry sprite at ({PLAYER_PARRY_X},{PLAYER_ANIM_Y}).")

    # --- Create Damage/Defeat Animation Sprite (112,16) ---
    img_bank.rect(PLAYER_DAMAGE_X, PLAYER_ANIM_Y, SPRITE_WIDTH, SPRITE_HEIGHT, COLOR_TRANSPARENT)
    # Body recoiling, head tilted back, limbs splayed or contorted.
    # Head thrown back
    head_x = PLAYER_DAMAGE_X + 6
    head_y = PLAYER_ANIM_Y + 1
    img_bank.rect(head_x, head_y, 5, 1, COLOR_PLAYER_HAIR)  # Hair top
    img_bank.rect(head_x - 1, head_y + 1, 7, 3, COLOR_PLAYER_SKIN)  # Face exposed, tilted up
    img_bank.rect(head_x + 1, head_y + 2, 1, 1, COLOR_PLAYER_EYE)  # Eyes could be X or closed
    img_bank.pset(head_x + 1, head_y + 2, COLOR_RED)  # Simple X eye
    img_bank.pset(head_x, head_y + 3, COLOR_RED)
    img_bank.rect(head_x + 3, head_y + 2, 1, 1, COLOR_PLAYER_EYE)
    img_bank.pset(head_x + 3, head_y + 2, COLOR_RED)
    img_bank.pset(head_x + 2, head_y + 3, COLOR_RED)

    img_bank.rect(head_x - 1, head_y + 4, 7, 1, COLOR_PLAYER_HAIR)  # Hair back

    # Body arched back/crumpling
    img_bank.rect(
        PLAYER_DAMAGE_X + 3, PLAYER_ANIM_Y + 5, 10, 4, COLOR_PLAYER_UWAGI
    )  # Torso distorted
    img_bank.rect(PLAYER_DAMAGE_X + 4, PLAYER_ANIM_Y + 8, 8, 1, COLOR_PLAYER_BELT)  # Belt askew

    # Legs giving way
    img_bank.rect(PLAYER_DAMAGE_X + 4, PLAYER_ANIM_Y + 9, 3, 3, COLOR_PLAYER_HAKAMA)  # Left leg
    img_bank.pset(PLAYER_DAMAGE_X + 3, PLAYER_ANIM_Y + 12, COLOR_BLACK)  # Foot
    img_bank.rect(PLAYER_DAMAGE_X + 9, PLAYER_ANIM_Y + 9, 3, 4, COLOR_PLAYER_HAKAMA)  # Right leg
    img_bank.pset(PLAYER_DAMAGE_X + 10, PLAYER_ANIM_Y + 13, COLOR_BLACK)  # Foot

    # Arms flailing
    # Left arm
    img_bank.line(
        PLAYER_DAMAGE_X + 2,
        PLAYER_ANIM_Y + 5,
        PLAYER_DAMAGE_X + 0,
        PLAYER_ANIM_Y + 7,
        COLOR_PLAYER_UWAGI,
    )
    img_bank.pset(PLAYER_DAMAGE_X + 0, PLAYER_ANIM_Y + 8, COLOR_PLAYER_SKIN)
    # Right arm
    img_bank.line(
        PLAYER_DAMAGE_X + 13,
        PLAYER_ANIM_Y + 5,
        PLAYER_DAMAGE_X + 15,
        PLAYER_ANIM_Y + 7,
        COLOR_PLAYER_UWAGI,
    )
    img_bank.pset(PLAYER_DAMAGE_X + 15, PLAYER_ANIM_Y + 8, COLOR_PLAYER_SKIN)

    # Sword dropped or absent
    print(f"Created Damage/Defeat sprite at ({PLAYER_DAMAGE_X},{PLAYER_ANIM_Y}).")

    # --- Create Victory Animation Sprite (Optional - 128,16) ---
    img_bank.rect(PLAYER_VICTORY_X, PLAYER_ANIM_Y, SPRITE_WIDTH, SPRITE_HEIGHT, COLOR_TRANSPARENT)
    # Proud pose, sword raised or held firmly.
    # Standing tall, similar to idle but with more heroic pose.
    head_x = PLAYER_VICTORY_X + 5
    head_y = PLAYER_ANIM_Y + 1  # Head held high
    img_bank.rect(head_x, head_y, 6, 1, COLOR_PLAYER_HAIR)
    img_bank.rect(head_x - 1, head_y + 1, 8, 1, COLOR_PLAYER_HAIR)
    img_bank.pset(head_x + 2, head_y + 1, COLOR_PLAYER_SKIN)
    img_bank.pset(head_x + 3, head_y + 1, COLOR_PLAYER_SKIN)
    img_bank.rect(head_x, head_y + 2, 6, 2, COLOR_PLAYER_SKIN)  # Face
    img_bank.rect(head_x + 1, head_y + 2, 1, 1, COLOR_PLAYER_EYE)
    img_bank.rect(head_x + 4, head_y + 2, 1, 1, COLOR_PLAYER_EYE)
    img_bank.rect(head_x, head_y + 4, 6, 1, COLOR_PLAYER_HAIR)

    img_bank.rect(
        PLAYER_VICTORY_X + 2, PLAYER_ANIM_Y + 5, 12, 1, COLOR_PLAYER_UWAGI
    )  # Broad shoulders
    img_bank.rect(PLAYER_VICTORY_X + 3, PLAYER_ANIM_Y + 6, 10, 1, COLOR_PLAYER_UWAGI)
    img_bank.rect(PLAYER_VICTORY_X + 4, PLAYER_ANIM_Y + 7, 8, 3, COLOR_PLAYER_UWAGI)  # Chest out
    img_bank.rect(PLAYER_VICTORY_X + 4, PLAYER_ANIM_Y + 9, 8, 1, COLOR_PLAYER_BELT)
    img_bank.pset(PLAYER_VICTORY_X + 3, PLAYER_ANIM_Y + 9, COLOR_PLAYER_BELT)
    img_bank.pset(PLAYER_VICTORY_X + 12, PLAYER_ANIM_Y + 9, COLOR_PLAYER_BELT)

    img_bank.rect(PLAYER_VICTORY_X + 4, PLAYER_ANIM_Y + 10, 8, 2, COLOR_PLAYER_HAKAMA)  # Legs firm
    img_bank.rect(PLAYER_VICTORY_X + 3, PLAYER_ANIM_Y + 12, 4, 3, COLOR_PLAYER_HAKAMA)
    img_bank.pset(PLAYER_VICTORY_X + 2, PLAYER_ANIM_Y + 12, COLOR_PLAYER_HAKAMA)
    img_bank.pset(PLAYER_VICTORY_X + 3, PLAYER_ANIM_Y + 15, COLOR_BLACK)
    img_bank.pset(PLAYER_VICTORY_X + 4, PLAYER_ANIM_Y + 15, COLOR_BLACK)
    img_bank.rect(PLAYER_VICTORY_X + 9, PLAYER_ANIM_Y + 12, 4, 3, COLOR_PLAYER_HAKAMA)
    img_bank.pset(PLAYER_VICTORY_X + 11, PLAYER_ANIM_Y + 12, COLOR_PLAYER_HAKAMA)
    img_bank.pset(PLAYER_VICTORY_X + 10, PLAYER_ANIM_Y + 15, COLOR_BLACK)
    img_bank.pset(PLAYER_VICTORY_X + 11, PLAYER_ANIM_Y + 15, COLOR_BLACK)

    # Arms - One arm holding sword upwards, other arm on hip or determined pose.
    # Right arm holding sword up
    img_bank.rect(
        PLAYER_VICTORY_X + 10, PLAYER_ANIM_Y + 6, 3, 2, COLOR_PLAYER_UWAGI
    )  # Right shoulder
    img_bank.pset(PLAYER_VICTORY_X + 10, PLAYER_ANIM_Y + 5, COLOR_PLAYER_SKIN)  # Hand
    img_bank.pset(PLAYER_VICTORY_X + 11, PLAYER_ANIM_Y + 5, COLOR_PLAYER_SKIN)
    # Sword raised
    sword_hilt_victory_x = PLAYER_VICTORY_X + 10
    sword_hilt_victory_y = PLAYER_ANIM_Y + 4
    img_bank.pset(sword_hilt_victory_x, sword_hilt_victory_y, COLOR_PLAYER_SWORD_HILT)
    img_bank.pset(sword_hilt_victory_x - 1, sword_hilt_victory_y, COLOR_PLAYER_SWORD_GUARD)
    img_bank.pset(sword_hilt_victory_x + 1, sword_hilt_victory_y, COLOR_PLAYER_SWORD_GUARD)
    img_bank.line(
        sword_hilt_victory_x,
        sword_hilt_victory_y - 1,
        sword_hilt_victory_x,
        PLAYER_ANIM_Y + 0,
        COLOR_PLAYER_SWORD_BLADE,
    )
    img_bank.pset(sword_hilt_victory_x - 1, PLAYER_ANIM_Y + 0, COLOR_PLAYER_SWORD_BLADE)  # Tip
    img_bank.pset(sword_hilt_victory_x + 1, PLAYER_ANIM_Y + 0, COLOR_PLAYER_SWORD_BLADE)  # Tip

    # Left arm on hip
    img_bank.rect(PLAYER_VICTORY_X + 2, PLAYER_ANIM_Y + 6, 2, 2, COLOR_PLAYER_UWAGI)
    img_bank.pset(PLAYER_VICTORY_X + 3, PLAYER_ANIM_Y + 8, COLOR_PLAYER_SKIN)  # Hand on belt
    print(f"Created Victory sprite at ({PLAYER_VICTORY_X},{PLAYER_ANIM_Y}).")

    # Save the changes
    pyxel.save(RESOURCE_FILE)
    print(f"Saved changes to resource file: {RESOURCE_FILE}")


if __name__ == "__main__":
    main()
