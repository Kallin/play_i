from play_i.player.player import Player


class MinMaxPlayer(Player):
    def make_choice(self, options, game):
        choice_scores = self.choice_scores(options, game)

        best_index = choice_scores.index(max(choice_scores))

        return options[best_index]

    def choice_scores(self, options, game):
        option_scores = []

        for i, option in enumerate(options):
            copy = self.prepare_copy(game, option)

            if copy.game_over():
                self.score_end_of_game(copy, option_scores)

            else:
                self.score_sub_states(copy, option_scores)

        # this code is smelly
        # if we just returned one move, along with it's score, that might be simpler
        # todo: if we can win right now, we should make that move

        return option_scores

    def score_sub_states(self, copy, option_scores):
        # not at a terminal state, need to branch out to all sub-moves
        copy.swap_players()
        scores = self.choice_scores(copy.options(), copy)
        if copy.active_player().number == self.number:
            # the next turn is ours, so we would choose the best
            option_scores.append(max(scores))
        else:
            # the next turn is opponent, so they would take the worse
            option_scores.append(min(scores))

    def score_end_of_game(self, copy, option_scores):
        if copy.draw():
            option_scores.append(0)
        else:
            if copy.active_player().number == self.number:
                option_scores.append(1)
            else:
                option_scores.append(-1)

    def prepare_copy(self, game, option):
        copy = game.copy()
        copy.apply_choice(option)
        copy.check_game_over()
        return copy
