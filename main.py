
if __name__ == "__main__":
    from game_logic.game import play_round, init_game
    game_dict = init_game()
    player_1 = game_dict["player_1"]
    player_2 = game_dict["player_2"]
    while player_1["hand"]:
        play_round(player_1, player_2)
        player_1["hand"].pop()
        player_2["hand"].pop()
