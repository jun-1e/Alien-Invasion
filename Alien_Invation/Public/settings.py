class Settings:
    def __init__(self):
        """初始化游戏设置"""
        self.Button_color_default = (255,191,0)
        self.Button_color_check = (141,105,0)
        self.color_RED = (255,0,0)
        self.color_dark_RED = (138,0,0)
        self.scorePad_width = 500
        self.scorePad_height = 40

        #游戏等级设置
        self.stage_score = {0:0,1:30,2:50,3:100,4:200,5:400,6:800,7:1500}
        ######speed_3_test
        self.stage_speed = {0:1,1:1,2:1.2,3:2,4:2.5,5:3,6:4,7:5.5} 
        self.aliens_life_incre = {0:1,1:1,2:2,3:3,4:4,5:5,6:6,7:7}

        #屏幕设置
        self.screen_width = 1600
        self.screen_height = 1000
        self.bg_color = (255,255,255) #设置背景颜色
        self.Pause_transparency = 128
        
        #飞船设置
        self.ship_speed = 20.0
        self.life_limit = 200
        self.PLB_width = 300
        self.PLB_height = 10

        ###子弹设置###
        self.bullet_speed = 10.0
        self.bullet_width =5
        self.bullet_height = 20
        self.bullet_color = (60,60,60)
        self.bullet_cooldown = 100
        self.bullets_allowed = 9999
            #跟踪子弹
        self.TrBul_speed = 10.0
        self.TrBul_width =5
        self.TrBul_height = 20
        self.TrBul_color = (60,60,60)
        self.TrBul_cooldown = 200

        ###外星人设置###
        self.aliens_allowed = 20
        self.create_max_attempts = 5
        self.alien_speed = 2.0
        self.enemy_bullet_damage = 1
        self.EnemyInvade_damage = 1
        self.crash_damage = 50
        self.spawn_timer_set = 20
        self.enemy_lfbar_width = 100
        self.enemy_lfbar_height = 5
            #shooter
        self.Shooter_cooldown = 100 

         