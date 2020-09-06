from unittest import TestCase

import numpy as np
from numpy.testing import assert_array_equal, assert_raises

from gol.board import Board
from gol import patterns


class CommonPatternTests(TestCase):
    # Still life pattern tests
    def test_block_stays_the_same(self):
        board = patterns.block()
        self.assertStillLife(board)

    def test_beehive_stays_the_same(self):
        board = patterns.beehive()
        self.assertStillLife(board)

    def test_loaf_stays_the_same(self):
        board = patterns.loaf()
        self.assertStillLife(board)

    def test_boat_stays_the_same(self):
        board = patterns.boat()
        self.assertStillLife(board)

    def test_tub_stays_the_same(self):
        board = patterns.tub()
        self.assertStillLife(board)

    # Oscillator patterns tests
    def test_blinker_oscillates(self):
        board = patterns.blinker()
        self.assertOscillator(board, 2)

    def test_toad_oscillates(self):
        board = patterns.toad()
        self.assertOscillator(board, 2)

    def test_beacon_oscillates(self):
        board = patterns.beacon()
        self.assertOscillator(board, 2)

    def test_pulsar_oscillates(self):
        board = patterns.pulsar()
        self.assertOscillator(board, 3)

    def test_pentadecathlon_oscillates(self):
        board = patterns.pentadecathlon()
        self.assertOscillator(board, 15)

    # Spaceship patterns tests
    def test_glider_moves(self):
        board = patterns.glider()
        self.assertSpaceship(board, 4, 1, 1)

    def test_glider_wraps_around(self):
        board = patterns.glider()
        self.assertOscillator(board, 20)

    def test_lwss_moves(self):
        board = patterns.lightweight_spaceship()
        self.assertSpaceship(board, 4, 0, 2)

    # Assert methods
    def assertStillLife(self, board):
        self.assertOscillator(board, 0)

    def assertOscillator(self, board, period):
        initial = board.copy()
        for i in range(period):
            board.update()
            with self.subTest(i=i):
                if i >= period - 1:
                    assert_array_equal(board, initial)
                else:
                    assert_raises(AssertionError, assert_array_equal, board, initial)

    def assertSpaceship(self, board, iterations, row_displacement, column_displacement):
        initial = board.copy()
        for i in range(iterations):
            board.update()
            with self.subTest(i=i):
                if i >= iterations - 1:
                    expected = np.roll(initial, (row_displacement, column_displacement), (0, 1))
                    assert_array_equal(board, expected)
                else:
                    assert_raises(AssertionError, assert_array_equal, board, initial)


