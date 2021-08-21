import pygame
import pyperclip

from tkinter import *
from tkinter.filedialog import asksaveasfile, askopenfile
Tk().withdraw()

import Button
import PixelGrid
import ColorSelect

pygame.init()

SCREEN_WIDTH = pygame.display.Info().current_w
SCREEN_HEIGHT = pygame.display.Info().current_h
SCREEN_WINDOW_RATIO = 2
PIXEL_SQUARE_SIZE = int(SCREEN_WIDTH / 32)
# The size of the window is computes as a number of squares
WINDOW_WIDTH = 13 * PIXEL_SQUARE_SIZE
WINDOW_HEIGHT = 8 * PIXEL_SQUARE_SIZE

BUTTON_UP_COLOR = (225, 225, 225)
BUTTON_DOWN_COLOR = (128, 128, 128)
BUTTON_OVER_COLOR = (255, 255, 255)

BACKGROUND_COLOR = (200, 200, 200)

pygame.display.set_caption("GB Tile Maker")
icon_surface = pygame.image.load("./icon.png")
pygame.display.set_icon(icon_surface)

window_surface = pygame.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])

copy_c_code_button = Button.Button(9*PIXEL_SQUARE_SIZE, 0.5*PIXEL_SQUARE_SIZE, 2.5*PIXEL_SQUARE_SIZE, 0.5*PIXEL_SQUARE_SIZE, "Copy C Code", BUTTON_UP_COLOR, BUTTON_DOWN_COLOR, BUTTON_OVER_COLOR)
save_tile_button = Button.Button(9*PIXEL_SQUARE_SIZE, 1.5*PIXEL_SQUARE_SIZE, 2.5*PIXEL_SQUARE_SIZE, 0.5*PIXEL_SQUARE_SIZE, "Save .csv File", BUTTON_UP_COLOR, BUTTON_DOWN_COLOR, BUTTON_OVER_COLOR)
load_tile_button = Button.Button(9*PIXEL_SQUARE_SIZE, 2.5*PIXEL_SQUARE_SIZE, 2.5*PIXEL_SQUARE_SIZE, 0.5*PIXEL_SQUARE_SIZE, "Load .csv File", BUTTON_UP_COLOR, BUTTON_DOWN_COLOR, BUTTON_OVER_COLOR)

pixel_grid = PixelGrid.PixelGrid(0, 0, PIXEL_SQUARE_SIZE)

color_select = ColorSelect.ColorSelect(8.5*PIXEL_SQUARE_SIZE, 6*PIXEL_SQUARE_SIZE, PIXEL_SQUARE_SIZE)

#Main loop
running = True
while(running):

    mouse_pos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        pixel_grid.handle_mouse_input(mouse_pos, event, color_select.get_selected_value())
        if copy_c_code_button.handle_mouse_input(mouse_pos, event):
            pyperclip.copy(pixel_grid.dump_to_c_code())

        if save_tile_button.handle_mouse_input(mouse_pos, event):

            types_and_extentions = [("CSV Files", "*.csv"), ("All Files", "*.*")]
            file = asksaveasfile(filetypes = types_and_extentions, defaultextension = types_and_extentions)
            if file is not None:
                csv_string = pixel_grid.dump_to_csv_string()
                file.write(csv_string)
                file.close()

        if load_tile_button.handle_mouse_input(mouse_pos, event):

            file = askopenfile(mode='r')

            if file is not None:
                csv_string = file.read()
                pixel_grid.exttract_from_csv(csv_string)

        color_select.handle_mouse_input(mouse_pos, event)

    window_surface.fill(BACKGROUND_COLOR)

    pixel_grid.draw(window_surface)

    copy_c_code_button.draw(window_surface)
    save_tile_button.draw(window_surface)
    load_tile_button.draw(window_surface)

    color_select.draw(window_surface)

    pygame.display.flip()


