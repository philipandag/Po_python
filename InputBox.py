import pygame


COLOR_INACTIVE = (220, 220, 220)
COLOR_ACTIVE = (50, 80, 200)

class InputBox:

    def __init__(self, x, y, w, h, title=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.font = pygame.font.SysFont('consolas', 32)
        self.color = COLOR_INACTIVE
        self.title = title
        self.text = ""
        self.txt_surface = self.font.render('', True, self.color)
        self.title_surface = self.font.render(self.title, True, (220, 220, 220))
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode

                self.txt_surface = self.font.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        # Blit the text.
        pygame.draw.rect(screen, (255, 255, 255), self.rect)
        pygame.draw.rect(screen, self.color, self.rect, 2)
        if len(self.text) == 0:
            screen.blit(self.title_surface, (self.rect.x+5, self.rect.y+5))
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
