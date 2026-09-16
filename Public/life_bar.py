from Public.settings import Settings
import pygame

class Life_Bar:
    """关于血条的类"""
    def __init__(self,pos_x,pos_y,screen,rect_width,rect_height,life_limit):
        self.settings = Settings()
        self.rect = pygame.Rect(pos_x,pos_y,rect_width,rect_height)
        self.current_rect = self.rect.copy()
        self.screen = screen
        self.life_limit = life_limit
        
    
    def draw_life_bar(self,color_bkg,color_frt,current_life):
        """绘制血条"""
        pygame.draw.rect(self.screen,color_bkg,self.rect)
        current_width =int(self.rect.width*(current_life/self.life_limit))
        self.current_rect = (self.rect.x,self.rect.y,current_width,self.rect.height)
        pygame.draw.rect(self.screen,color_frt,self.current_rect)


