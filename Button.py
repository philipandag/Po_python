import pygame
from InterfaceElement import InterfaceElement


class Button(InterfaceElement):
    default_font = "consolas"

    def __init__(self, size: (int, int), pos: (int, int), text: str = ""):
        self.size: (int, int) = size
        self.pos: (int, int) = pos
        self.color = (200, 200, 200)
        self.fontColor = (0, 0, 0)
        self.hover_effect = (32, 32, 32)
        self.text = text
        self.fontSize = 30
        self.font = pygame.font.SysFont(self.default_font, self.fontSize)
        if text != "":
            self.fontRender = self.renderText()
        else:
            self.fontRender = pygame.Surface((0, 0))
        self.image = pygame.Surface(size)
        self.rect = self.image.get_rect(topleft=pos)
        self.hovered = False
        self.hover_effect_on = False

    def update(self):
        self.image.fill(self.color)
        if self.hovered and not self.hover_effect_on:
            self.image.fill(self.hover_effect, special_flags=pygame.BLEND_RGB_ADD)
            self.hover_effect_on = True
        elif not self.hovered:
            if self.hover_effect_on:
                self.hover_effect_on = False
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

    def draw(self, surface):
        pygame.draw.rect(surface, (0, 0, 0), (self.pos[0] - 1, self.pos[1] - 1, self.image.get_width() + 2, self.image.get_height() + 2), 1)
        surface.blit(self.image, self.rect)
        surface.blit(self.fontRender, self.rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            if self.rect.collidepoint(event.pos):
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                self.hovered = True
            else:
                self.hovered = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.onClick()

    def onClick(self):
        pass

    def moveTo(self, pos):
        self.pos = pos
        return self

    def resize(self, size: (int, int)):
        self.size = size
        self.fontRender = self.renderText()
        return self

    def setText(self, text: str):
        self.text = text
        self.fontRender = self.renderText()

    def resizeFont(self, size):
        self.font = pygame.font.SysFont(self.default_font, size)
        self.fontRender = self.renderText()

    def renderText(self):
        max_size = 20
        lower, upper = 0, self.size[1]
        while True:
            font = pygame.font.SysFont(self.default_font, max_size)
            size = font.size(self.text)

            if upper - lower <= 1:
                return font.render(self.text, False, self.fontColor)
            if size[0] <= self.size[0] and size[1] <= self.size[1]:
                lower = max_size
                max_size = (lower + upper) // 2
            else:
                upper = max_size
                max_size = (lower + upper) // 2

