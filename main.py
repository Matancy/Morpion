import pygame

def init():
    display.fill((255, 255, 255))
    pygame.draw.line(display, (0, 0, 0), (0, 100), (300, 100), 2), pygame.draw.line(display, (0, 0, 0), (0, 200), (300, 200), 2), pygame.draw.line(display, (0, 0, 0), (100, 0), (100, 300), 2), pygame.draw.line(display, (0, 0, 0), (200, 0), (200, 300), 2)
    global player_count, game_data, game_finished
    player_count, game_data, game_finished = 0, [[0, 0, 0], [0, 0, 0], [0, 0, 0]], 0
def save(x, y, player):
    game_data[y-1][x-1] = player
def winner():
    for i in range(3):
        if game_data[i][0] == game_data[i][1] == game_data[i][2] and game_data[i][0] != 0:
            return "Cercle Gagnant" if game_data[i][0] == 1 else "Croix Gagnante"
        if game_data[0][i] == game_data[1][i] == game_data[2][i] and game_data[0][i] != 0:
            return "Cercle Gagnant" if game_data[0][i] == 1 else "Croix Gagnante"
    if game_data[0][0] == game_data[1][1] == game_data[2][2] and game_data[1][1] != 0 or game_data[0][2] == game_data[1][1] == game_data[2][0] and game_data[1][1] != 0:
        return "Cercle Gagnant" if game_data[1][1] == 1 else "Croix Gagnante"
def cercle(x, y):
    pygame.draw.circle(display, (0, 0, 0), (x * 100 - 50, y * 100 - 50), 50, 2)
    save(x, y, 1)
def croix(x, y):
    pygame.draw.line(display, (0, 0, 0), (x * 100 - 100, y * 100 - 100), (x * 100, y * 100), 2)
    pygame.draw.line(display, (0, 0, 0), (x * 100, y * 100 - 100), (x * 100 - 100, y * 100), 2)
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
        if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed() == (1, 0, 0) and game_finished == 0: #Gauche
            pos = pygame.mouse.get_pos()
            x, y = int((pos[0] + 100) / 100), int((pos[1] + 100) / 100)
            if player_count % 2 == 0:
                cercle(x, y)
            else:
                croix(x, y)
            player_count += 1
            if winner() != None:
                game_finished = 1
                print(winner())
    pygame.display.flip()