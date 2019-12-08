from game_state import GameState
from settings import *
import pygame
from button import Button
pygame.init()

window = GameState()

window.loading()

while window.play:
    new_x = None
    new_y = 0
    events = pygame.event.get()
    mouse = pygame.mouse.get_pressed()
    mouse_pos = pygame.mouse.get_pos()
    for e in events:
        if e.type == pygame.QUIT:
            pygame.quit()
            play = False
        if e.type == pygame.MOUSEBUTTONUP:
            if e.button == 1 and (window.last_button == INSERT_BUTTON or window.last_button == DELETE_BUTTON):
                new_x = mouse_pos
                new_y = 0
            if e.button == 3 and window.last_button == INSERT_BUTTON:
                new_x = mouse_pos
                new_y = 1
            if e.button == 1 and window.last_button == UNDO_BUTTON:
                window.undo()
   
    if window.state == MENU:
        window.menu()
    if window.state == TRAINING:
        window.training()
    if window.state == REFRESH:
        window.refresh()
    cursor = False
    for type, button in window.buttons.items():
        if button.on_focus(mouse_pos):
            cursor = True
            if mouse[0] == 1:
                if type == RETURN_BUTTON:
                    window.state = MENU
                    window.last_button = RETURN_BUTTON
                if type == START_BUTTON:
                    window.state = TRAINING
                    window.last_button = START_BUTTON
                if type == INSERT_BUTTON:
                    window.last_button = INSERT_BUTTON
                if type == DELETE_BUTTON:
                    window.last_button = DELETE_BUTTON
                if type == REFRESH_BUTTON:
                    window.state = REFRESH
                    window.last_button = REFRESH_BUTTON
                if type == UNDO_BUTTON:
                    window.last_button = UNDO_BUTTON
                   
    if cursor:
        pygame.mouse.set_cursor(*pygame.cursors.diamond)
    else:
        pygame.mouse.set_cursor(*pygame.cursors.arrow)
        if new_x != None:
            window.training(new_x, new_y)
            