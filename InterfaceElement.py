from abc import ABC
import pygame


class InterfaceElement(ABC):
    def draw(self, surface: pygame.Surface):
        pass

    def handle_event(self, event: pygame.event.Event):
        pass

    def update(self):
        pass

