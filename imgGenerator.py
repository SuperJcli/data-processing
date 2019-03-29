# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 16:57:26 2018

@author: SuperLee
"""

#import matplotlib.pyplot as plt
from PIL import Image
from keras.preprocessing import image as imageGenerator
#import glob


source_img = 'G:/Engine_blade_crackdetect/tempimage/'
SAVE_PATH = 'G:/Engine_blade_crackdetect/tempimagenerator/'

datagen = imageGenerator.ImageDataGenerator(rotation_range = 360)
    
gen_data = datagen.flow_from_directory(source_img,
                                       batch_size=1,
                                       shuffle=False,
                                       save_to_dir=SAVE_PATH,
                                       save_prefix='gen',
                                       save_format='png',
                                       target_size=(512, 512))
# #生成x张图
#一般来说循环次数决定了每一张图片的生成个数
for i in range(1745):
        
    gen_data.next()

'''
name_list = glob.glob(SAVE_PATH+'/*')
fig = plt.figure()


for i in range(9):
    img = Image.open(name_list[i])
    sub_img = fig.add_subplot(331 + i)
    sub_img.imshow(img)
   #fig.savefig(gen_path + '/original_1.png', dpi=200, papertype='a5')
plt.show()
'''