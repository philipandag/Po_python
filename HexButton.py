import math

from Button import Button
import pygame


class HexButton(Button):
    SQRT3O2 = 0.86602540378
    SIDES = 6
    def __init__(self, size: (int, int), pos: (int, int), text: str = ""):
        self.needs_redraw = True
        self.size: (int, int) = size
        self.pos: (int, int) = pos
        self.color = (240, 240, 240, 255)
        self.side_length = self.size[0]//math.sqrt(3)
        self.center = (self.pos[0] + self.side_length, self.pos[1] + self.side_length)
        self.shape, self.triangles = self.create_shape()
        self.fontColor = (0, 0, 0)
        self.hover_effect = (32, 32, 32, 0)
        self.text = text
        self.fontSize = 30
        self.font = pygame.font.SysFont(self.default_font, self.fontSize)
        if text != "":
            self.fontRender = self.renderText()
        else:
            self.fontRender = pygame.Surface((0, 0))
        self.image_normal, self.image_hover = self.create_images()
        self.image = self.image_normal

        self.hovered = False
        self.hover_effect_on = False
        self.onClickFunction = None

    def create_shape(self):
        from math import sin, cos, pi
        n, r = self.SIDES, self.side_length
        x, y = self.size[0] // 2, self.size[1] // 2
        points = [
            (x + r * sin(2 * pi * i / n), y + r * cos(2 * pi * i / n))
            for i in range(n)]
        triangles = [[points[0], points[1], self.center],
                     [points[1], points[2], self.center],
                     [points[2], points[3], self.center],
                     [points[3], points[4], self.center],
                     [points[4], points[5], self.center],
                     [points[5], points[0], self.center]]
        return points, triangles

    def create_images(self):

        image_normal = pygame.Surface(self.size, pygame.SRCALPHA, 32)
        image_normal.convert_alpha()
        pygame.draw.polygon(image_normal, self.color, self.shape)
        pygame.draw.polygon(image_normal, (0, 0, 0), self.shape, 1)

        image_hover = image_normal.copy()
        image_hover.fill(self.hover_effect, special_flags=pygame.BLEND_RGBA_ADD)
        return image_normal, image_hover

    def draw(self, surface):
        if self.needs_redraw:
            surface.blit(self.image, (self.pos[0] + 1, self.pos[1] + 1, self.image.get_width() - 1, self.image.get_height() - 1))
            surface.blit(self.fontRender, (self.pos[0] + (self.size[0] - self.fontRender.get_size()[0]) // 2,
                                           self.pos[1]*1.01 + (self.size[1] - self.fontRender.get_size()[1]) // 2))
            self.needs_redraw = False

    def collides_extended(self, pos):
        collides = True
        for triangle in self.triangles:
            if not self.equilateral_triangle_collision(triangle, pos):
                collides = False
                return False

    def collides_simple(self, pos):
        from math import pow
        if abs(self.center[0] - pos[0]) + abs(self.center[1] - pos[1]) > self.side_length * 2:
            return False
        return pow(self.pos[0] + self.size[0]//2 - pos[0], 2) + pow(self.pos[1] + self.size[1]//2 - pos[1], 2) <= pow(self.side_length*self.SQRT3O2, 2)

    def collides(self, pos):
        return self.collides_simple(pos) and self.collides_extended(pos)

    def equilateral_triangle_collision(self, triangle, point):
        [p1, p2, p3] = triangle
        [px, py] = [point[0] - self.center[0], point[1] - self.center[1]] # TODO COLLISION FIX
        [x1, y1] = p1
        [x2, y2] = p2
        [x3, y3] = p3
        triangle_area = abs((x2-x1)*(y3-y1) - (x3-x1)*(y2-y1))
        area1 = abs((x1-px)*(y2-py) - (x2-px)*(y1-py))
        area2 = abs((x2-px)*(y3-py) - (x3-px)*(y2-py))
        area3 = abs((x3-px)*(y1-py) - (x1-px)*(y3-py))
        buffer = 0.1
        if triangle_area - buffer <= area1 + area2 + area3 <= triangle_area + buffer:
            return True
        return False

