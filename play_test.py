import play_i

if __name__ == '__main__':

    print("hello")
    tic = play_i.TicTacToe()
    tic.add_player(play_i.MinMaxPlayer(tic.play_area))
    tic.add_player(play_i.ConsolePlayer(tic.play_area))
    tic.setup()
    tic.play()
