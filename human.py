from game import Player

class HumanPlayer(Player):
    def choose_action(self, state):
        possible_actions = self.get_possible_actions(state)
        
        for i in range(len(possible_actions)):
            print(f"{i}: {possible_actions[i]}")
        
        user_choice = int(input("Please choose an action: "))
        return possible_actions[user_choice]