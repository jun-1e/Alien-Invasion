import pygame
from Public.settings import Settings
import pygame.font

class Button:
    def __init__(self,rect_ctx,rect_cty,width,height,msg,game):
        #位置
        self.setting = Settings()
        self.rect = pygame.Rect(0,0,width,height)
        self.rect.centerx = rect_ctx
        self.rect.centery = rect_cty
        self.rect_tmp = pygame.Rect(0,0,width,height)
        self.rect_tmp.centerx = rect_ctx
        self.rect_tmp.centery = rect_cty
        #字体
        self.tex_col = (30,30,30)
        self.font = pygame.font.SysFont(None,48)
        self.prep_msg(msg)
        #按钮图像
        self.btn_img = game.prep_Pic.prep_button(width,height)
        self.btn_img.fill((200,200,200), special_flags=pygame.BLEND_RGB_MULT)
        self.btn_img = self.btn_img.copy()
        self.btn_img_copy = self.btn_img.copy()
        self.btn_img_copy.fill((160,160,160), special_flags=pygame.BLEND_RGB_MULT)

    def button_events(self):
        """按钮行为"""
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.btn_img = self.btn_img_copy
            self.rect.centery = self.rect_tmp.centery + 1
        else:
            self.btn_img = self.btn_img
            self.rect.centery = self.rect_tmp.centery
    
    def prep_msg(self,msg):
        """将msg渲染为图像并显示在按钮上"""
        self.msg_img = self.font.render(msg,True,self.tex_col,
                                          None)
        self.msg_img_rect = self.msg_img.get_rect()
        
            
    def draw_button(self,game):
        """绘制按钮"""       
        game.screen.blit(self.btn_img,self.rect)
        self.msg_img_rect.center = self.rect.center
        game.screen.blit(self.msg_img,self.msg_img_rect)

    def check_restart(self,game):
        """重新开始"""
        if  game.restart_button.rect.collidepoint(game.mouse_pos):
            game.Dead = not game.Dead
            game.game_stats.reset_game()

    

        