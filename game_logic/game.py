from utils import deck
def create_player(name :str = "AI") -> dict:
    player = {"name": name,
              "hand": [],
              "won_pile": []}
    return player

def init_game()-> dict:
    player1 = create_player("Israel")
    player2 = create_player()
    cards = deck.shuffle(deck.create_deck())
    player1["hand"] = cards[26:]
    player2["hand"] = cards[:26]
    game_dict = {"deck": cards,
                 "player_1": player1,
                 "player_2": player2}
    return game_dict


def play_round(p1:dict, p2: dict) -> None:
    p1_card = p1["hand"][-1]
    p2_card = p2["hand"][-1]
    winner = deck.compare_cards(p1_card, p2_card)
    if winner == "WAR":
        return
    elif winner == "p1":
        p1["won_pile"].append(p1_card)
        p1["won_pile"].append(p2_card)
    else:
        p2["won_pile"].append(p1_card)
        p2["won_pile"].append(p2_card)
    # p1["hand"] = p1["hand"][:-1]
    # p2["hand"] = p2["hand"][:-1]
    print(winner)


if __name__ == "__main__":
    a = (init_game()["player_1"])
    print(a["hand"][25])
