import unittest
from tictactoe import check_win, empty_cells, gameover, minimax

class TestTicTacToe(unittest.TestCase):

    def test_check_win(self):
        self.assertTrue(check_win(+1, [[+1, +1, +1], [0, 0, 0], [0, 0, 0]]))
        self.assertTrue(check_win(-1, [[-1, -1, -1], [0, 0, 0], [0, 0, 0]]))
        self.assertFalse(check_win(+1, [[+1, 0, +1], [0, 0, 0], [0, 0, 0]]))
        self.assertFalse(check_win(-1, [[0, 0, 0], [0, 0, 0], [0, 0, 0]]))

    def test_empty_cells(self):
        self.assertEqual(empty_cells([[0, 0, 0], [0, 0, 0], [0, 0, 0]]), [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]])
        self.assertEqual(empty_cells([[+1, 0, 0], [0, -1, 0], [0, 0, 0]]), [[0, 1], [0, 2], [1, 0], [1, 2], [2, 0], [2, 1], [2, 2]])
        self.assertEqual(empty_cells([[+1, +1, +1], [+1, +1, +1], [+1, +1, +1]]), [])

    def test_gameover(self):
        self.assertTrue(gameover(0, [[+1, +1, +1], [0, 0, 0], [0, 0, 0]]))
        self.assertTrue(gameover(0, [[-1, -1, -1], [0, 0, 0], [0, 0, 0]]))
        self.assertTrue(gameover(0, [[0, 0, 0], [0, 0, 0], [0, 0, 0]]))
        self.assertFalse(gameover(1, [[0, 0, 0], [0, 0, 0], [0, 0, 0]]))

    def test_minimax(self):
        self.assertEqual(minimax([[0, 0, 0], [0, 0, 0], [0, 0, 0]], +1, 1), [0, 0, 0])
        self.assertEqual(minimax([[+1, +1, 0], [0, 0, 0], [0, 0, 0]], +1, 1), [0, 2, 1])
        self.assertEqual(minimax([[+1, +1, 0], [0, 0, 0], [0, 0, 0]], -1, 1), [0, 2, 0])


if __name__ == '__main__':
    unittest.main()     