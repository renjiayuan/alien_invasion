class Settings:
    """存储游戏《外星人入侵》中所有设置的类的静态设置"""

    def __init__(self):
        """初始化游戏设置"""

        #屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)  

        #子弹设置
        self.ship_limit = 3  
        self.bullet_width = 1000
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        #外星人设置
        self.fleet_drop_speed = 10

        #加快游戏的进度
        self.speedup_scale = 1.1
        self.score_scale = 1.1
        self.bullet_scale = 1.1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """初始化随游戏进行而变化的设置"""
        self.ship_speed = 1.0
        self.bullet_speed = 1.0
        self.alien_speed = 1.0

        #fleet_direction为1表示向右移动，-1表示向左移动
        self.fleet_direction = 1

        #积分
        self.alien_points = 50

    def increase_speed(self):
        """提高速度设置和外星人的分数"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.bullet_width /= self.bullet_scale

        self.alien_points = int (self.alien_points * self.score_scale)