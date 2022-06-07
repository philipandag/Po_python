import pygame
from InterfaceElement import InterfaceElement


class Button(InterfaceElement):
    default_font = "consolas"

    def __init__(self, size: (int, int), pos: (int, int), text: str = ""):
        self.needs_redraw = True
        self.size: (int, int) = size
        self.pos: (int, int) = pos
        self.color = (240, 240, 240)
        self.fontColor = (0, 0, 0)
        self.hover_effect = (32, 32, 32)
        self.text = text
        self.fontSize = 30
        self.font = pygame.font.SysFont(self.default_font, self.fontSize)
        if text != "":
            self.fontRender = self.renderText()
        else:
            self.fontRender = pygame.Surface((0, 0))
        self.image_normal, self.image_hover = self.create_images()
        self.image = self.image_normal
        self.rect = self.image.get_rect(topleft=pos)
        self.hovered = False
        self.hover_effect_on = False
        self.onClickFunction = None

    def update(self):
        if self.hovered:
            self.image = self.image_hover
        elif self.image == self.image_hover:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
            self.image = self.image_normal
        else:
            self.image = self.image_normal

    def setHoverEffect(self, flag):
        self.hovered = flag
        self.needs_redraw = True

    def onMouseOver(self):
        if not self.hovered:
            self.needs_redraw = True
        self.hovered = True
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)


    def onMouseLeave(self):
        self.needs_redraw = True
        self.hovered = False


    def draw(self, surface):
        if self.needs_redraw:
            surface.blit(self.image, (self.pos[0] + 1, self.pos[1] + 1, self.image.get_width() - 1, self.image.get_height() - 1))
            pygame.draw.rect(surface, (0, 0, 0), (self.pos[0], self.pos[1], self.image.get_width() + 1, self.image.get_height() + 1), 1)
            surface.blit(self.fontRender, (self.pos[0] + (self.size[0] - self.fontRender.get_size()[0])//2,  self.pos[1] + (self.size[1] - self.fontRender.get_size()[1])//2))
            self.needs_redraw = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            if self.collides(event.pos):
                self.onMouseOver()
            elif self.hovered:
                self.onMouseLeave()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if self.collides(event.pos):
                self.onClick()

    def collides(self, pos):
        return self.rect.collidepoint(pos)

    def onClick(self):
        if self.onClickFunction is not None:
            self.onClickFunction()

    def moveTo(self, pos):
        self.pos = pos
        self.needs_redraw = True
        return self

    def resize(self, size: (int, int)):
        self.size = size
        self.fontRender = self.renderText()
        self.needs_redraw = True
        return self

    def setText(self, text: str):
        self.text = text
        self.fontRender = self.renderText()
        self.needs_redraw = True

    def resizeFont(self, size):
        self.font = pygame.font.SysFont(self.default_font, size)
        self.fontRender = self.renderText()
        self.needs_redraw = True

    def renderText(self):
        max_size = 20
        lower, upper = 0, int(self.size[1])
        while True:
            font = pygame.font.SysFont(self.default_font, int(max_size))
            size = font.size(self.text)

            if upper - lower <= 1:
                return font.render(self.text, False, self.fontColor)
            if size[0] <= self.size[0] and size[1] <= self.size[1]:
                lower = max_size
                max_size = (lower + upper) // 2
            else:
                upper = max_size
                max_size = (lower + upper) // 2

    def set_color(self, color):
        self.color = color
        self.image_normal.fill(color)
        self.image_hover.fill(color)
        self.image_hover.fill(self.hover_effect, special_flags=pygame.BLEND_RGB_ADD)

    def setOnClick(self, function):
        self.onClickFunction = function
        return self

    def toggle_needs_redraw(self):
        self.needs_redraw = True

    def create_images(self) -> (pygame.Surface, pygame.Surface):
        image_normal = pygame.Surface(self.size)
        image_normal.fill(self.color)
        image_hover = pygame.Surface(self.size)
        image_hover.fill(self.color)
        image_hover.fill(self.hover_effect, special_flags=pygame.BLEND_RGB_ADD)

        return image_normal, image_hover

