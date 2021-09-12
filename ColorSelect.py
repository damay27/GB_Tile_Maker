import pygame

from Colors import *

class ColorSelect:

    '''
    Color swatch selector GUI element.
    '''

    def __init__(self, x, y, square_size):
        '''
        Initialize the color swatch GUI element class.

        Parameters:
            x           : Horizontal position of the top left corner of the GUI element within the window.
            y           : Vertical position of the top left corner of the GUI element within the window.
            square_size : The size of each square swatch in the color selector.
        '''

        self.x = x
        self.y = y
        self.square_size = square_size

        # By default the darkest shade of green is selected.
        self.selected_value = 3

        # Create a fill in a list of rectangles (they are square in reality) that
        # represent the color swatches.
        self.square_list = []
        for i in range(4):
            self.square_list.append(pygame.Rect(x + i * self.square_size, y, self.square_size, self.square_size))

        
    def draw(self, surface):
        '''
        Actually draw the color picker GUI element on the given surface.

        Parameters:
            surface : The pygame surface which the GUI element is draw on to.

        Return:
            Nothing.
        '''

        # Draw all four of the color picker elements.
        pygame.draw.rect(surface, LIGHTEST_GREEN, self.square_list[0])
        pygame.draw.rect(surface, LIGHT_GREEN, self.square_list[1])
        pygame.draw.rect(surface, DARK_GREEN, self.square_list[2])
        pygame.draw.rect(surface, DARKEST_GREEN, self.square_list[3])

        # Draw the boarder around the selected color
        pygame.draw.rect(surface, (0, 0, 0), self.square_list[self.selected_value], width = 4)

        # Draw the vertical lines that divide the squares
        for i in range(1, 4):
                pygame.draw.line(surface, (0, 0, 0), (self.x + i*self.square_size, self.y), (self.x + i*self.square_size, self.y + self.square_size - 1), 1)


    def handle_mouse_input(self, mouse_pos, event):
        '''
        Check if the element has been clicked.

        Parameters:
            mouse_pos   : Tuple that represents the position of 
                          the mouse with in the window.
            event       : Pygame event object fo the event that just happened.

        Return:
            Nothing.
        '''
        
        # Check if the event was a button press and was the right mouse
        # button.
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            index = 0
            # Figure out which of the color squares was selected and
            # based on that change the selected_value member variable.
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
        '''
        Return the value that was most recently selected

        Return:
            Integer representing the selected color value.
        '''
        return self.selected_value