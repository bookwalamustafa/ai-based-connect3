from connect3 import State
import util
from game import Game
from human import HumanPlayer
from agent import RandomPlayer, MinimaxPlayer

def get_player(player_type, char):
    if player_type == 'human':
        return HumanPlayer(char)
    elif player_type == 'random':
        return RandomPlayer(char)
    elif player_type == 'minimax':
        return MinimaxPlayer(char)
    
def main():
    # repetition = 500
    # first_player_counter = 0
    # second_player_counter = 0
    # draw_counter = 0
    # play = ['python3', 'main.py', 'random', 'minimax']
    
    player1 = util.get_arg(1)
    player2 = util.get_arg(2)

    # for i in range(repetition):
        
        # player1 = play[2]
        # player2 = play[3]
    player1 = get_player(player1, 'X')
    player2 = get_player(player2, 'O')

    initial_state = State()
    game = Game(initial_state=initial_state, player1=player1, player2=player2)
    winner, visited_states = game.play()
    
    if winner == 'X':
        # first_player_counter += 1
        print(f"{winner} wins")
    elif winner == 'O':
        # second_player_counter += 1
        print(f"{winner} wins")
    else:
        # draw_counter += 1
        print("Draw")

    util.pprint(visited_states)
    
    # print(f"% games {play[2]} won playing first: {(first_player_counter/repetition)*100}")
    # print(f"% games {play[3]} won playing second: {(second_player_counter/repetition)*100}")
    # print(f"% games there was a draw: {(draw_counter/repetition)*100}")

if __name__ == "__main__":
    main()
