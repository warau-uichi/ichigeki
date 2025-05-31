import pyxel
import os

RESOURCE_FILE = "assets/game.pyxres"
SCREEN_WIDTH_PIXELS = 32 * 8  # Consistent with previous scripts
SCREEN_HEIGHT_PIXELS = 24 * 8 # Consistent with previous scripts

# Sound properties
SOUND_ATTACK = 0
SOUND_UI_CONFIRM = 1

def main():
    if not os.path.exists(RESOURCE_FILE):
        print(f"Error: Resource file {RESOURCE_FILE} not found.")
        print("Please run previous scripts first.")
        return

    # Initialize Pyxel.
    pyxel.init(SCREEN_WIDTH_PIXELS, SCREEN_HEIGHT_PIXELS, title="Sound Adder")
    print("Initialized Pyxel.")

    # Load the existing resource file
    pyxel.load(RESOURCE_FILE)
    print(f"Loaded resource file: {RESOURCE_FILE}")

    # Access Sound 0 for Attack Sound
    sound0 = pyxel.sounds[SOUND_ATTACK]
    sound0.set(
        notes="c3",      # A single short note
        tones="n",       # n for noise
        volumes="4",     # Mid volume (0-7)
        effects="n",     # n for none
        speed=10         # Duration of each note/effect step
    )
    print(f"Set properties for Sound {SOUND_ATTACK} (Attack Placeholder).")

    # Access Sound 1 for UI Confirm Sound
    sound1 = pyxel.sounds[SOUND_UI_CONFIRM]
    sound1.set(
        notes="c4",      # Higher pitch
        tones="t",       # t for triangle wave
        volumes="3",     # Slightly softer
        effects="n",     # n for none
        speed=8          # Slightly faster/shorter
    )
    print(f"Set properties for Sound {SOUND_UI_CONFIRM} (UI Confirm Placeholder).")

    # Save the changes
    # Note: pyxel.save() saves all currently loaded resources, including sounds.
    pyxel.save(RESOURCE_FILE)
    print(f"Saved changes to resource file: {RESOURCE_FILE}")

if __name__ == "__main__":
    main()
