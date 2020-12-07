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


def player(player_count):
    player_count += 1
    if player_count % 2 == 0:
        return "cross"
    else:
        return "circle"
