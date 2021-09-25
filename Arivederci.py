import pygame 
class Chel0(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        self.walk_back_animation = False
        self.walk_front_animation = False 
        self.walk_right_animation = False 
        self.walk_left_animation = False
        self.x_speed = 0
        self.y_speed = 0
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.speed = 3
        self.walk_back_sprits, self.walk_front_spites = [chel_22!,chel_6,chel_10,chel_15], [chel0,chel_4,chel_8,chel_13]
        self.walk_right_sprits, self.walk_left_sprites = [chel_3,chel_7,chel_11,], []
