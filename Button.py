import pygame

class Button:

    def __init__(self, x, y, width, height, text, up_color, down_color, over_color, text_color = (0, 0, 0), text_size = 24):
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
        if self.button_state == 0:
            pygame.draw.rect(surface, self.up_color, self.rect, border_radius = self.rounding)
            pygame.draw.rect(surface, (0, 0, 0), self.rect, border_radius = self.rounding, width = 2)
            # print("up")
        elif self.button_state == 1:
            pygame.draw.rect(surface, self.over_color, self.rect, border_radius = self.rounding)
            pygame.draw.rect(surface, (0, 0, 0), self.rect, border_radius = self.rounding, width = 2)

            # print("over")
        elif self.button_state == 2:
            pygame.draw.rect(surface, self.down_color, self.rect, border_radius = self.rounding)
            pygame.draw.rect(surface, (0, 0, 0), self.rect, border_radius = self.rounding, width = 2)
            # print("down")

        text_surface = self.font.render(self.text, True, self.text_color)
        text_x_pos = int(self.rect.x + self.rect.width / 2 - text_surface.get_width() / 2)
        text_y_pos = int(self.rect.y + self.rect.height / 2 - text_surface.get_height() / 2)
        surface.blit(text_surface, (text_x_pos, text_y_pos))


