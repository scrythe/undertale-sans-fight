from pygame import Rect
from bone import Bone_Group, Bone_Bul
from typing import List


class Bone_Wave(Bone_Group):
    def __init__(self, battle_box: Rect):
        super().__init__(battle_box)
        amount_bones = 18
        bone_group_width = self.battle_box.width * 2
        self.max_height = self.battle_box.height - 50
        self.create_bone_wave(amount_bones, bone_group_width)
        self.draw_bones()

    def create_bone_wave(self, amout_bones, width):
        steps = width / (amout_bones - 1)
        default_rect_top = Bone_Bul().get_default_rect()
        default_rect_bottom = Bone_Bul().get_default_rect()
        default_rect_top.topright = self.battle_box.topright
        default_rect_bottom.bottomright = self.battle_box.bottomright
        self.top_shrinking = False
        self.current_height_top = self.max_height - 100
        self.current_height_bottom = self.max_height - self.current_height_top
        for index in range(amout_bones):
            bone_top = Bone_Bul(self.current_height_top,
                                (default_rect_top.x, default_rect_top.y))
            bone_bottom = Bone_Bul(self.current_height_bottom,
                                   (default_rect_bottom.x, default_rect_bottom.y))
            bone_top.create_rect_inside_surf(self.surface_rect)
            bone_bottom.create_rect_inside_surf(self.surface_rect)
            self.bone_group.add(bone_top)
            self.bone_group.add(bone_bottom)
            default_rect_top.x -= steps
            default_rect_bottom.x -= steps
            self.change_bone_height()
            default_rect_top.height = self.current_height_top
            default_rect_bottom.height = self.current_height_bottom
            default_rect_top.top = self.battle_box.top
            default_rect_bottom.bottom = self.battle_box.bottom
        self.bone_group_sprites: List[Bone_Bul] = self.bone_group.sprites()

    def change_bone_height(self):
        if self.top_shrinking:
            self.current_height_top += 5
            self.current_height_bottom -= 5
            self.check_height()
        else:
            self.current_height_top -= 5
            self.current_height_bottom += 5
            self.check_height()

    def check_height(self):
        if self.current_height_top <= 20:
            self.top_shrinking = True
        # only change state when EITHER of them exceed max_height
        elif self.current_height_bottom <= 20:
            self.top_shrinking = False
