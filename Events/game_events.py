import pygame
from enemy.aliens import Alien
from enemy.shooter import Shooter
from random import randint
import json
from Public.button import Button

class Game_Events:
     def __init__(self,game):
        self.game = game
        self.gm_sts = game.game_stats
        self.setting = self.gm_sts.setting       
        self.screen = game.screen
        self.alien = Alien(self.game)
        self.randint = randint
        self.alns_flt = game.aliens_fleet
        self.pship = game.playership      
        self.scboard = game.scoreboard       
        self.p_lfb = self.pship.life_bar
        self.bg_ori = self.game.prep_Pic.prep_bg(self.gm_sts.stage)
        self.bg = pygame.transform.smoothscale(self.bg_ori,
                                     (self.setting.screen_width, self.setting.screen_height))
         
        
     def get_spawn_loc(self,alien_type):
         """获得新创建的外星人位置"""
         alien_type.rect.x = self.randint(0,self.setting.screen_width-alien_type.rect.width)
         alien_type.rect.y = 0 

    
     def check_score(self):
        """检查玩家得分是否满足阶段要求"""
        if self.gm_sts.score >= self.setting.stage_score[self.gm_sts.stage+1]:
            self.gm_sts.stage+=1
            self.bg = self.game.prep_Pic.prep_bg(self.gm_sts.stage)
            self.bg = pygame.transform.smoothscale(self.bg,
                                    (self.setting.screen_width, self.setting.screen_height))
            self.bg.set_alpha(0)
            pygame.display.flip()
            print(f"stage up!{self.gm_sts.stage}")
        if self.gm_sts.score > self.gm_sts.high_score:
            self.gm_sts.high_score = self.gm_sts.score
            
                            
     def _create_fleet(self):
        """创建外星人群"""
        #根据run_game循环次数创建一个外星人，并受到最大数量限制
        self.game.spawn_timer+=(10*self.setting.stage_speed.get(self.gm_sts.stage))
        if self.game.spawn_timer >= self.setting.spawn_timer_set*50:            
            if len(self.alns_flt) < self.setting.aliens_allowed:            
                for times in range(self.setting.create_max_attempts):
                    #每个外星人都出现在屏幕最上方随机位置
                    alien_type = randint(0,1)
                    if alien_type:
                        alien = Alien(self.game)
                        self.get_spawn_loc(alien)
                    else:
                        alien = Shooter(self.game)
                        self.get_spawn_loc(alien)
                    #新创建的外星人不会与目前已有的外星人重叠
                    if not any(alien.rect.colliderect(existing_alien.rect) 
                            for existing_alien in self.alns_flt):
                        alien.maxlife *= self.setting.aliens_life_incre[self.gm_sts.stage]  
                        alien.life_bar.life_limit = alien.maxlife
                        alien.life = alien.maxlife                  
                        self.alns_flt.add(alien)
                        break
            self.game.spawn_timer = 0

     def _check_collisions(self):
        """检查外星人碰撞相关信息"""        
        # 碰撞检测，删除子弹和被击中的外星人
        collisions = pygame.sprite.groupcollide(
            self.pship.bullets, self.alns_flt,True,False)
        if collisions:
            total_score = 0
            for bullet, aliens in collisions.items():
                for alien in aliens:                   
                    alien.life-=1
                    if alien.life<=0:
                        alien.kill() 
                        total_score += alien.score  
                self.gm_sts.score += total_score
                
        #检查外星人和墙壁碰撞
        for alien in self.alns_flt.copy():
            if alien.rect.bottom >= self.game.screen.get_rect().bottom+20:
                self.pship.life -= self.setting.EnemyInvade_damage
                alien.kill()
                #如果外星人碰到侧面的墙壁则则改变水平运动方向
            if (alien.rect.right >= self.screen.get_rect().right+20 or 
                alien.rect.left <= self.screen.get_rect().left-20):
                alien.xdirection *= -1
                break
        #检查外星人和飞船碰撞
        for alien in self.alns_flt.copy():
            if alien.rect.colliderect(self.pship.rect):
                self.pship.life -= self.setting.crash_damage
                alien.kill()
        #检查Shooter型外星人的子弹与玩家飞船的碰撞
        for alien in self.alns_flt.sprites():
            if type(alien) == Shooter:
                for bullet in alien.bullets.sprites():
                    if bullet.rect.colliderect(self.pship.rect):
                        self.pship.life -= 5
                        bullet.kill()
    
     def check_life_change(self):
        """检查玩家生命值变化"""    
        if self.pship.life <= 0:
            self.game.Dead = True 

     def update_screen(self):
        """绘制屏幕"""
        self.screen.fill((100,100,100))
        self.screen.blit(self.bg,(0,0))
        if self.bg.get_alpha() < 175 :    
            self.bg.set_alpha(self.bg.get_alpha()+3)

        self.scboard.prep_score()
        self.scboard.prep_stage()
        #Shooter类敌人发射子弹
        for alien in self.alns_flt.copy():
            if type(alien) == Shooter:
                alien.shoot()
        #绘制子弹
        for bullet in self.pship.bullets.sprites():
            bullet.draw_player_bullet()
                
        #绘制外星人          
        for alien in self.alns_flt.sprites():
            alien.draw_alien()
            alien.life_bar.rect.midtop = alien.rect.midbottom
            alien.life_bar.draw_life_bar(self.setting.DARK_RED,self.setting.RED,alien.life) 
            if type(alien) == Shooter:                
                for bullet in alien.bullets.sprites():
                    bullet.update()
                    bullet.draw_Hbullet() 
        #绘制玩家飞船和血量    
        self.pship.blitme()
        self.p_lfb.draw_life_bar(self.setting.DARK_RED,self.setting.RED,self.pship.life)
        #self.screen.blit(self.game.prep_Pic.prep_lfb_tex(),self.p_lfb.rect)血条纹理
        self.scboard.show_score()
        pygame.display.flip()

             
     def draw_pause_lay(self):
         """绘制暂停界面"""
         while self.game.transparency_count < self.setting.Pause_transparency:
            overlay = pygame.Surface((self.setting.screen_width,self.setting.screen_height),
                                    pygame.SRCALPHA)
            overlay.fill((0,0,0,2))
            self.screen.blit(overlay,(0,0))
            pygame.display.flip()
            self.game.transparency_count+=1

     def create_button(self):
         """创建游戏功能按钮"""
         #继续游戏按钮
         self.game.pause_button = Button(self.screen.get_rect().width*1/3,
                                            self.screen.get_rect().height/2,
                                            400,250,'continue',self.game)
         #开始游戏按钮
         self.game.start_button = Button(self.screen.get_rect().centerx,
                                            self.screen.get_rect().centery,
                                            600,75,'New Game',self.game) 
         #生命值耗尽界面的重新开始按钮
         self.game.restart_button = Button(self.screen.get_rect().centerx,
                                              self.screen.get_rect().centery,
                                              200,150,'restart',self.game)
         #暂停界面的restart按钮
         self.game.restart_button2 = Button(self.screen.get_rect().width*2/3,
                                               self.screen.get_rect().height/2,
                                               400,250,'restart',self.game)

     def save_game(self):
         """保存游戏"""
         data = {
            "highscore" : self.gm_sts.high_score,
            #"stage" : self.game.game_stats.stage,
            #"score" : self.ai_gae.game_stats.score,
         }
         with open("savefile.json","w") as file:
             json.dump(data,file,indent=4)

     def load_game(self):
         """读取游戏"""
         with open("savefile.json","r") as file:
             data = json.load(file)
         self.gm_sts.high_score = data["highscore"]

            
         