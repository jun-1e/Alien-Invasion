import pygame
import sys
from Public.settings import Settings
from player_ship import Ship
from Events.hardware_event import Hardware_Event
from Events.game_events import Game_Events
from Public.button import Button
from Public.Game_Stats import game_stats

class AlienInvasion:
    """管理游戏资源和行为类"""
    def __init__(self):
        """初始化游戏并创建游戏资源"""
        pygame.init()       
        self.transparency_count = 0
        self.spawn_timer = 0
        self.clock = pygame.time.Clock()
        self.settings = Settings()     
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("gametest")

        #初始化游戏内容
        self.Active = False
        self.Pause = False
        self.Dead = False
        self.shooting = False
        self.bullets = pygame.sprite.Group()
        self.aliens_fleet = pygame.sprite.Group()
        self.playership = Ship(self)
        self.game_stats = game_stats()
        self.event = Game_Events(self)        
        self.hardware_event = Hardware_Event(self)
        self.event.create_button()
                        
    def run_game(self):
        """开始游戏主循环"""
        while True:
            """游戏开始前进行事件检测"""
            self.screen.fill(self.settings.bg_color)
            self.start_button.button_events((0,142,255),(0,76,136))
            
            self.start_button.draw_button(self)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    #点击开始按钮开始游戏
                    if  self.start_button.rect.collidepoint(mouse_pos):
                        self.Active = True
            if self.Active: 
                break
            pygame.display.flip()    
            self.clock.tick(60)
                   
        while self.Active:
            ##检查游戏是否处于运行状态，是则检查键盘鼠标行为及玩家生命
            self.hardware_event.check_events()
            self.event.check_life_change() 

            if not self.Dead:
                if not self.Pause:
                    #检查同时满足玩家没有死亡和游戏不处于暂停后,游戏进行                           
                    self.playership.update()
                    self.playership.fire_bullet()
                    self.playership.update_bullet()
                    self.event._check_collisions()
                    self.event._create_fleet()
                    self.aliens_fleet.update()
                    self.event.check_score()
                    self.event.update_screen()                                    
                elif self.Pause:
                    #绘制暂停页面                    
                        self.event.draw_pause_lay()   
                        self.pause_button.button_events((255,191,0),(141,105,0))
                        self.pause_button.draw_button(self) 
                        #self.restart_button.button_events((0,0,0),(0,0,0)) 暂停页面的重新开始游戏按钮                      
            elif self.Dead:
                #更新最高分数
                if self.game_stats.score>self.game_stats.high_score:
                    self.game_stats.high_score=self.game_stats.score
                    self.event.scoreboard.prep_highscore()
                #背景逐渐变暗效果    
                while self.transparency_count < self.settings.Pause_transparency:
                    self.event.draw_pause_lay()
                    self.transparency_count+=1
                #重新开始按钮
                    self.restart_button.button_events((255,191,0),(141,105,0))
                    self.restart_button.draw_button(self)
                    
            pygame.display.flip()    
            self.clock.tick(60)
            
if __name__ == '__main__':
    #创建游戏实例并运行游戏
    ai=AlienInvasion()
    ai.run_game()