# menu.py

import pygame
import sys
from button import Button
from p1 import game_logic, initialize_game  # Import the functions from p1.py


SCREEN = pygame.display.set_mode((1100, 850))
pygame.display.set_caption("Menu")

BG = pygame.image.load("Menu_bk.png")

def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font("font.ttf", size)

# Function to start the game
def start_game():
    # Call the initialize_game and game_logic functions from p1.py
    initialize_game()  # Initialize the game
    game_logic()       # Run the game loop
    print("Game Started")  # Just to verify that the function is called

def show_restart_button():
    restart_button = Button(image=None, pos=(550, 700),
                            text_input="RESTART", font=get_font(50), base_color="White", hovering_color="Green")
    restart_button.changeColor(pygame.mouse.get_pos())
    restart_button.update(SCREEN)
    return restart_button

# Function to show the play screen
def play():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")

        PLAY_TEXT = get_font(45).render("This is the PLAY screen.", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = Button(image=None, pos=(640, 460),
                           text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()

        pygame.display.update()

# Function for options menu
def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        OPTIONS_TEXT = get_font(45).render("This is the OPTIONS screen.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(640, 460),
                              text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()

# Main menu function
def main_menu():
    pygame.init()
    pygame.mixer.music.load("menu_music.mp3")  # Replace with your actual file path
    pygame.mixer.music.set_volume(0.5)  # Adjust volume if necessary
    pygame.mixer.music.play(-1)  # Loop the music indefinitely
  
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(70).render("SPACE SHOOTER", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(550, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("Play_Rect.png"), pos=(550, 250),
                             text_input="PLAY", font=get_font(50), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("Options_Rect.png"), pos=(550, 400),
                                text_input="OPTIONS", font=get_font(50), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("Quit_Rect.png"), pos=(550, 550),
                             text_input="QUIT", font=get_font(50), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    start_game()  # Starts the game when PLAY button is clicked
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

# Call the main menu function to start
main_menu()
