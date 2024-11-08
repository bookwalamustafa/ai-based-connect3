from connect3 import State
import util

class Player:
    def __init__(self, char):
        self.char = char

    def choose_action(state):
        pass
    
    def get_possible_actions(self, state, char=None):
        if char:
            return state.get_actions(char)
        else:
            return state.get_actions(self.char)

class Game:
    def __init__(self, initial_state, player1, player2):
        if initial_state!=None:
            self.state = initial_state
        else:
            self.state = State()
            
        self.players = [player1, player2]
        self.current_player = 0  
        self.visited_states = []

    def play(self):
        while not self.state.is_game_over():
            self.visited_states.append(self.state._clone())
            current_player = self.players[self.current_player]
            action = current_player.choose_action(self.state)
            self.state = self.state.execute(action)
            util.pprint(self.state)
            self.current_player = 1 - self.current_player
            
        self.visited_states.append(self.state._clone())
        return self.state.get_winner(), self.visited_states