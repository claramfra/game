import pygame

class Mushroom(pygame.sprite.Sprite):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen

        # Background and floor variables
        self.mushroom_image = pygame.image.load("pilz.png").convert_alpha()
        self.mushroom_image = pygame.transform.scale(self.mushroom_image, (150, 150))
        self.mushroom = pygame.Rect(self.screen.get_width() - 200, 420, 50, 50)
        self.x = self.screen.get_width() - 200
        self.y = 420

    
    def draw(self):
        self.screen.blit(self.mushroom_image, (self.mushroom.x, self.mushroom.y))

    def move(self, dx, dir):
        if dir == "left":
            self.mushroom.x += dx
        elif dir == "right":
            self.mushroom.x -= dx