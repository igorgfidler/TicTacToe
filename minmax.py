import sys
from random import randint, seed

class MinMax():

    def __init__(self, game, players):
        self.game = game
        self.players = players
        seed()


    def apply_action(self, state, action, player):
        state.board[action] = player
        return state


    def undo_action(self, state, action):
        state.board[action] = str(action+1)
        return state


    def get_moves(self, state):
        return state.get_moves()


    def get_decision(self, state, player):
        actions = self.get_moves(state)

        best_i = None
        best_val = -sys.maxsize

        best_values = []

        for i, action in enumerate(actions):
            val = self.minmax(self.apply_action(state, action, player[0]),
                              0, player, False)
            state.board[action] = str(action+1)

            if val > best_val:
                best_i = i
                best_val = val
                best_values = []
            if val == best_val:
                best_values.append(best_i)

        return actions[best_values[randint(0, len(best_values)-1)]]
    
    
    def minmax(self, state, depth, player, is_max):

        result = state.result()
        if result == player[0]:
            return 10 - depth
        elif result == player[1]:
            return -10 + depth
        elif result is not None:
            return 0

        actions = self.get_moves(state)

        if is_max:
            best = -sys.maxsize

            for action in actions:
                val = self.minmax(self.apply_action(state, action, player[0]),
                                   depth + 1, player, False)
                self.undo_action(state, action)
                best = max(best, val)
        else:
            best = sys.maxsize

            for action in actions:
                val = self.minmax(self.apply_action(state, action, player[1]),
                                   depth + 1, player, True)
                self.undo_action(state, action)
                best = min(best, val)


        return best
