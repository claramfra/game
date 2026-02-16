import pygame

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720))
        self.clock = pygame.time.Clock()
        self.player_pos = pygame.Vector2(0, 600)
        self.running = True

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.screen.fill(("white"))  # Clear the screen with white
            pygame.draw.rect(self.screen, "black", pygame.Rect(0, 600, 1280, 120))  # Draw a black floor rectangle
            pygame.draw.circle(self.screen, "red", self.player_pos, 40)
            keys = pygame.key.get_pressed()
            dt = 0.1
            if keys[pygame.K_a]:
                self.player_pos.x -= 300 * dt
            if keys[pygame.K_d]:
                self.player_pos.x += 300 * dt
            pygame.display.flip()  # Update the display
            self.clock.tick(60)  # Limit to 60 frames per second
            self.screen.fill((255, 0, 0))  # Fill the screen with red

        pygame.quit()

Game().run()