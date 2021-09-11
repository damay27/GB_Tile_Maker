import pygame

class Button:

    def __init__(self, x, y, width, height, text, up_color, down_color, over_color, text_color = (0, 0, 0), text_size = 24):
        '''
        Initialize the button class.

        Parameters:
            x           : X location in pixels of the upper Left corner of the button within the window.
            y           : Y location in pixels of the upper Left corner of the button within the window.
            width       : Width of the button in pixels.
            height      : Height of the button in pixels.
            text        : Text displayed within the button
            up_color    : The color of the button when it is in the up state. This occurs when the button
                          is not pressed and the mouse is not over the button.
            down_color  : The color of the button when it is in the down state. This occurs when the button
                          is pressed.
            over_color  : The color of the button when the mouse is hovering over it.
            text_color  : Color of the text drawin within the button.
            text_size   : Size of the text in points.
        '''
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.up_color = up_color
        self.down_color = down_color
        self.over_color = over_color
        self.draw_color = self.up_color
        self.button_state = 0
        self.font = pygame.font.SysFont(None, text_size)
        self.text_color = text_color
        self.rounding = int(width / 20)


    def handle_mouse_input(self, point, event):
        '''
        React to user input from the mouse.

        Parameters:
            point   : A tuple that stores the x and y location of the mouse within the window.
            event   : The type of mouse even that occured. The object is a
                      pygame event object.
        '''
        if self.rect.collidepoint(point):
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                self.button_state = 2
                return True
            else:
                self.button_state = 1
                return False
        else:
            self.button_state = 0
            return False


    def draw(self, surface):
        '''
        Draw the button on screen.

        Parameters:
            surface : Surface which the button gets drawn on.
        '''

        # Draw the button when the button is not pressed and the mouse is not hovering over it.
        if self.button_state == 0:
            pygame.draw.rect(surface, self.up_color, self.rect, border_radius = self.rounding)
            pygame.draw.rect(surface, (0, 0, 0), self.rect, border_radius = self.rounding, width = 2)

        # Draw the button when mouse is hovering over the button.
        elif self.button_state == 1:
            pygame.draw.rect(surface, self.over_color, self.rect, border_radius = self.rounding)
            pygame.draw.rect(surface, (0, 0, 0), self.rect, border_radius = self.rounding, width = 2)

        # Draw the button when it is clicked.
        elif self.button_state == 2:
            pygame.draw.rect(surface, self.down_color, self.rect, border_radius = self.rounding)
            pygame.draw.rect(surface, (0, 0, 0), self.rect, border_radius = self.rounding, width = 2)

        # Render the text with in the button
        text_surface = self.font.render(self.text, True, self.text_color)
        # We want the text to be centered with in the button. We start at the top left
        # corner of the button and half the width/height of the button rectangle to get 
        # to the center of the button. Then we need to half the width/height of the text
        # suface and move back by that amount (either up or left). If we didn't do that 
        # last part the top left corner of the text surface would be centered but the text
        # itselft would not be.
        text_x_pos = int(self.rect.x + self.rect.width / 2 - text_surface.get_width() / 2)
        text_y_pos = int(self.rect.y + self.rect.height / 2 - text_surface.get_height() / 2)

        # Actually apply the text to the surface.
        surface.blit(text_surface, (text_x_pos, text_y_pos))


