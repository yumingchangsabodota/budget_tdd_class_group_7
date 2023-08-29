
from typing import Union


from tennis_player import Player

class TennisGame:
    def __init__(self, player1: Player, player2:Player):
        self.player1 = player1
        self.player2 = player2
        self.score_map = {
            0: 'love',
            1: 'fifteen',
            2: 'thirty',
            3: 'forty'
        }
        self.deuce = 'deuce'
        self.win = 'win'
        self.adv = 'adv'
        self.winner = None

    def score_player_one(self):
        if self.winner == None:
            self.player1.score += 1

    def score_player_two(self):
        if self.winner == None:
            self.player2.score += 1
        
    @property
    def game_state(self) -> str:
        if self.player1.score + self.player2.score < 6:
            if self.player1.score == self.player2.score:
                return f"{self.score_map[self.player1.score]} all"
            else:
                winner = self.__check_winner()
                if winner != None:
                    self.winner = winner
                    return f"{winner.name} {self.win}"
                return f"{self.score_map[self.player1.score]} {self.score_map[self.player2.score]}"
        else:
            winner = self.__check_deuce_winner()
            if winner != None:
                self.winner = winner
                return f"{winner.name} {self.win}"
            adv = self.__check_adv()
            if adv != None:
                return f"{adv.name} {self.adv}"
            if self.player1.score == self.player2.score:
                return self.deuce

    def __check_winner(self) -> Union[None, Player]:
        winner = None
        if self.player1.score > 3:
            winner = self.player1
        elif self.player2.score > 3:
            winner = self.player2
        return winner
            
    def __check_deuce_winner(self) -> Union[None, Player]:
        winner = None
        if self.player1.score - self.player2.score >= 2:
            winner = self.player1
        elif self.player2.score - self.player1.score >= 2:
            winner = self.player2
        return winner
    
    def __check_adv(self) -> Union[None, Player]:
        adv = None
        if self.player1.score - self.player2.score == 1:
            adv = self.player1
        elif self.player2.score - self.player1.score == 1:
            adv = self.player2
        return adv
    
                
    def reset(self):
        self.player1.score = 0
        self.player2.score = 0
        self.winner = None
            

if __name__ == "__main__":
    p1 = Player('Joey')
    p2 = Player('Tom')
    game = TennisGame(p1,p2)
    print("game1 start")
    print(f"{p1.name} {p2.name}")
    print(f"{game.player1.score} {game.player2.score} {game.game_state}")
    game.score_player_one()
    print(f"{game.player1.score} {game.player2.score} {game.game_state}")
    game.score_player_one()
    print(f"{game.player1.score} {game.player2.score} {game.game_state}")
    game.score_player_two()
    print(f"{game.player1.score} {game.player2.score} {game.game_state}")
    game.score_player_one()
    print(f"{game.player1.score} {game.player2.score} {game.game_state}")
    game.score_player_two()
    print(f"{game.player1.score} {game.player2.score} {game.game_state}")
    game.score_player_two()
    print(f"{game.player1.score} {game.player2.score} {game.game_state}")
    game.score_player_two()
    print(f"{game.player1.score} {game.player2.score} {game.game_state}")
    game.score_player_one()
    print(f"{game.player1.score} {game.player2.score} {game.game_state}")
    game.score_player_two()
    print(f"{game.player1.score} {game.player2.score} {game.game_state}")
    game.score_player_one()
    print(f"{game.player1.score} {game.player2.score} {game.game_state}")
    game.score_player_two()
    print(f"{game.player1.score} {game.player2.score} {game.game_state}")
    game.score_player_one()
    print(f"{game.player1.score} {game.player2.score} {game.game_state}")
    game.score_player_one()
    print(f"{game.player1.score} {game.player2.score} {game.game_state}")
    game.score_player_one()
    print(f"{game.player1.score} {game.player2.score} {game.game_state}")
    game.score_player_one()
    print(f"{game.player1.score} {game.player2.score} {game.game_state}")
    game.score_player_one()
    print(f"{game.player1.score} {game.player2.score} {game.game_state}")
    game.reset()
    print("game2 start")
    print(f"{p1.name} {p2.name}")
    print(f"{game.player1.score} {game.player2.score} {game.game_state}")
    game.score_player_two()
    print(f"{game.player1.score} {game.player2.score} {game.game_state}")
    game.score_player_two()
    print(f"{game.player1.score} {game.player2.score} {game.game_state}")
    game.score_player_two()
    print(f"{game.player1.score} {game.player2.score} {game.game_state}")
    game.score_player_one()
    print(f"{game.player1.score} {game.player2.score} {game.game_state}")
    game.score_player_one()
    print(f"{game.player1.score} {game.player2.score} {game.game_state}")
    game.score_player_two()
    print(f"{game.player1.score} {game.player2.score} {game.game_state}")
    game.score_player_two()
    print(f"{game.player1.score} {game.player2.score} {game.game_state}")
    game.score_player_one()
    print(f"{game.player1.score} {game.player2.score} {game.game_state}")