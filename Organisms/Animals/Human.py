import pygame

from Organisms.Animals.Animal import Animal


class Human(Animal):
    NAME = "Human"
    SYMBOL = "H"
    ABILITY_COLOR = (255, 50, 255)
    COOLDOWN_COLOR = (70, 50, 70)
    COLOR = (180, 20, 180)
    STRENGTH = 5
    INITIATIVE = 4
    ABILITY_COOLDOWN = 5
    ABILITY_BONUS = 5

    def __init__(self):
        super(Human, self).__init__(Human.NAME, Human.SYMBOL, Human.COLOR, Human.STRENGTH, Human.INITIATIVE)
        self.direction = None
        self.ability_bonus_strength = 0
        self.ability_cooldown = 0

    def set_world(self, world):
        if self.world is not None:
            self.world.remove_listener(self)
        self.world = world
        self.world.add_listener(self)
        self.direction = self.world.get_direction()()

    def action(self):
        delta = self.direction.delta()
        pos = (self.pos[0] + delta[0], self.pos[1] + delta[1])
        if self.get_board().onBoard(pos):
            self.try_to_move_to(pos)
        self.special_ability_tick()

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP):
                self.direction.key_to_dir(event.key)
            elif event.key == pygame.K_q:
                self.special_ability()


    def special_ability(self):
        if self.ability_cooldown == 0:
            self.ability_bonus_strength = self.ABILITY_BONUS
            self.ability_cooldown = self.ABILITY_COOLDOWN
            print(self.get_name(), self.pos, "uses magic potion, strength=", self.get_strength())
        else:
            print(self.get_name(), self.pos, "cant use ability for", (self.ability_bonus_strength + self.ability_cooldown), "turns, strength=", self.get_strength())

    def special_ability_tick(self):
        if self.ability_bonus_strength > 0:
            self.ability_bonus_strength -= 1
        elif self.ability_cooldown > 0:
            self.ability_cooldown -= 1

    def get_strength(self):
        return self.strength + self.ability_bonus_strength

    def get_colour(self):
        if self.ability_bonus_strength > 0:
            return self.ABILITY_COLOR
        elif self.ability_cooldown > 0:
            return self.COOLDOWN_COLOR
        else:
            return self.color
