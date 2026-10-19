import pygame
from Public.settings import Settings

class game_stats:
    """管理游戏内数值变化的类"""
    def __init__(self,game):
        self.game = game
        self.plyship = game.playership
        self.setting = Settings()
        self.score = 0
        self.stage = 0
        self.high_score = 0

    def reset_game(self):
        """重置游戏"""
        if self.game.Dead:
            self.game.Dead = False
        if self.game.Pause:
            self.game.Pause = False
        self.game.game_stats.score = 0
        self.game.game_stats.stage = 0
        self.game.event.bg = self.game.prep_Pic.prep_bg(self.game.game_stats.stage)
        self.game.event.bg = pygame.transform.smoothscale(self.game.event.bg,
                                    (self.setting.screen_width, self.setting.screen_height))
        self.game.aliens_fleet.empty()
        self.plyship.life = 200
        self.plyship.rect.midbottom = self.plyship.screen_rect.midbottom
        self.plyship.x = float(self.plyship.rect.x)
        self.plyship.y = float(self.plyship.rect.y)
        
        