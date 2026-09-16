import pygame.font
class Scoreboard:
    """显示得分信息的类"""
    def __init__(self,ai_game):
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        self.stats = ai_game.game_stats
        self.stage = self.stats.stage
        #字体设置
        self.text_color = (30,30,30)
        self.font = pygame.font.SysFont(None,48)
        self.prep_score()
        self.prep_highscore()
        self.prep_stage()

    def prep_score(self):
        """将得分渲染为图像"""
        rounded_score = round(self.stats.score,-1)
        score_str = f"{rounded_score:,}"
        self.score_image = self.font.render(score_str,True,self.text_color,None)
        #在屏幕右上角显示评分
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
    
    def prep_highscore(self):
        """将最高分渲染为图像"""
        high_score = round(self.stats.high_score,-1)
        high_score_str = f"{high_score:,}"
        self.high_score_image = self.font.render(high_score_str,True,self.text_color,None)
        #将最高分放在屏幕顶端
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top
    
    def prep_stage(self):
        """将游戏等级渲染为图像"""
        cur_stage = self.stats.stage
        cur_stage_str = f"stage  {cur_stage}"
        self.cur_stage_image = self.font.render(cur_stage_str,True,self.text_color,None)
        #将游戏等级放在得分下方
        self.cur_stage_rect = self.cur_stage_image.get_rect()
        self.cur_stage_rect.right = self.screen_rect.right-20
        self.cur_stage_rect.top = self.score_rect.bottom
        
    def show_score(self):
        """绘制玩家得分"""
        self.screen.blit(self.score_image,self.score_rect)
        self.screen.blit(self.cur_stage_image,self.cur_stage_rect)
        self.screen.blit(self.high_score_image,self.high_score_rect)