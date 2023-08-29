import unittest

from typing import Union
from tennis_player import Player
from tennis import TennisGame
from tennis_tdd import TennisGameTdd

class TennisTestCase(unittest.TestCase):
    def given_game_start(self):
        return TennisGameTdd(Player('Joey'),Player('Tom'))

    def given_score_p2(self, game:Union[TennisGame,TennisGameTdd], 
                       score:int):
        for i in range(0,score):
            game.score_player_two()

    def given_score_p1(self, game:Union[TennisGame,TennisGameTdd], 
                       score:int):
        for i in range(0,score):
            game.score_player_one()

    def given_deuce(self, game:Union[TennisGame,TennisGameTdd]):
        self.given_score_p1(game, 3)
        self.given_score_p2(game, 3)

    def given_game_point(self, game:Union[TennisGame,TennisGameTdd]):
        pass


    def test_game_start(self):
        game = self.given_game_start()
        self.assertEqual(game.game_state,'love all')
        self.assertEqual(game.winner, None)

    
    def test_p1_score(self):
        game = self.given_game_start()
        game.score_player_one()
        self.assertEqual(game.game_state,'fifteen love')

    
    def test_p2_score(self):
        game = self.given_game_start()
        game.score_player_two()
        self.assertEqual(game.game_state,'love fifteen')

    
    def test_reset(self):
        game = self.given_game_start()
        game.reset()
        self.assertEqual(game.game_state,'love all')
        self.assertEqual(game.winner, None)

    
    def test_deuce(self):
        game = self.given_game_start()
        game.reset()
        self.given_deuce(game)
        self.assertEqual(game.player1.score, 3)
        self.assertEqual(game.player2.score, 3)
        self.assertEqual(game.game_state,'deuce')

    """
    def test_game_point_deuce(self):
        game = self.given_game_start()
    """


if __name__ == '__main__':
    unittest.main()