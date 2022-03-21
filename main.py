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
player1_color = (5, 153, 17)
player2_color = (153, 118, 5)

# =========================================FONTS========================================================================
font_path = r'Fonts/'

harukaze = pygame.font.Font(font_path + "Harukaze.ttf", 25)

# =========================================TEXTS========================================================================
txt_exit = harukaze.render("EXIT", True, white)

# ====================================WINDOW_START_SEIZE================================================================
window_seize = (1920, 1025)

# =====================================CREATING_WINDOW==================================================================
window = pygame.display.set_mode(window_seize, pygame.RESIZABLE)
pygame.display.set_caption("TicTacToe")
image_path = r'C:\Users\User\Downloads\Download.png'
programIcon = pygame.image.load(image_path)
window_color = lila
game_clock = pygame.time.Clock()

# ========================================TOGGLES=======================================================================
fullscreen_toggle = 1
player_switch = 1
menu_toggle = 1
menu_interface = False
game_status = True

# ========================================FUNCTIONS=====================================================================
def player_color_changer(switch, p1c, p2c):
    if switch == 1:
        player_color = p1c
    else:
        player_color = p2c
    return player_color

# =======================================MAIN_LOOP======================================================================
while game_status:

    # ==================================CALCULATIONS====================================================================
    pygame.display.set_icon(programIcon)

    window_high = window.get_height()
    window_width = window.get_width()

    new_window_width = (window_width - 200) / 2.0
    new_window_high = (window_high - 280) / 2.0

    mouse = pygame.mouse.get_pos()

    # ====================================BOXES=========================================================================
    Box1 = [window_width/6, window_high/6]
    Box2 = [window_width/2, window_high/6]
    Box3 = [window_width/1.20, window_high/6]
    Box4 = [window_width/6, window_high/2]
    Box5 = [window_width/2, window_high/2]
    Box6 = [window_width/1.20, window_high/2]
    Box7 = [window_width/6, window_high/1.2]
    Box8 = [window_width/2, window_high/1.2]
    Box9 = [window_width/1.20, window_high/1.2]

    # =================================WINDOW_X_BUTTON==================================================================
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_status = False

        # ================================KEYBOARD_ACTIONS==================================================================
        elif event.type == pygame.KEYDOWN:

            # ===========================F11_KEY========================================================================
            if event.key == pygame.K_F11:
                if fullscreen_toggle == 1:
                    pygame.display.quit()
                    pygame.display.init()
                    window_seize = (1920, 1080)
                    window = pygame.display.set_mode(window_seize, pygame.FULLSCREEN)
                    fullscreen_toggle -= 1
                elif fullscreen_toggle == 0:
                    pygame.display.quit()
                    pygame.display.init()
                    window_seize = (1920, 1025)
                    window = pygame.display.set_mode(window_seize, pygame.RESIZABLE)
                    fullscreen_toggle += 1

            # ==========================ESC_KEY=========================================================================
            elif event.key == pygame.K_ESCAPE:
                if menu_toggle == 1:
                    window_color = grey_lila
                    menu_interface = True
                    menu_toggle -= 1
                elif menu_toggle == 0:
                    window_color = lila
                    menu_interface = False
                    menu_toggle += 1

        # ==============================MOUSE_ACTIONS===================================================================
        elif event.type == pygame.MOUSEBUTTONDOWN:

            # ==========================EXIT_BUTTON=====================================================================
            if new_window_width <= mouse[0] <= new_window_width + 190 and new_window_high <= mouse[1] <= new_window_high + 35 and menu_interface:
                game_status = False

    # ==================================WINDOW_RESET====================================================================
    window.fill(window_color)

    # ==================================SOIL_BOARD======================================================================
    pygame.draw.line(window, black, [0, window_high / 3], [window_width, window_high / 3], 20)
    pygame.draw.line(window, black, [0, window_high / 1.5], [window_width, window_high / 1.5], 20)
    pygame.draw.line(window, black, [window_width / 3, 0], [window_width / 3, window_high], 20)
    pygame.draw.line(window, black, [window_width / 1.5, 0], [window_width / 1.5, window_high], 20)

    # ================================MARKER_PREVIEW====================================================================
    if not menu_interface:
        marker_color = player_color_changer(player_switch, player1_color, player2_color)
        # ==============================UPPER_LINE======================================================================
        if 0 <= mouse[0] <= window_width/3 and 0 <= mouse[1] <= window_high/3:
            pygame.draw.circle(window, marker_color, Box1, 40, 7)
        elif 0 <= mouse[0] <= window_width/1.5 and 0 <= mouse[1] <= window_high/3:
            pygame.draw.circle(window, marker_color, Box2, 40, 7)
        elif 0 <= mouse[0] <= window_width/0.75 and 0 <= mouse[1] <= window_high/3:
            pygame.draw.circle(window, marker_color, Box3, 40, 7)

        # ==============================MID_LINE========================================================================
        elif 0 <= mouse[0] <= window_width/3 and window_high/6 <= mouse[1] <= window_high / 1.5:
            pygame.draw.circle(window, marker_color, Box4, 40, 7)
        elif 0 <= mouse[0] <= window_width/1.5 and window_high/6 <= mouse[1] <= window_high / 1.5:
            pygame.draw.circle(window, marker_color, Box5, 40, 7)
        elif 0 <= mouse[0] <= window_width/0.75 and window_high/6 <= mouse[1] <= window_high/1.5:
            pygame.draw.circle(window, marker_color, Box6, 40, 7)

        # =============================LOWER_LINE=======================================================================
        elif 0 <= mouse[0] <= window_width/3 and window_high/3 <= mouse[1] <= window_high:
            pygame.draw.circle(window, marker_color, Box7, 40, 7)
        elif 0 <= mouse[0] <= window_width/1.5 and window_high/3 <= mouse[1] <= window_high:
            pygame.draw.circle(window, marker_color, Box8, 40, 7)
        elif 0 <= mouse[0] <= window_width/0.75 and window_high/3 <= mouse[1] <= window_high:
            pygame.draw.circle(window, marker_color, Box9, 40, 7)

    # ==================================MENU============================================================================
    if menu_interface:
        pygame.draw.rect(window, black, [new_window_width, new_window_high, 200, 280])
        if new_window_width <= mouse[0] <= new_window_width + 190 and new_window_high <= mouse[1] <= new_window_high + 35:
            pygame.draw.rect(window, tur_bright, [new_window_width + 10, new_window_high + 5, 180, 30])
        else:
            pygame.draw.rect(window, tur_dark, [new_window_width + 10, new_window_high + 5, 180, 30])
        window.blit(txt_exit, [new_window_width + 75, new_window_high + 6])

    pygame.display.flip()

    game_clock.tick(60)

pygame.quit()
