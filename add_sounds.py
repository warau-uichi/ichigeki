import pyxel
import os

RESOURCE_FILE = "assets/game.pyxres"
SCREEN_WIDTH_PIXELS = 32 * 8  # Consistent with previous scripts
SCREEN_HEIGHT_PIXELS = 24 * 8  # Consistent with previous scripts

# Sound properties
SOUND_ATTACK = 0
SOUND_UI_CONFIRM = 1
SOUND_PARRY_SUCCESS = 2
SOUND_PLAYER_DAMAGE = 3
SOUND_MOVEMENT_FOOTSTEP = 4
SOUND_UI_CANCEL = 5
SOUND_UI_CURSOR = 6
SOUND_SIMULTANEOUS_HIT = 7
SOUND_PENALTY_APPLIED = 8
SOUND_BGM_TITLE_MOTIF = 9
SOUND_BGM_GAMEPLAY_MOTIF = 10


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

    # Access Sound 0 for Attack Sound - Updated
    # Target: A "sword swing/swoosh". Noise or fast descending pitch slide. Short duration.
    sound_attack = pyxel.sounds[SOUND_ATTACK]
    sound_attack.set(
        notes="g2f#2e2d2",  # Fast descending pitch
        tones="nnnn",  # Noise for a swoosh, or ssss for square wave
        volumes="6543",  # Fade out
        effects="snnn",  # Slide effect for pitch change, then none
        speed=4,  # Fast speed for quick swoosh
    )
    # Alternative: notes="c4", tones="n", volumes="7", effects="f", speed=6 (short sharp noise)
    print(f"Updated properties for Sound {SOUND_ATTACK} (Attack Swoosh).")

    # Sound 1 for UI Confirm Sound (Existing - No change requested)
    sound_ui_confirm = pyxel.sounds[SOUND_UI_CONFIRM]
    sound_ui_confirm.set(
        notes="c4",
        tones="t",
        volumes="4",  # Keep volume consistent or adjust as per overall sound design
        effects="n",
        speed=8,
    )
    print(f"Set properties for Sound {SOUND_UI_CONFIRM} (UI Confirm).")

    # --- Add New Sound Effects ---

    # Sound 2: Parry Success Sound
    # Target: "Metallic 'clank' or 'clang'." Sharp and distinct.
    sound_parry = pyxel.sounds[SOUND_PARRY_SUCCESS]
    sound_parry.set(
        notes="b4g4",  # Changed c5 to b4 (valid high note) and a4 to g4 for interval
        tones="ts",  # Triangle then Square for metallic feel
        volumes="76",  # Loud and sharp
        effects="fn",  # Fast fade out on first note
        speed=5,  # Quick sound
    )
    print(f"Set properties for Sound {SOUND_PARRY_SUCCESS} (Parry Success).")

    # Sound 3: Player Damage Sound
    # Target: "Groan or dull thud." Lower-pitched, possibly noisy.
    sound_damage = pyxel.sounds[SOUND_PLAYER_DAMAGE]
    sound_damage.set(
        notes="a1g1",  # Low notes
        tones="pn",  # Pulse then Noise for a thud/groan
        volumes="76",  # Relatively loud
        effects="s",  # Slight slide down
        speed=10,  # Moderate speed
    )
    print(f"Set properties for Sound {SOUND_PLAYER_DAMAGE} (Player Damage).")

    # Sound 4: Movement (Footstep) Sound
    # Target: "Footstep sound (simple click or soft noise)." Short, subtle.
    sound_footstep = pyxel.sounds[SOUND_MOVEMENT_FOOTSTEP]
    sound_footstep.set(
        notes="c2",  # Low pitch
        tones="n",  # Noise for a soft click/thump
        volumes="2",  # Low volume
        effects="f",  # Fast fade out
        speed=6,  # Very short
    )
    print(f"Set properties for Sound {SOUND_MOVEMENT_FOOTSTEP} (Movement Footstep).")

    # Sound 5: UI Cancel Sound
    # Target: Distinct from UI Confirm. Lower pitch or different tone.
    sound_ui_cancel = pyxel.sounds[SOUND_UI_CANCEL]
    sound_ui_cancel.set(
        notes="g3e3",  # Lower than confirm (c4)
        tones="ss",  # Square wave
        volumes="43",  # Moderate volume
        effects="n",
        speed=8,
    )
    print(f"Set properties for Sound {SOUND_UI_CANCEL} (UI Cancel).")

    # Sound 6: UI Cursor Movement Sound
    # Target: "A very short, light click or blip."
    sound_ui_cursor = pyxel.sounds[SOUND_UI_CURSOR]
    sound_ui_cursor.set(
        notes="b4",  # Changed c5 to b4 (valid high note)
        tones="t",  # Triangle wave for a clean sound
        volumes="2",  # Low volume
        effects="f",  # Fast fade out
        speed=3,  # Extremely short, adjusted speed for b4
    )
    print(f"Set properties for Sound {SOUND_UI_CURSOR} (UI Cursor).")

    # Sound 7: Simultaneous Hit (Sou-uchi) Sound
    # Target: "A distinct, heavier impact sound" than normal attack hit.
    sound_sou_uchi = pyxel.sounds[SOUND_SIMULTANEOUS_HIT]
    sound_sou_uchi.set(
        notes="e2c#2a1",  # Low, somewhat dissonant chord
        tones="ptn",  # Pulse, Triangle, Noise for complex, heavy impact
        volumes="765",  # Loud
        effects="n",  # No effect, let notes ring a bit
        speed=10,  # Moderate duration for impact
    )
    print(f"Set properties for Sound {SOUND_SIMULTANEOUS_HIT} (Simultaneous Hit).")

    # --- Add Optional Sound Effects (from new subtask) ---

    # Sound 8: Attack Failure Penalty Sound
    # Target: Short, distinct, somewhat negative/alerting.
    sound_penalty = pyxel.sounds[SOUND_PENALTY_APPLIED]
    sound_penalty.set(
        notes="e2c2",  # Descending, slightly jarring
        tones="sp",  # Square then Pulse
        volumes="65",  # Moderate volume, slight decay
        effects="f",  # Fadeout
        speed=15,  # Relatively quick
    )
    print(f"Set properties for Sound {SOUND_PENALTY_APPLIED} (Attack Failure Penalty).")

    # Sound 9: Placeholder Title BGM Motif
    # Target: Short, anticipatory, loopable sequence.
    sound_bgm_title = pyxel.sounds[SOUND_BGM_TITLE_MOTIF]
    sound_bgm_title.set(
        notes="c3e3g3c4 g3e3c3",  # Simple C-major arpeggio up and down
        tones="tttt ttt",  # Triangle wave for a clear, melodic sound
        volumes="4445 444",  # Consistent volume, slight emphasis on top note
        effects="nnnn nnn",  # No effects
        speed=12,  # Moderate speed for a motif
    )
    print(f"Set properties for Sound {SOUND_BGM_TITLE_MOTIF} (Title BGM Motif).")

    # Sound 10: Placeholder Gameplay BGM Motif
    # Target: Short, tense or neutral, loopable sequence.
    sound_bgm_gameplay = pyxel.sounds[SOUND_BGM_GAMEPLAY_MOTIF]
    sound_bgm_gameplay.set(
        notes="a2d3f3e3 d3a2",  # Sequence with a slightly tense/minor feel
        tones="psps ps",  # Pulse and Square for a bit of texture
        volumes="4444 44",  # Consistent volume
        effects="nnnn nn",  # No effects
        speed=14,  # Slightly slower pace for gameplay background
    )
    print(f"Set properties for Sound {SOUND_BGM_GAMEPLAY_MOTIF} (Gameplay BGM Motif).")

    # Single save call at the end of all sound definitions
    pyxel.save(RESOURCE_FILE)
    print(f"Saved all sound changes to resource file: {RESOURCE_FILE}")


if __name__ == "__main__":
    main()
