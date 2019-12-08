import pygame
from pygame.locals import *
from settings import *
from threading import Thread
from linear_regression import LogisticRegression
import numpy as np
from button import Button


class GameState:
    def __init__(self):
        pygame.display.set_caption("Perceptron")
        self.screen = pygame.display.set_mode((WIDTH + 100, HEIGHT))
        self.play = True
        self.clock = pygame.time.Clock()
        self.state = MENU
        self.linear = LogisticRegression()
        self.linear.get_datas()
        
        self.buttons = self.get_buttons()
        self.f1 = pygame.font.Font(None, NORMAL)
        self.last_button = None

        
    def get_buttons(self):
        buttons = {}
        buttons[START_BUTTON] = Button("START", CENTER_2, START_BUTTON, NORMAL)
        buttons[RETURN_BUTTON] = Button("BACK", RIGHT_UP, RETURN_BUTTON, SMALL)
        buttons[INSERT_BUTTON] = Button("INSERT",RIGHT_DOWN_2, INSERT_BUTTON, SMALL)
        buttons[DELETE_BUTTON] = Button("DELETE",RIGHT_DOWN_3, DELETE_BUTTON, SMALL)
        buttons[REFRESH_BUTTON] = Button("REFRESH",RIGHT_DOWN_1, REFRESH_BUTTON, SMALL)
        buttons[UNDO_BUTTON] = Button("UNDO",RIGHT_DOWN_4, UNDO_BUTTON, SMALL)
        
        return buttons
        
    def loading(self):
        global play
        self.screen.fill(BACKGROUND)
        for i in range(50, WIDTH-49, 4):
            events = pygame.event.get()
            for e in events:
                if e.type == pygame.QUIT:
                    pygame.quit()
                    play = False
            
            pygame.draw.line(self.screen, LINE_COLOR, [50, HEIGHT-50], [i, HEIGHT-50], 3)
            self.clock.tick(FPS)
            pygame.display.update()

    def menu(self):
        global play
        self.buttons[START_BUTTON].active = True
        self.buttons[RETURN_BUTTON].active = False
        self.buttons[INSERT_BUTTON].active = False
        self.buttons[DELETE_BUTTON].active = False
        self.buttons[REFRESH_BUTTON].active = False
        self.buttons[UNDO_BUTTON].active = False
        self.screen.fill(BACKGROUND)
        self.buttons[START_BUTTON].block(self.screen)
        f2 = pygame.font.Font(None, SMALL)
        gen = f2.render("(c) 2019 Nurbergen Khinatolla", 1, TEXT_COLOR)
        self.screen.blit(gen, CENTER_DOWN)        
        self.clock.tick(FPS)
        pygame.display.update()

    def training(self, new_x=None, new_y=None):
        import time
        if self.last_button == INSERT_BUTTON:
            self.linear.add_data(self.from_pixel_to_dot(new_x), new_y)
        if self.last_button == DELETE_BUTTON:
            self.linear.delete_data(self.from_pixel_to_dot(new_x), new_y)

        self.screen.fill(BACKGROUND)
        self.state = TRAINING_PROCESS
        time.sleep(0.2)
        self.buttons[START_BUTTON].active = False
        self.buttons[RETURN_BUTTON].active = True
        self.buttons[INSERT_BUTTON].active = True
        self.buttons[DELETE_BUTTON].active = True
        self.buttons[REFRESH_BUTTON].active = True
        Thread(target=self.training_process).start()    

    def refresh(self):
        import time
        train_x = self.linear.train_x
        train_y = self.linear.train_y
        log = self.linear.log
        self.state = TRAINING
        time.sleep(0.2)
        self.linear = LogisticRegression()
        self.linear.train_x = train_x
        self.linear.train_y = train_y
        self.linear.log = log
    
    def undo(self):
        if len(self.linear.log) > 1: 
            self.linear.log.pop()
            self.linear.train_x = self.linear.log[-1][0] 
            self.linear.train_y = self.linear.log[-1][1] 
            self.state = REFRESH
        

    def graph(self, color=TEXT_COLOR):
        pygame.draw.line(self.screen, LINE_COLOR, [50, HEIGHT-50], [WIDTH-50, HEIGHT-50], 3)
        pygame.draw.line(self.screen, LINE_COLOR, [50, HEIGHT-50], [50, 50], 3)
        for i in range(len(self.linear.train_x)):
            x = self.linear.train_x[i][0]
            y = self.linear.train_x[i][1]
            if  self.linear.train_y[i] == 0:
                pygame.draw.circle(self.screen, GREEN, self.from_dot_to_pixel(x, y), 5)
            else:
                pygame.draw.circle(self.screen, RED, self.from_dot_to_pixel(x, y), 5)
        
    def training_process(self):
        self.linear.fit()
        i = 0
        while self.state == TRAINING_PROCESS and i < self.linear.epoch:
            x1, y1 = self.linear.get_line(self)
            try:
                if x1 == -1:
                    return
            except:
                pass
            if len(self.linear.log) <= 1:
                self.buttons[UNDO_BUTTON].active = False
            else:
                self.buttons[UNDO_BUTTON].active = True

            i += 1
            x2, y2 = self.from_dot_to_pixel(x1[0], y1[0])
            x3, y3 = self.from_dot_to_pixel(x1[-1], y1[-1]) 
            self.screen.fill(BACKGROUND)
            self.graph()
            for t, button in self.buttons.items():
                button.block(self.screen)
                if self.last_button == t:
                    button.selected(self.screen)
            gen = self.f1.render("GEN: "+str(i), 1, TEXT_COLOR)
            accuracy = self.f1.render(str(self.linear.accuracy)+'%', 1, TEXT_COLOR)
            self.screen.blit(accuracy, RIGHT_UP_3)   
            self.screen.blit(gen, LEFT_UP)     
            pygame.draw.aaline(self.screen, LINE_COLOR, [x2, y2], [x3, y3])
            
            self.clock.tick(FPS)
            pygame.display.update()
        return
    def from_dot_to_pixel(self, x, y):
        pix = 50 + (x - O_X) * DOT
        piy = HEIGHT-50 - (y - O_Y) * DOT
        return (int(pix), int(piy))

    def from_pixel_to_dot(self, pix):
        if pix == None:
            return (None, None)
        x = (pix[0] - 50) / DOT + O_X    
        y = -(pix[1] - HEIGHT + 50) / DOT + O_Y

        return (x, y)
        