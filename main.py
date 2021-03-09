import pygame

def init():
    display.fill((255, 255, 255))
    pygame.draw.line(display, (0, 0, 0), (0, 100), (300, 100), 2), pygame.draw.line(display, (0, 0, 0), (0, 200), (300, 200), 2), pygame.draw.line(display, (0, 0, 0), (100, 0), (100, 300), 2), pygame.draw.line(display, (0, 0, 0), (200, 0), (200, 300), 2)
    global player_count, game_data, game_finished, black, red
    player_count, game_data, game_finished, black, red = 0, [[0, 0, 0], [0, 0, 0], [0, 0, 0]], 0, (0, 0, 0), (255, 0, 0)
def save(x, y, player):
    game_data[y-1][x-1] = player
def winner():
    for i in range(3):
        if game_data[i][0] == game_data[i][1] == game_data[i][2] and game_data[i][0] != 0:
            return ("True", cercle(1, i+1, red), cercle(2, i+1, red), cercle(3, i+1, red)) if game_data[i][0] == 1 else ("True", croix(1, i+1, red), croix(2, i+1, red), croix(3, i+1, red))
        elif game_data[0][i] == game_data[1][i] == game_data[2][i] and game_data[0][i] != 0:
            return ("True", cercle(i+1, 1, red), cercle(i+1, 2, red), cercle(i+1, 3, red)) if game_data[0][i] == 1 else ("True", croix(i+1, 1, red), croix(i+1, 2, red), croix(i+1, 3, red))
    if game_data[0][0] == game_data[1][1] == game_data[2][2] and game_data[1][1] != 0:
        return ("True", cercle(1, 1, red), cercle(2, 2, red), cercle(3, 3, red)) if game_data[1][1] == 1 else ("True", croix(1, 1, red), croix(2, 2, red), croix(3, 3, red))
    elif game_data[0][2] == game_data[1][1] == game_data[2][0] and game_data[1][1] != 0:
        return ("True", cercle(3, 1, red), cercle(2, 2, red) and cercle(1, 3, red)) if game_data[1][1] == 1 else ("True", croix(3, 1, red), croix(2, 2, red), croix(1, 3, red))
def cercle(x, y, color):
    pygame.draw.circle(display, color, (x * 100 - 50, y * 100 - 50), 50, 2)
    save(x, y, 1)
def croix(x, y, color):
    pygame.draw.line(display, color, (x * 100 - 100, y * 100 - 100), (x * 100, y * 100), 2)
    pygame.draw.line(display, color, (x * 100, y * 100 - 100), (x * 100 - 100, y * 100), 2)
    save(x, y, 2)
display = pygame.display.set_mode((300, 300))
init()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            init()
        if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed() == (1, 0, 0) and game_finished == 0:
            pos = pygame.mouse.get_pos()
            x, y = (pos[0] + 100) // 100, (pos[1] + 100) // 100
            if player_count % 2 == 0:
                cercle(x, y, black)
            else:
                croix(x, y, black)
            player_count += 1
            game_finished = 1 if player_count == 9 else 0
            if winner() != None:
                game_finished = 1
    pygame.display.flip()