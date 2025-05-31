import unittest
import sys
import os

# Add src directory to Python path to import main
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

# Mock pyxel before importing main
class MockPyxel:
    def __init__(self):
        self.KEY_A = 10 # Assign arbitrary unique values for keys
        self.KEY_D = 11
        self.width = 256
        self.height = 192
        self._btn_states = {}

    def init(self, width, height, title, fps):
        self.width = width
        self.height = height
        # print(f"Pyxel init: {width}x{height}, title='{title}', fps={fps}")

    def load(self, filename):
        # print(f"Pyxel load: {filename}")
        pass

    def cls(self, color):
        pass

    def rect(self, x, y, w, h, color):
        pass

    def btn(self, key):
        return self._btn_states.get(key, False)

    def run(self, update_func, draw_func):
        # print("pyxel.run called")
        pass

# Replace pyxel with the mock before importing main
sys.modules['pyxel'] = MockPyxel()

import main

class TestGame(unittest.TestCase):

    def setUp(self):
        # Reset player state and pyxel mock before each test
        main.pyxel = MockPyxel() # Re-initialize mock to reset width/height
        # These assignments assume main.py defines these as global variables
        # accessible for modification and that their values are set before setup is called.
        # The player_x, player_y should be reset based on how main.py initializes them.
        main.player_x = main.pyxel.width / 2 - main.player_width / 2
        main.player_y = main.pyxel.height / 2 - main.player_height / 2
        main.pyxel._btn_states = {}

    def test_player_initial_position(self):
        expected_x = main.pyxel.width / 2 - main.player_width / 2
        expected_y = main.pyxel.height / 2 - main.player_height / 2
        self.assertEqual(main.player_x, expected_x)
        self.assertEqual(main.player_y, expected_y)

    def test_player_move_left(self):
        initial_x = main.player_x
        main.pyxel._btn_states[main.pyxel.KEY_A] = True
        main.update() # Call the global update function from main
        self.assertEqual(main.player_x, initial_x - main.player_speed)

    def test_player_move_right(self):
        initial_x = main.player_x
        main.pyxel._btn_states[main.pyxel.KEY_D] = True
        main.update()
        self.assertEqual(main.player_x, initial_x + main.player_speed)

    def test_player_boundary_left_stop(self):
        main.player_x = 0 # Start at the boundary
        main.pyxel._btn_states[main.pyxel.KEY_A] = True
        main.update()
        self.assertEqual(main.player_x, 0)

    def test_player_boundary_right_stop(self):
        main.player_x = main.pyxel.width - main.player_width # Start at the boundary
        main.pyxel._btn_states[main.pyxel.KEY_D] = True
        main.update()
        self.assertEqual(main.player_x, main.pyxel.width - main.player_width)

    def test_player_boundary_left_from_positive(self):
        main.player_x = main.player_speed / 2
        main.pyxel._btn_states[main.pyxel.KEY_A] = True
        main.update()
        self.assertEqual(main.player_x, 0)

    def test_player_boundary_right_from_close(self):
        main.player_x = main.pyxel.width - main.player_width - (main.player_speed / 2)
        main.pyxel._btn_states[main.pyxel.KEY_D] = True
        main.update()
        self.assertEqual(main.player_x, main.pyxel.width - main.player_width)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
