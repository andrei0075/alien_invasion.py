import pygame

class Ship():

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        self.image = pygame.image.load('image/1.bmp')
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.x =float(self.rect.x)
        self.y = float(self.rect.y)

        #флаг перемещения
        self.mov_rgth = False
        self.mov_lft = False
        self.mov_down = False
        self.mov_top = False

    def update(self):
        # обновляеться х(атрибут) - а не х
        if self.mov_rgth and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.mov_lft and  self.rect.left > 0:
            self.x -= self.settings.ship_speed
        if self.mov_top and self.rect.top > 0:
            self.y -= self.settings.ship_speed
        if self.mov_down and self.rect.top < (self.screen_rect.right - self.image.get_height()):
            self.y += self.settings.ship_speed

        self.rect.x  = self.x
        self.rect.y = self.y

    def blitme(self):
        self.screen.blit(self.image, self.rect)

