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

        #флаг перемещения
        self.mov_rgth = False
        self.mov_lft = False

    def update(self):
        # обновляеться х(атрибут) - а не х
        if self.mov_rgth and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.mov_lft and  self.rect.left > 0:
            self.x -= self.settings.ship_speed
#обновление атрибутов на основании селф х
        self.rect.x  = self.x

    def blitme(self):
        self.screen.blit(self.image, self.rect)


    ''' Загружает корабль '''
