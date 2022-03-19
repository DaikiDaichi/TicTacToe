# =========================================IMPORTS======================================================================
import pygame

# ====================================PYGAME_INITIALISATION=============================================================
pygame.init()

# =========================================COLORS=======================================================================
tur_bright = (0, 221, 250)
tur_dark = (1, 90, 102)
lila = (85, 43, 148)
grey_lila = (70, 40, 120)
black = (0, 0, 0)
white = (255, 255, 255)

# =========================================FONTS========================================================================
font_path = r'Fonts/'

harukaze = pygame.font.Font(font_path+"Harukaze.ttf", 25)

# =========================================TEXTS========================================================================
txt_exit = harukaze.render("EXIT", True, white)

# ====================================WINDOW_START_SEIZE================================================================
x = 500
y = 500
window_seize = (x, y)

# =====================================CREATING_WINDOW==================================================================
window = pygame.display.set_mode(window_seize, pygame.RESIZABLE)
pygame.display.set_caption("TicTacToe")
image_path = r'C:\Users\User\Downloads\Download.png'
programIcon = pygame.image.load(image_path)
window_color = lila
game_clock = pygame.time.Clock()

# ========================================TOGGLES=======================================================================
fullscreen_toggle = 1
menu_toggle = 1
menu_interface = False
game_status = True

# =======================================MAIN_LOOP======================================================================
while game_status:
    pygame.display.set_icon(programIcon)

    window_high = window.get_height()
    window_width = window.get_width()

    new_window_width = (window_width-200)/2.0
    new_window_high = (window_high-280)/2.0

    mouse = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_status = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F11:
                if fullscreen_toggle == 1:
                    pygame.display.quit()
                    pygame.display.init()
                    window = pygame.display.set_mode(window_seize, pygame.FULLSCREEN)
                    fullscreen_toggle -= 1
                elif fullscreen_toggle == 0:
                    pygame.display.quit()
                    pygame.display.init()
                    window = pygame.display.set_mode(window_seize, pygame.RESIZABLE)
                    fullscreen_toggle += 1

            elif event.key == pygame.K_ESCAPE:
                if menu_toggle == 1:
                    window_color = grey_lila
                    menu_interface = True
                    menu_toggle -= 1

                elif menu_toggle == 0:
                    window_color = lila
                    menu_interface = False
                    menu_toggle += 1

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if new_window_width <= mouse[0] <= new_window_width+190 and new_window_high <= mouse[1] <= new_window_high + 35 and menu_interface:
                game_status = False

    window.fill(window_color)

    if menu_interface:
        pygame.draw.rect(window, black, [new_window_width, new_window_high, 200, 280])
        if new_window_width <= mouse[0] <= new_window_width+190 and new_window_high <= mouse[1] <= new_window_high + 35:
            pygame.draw.rect(window, tur_bright, [new_window_width+10, new_window_high+5, 180, 30])
        else:
            pygame.draw.rect(window, tur_dark, [new_window_width+10, new_window_high+5, 180, 30])
        window.blit(txt_exit, [new_window_width+75, new_window_high+10])

    pygame.display.flip()

    game_clock.tick(60)

pygame.quit()
