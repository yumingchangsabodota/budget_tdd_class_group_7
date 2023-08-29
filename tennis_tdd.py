
from tennis_player import Player

class TennisGameTdd:
    def __init__(self, player1: Player, player2:Player):
        self.player1 = player1
        self.player2 = player2
        self.winner = None
        self.score_map = {
            0: 'love',
            1: 'fifteen',
            2: 'thirty',
            3: 'forty'
        }
        self.deuce = 'deuce'

    def score_player_one(self):
        self.player1.score += 1

    def score_player_two(self):
        self.player2.score += 1

    @property
    def game_state(self):
        if self.__is_all():
            if self.__is_deuce():
                return self.__state_deuce()
            return self.__state_all()
        return self.__state_regular()
        
    def __state_deuce(self):
        return self.deuce

    def __state_regular(self):
        return f"{self.score_map[self.player1.score]} {self.score_map[self.player2.score]}"
        
    def __state_all(self) -> str:
        return f"{self.score_map[self.player1.score]} all"

    def __is_all(self):
        if self.player1.score == self.player2.score:
            return True
        return False
    
    def __is_deuce(self):
        if self.player1.score >= 3:
                return True
        return False
    
    def reset(self):
        self.winner = None
        self.player1.score = 0
        self.player2.score = 0