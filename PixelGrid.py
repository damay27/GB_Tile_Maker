
import pygame

from Colors import *

class PixelGrid:

    def __init__(self, x, y, square_size):

        self.square_size = square_size
        self.x = x
        self.y = y

        #Create a list to hold the 
        #values of the pixels in the tile
        self.pixel_values_list = [3] * 64
        
        # Create a list of rectangle objects that represent the pixels of the tile
        self.square_list = []

        for j in range(8):
            for i in range(8):
                self.square_list.append(pygame.Rect(x + i * self.square_size, y + j * self.square_size, self.square_size, self.square_size))


    def draw(self, surface):
        # Draw all the squares that represent the pixels
        index = 0
        while index < len(self.square_list):
            square = self.square_list[index]
            pixel_value = self.pixel_values_list[index]

            if pixel_value == 0:
                pygame.draw.rect(surface, LIGHTEST_GREEN, square)
            elif pixel_value == 1:
                pygame.draw.rect(surface, LIGHT_GREEN, square)
            elif pixel_value == 2:
                pygame.draw.rect(surface, DARK_GREEN, square)
            elif pixel_value == 3:
                pygame.draw.rect(surface, DARKEST_GREEN, square)

            index += 1

        # Draw the vertical lines that divide the squares
        for i in range(1, 8):
                pygame.draw.line(surface, (0, 0, 0), (self.x + i*self.square_size, self.y), (self.x + i*self.square_size, self.y + 8*self.square_size - 1), 1)

        # Draw the horizontal lines that divide the squares
        for j in range(1, 8):
            pygame.draw.line(surface, (0, 0, 0), (self.x, self.y + j*self.square_size), (self.x + 8*self.square_size - 1, self.y + j*self.square_size), 1)

    def handle_mouse_input(self, mouse_pos, event, pixel_color):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            index = 0
            while index < len(self.square_list):
                if self.square_list[index].collidepoint(mouse_pos):
                    self.pixel_values_list[index] = pixel_color
                    break
                index += 1

    def dump_to_c_code(self):

        return "const char tile_array[16] = {" + self.dump_to_csv_string() + "};"

    def dump_to_csv_string(self):

        binary_string = ""
        for value in self.pixel_values_list:
            binary_string += f'{value:02b}'

        packed_data = []

        count = 0
        byte_a = ""
        byte_b = ""
        for bit in list(binary_string):
            if count % 2 == 0:
                byte_a += bit
            else:
                byte_b += bit
            count += 1

            if(count == 16):
                packed_data.append(int(byte_b, base = 2))
                packed_data.append(int(byte_a, base = 2))

                count = 0
                byte_a = ""
                byte_b = ""

        output_string = ""

        for byte in packed_data:
            output_string += f"{hex(byte)}, "

        #Drop the trailing space and trailing comma
        return output_string[:-2]

        # string = ""

        # index = 0
        # while index < len(self.pixel_values_list):
        #     byte_a = ""
        #     byte_b = ""
        #     for i in range(4):
        #         # tmp |= self.pixel_values_list[index+i] << (i*2)
        #         byte_a += str(self.pixel_values_list[index+i] & 1)
        #         byte_b += str( (self.pixel_values_list[index+i] & 2) >> 1 )

        #     if index == 0:
        #         string += f"{hex(tmp)}," # No leading space
        #     if index == len(self.pixel_values_list) - 4:
        #         string += f" {hex(tmp)}" # No trailing comma
        #     else:
        #         string += f" {hex(tmp)},"

        #     index += 4


        # return string

    def exttract_from_csv(self, csv_string):
        value_list =  list(csv_string.split(','))

        #Clear the internal list of the grid
        self.pixel_values_list = []

        index = 0
        while index < len(value_list):
            value_a = value_list[index]
            value_b = value_list[index + 1]
            bin_a = f'{int(value_a, base=16):02b}'
            bin_b = f'{int(value_b, base=16):02b}'
            print(bin_a, bin_b)

            for i in range(8):
                pixel_value = int(bin_a[i] + bin_b[i], base=2)
                self.pixel_values_list.append(pixel_value)

            index += 2
            

