def count_player():#input how many players
    while True:
        try:
            x = int(input("How many player?"))
            while x not in {2,3,4}:
                x = int(input("How many player?"))
            break
        except ValueError:
            continue
    return x
