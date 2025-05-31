import os
import sys
import unittest

# Add src directory to Python path to import main
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))


# Mock pyxel before importing main
class MockPyxel:
    def __init__(self):
        self.KEY_A = 10  # Assign arbitrary unique values for keys
        self.KEY_D = 11
        self.KEY_LEFT = 12
        self.KEY_RIGHT = 13
        self.KEY_F = 14
        self.width = 256
        self.height = 192
        self._btn_states = {}
        self._btnp_states = {} # For btnp, can be more sophisticated if needed

    def init(self, width, height, title=None, fps=None):
        self.width = width
        self.height = height
        # title and fps are ignored in the mock implementation

    def load(self, filename):
        pass

    def cls(self, color):
        pass

    def rect(self, x, y, w, h, color):
        pass

    def bltm(self, x, y, tm, u, v, w, h, colkey=None): # Added colkey
        pass

    def blt(self, x, y, img, u, v, w, h, colkey=None): # Added colkey
        pass

    def btn(self, key):
        return self._btn_states.get(key, False)

    def btnp(self, key, hold=None, period=None): # Added hold and period params
        # Simple mock: behaves like btn for testing, or can be made more complex
        return self._btnp_states.get(key, False)

    def play(self, ch, snd, loop=False): # Added loop param
        pass

    def run(self, update_func, draw_func):
        pass


# Replace pyxel with the mock before importing main
sys.modules["pyxel"] = MockPyxel()

import main


class TestGame(unittest.TestCase):
    def setUp(self):
        # Reset player state and pyxel mock before each test
        main.pyxel = MockPyxel()  # Re-initialize mock to reset width/height
        # These assignments assume main.py defines these as global variables
        # accessible for modification and that their values are set before setup is called.
        # The player_x, player_y should be reset based on how main.py initializes them.
        main.player_x = main.pyxel.width / 2 - main.player_width / 2
        main.player_y = main.pyxel.height / 2 - main.player_height / 2
        main.pyxel._btn_states = {}

    def test_player_initial_position(self):
        expected_x = main.pyxel.width / 2 - main.player_width / 2
        expected_y = main.pyxel.height / 2 - main.player_height / 2
        assert main.player_x == expected_x
        assert main.player_y == expected_y

    def test_player_move_left(self):
        initial_x = main.player_x
        main.pyxel._btn_states[main.pyxel.KEY_A] = True
        main.update()  # Call the global update function from main
        assert main.player_x == initial_x - main.player_speed

    def test_player_move_right(self):
        initial_x = main.player_x
        main.pyxel._btn_states[main.pyxel.KEY_D] = True
        main.update()
        assert main.player_x == initial_x + main.player_speed

    def test_player_boundary_left_stop(self):
        main.player_x = 0  # Start at the boundary
        main.pyxel._btn_states[main.pyxel.KEY_A] = True
        main.update()
        assert main.player_x == 0

    def test_player_boundary_right_stop(self):
        main.player_x = main.pyxel.width - main.player_width  # Start at the boundary
        main.pyxel._btn_states[main.pyxel.KEY_D] = True
        main.update()
        assert main.player_x == main.pyxel.width - main.player_width

    def test_player_boundary_left_from_positive(self):
        # What we want to do is have the player close to the left edge,
        # then press left, and expect the player to stop at the boundary (0)
        main.player_x = main.player_speed / 2  # Setting to 1.0 (half of player_speed)

        # Press the left key
        main.pyxel._btn_states[main.pyxel.KEY_A] = True

        # Call update
        main.update()

        # This should be 0 because moving left from 1.0 by 2.0 would go below 0,
        # so it should clamp to 0
        assert main.player_x == 0

    def test_player_boundary_right_from_close(self):
        main.player_x = main.pyxel.width - main.player_width - (main.player_speed / 2)
        main.pyxel._btn_states[main.pyxel.KEY_D] = True
        main.update()
        assert main.player_x == main.pyxel.width - main.player_width


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
