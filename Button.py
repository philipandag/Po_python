import pygame
from InterfaceElement import InterfaceElement


class Button(InterfaceElement):
    default_font = "consolas"
    def __init__(self, size: (int, int), pos: (int, int), text: str = ""):
        self.size: (int, int) = size
        self.pos: (int, int) = pos
        self.color = (200, 200, 200)
        self.hover_effect = (32, 32, 32)
        self.font = None
        self.text = None
        self.setText(text)
        fontsize = min(size[0], size[1])

        self.font = pygame.font.SysFont(Button.default_font, fontsize)
        self.image = pygame.Surface(size)
        self.rect = self.image.get_rect(topleft=pos)
        self.hovered = False
        self.hover_effect_on = False

    def update(self):
        if self.hovered and not self.hover_effect_on:
            self.image.fill(self.hover_effect, special_flags=pygame.BLEND_RGB_ADD)
            self.hover_effect_on = True
        elif self.hovered:
            pass
        else:
            self.image.fill(self.color)
            if self.hover_effect_on:
                self.hover_effect_on = False
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

    def draw(self, surface):
        pygame.draw.rect(surface, (0, 0, 0), (self.pos[0]-1, self.pos[1]-1, self.image.get_width() + 2, self.image.get_height() + 2), 1)
        surface.blit(self.image, self.rect)
        text = self.font.render(self.text, False, (0, 0, 0))
        text_centred_pos = (self.rect.centerx - text.get_rect().centerx, self.rect.centery - text.get_rect().centery)
        surface.blit(text, text_centred_pos)

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
        return self

    def setText(self, text: str):
        self.text = text
