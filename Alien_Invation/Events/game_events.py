import pygame
from enemy.aliens import Alien
from enemy.shooter import Shooter
from Public.scoreboard import Scoreboard
from random import randint
from Public.button import Button

class Game_Events:
     def __init__(self,ai_game):
        self.ai_game = ai_game
        self.settings = ai_game.game_stats.setting       
        self.screen = ai_game.screen
        self.alien = Alien(self.ai_game)
        self.randint = randint
        self.aliens_fleet = ai_game.aliens_fleet
        self.playership = ai_game.playership
        self.game_stats = ai_game.game_stats
        self.scoreboard = Scoreboard(self.ai_game)        
        self.p_life_bar = self.playership.life_bar
        
     def get_spawn_loc(self,alien_type):
         """获得新创建的外星人位置"""
         alien_type.rect.x = self.randint(0,self.settings.screen_width-alien_type.rect.width)
         alien_type.rect.y = 0 

    
     def check_score(self):
        """检查玩家得分是否满足阶段要求"""
        if self.game_stats.score >= self.settings.stage_score[self.game_stats.stage+1]:
            self.game_stats.stage+=1
            self.scoreboard.prep_stage()
            print(f"stage up!{self.game_stats.stage}")
            
                 
     def _create_fleet(self):
        """创建外星人群"""
        #根据run_game循环次数创建一个外星人，并受到最大数量限制
        self.ai_game.spawn_timer+=(10*self.settings.stage_speed.get(self.game_stats.stage))
        if self.ai_game.spawn_timer >= self.settings.spawn_timer_set*50:            
            if len(self.aliens_fleet) < self.settings.aliens_allowed:            
                for times in range(self.settings.create_max_attempts):
                    #每个外星人都出现在屏幕最上方随机位置
                    alien_type = randint(0,1)
                    if alien_type:
                        alien = Alien(self.ai_game)
                        self.get_spawn_loc(alien)
                    else:
                        alien = Shooter(self.ai_game)
                        self.get_spawn_loc(alien)
                    #新创建的外星人不会与目前已有的外星人重叠
                    if not any(alien.rect.colliderect(existing_alien.rect) 
                            for existing_alien in self.aliens_fleet):
                        alien.maxlife *= self.settings.aliens_life_incre[self.game_stats.stage]  
                        alien.life_bar.life_limit = alien.maxlife
                        alien.life = alien.maxlife                  
                        self.aliens_fleet.add(alien)
                        break
            self.ai_game.spawn_timer = 0

     def _check_collisions(self):
        """检查外星人碰撞相关信息"""        
        # 碰撞检测，删除子弹和被击中的外星人
        collisions = pygame.sprite.groupcollide(
            self.playership.bullets, self.aliens_fleet,True,False)
        if collisions:
            total_score = 0
            for bullet, aliens in collisions.items():
                for alien in aliens:                   
                    alien.life-=1
                    if alien.life<=0:
                        alien.kill() 
                        total_score += alien.score  
                self.game_stats.score += total_score
                self.scoreboard.prep_score()
        #检查外星人和墙壁碰撞
        for alien in self.aliens_fleet.copy():
            if alien.rect.bottom >= self.ai_game.screen.get_rect().bottom+20:
                self.ai_game.playership.life -= self.settings.EnemyInvade_damage
                alien.kill()
                #如果外星人碰到侧面的墙壁则则改变水平运动方向
            if (alien.rect.right >= self.screen.get_rect().right+20 or 
                alien.rect.left <= self.screen.get_rect().left-20):
                alien.xdirection *= -1
                break
        #检查外星人和飞船碰撞
        for alien in self.aliens_fleet.copy():
            if alien.rect.colliderect(self.playership.rect):
                self.playership.life -= self.settings.crash_damage
                alien.kill()
        #检查Shooter型外星人的子弹与玩家飞船的碰撞
        for alien in self.aliens_fleet.sprites():
            if type(alien) == Shooter:
                for bullet in alien.bullets.sprites():
                    if bullet.rect.colliderect(self.playership.rect):
                        self.playership.life -= 5
                        bullet.kill()
    
     def check_life_change(self):
        """检查玩家生命值变化"""    
        if self.playership.life <= 0:
            self.ai_game.Dead = True 

     def update_screen(self):
        """绘制屏幕"""
        #Shooter类敌人发射子弹
        for alien in self.aliens_fleet.copy():
            if type(alien) == Shooter:
                alien.shoot()
        self.screen.fill(self.settings.bg_color)
        #绘制子弹
        for bullet in self.playership.bullets.sprites():
            bullet.draw_player_bullet()
                
        #绘制外星人          
        for alien in self.aliens_fleet.sprites():
            alien.draw_alien()
            alien.life_bar.rect.top = alien.rect.bottom
            alien.life_bar.rect.left = alien.rect.left
            alien.life_bar.draw_life_bar(self.settings.color_dark_RED,self.settings.color_RED,alien.life) 
            if type(alien) == Shooter:                
                for bullet in alien.bullets.sprites():
                    bullet.update()
                    bullet.draw_Hbullet() 
        #绘制玩家飞船和血量    
        self.playership.blitme()
        self.p_life_bar.draw_life_bar(self.settings.color_dark_RED,self.settings.color_RED,self.playership.life)
        self.scoreboard.show_score()  
             
     def draw_pause_lay(self):
         """绘制暂停界面"""
         while self.ai_game.transparency_count < self.settings.Pause_transparency:
            overlay = pygame.Surface((self.settings.screen_width,self.settings.screen_height),
                                    pygame.SRCALPHA)
            overlay.fill((0,0,0,2))
            self.screen.blit(overlay,(0,0))
            pygame.display.flip()
            self.ai_game.transparency_count+=1

     def create_button(self):
         """创建游戏功能按钮"""
         self.ai_game.pause_button = Button(400,250,400,250,'continue')
         self.ai_game.pause_button.rect.centerx = self.screen.get_rect().width*1/3
         self.ai_game.pause_button.rect.centery = self.screen.get_rect().height/2
         self.ai_game.start_button = Button(600,400,200,150,'start')
         self.ai_game.start_button.rect.center = self.screen.get_rect().center
         self.ai_game.restart_button = Button(600,400,200,150,'restart')
         self.ai_game.restart_button.rect.center = self.screen.get_rect().center
         self.ai_game.restart_button.type = 2
            
         