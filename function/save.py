def save_cords(save_game, cords, type):
    if cords[0] == 0 and cords[1] == 0:
        if save_game[0] == 0:
            save_game[0] = type
            return True
        else:
            return False
    elif cords[0] == 1 and cords[1] == 0:
        if save_game[1] == 0:
            save_game[1] = type
            return True
        else:
            return False
    elif cords[0] == 2 and cords[1] == 0:
        if save_game[2] == 0:
            save_game[2] = type
            return True
        else:
            return False
    elif cords[0] == 0 and cords[1] == 1:
        if save_game[3] == 0:
            save_game[3] = type
            return True
        else:
            return False
    elif cords[0] == 1 and cords[1] == 1:
        if save_game[4] == 0:
            save_game[4] = type
            return True
        else:
            return False
    elif cords[0] == 2 and cords[1] == 1:
        if save_game[5] == 0:
            save_game[5] = type
            return True
        else:
            return False
    elif cords[0] == 0 and cords[1] == 2:
        if save_game[6] == 0:
            save_game[6] = type
            return True
        else:
            return False
    elif cords[0] == 1 and cords[1] == 2:
        if save_game[7] == 0:
            save_game[7] = type
            return True
        else:
            return False
    elif cords[0] == 2 and cords[1] == 2:
        if save_game[8] == 0:
            save_game[8] = type
            return True
        else:
            return False