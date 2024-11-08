import random
from game import Player

class RandomPlayer(Player):
    def choose_action(self, state):
        possible_actions = self.get_possible_actions(state)
        if possible_actions:
            return random.choice(possible_actions)
        else:
            return None
    
class MinimaxPlayer(Player):
    def choose_action(self, state):
        optimal_action = None
        optimal_value = float('-inf')
        
        for action in self.get_possible_actions(state):
            value = self.min_value(state.execute(action))
            if value > optimal_value:
                optimal_value = value
                optimal_action = action
        
        return optimal_action

    def max_value(self, state):
        if state.is_game_over():
            return self.utility(state)
        
        v = float('-inf')
        for a in self.get_possible_actions(state):
            v = max(v, self.min_value(state.execute(a)))
        
        return v

    def min_value(self, state):
        if state.is_game_over():
            return self.utility(state)

        v = float('inf')
        for a in self.get_possible_actions(state, self.opponent_char()):
            v = min(v, self.max_value(state.execute(a)))
            
        return v

    def utility(self, state):
        winner = state.get_winner()
        if winner == self.char:
            return 100
        elif winner == self.opponent_char():
            return -100
        else:
            return 0

    def opponent_char(self):
        if self.char == 'X':
            return 'O'
        else:
            return 'X'
