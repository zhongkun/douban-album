# -*- coding:utf8 -*-

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



def compound_avatar(files, new_file):
    
    ''' 合并图片'''
    images = []
    item_width = 48
    item_height = 48
    
    for file in files:
        img = Image.open('img/%s' % file)
        images.append(img)
    image_count = len(images)
    while image_count != DEFAULT_ITEM_COUNT:
        images.append(choice(images))
    new_image = Image.new('RGB', (DEFAULT_WIDTH, DEFAULT_HEIGHT), 0xffffff)
    for i in range(len(images)):
        image = images[i]
        x = i % 20 
        y = i / 20
        x = x * item_width
        y = y * item_height
        new_image.paste(image, (x, y))
    new_image.save(new_file, quality = 70)

def compound_user_avatar(file_name):
    file_list = os.listdir(file_name)
    compound_avatar(file_list, '%s_compound' % file_name) 

def download_user_avatar(user_list):
    pass          

