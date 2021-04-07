import pygame
def circle(x, y, display):
    if x < 100 and y < 100:
        pygame.draw.circle(display, (0, 0, 0), (50, 50), 75, 2)
    elif x > 100 and x < 200 and y < 100:
        pygame.draw.circle(display, (0, 0, 0), (450, 150), 75, 2)
    elif x > 200 and x < 300 and y < 100:
        pygame.draw.circle(display, (0, 0, 0), (750, 150), 75, 2)
    elif x < 100 and y > 100 and y < 200:
        pygame.draw.circle(display, (0, 0, 0), (150, 450), 75, 2)
    elif x > 100 and x < 200 and y > 100 and y < 200:
        pygame.draw.circle(display, (0, 0, 0), (450, 450), 75, 2)
    elif x > 200 and x < 300 and y > 100 and y < 200:
        pygame.draw.circle(display, (0, 0, 0), (750, 450), 75, 2)
    elif x < 100 and y > 200 and y < 300:
        pygame.draw.circle(display, (0, 0, 0), (150, 750), 75, 2)
    elif x > 100 and x < 200 and y > 200 and y < 300:
        pygame.draw.circle(display, (0, 0, 0), (450, 750), 75, 2)
    elif x > 200 and x < 300 and y > 200 and y < 300:
        pygame.draw.circle(display, (0, 0, 0), (750, 750), 75, 2)
    pygame.display.flip()
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
    for i in range(0, 3):
        if game_data[i] != 0 and game_data[i+3] != 0 and game_data[i+6]:
            if game_data[i] == game_data[i+3] == game_data[i+6]:
                return True
    if game_data[0] != 0 and game_data[4] != 0 and game_data[8] != 0:
        if game_data[0] == game_data[4] == game_data[8]:
            return True
    elif game_data[2] != 0 and game_data[4] != 0 and game_data[6] != 0:
        if game_data[2] == game_data[4] == game_data[6]:
            return True
    else:
        return False