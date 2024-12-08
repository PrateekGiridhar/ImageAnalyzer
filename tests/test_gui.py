import unittest
from ImageAnalyzer.gui.gui_main import run_gui

class TestGUI(unittest.TestCase):

    def test_gui_launch(self):
        # This is a placeholder test to ensure GUI launches without errors.
        # GUI tests are typically more complex and may require tools like PyAutoGUI or Tkinter testing libraries.
        try:
            run_gui()
            success = True
        except Exception as e:
            success = False
            print(f"GUI launch failed: {e}")

        self.assertTrue(success)

if __name__ == "__main__":
    unittest.main()