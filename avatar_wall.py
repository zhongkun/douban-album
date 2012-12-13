# -*- coding: utf-8 -*-
'''
    created: 2012-12-06

                by 6a209
'''

import Image
import os
from random import choice

DEFAULT_WIDTH = 960
DEFAULT_HEIGHT = 960

# 48 * 48
DEFAULT_ITEM_COUNT = 400

class CompoundPicture:

    line_count = 20
    item_width = 48
    item_height = 48
    def compound_avatar(self, file_name):
        ''' 合并图片'''
        images = []
        files = os.listdir(file_name)
        new_file = 'compound.jpg'
        for file in files:
            if not 'jpg' in file:
                continue
            img = Image.open('%s%s' % (file_name, file))
            images.append(img)
        while len(images) != DEFAULT_ITEM_COUNT:
            item = self.get_radom_not_repeat(images)
            images.append(item)
        new_image = Image.new('RGB', (DEFAULT_WIDTH, DEFAULT_HEIGHT), 0xffffff)
        for i in range(len(images)):
            image = images[i]
            x = i % self.line_count
            y = i / self.line_count
            x = x * self.item_width
            y = y * self.item_height
            new_image.paste(image, (x, y))
        new_image.save(file_name + new_file, quality = 70)

    def compound_user_avatar(self, file_name):
        self.compound_avatar(file_name)

    def download_user_avatar(user_list):
        pass

    def get_radom_not_repeat(self, image_list):
        item = choice(image_list)
        length = len(image_list)
        if length < self.line_count:
            return item
        top_item = image_list[length - self.line_count]
        # 左边缘
        if 0 == length % self.line_count:
           left_item = None
           left_top_item = None
        else:
           left_item = image_list[length - 1]
           left_top_item = image_list[length - 1 - self.line_count]
        # 右边缘
        if self.line_count - 1 == length % self.line_count:
            right_top_item = None
        else:
            right_top_item = image_list[length - self.line_count + 1]

        # 不重复!
        while item == top_item \
            or item == left_top_item \
            or item == left_item \
            or item == right_top_item:
            item = choice(image_list)
        return item

#compound_avatar('/Users/kun/Desktop/avatar/')
