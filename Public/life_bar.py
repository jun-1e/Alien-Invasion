from Public.settings import Settings
from Events.prep_Pic import prep_Pic
import pygame

class Life_Bar:
    """关于血条的类"""
    def __init__(self,pos_x,pos_y,screen,rect_width,rect_height,lf_lim):
        self.settings = Settings()
        self.rect = pygame.Rect(pos_x,pos_y,rect_width,rect_height)
        self.current_rect = self.rect.copy()
        self.screen = screen
        self.lf_lim = lf_lim

        
    
    def draw_life_bar(self,color_bkg,color_frt,cur_lf):
        """绘制血条"""
        pygame.draw.rect(self.screen,color_bkg,self.rect)
        current_width =int(self.rect.width*(cur_lf/self.lf_lim))
        self.current_rect = (self.rect.x,self.rect.y,current_width,self.rect.height)
        pygame.draw.rect(self.screen,color_frt,self.current_rect)


