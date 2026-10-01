import pygame

class prep_Pic:
    def __init__(self,ai_game):
        self.ai_game = ai_game
        self.screen = ai_game.screen
        #玩家图像
        self.player_img_ori = pygame.image.load('resource/Images/Big/ship_G.png').convert_alpha()
        #敌人图像
        self.shooter_img_ori = pygame.image.load('resource/Images/Big/enemy_C.png').convert_alpha()
        self.alien_img_ori = pygame.image.load('resource/Images/Big/enemy_D.png').convert_alpha()
        #背景图
        self.bg = {
            "0": pygame.image.load('resource/Images/BG/stage_1.jpg').convert_alpha(),
            "1": pygame.image.load('resource/Images/BG/stage_2.jpg').convert_alpha(),
            "2": pygame.image.load('resource/Images/BG/stage_3.jpg').convert_alpha(),
            "3": pygame.image.load('resource/Images/BG/stage_4.jpg').convert_alpha()
        }
        
        # self.bg_1 = pygame.image.load('resource/Images/BG/stage_1.png').convert_alpha()
        # self.bg_2 = pygame.image.load('resource/Images/BG/stage_2.png').convert_alpha()
        # self.bg_3 = pygame.image.load('resource/Images/BG/stage_3.png').convert_alpha()
        # self.bg_4 = pygame.image.load('resource/Images/BG/stage_4.png').convert_alpha()

    def prep_player(self):
        player_img = self.player_img_ori
        return player_img
    
    def prep_shooter(self):  
        shooter_img  = pygame.transform.flip(self.shooter_img_ori,False,True)
        return shooter_img

    def prep_alien(self):
        alien_img = pygame.transform.flip(self.alien_img_ori,False,True)
        return alien_img

    def prep_bg(self,stage):
        bg = self.bg[str(stage)]
        return bg
    