import pygame
from Public.settings import Settings

class game_stats:
    """管理游戏内数值变化的类"""
    def __init__(self,ai_game):
        self.ai_game = ai_game
        self.playership = ai_game.playership
        self.setting = Settings()
        self.score = 0
        self.stage = 0
        self.high_score = 0

    def reset_game(self):
        """重置游戏"""
        if self.ai_game.Dead:
            self.ai_game.Dead = False
        if self.ai_game.Pause:
            self.ai_game.Pause = False
        self.ai_game.game_stats.score = 0
        self.ai_game.game_stats.stage = 0
        self.playership.life = 200
        self.playership.rect.midbottom = self.playership.screen_rect.midbottom
        self.playership.x = float(self.playership.rect.x)
        self.playership.y = float(self.playership.rect.y)
        print("321")
        
        