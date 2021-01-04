import pygame

def init():
    display.fill((255, 255, 255))
    pygame.draw.line(display, (0, 0, 0), (0, 100), (300, 100), 2), pygame.draw.line(display, (0, 0, 0), (0, 200), (300, 200), 2), pygame.draw.line(display, (0, 0, 0), (100, 0), (100, 300), 2), pygame.draw.line(display, (0, 0, 0), (200, 0), (200, 300), 2), pygame.display.flip()
    global player_count, game_data, game_finished
    player_count, game_data, game_finished = 0, [0, 0, 0, 0, 0, 0, 0, 0, 0], 0

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
            x, y = int(pos[0] / 100), int(pos[1] / 100)
            if player_count % 2 == 0:
                pygame.draw.circle(display, (0, 0, 0), (50, 50), 75, 2)
            else: