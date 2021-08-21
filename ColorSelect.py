import pygame

from Colors import *

class ColorSelect:

    def __init__(self, x, y, square_size):

        self.x = x
        self.y = y
        self.square_size = square_size
        self.selected_value = 3

        self.square_list = []
        for i in range(4):
            self.square_list.append(pygame.Rect(x + i * self.square_size, y, self.square_size, self.square_size))

        
    def draw(self, surface):

        pygame.draw.rect(surface, LIGHTEST_GREEN, self.square_list[0])
        pygame.draw.rect(surface, LIGHT_GREEN, self.square_list[1])
        pygame.draw.rect(surface, DARK_GREEN, self.square_list[2])
        pygame.draw.rect(surface, DARKEST_GREEN, self.square_list[3])

        pygame.draw.rect(surface, (0, 0, 0), self.square_list[self.selected_value], width = 4)

        # Draw the vertical lines that divide the squares
        for i in range(1, 4):
                pygame.draw.line(surface, (0, 0, 0), (self.x + i*self.square_size, self.y), (self.x + i*self.square_size, self.y + self.square_size - 1), 1)


    def handle_mouse_input(self, mouse_pos, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            index = 0
            while index < len(self.square_list):
                if self.square_list[index].collidepoint(mouse_pos):
                    if index == 0:
                        self.selected_value = LIGHTEST_GREEN_VAL
                    elif index == 1:
                        self.selected_value = LIGHT_GREEN_VAL
                    elif index == 2:
                        self.selected_value = DARK_GREEN_VAL
                    elif index == 3:
                        self.selected_value = DARKEST_GREEN_VAL
                    break
                index += 1

    def get_selected_value(self):
        return self.selected_value