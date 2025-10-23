from random import randint as rand
def create_card(rank:str,suite:str) -> dict:
    value = None
    hi_cards = {"10": 10,
                "J": 11,
                "Q": 12,
                "K": 13,
                "A": 14}
    if rank >= '2' and rank <= '9':
       value = int(rank)
    else:
        value = hi_cards[rank]

    return {"rank": rank ,
            "suite": suite,
            "value": value}


def compare_cards(p1_card: dict, p2_card: dict) -> str:
    if p1_card["value"] > p2_card["value"]:
        return "p1"
    elif p2_card["value"] > p1_card["value"]:
        return "p2"
    return "WAR"

def create_deck() -> [dict]:
    deck_list = []
    suites_list = ['S', 'H', 'C', 'D']
    cards_list = [ '2', '3', '4', '5', '6','7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    for card in cards_list:
        for suite in suites_list:
            deck_list.append(create_card(card, suite))
    return deck_list



def shuffle(deck: [dict]) -> [dict]:
    i = 0
    while i < 1000:
        index1 = rand(0, 51)
        index2 = rand(0, 51)
        if index1 == index2:
            continue
        deck[index1], deck[index2] = deck[index2], deck[index1]
        i += 1
    return deck


if __name__ == "__main__":
    # print(create_card("A", "S"))
    # print(create_card("J", "S"))
    # print(create_card("10", "S"))
    # print(create_card("2", "S"))
    # print(compare_cards({"value":14}, {"value":13}))
    # print(compare_cards({"value":13}, {"value":14}))
    # print(compare_cards({"value":14}, {"value":14}))
    #print(len(create_deck()))
    d = (shuffle(create_deck()))
    for i in d:
        print(i)
    print(len(d))
