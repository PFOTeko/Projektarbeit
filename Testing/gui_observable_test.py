import unittest
from Game.gui import Gui


class MyTestCase(unittest.TestCase):
    def test_gui_observable(self):
        self.assertEqual(True, False)  # add assertion here



if __name__ == '__main__':
    unittest.main()


#controller objekt erstellen, callback-funktion hinzufügen
#mit dem controller objekt, notify funktion aufrufen