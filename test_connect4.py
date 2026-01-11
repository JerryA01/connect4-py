import unittest
from Connect4 import create_board, drop_counter, remove_row, remove_counter, check_win, apply_gravity

class TestConnect4(unittest.TestCase):
      
    
    def test_create_board(self):
        board = create_board()
        self.assertEqual(len(board), 6)
        self.assertEqual(len(board[0]), 7)
        self.assertTrue(all(cell == " " for row in board for cell in row))


    def test_drop_counter(self):
        board = create_board()
        success = drop_counter(board, 3, "X")
        self.assertTrue(success)
        self.assertEqual(board[5][3], "X")

    def test_drop_counter_full_column(self):
        board = create_board()
        for _ in range(6):
            drop_counter(board, 0, "X")
        self.assertFalse(drop_counter(board, 0, "O"))


    def test_horizontal_win(self):
        board = create_board()
        for col in range(4):
            drop_counter(board, col, "X")
        self.assertTrue(check_win(board))


    def test_vertical_win(self):
        board = create_board()
        for _ in range(4):
            drop_counter(board, 2, "O")
        self.assertTrue(check_win(board))

    def test_remove_row(self):
        board = create_board()
        drop_counter(board, 0, "X")
        drop_counter(board, 1, "O")

        success = remove_row(board, 5)
        self.assertTrue(success)
        self.assertTrue(all(cell == " " for cell in board[0]))


    def test_remove_counter(self):
        board = create_board()
        drop_counter(board, 0, "X")
        drop_counter(board, 0, "O")

        success = remove_counter(board, 5, 0)
        self.assertTrue(success)
        self.assertEqual(board[5][0], "X")


    def test_remove_empty_counter_fails(self):
        board = create_board()
        self.assertFalse(remove_counter(board, 0, 0))











