import pygame
from Public.settings import Settings
import pygame.font
class Button:
    def __init__(self,pos_x,pos_y,width,height,msg):
        self.setting = Settings()
        self.rect = pygame.Rect(pos_x,pos_y,width,height)
        self.text_color = (30,30,30)
        self.font = pygame.font.SysFont(None,48)
        self.prep_msg(msg)
        self.type = 1

    def button_events(self,button_color_default,button_color_check):
        """按钮行为"""
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.button_color = (button_color_check) 
        else:
            self.button_color = button_color_default

    
    def prep_msg(self,msg):
        """将msg渲染为图像并显示在按钮上"""
        self.msg_image = self.font.render(msg,True,self.text_color,
                                          None)
        self.msg_image_rect = self.msg_image.get_rect()
        
            
    def draw_button(self,ai_game):
        """绘制按钮"""
        pygame.draw.rect(ai_game.screen,self.button_color,self.rect)
        self.msg_image_rect.center = self.rect.center
        ai_game.screen.blit(self.msg_image,self.msg_image_rect)

    def check_restart(self,ai_game):
        """重新开始"""
        if  ai_game.restart_button.rect.collidepoint(ai_game.mouse_pos):
            ai_game.Dead = not ai_game.Dead
            ai_game.game_stats.reset_game()

    

        