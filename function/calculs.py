def calcul_pos(x, y):
    if x < 300 and y < 300:
        return 0, 0
    elif x > 300 and x < 600 and y < 300:
        return 1, 0
    elif x > 600 and x < 900 and y < 300:
        return 2, 0
    ###
    elif x < 300 and y > 300 and y < 600:
        return 0, 1
    elif x > 300 and x < 600 and y > 300 and y < 600:
        return 1, 1
    elif x > 600 and x < 900 and y > 300 and y < 600:
        return 2, 1
    ###
    elif x < 300 and y > 600 and y < 900:
        return 0, 2
    elif x > 300 and x < 600 and y > 600 and y < 900:
        return 1, 2
    elif x > 600 and x < 900 and y > 600 and y < 900:
        return 2, 2
    else:
        return 0, 0


def player(player_count):
    if player_count % 2 == 0:
        return "cross"
    else:
        return "circle"


def is_winner(game_data):
    for i in range(0, len(game_data), 3):
        if game_data[i] != 0 and game_data[i+1] != 0 and game_data[i+2] != 0:
            if game_data[i] == game_data[i + 1] == game_data[i + 2]:
                return True
    if game_data[0] != 0 and game_data[4] != 0 and game_data[8] != 0:
        if game_data[0] == game_data[4] == game_data[8]:
            return True
    elif game_data[2] != 0 and game_data[4] != 0 and game_data[6] != 0:
        if game_data[2] == game_data[4] == game_data[6]:
            return True
    else:
        return False