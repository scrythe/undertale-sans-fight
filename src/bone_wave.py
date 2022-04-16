from pygame import Rect, sprite
from bone import Bone_Group, Bone_Bul
from typing import List


class Bone_Wave(Bone_Group):
    def __init__(self, battle_box: Rect):
        super().__init__(battle_box)
        amount_bones = 18
        bone_group_width = self.battle_box.width * 2
        max_height = self.battle_box.height - 50
        self.bone_group: sprite.Group = create_bone_wave(
            amount_bones, bone_group_width, battle_box, max_height, self.surface_rect).bone_group
        self.bone_group_sprites: List[Bone_Bul] = self.bone_group.sprites()
        self.draw_bones()


class create_bone_wave:
    def __init__(self, amount_bones, width, battle_box: Rect, max_height, surface_rect: Rect):
        self.bone_group = self.__create_bone_wave(amount_bones, width,
                                                  battle_box, max_height, surface_rect)

    def __create_bone_wave(self, amount_bones, width, battle_box: Rect, max_height, surface_rect):
        bone_group = sprite.Group()
        steps = width / (amount_bones - 1)
        default_rect_top = Bone_Bul().get_default_rect()
        default_rect_bottom = Bone_Bul().get_default_rect()
        default_rect_top.topright = battle_box.topright
        default_rect_bottom.bottomright = battle_box.bottomright
        top_shrinking = False
        current_height_top = max_height - 100
        current_height_bottom = max_height - current_height_top
        for index in range(amount_bones):
            bone_top, bone_bottom = self.__create_bone(current_height_top, current_height_bottom,
                                                       default_rect_top, default_rect_bottom, surface_rect)
            bone_group.add(bone_top)
            bone_group.add(bone_bottom)
            current_height_top, current_height_bottom = self.__update_bone_height(
                top_shrinking, current_height_top, current_height_bottom)
            top_shrinking = self.__check_height(
                current_height_top, current_height_bottom)
            default_rect_top, default_rect_bottom = self.__get_new_rect(steps,
                                                                        default_rect_top, default_rect_bottom, current_height_top, current_height_bottom, battle_box)
        return bone_group

    def __create_bone(self, current_height_top, current_height_bottom, default_rect_top: Rect, default_rect_bottom: Rect, surface_rect):
        bone_top = Bone_Bul(current_height_top,
                            (default_rect_top.x, default_rect_top.y))
        bone_bottom = Bone_Bul(current_height_bottom,
                               (default_rect_bottom.x, default_rect_bottom.y))
        bone_top.create_rect_inside_surf(surface_rect)
        bone_bottom.create_rect_inside_surf(surface_rect)
        return bone_top, bone_bottom

    def __update_bone_height(self, top_shrinking, current_height_top, current_height_bottom):
        if top_shrinking:
            current_height_top += 5
            current_height_bottom -= 5
        else:
            current_height_top -= 5
            current_height_bottom += 5
        return current_height_top, current_height_bottom

    def __check_height(self, current_height_top, current_height_bottom):
        if current_height_top <= 20:
            return True
        # only change state when EITHER of them exceed max_height
        elif current_height_bottom <= 20:
            return False

    def __get_new_rect(self, steps, default_rect_top: Rect, default_rect_bottom: Rect, current_height_top, current_height_bottom, battle_box):
        default_rect_top.x -= steps
        default_rect_bottom.x -= steps
        default_rect_top.height = current_height_top
        default_rect_bottom.height = current_height_bottom
        default_rect_top.top = battle_box.top
        default_rect_bottom.bottom = battle_box.bottom
        return default_rect_top, default_rect_bottom
