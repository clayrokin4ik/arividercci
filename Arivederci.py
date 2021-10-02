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
        self.walk_back_sprits, self.walk_front_spites = [], []
        self.walk_right_sprits, self.walk_left_sprites = [], []
        for i in range(4):
			self.walk_back_sprits.append(pygame.image.load(self.animal_type+'/'+self.animal_type+'_walk_back'+str(i+1)+'.png'))
			self.walk_front_spites.append(pygame.image.load(self.animal_type+'/'+self.animal_type+'_walk_front'+str(i+1)+'.png'))
			self.walk_right_sprits.append(pygame.image.load(self.animal_type+'/'+self.animal_type+'_walk_right'+str(i+1)+'.png'))
			self.self.walk_left_sprites.append(pygame.image.load(self.animal_type+'/'+self.animal_type+'_walk_left'+str(i+1)+'.png'))
