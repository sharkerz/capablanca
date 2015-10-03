# -*- coding: utf-8 -*-
# Copyright 2015, Dario Blanco

from capablanca.core import ChessPlayer


def test_draw_boards():
    """Should pretty print the board with the expected format"""
    cp = ChessPlayer(2, 2, {'R': 2})
    assert cp.pieces == ['R', 'R']

    cp.run()
    cp.elapsed_time = 0.000379

    expected_output = (
        '\nSolutions:\n\n'
        '* * * *\n'
        '* R - *\n'
        '* - R *\n'
        '* * * *\n\n'
        '* * * *\n'
        '* - R *\n'
        '* R - *\n'
        '* * * *\n\n'
        '2 solutions found in 0.000379 seconds\n'
    )
    assert cp.draw_boards() == expected_output


def test_chess_player_1x3_solutions():
    """Should give 1 solution when giving 2 Kings and 1x3"""
    cp = ChessPlayer(1, 3, {'K': 2, 'Q': 0, 'B': 0, 'R': 0, 'N': 0})
    assert cp.pieces == ['K', 'K']

    cp.run()

    expected_solutions = set([
        ('* * * * *\n'
         '* K - K *\n'
         '* * * * *\n')])
    assert cp.solutions == expected_solutions


def test_chess_player_3x3_solutions():
    """Should give four solutions when giving 2 Kings and 1 Rook for 3x3"""
    cp = ChessPlayer(3, 3, {'K': 2, 'Q': 0, 'B': 0, 'R': 1, 'N': 0})
    assert cp.pieces == ['R', 'K', 'K']

    cp.run()

    expected_solutions = set([
        ('* * * * *\n'
         '* K - - *\n'
         '* - - R *\n'
         '* K - - *\n'
         '* * * * *\n'),
        ('* * * * *\n'
         '* K - K *\n'
         '* - - - *\n'
         '* - R - *\n'
         '* * * * *\n'),
        ('* * * * *\n'
         '* - R - *\n'
         '* - - - *\n'
         '* K - K *\n'
         '* * * * *\n'),
        ('* * * * *\n'
         '* - - K *\n'
         '* R - - *\n'
         '* - - K *\n'
         '* * * * *\n')])
    assert cp.solutions == expected_solutions


def test_chess_player_4x4_solutions():
    """Should give eight solutions when giving 2 Rooks and 4 Knights for 4x4"""
    cp = ChessPlayer(4, 4, {'K': 0, 'Q': 0, 'B': 0, 'R': 2, 'N': 4})
    assert cp.pieces == ['R', 'R', 'N', 'N', 'N', 'N']

    cp.run()

    expected_solutions = set([
        ('* * * * * *\n'
         '* R - - - *\n'
         '* - N - N *\n'
         '* - - R - *\n'
         '* - N - N *\n'
         '* * * * * *\n'),
        ('* * * * * *\n'
         '* N - N - *\n'
         '* - R - - *\n'
         '* N - N - *\n'
         '* - - - R *\n'
         '* * * * * *\n'),
        ('* * * * * *\n'
         '* - - - R *\n'
         '* N - N - *\n'
         '* - R - - *\n'
         '* N - N - *\n'
         '* * * * * *\n'),
        ('* * * * * *\n'
         '* - R - - *\n'
         '* N - N - *\n'
         '* - - - R *\n'
         '* N - N - *\n'
         '* * * * * *\n'),
        ('* * * * * *\n'
         '* - N - N *\n'
         '* - - R - *\n'
         '* - N - N *\n'
         '* R - - - *\n'
         '* * * * * *\n'),
        ('* * * * * *\n'
         '* N - N - *\n'
         '* - - - R *\n'
         '* N - N - *\n'
         '* - R - - *\n'
         '* * * * * *\n'),
        ('* * * * * *\n'
         '* - N - N *\n'
         '* R - - - *\n'
         '* - N - N *\n'
         '* - - R - *\n'
         '* * * * * *\n'),
        ('* * * * * *\n'
         '* - - R - *\n'
         '* - N - N *\n'
         '* R - - - *\n'
         '* - N - N *\n'
         '* * * * * *\n')])
    assert cp.solutions == expected_solutions


def test_chess_player_4_queens():
    """Should solve the 4 queens problem with a 4x4 board"""
    cp = ChessPlayer(4, 4, {'K': 0, 'Q': 4, 'B': 0, 'R': 0, 'N': 0})
    assert cp.pieces == ['Q', 'Q', 'Q', 'Q']

    cp.run()

    expected_solutions = set([
        ('* * * * * *\n'
         '* - Q - - *\n'
         '* - - - Q *\n'
         '* Q - - - *\n'
         '* - - Q - *\n'
         '* * * * * *\n'),
        ('* * * * * *\n'
         '* - - Q - *\n'
         '* Q - - - *\n'
         '* - - - Q *\n'
         '* - Q - - *\n'
         '* * * * * *\n')])
    assert cp.solutions == expected_solutions


def test_chess_player_6_queens():
    """Should solve the 6 queens problem with a 6x6 board"""
    cp = ChessPlayer(6, 6, {'K': 0, 'Q': 6, 'B': 0, 'R': 0, 'N': 0})
    assert cp.pieces == ['Q', 'Q', 'Q', 'Q', 'Q', 'Q']

    cp.run()

    expected_solutions = set([
        ('* * * * * * * *\n'
         '* - Q - - - - *\n'
         '* - - - Q - - *\n'
         '* - - - - - Q *\n'
         '* Q - - - - - *\n'
         '* - - Q - - - *\n'
         '* - - - - Q - *\n'
         '* * * * * * * *\n'),
        ('* * * * * * * *\n'
         '* - - Q - - - *\n'
         '* - - - - - Q *\n'
         '* - Q - - - - *\n'
         '* - - - - Q - *\n'
         '* Q - - - - - *\n'
         '* - - - Q - - *\n'
         '* * * * * * * *\n'),
        ('* * * * * * * *\n'
         '* - - - Q - - *\n'
         '* Q - - - - - *\n'
         '* - - - - Q - *\n'
         '* - Q - - - - *\n'
         '* - - - - - Q *\n'
         '* - - Q - - - *\n'
         '* * * * * * * *\n'),
        ('* * * * * * * *\n'
         '* - - - - Q - *\n'
         '* - - Q - - - *\n'
         '* Q - - - - - *\n'
         '* - - - - - Q *\n'
         '* - - - Q - - *\n'
         '* - Q - - - - *\n'
         '* * * * * * * *\n')])
    assert cp.solutions == expected_solutions
