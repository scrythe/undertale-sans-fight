from pygame import Rect
from bone import Bone_Group


class Bone_Wall(Bone_Group):
    def __init__(self, battle_box: Rect):
        super().__init__(battle_box)
        self.amount_bones = 14
        self.bone_group_width = self.battle_box.width
        self.max_height = self.battle_box.height / 1.5
        self.attack_speed = 8
        super().create_bone_wall(self.amount_bones, self.bone_group_width)
        self.attack_state = False

    def start_attack(self):
        self.attack_state = True

    def check_end_of_attack(self):
        first_bone = self.bone_group_sprites[0]

        if first_bone.get_coords_inside_surf(self.surface_rect)[1] <= self.max_height:
            return True

    def attack(self):
        if self.attack_state:
            if not self.check_end_of_attack():
                self.go_upwards()
                self.draw_bones()
            else:
                self.attack_state = False

    def go_upwards(self):
        for bone in self.bone_group_sprites:
            bone.rect.y -= self.attack_speed

    def update(self):
        self.attack()
