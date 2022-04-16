from pygame import Rect, sprite
from bone import Bone_Group, Bone_Stab
from typing import List


class Bone_Stab_Wide(Bone_Group):
    def __init__(self, battle_box: Rect):
        super().__init__(battle_box)
        amount_bones = 14
        bone_group_width = self.battle_box.width
        self.max_attack_height = self.battle_box.height / 3
        self.attack_speed = 8
        self.bone_group = create_bone_wave(
            amount_bones, bone_group_width, self.battle_box, self.surface_rect).bone_group
        self.bone_group_sprites: List[Bone_Stab] = self.bone_group.sprites()
        self.attack_state = False

    def go_upwards(self):
        for bone in self.bone_group_sprites:
            bone.go_upwards(self.attack_speed)

    def attack(self):
        if self.attack_state:
            if not self.check_end_of_attack():
                self.go_upwards()
                self.draw_bones()
            else:
                self.attack_state = False

    def check_end_of_attack(self):
        current_height_of_attack = self.get_distance_from_bottom()
        if current_height_of_attack >= self.max_attack_height:
            return True
        return False

    def start_attack(self):
        self.attack_state = True

    def check_if_hit(self, player: sprite.Sprite):
        hit_bone_rect = sprite.spritecollide(player, self.bone_group, False)
        if hit_bone_rect:
            pixel_perfect_hit = sprite.spritecollide(
                player, self.bone_group, False, sprite.collide_mask)
            return pixel_perfect_hit
        return False

    def update(self):
        self.attack()


class create_bone_wave():
    def __init__(self, amount_bones, width, battle_box: Rect, surface_rect: Rect):
        self.bone_group: sprite.Group = self.__create_bone_wall(
            amount_bones, width, battle_box, surface_rect)

    def __create_bone_wall(self, amount_bones, width, battle_box: Rect, surface_rect: Rect):
        bone_group = sprite.Group()
        steps = width / (amount_bones - 1)
        default_rect = Bone_Stab().get_default_rect()
        default_rect.midtop = battle_box.bottomleft
        for index in range(amount_bones):
            bone = Bone_Stab((default_rect.x, default_rect.y))
            bone.create_rect_inside_surf(surface_rect)
            bone_group.add(bone)
            default_rect.x += steps
        return bone_group
