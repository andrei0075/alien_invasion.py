import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet


class AlienInvasion:

    def __init__(self):
        pygame.init()
        self.settings = Settings()
        #self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        #self.settings.screen_width = self.screen.get_rect().width
        #self.settings.screen_heigth = self.screen.get_rect().height - полноэкранный режим нужно поиграться.
        self.screen = pygame.display.set_mode((self.settings.screen_heigth, self.settings.screen_width))
        self.bg_color = self.settings.bg_color
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()



    def run_game(self):
        while True:
            self._check_events()
            self.ship.update()
            self._updte_sreen_()
            self.bullets.update()

    def _check_events(self):
        """Реагирует на нажатие клавиш и события мыши."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Реагирует на нажатие клавиш."""
        if event.key == pygame.K_RIGHT:
            self.ship.mov_rgth = True
        elif event.key == pygame.K_LEFT:
            self.ship.mov_lft = True
        elif event.key == pygame.K_DOWN:
            self.ship.mov_down = True
        elif event.key == pygame.K_UP:
            self.ship.mov_top = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _fire_bullet(self):
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)
    def _check_keyup_events(self, event):
        """Реагирует на отпускание клавиш."""
        if event.key == pygame.K_RIGHT:
            self.ship.mov_rgth = False
        elif event.key == pygame.K_LEFT:
            self.ship.mov_lft = False
        elif event.key == pygame.K_DOWN:
            self.ship.mov_down = False
        elif event.key == pygame.K_UP:
            self.ship.mov_top = False

    def _updte_sreen_(self):
        self.screen.fill(self.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
             bullet.draw_bullet()
        pygame.display.flip()  # last screen


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
