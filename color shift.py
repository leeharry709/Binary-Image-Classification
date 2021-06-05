# Gotten from stack exchange--------------------------------------------------

from PIL import Image, ImageEnhance
import numpy as np

def rgb_to_hsv(rgb):
    # Translated from source of colorsys.rgb_to_hsv
    # r,g,b should be a numpy arrays with values between 0 and 255
    # rgb_to_hsv returns an array of floats between 0.0 and 1.0.
    rgb = rgb.astype('float')
    hsv = np.zeros_like(rgb)
    # in case an RGBA array was passed, just copy the A channel
    hsv[..., 3:] = rgb[..., 3:]
    r, g, b = rgb[..., 0], rgb[..., 1], rgb[..., 2]
    maxc = np.max(rgb[..., :3], axis=-1)
    minc = np.min(rgb[..., :3], axis=-1)
    hsv[..., 2] = maxc
    mask = maxc != minc
    hsv[mask, 1] = (maxc - minc)[mask] / maxc[mask]
    rc = np.zeros_like(r)
    gc = np.zeros_like(g)
    bc = np.zeros_like(b)
    rc[mask] = (maxc - r)[mask] / (maxc - minc)[mask]
    gc[mask] = (maxc - g)[mask] / (maxc - minc)[mask]
    bc[mask] = (maxc - b)[mask] / (maxc - minc)[mask]
    hsv[..., 0] = np.select(
        [r == maxc, g == maxc], [bc - gc, 2.0 + rc - bc], default=4.0 + gc - rc)
    hsv[..., 0] = (hsv[..., 0] / 6.0) % 1.0
    return hsv

def hsv_to_rgb(hsv):
    # Translated from source of colorsys.hsv_to_rgb
    # h,s should be a numpy arrays with values between 0.0 and 1.0
    # v should be a numpy array with values between 0.0 and 255.0
    # hsv_to_rgb returns an array of uints between 0 and 255.
    rgb = np.empty_like(hsv)
    rgb[..., 3:] = hsv[..., 3:]
    h, s, v = hsv[..., 0], hsv[..., 1], hsv[..., 2]
    i = (h * 6.0).astype('uint8')
    f = (h * 6.0) - i
    p = v * (1.0 - s)
    q = v * (1.0 - s * f)
    t = v * (1.0 - s * (1.0 - f))
    i = i % 6
    conditions = [s == 0.0, i == 1, i == 2, i == 3, i == 4, i == 5]
    rgb[..., 0] = np.select(conditions, [v, q, p, p, t, v], default=v)
    rgb[..., 1] = np.select(conditions, [v, v, v, q, p, p], default=t)
    rgb[..., 2] = np.select(conditions, [v, p, t, v, v, q], default=p)
    return rgb.astype('uint8')


def shift_hue(arr,hout):
    hsv=rgb_to_hsv(arr)
    hsv[...,0]=hout
    rgb=hsv_to_rgb(hsv)
    return rgb


# Coded by me ----------------------------------------------------------------

import os
import random

home_dir = os.chdir('C:/Users/leeha/Documents/pythons/Ripe Mango Detector/fruits-360/Training/Mango Red')

x = []
y1 = []
y2 = []
final_array = []

if __name__=='__main__':

    print('Enter "Whole" or "Half" picture color shift: ')    
    whole_half = input()
    print('Enter "red_hue" or "yellow_hue": ')
    color_input1 = input()    

    red_hue = (180-170)/360.0
    yellow_hue = (180-140)/360.0
    
    
    for file in os.listdir(home_dir):
        filename = file[:-4]
        img = Image.open(file).convert('RGBA')
        arr = np.array(img)
        x = np.split(arr, 2)
        y1 = np.array(x[0])
        y2 = np.array(x[1])
        
        random_01 = random.randint(0,1)
        if random_01 == 0:
            other_num = 1
        else:
            other_num = 0
            
        halves = [y1,y2]
        chosen_half = halves[random_01]
        other_half = halves[other_num]
        
        
        if whole_half.lower() == 'whole':
            if color_input1.lower() == 'red_hue':
                new_img = Image.fromarray(shift_hue(arr,red_hue), 'RGBA')
                
                brightness = ImageEnhance.Brightness(new_img)
                saturation = ImageEnhance.Color(new_img)
                
                final_img = brightness.enhance(1.7)
                final_img = saturation.enhance(3)
    
                final_img.save('w'+filename+'.png')
                final_img.close()
                
            if color_input1.lower() == 'yellow_hue':
                new_img = Image.fromarray(shift_hue(arr,yellow_hue), 'RGBA')
                
                brightness = ImageEnhance.Brightness(new_img)
                saturation = ImageEnhance.Color(new_img)
                
                final_img = brightness.enhance(1.7)
                final_img = saturation.enhance(3)
    
                final_img.save('w'+filename+'.png')                

        
        if whole_half.lower() == 'half':
            if color_input1.lower() == 'red_hue':
                if file[0] == 'w' or file[0] == 'h':
                    pass
                else:
                    new_half = Image.fromarray(shift_hue(chosen_half,red_hue), 'RGBA')
                    
                    brightness = ImageEnhance.Brightness(new_half)
                    saturation = ImageEnhance.Color(new_half)
                    
                    final_half = brightness.enhance(1.7)
                    final_half = saturation.enhance(3)
            
                    if random_01 == 0:
                        final_array = np.concatenate((final_half, other_half))
                    else:
                        final_array = np.concatenate((other_half, final_half))
                        
                    final_img = Image.fromarray(final_array)
            
                    final_img.save('hr'+filename+'.png')

            if color_input1.lower() == 'yellow_hue':
                if file[0] == 'e' or file[0] == 'h':
                    pass
                else:
                    new_half = Image.fromarray(shift_hue(chosen_half,yellow_hue), 'RGBA')
                    
                    brightness = ImageEnhance.Brightness(new_half)
                    saturation = ImageEnhance.Color(new_half)
                    
                    final_half = brightness.enhance(1.7)
                    final_half = saturation.enhance(3)
            
                    if random_01 == 0:
                        final_array = np.concatenate((final_half, other_half))
                    else:
                        final_array = np.concatenate((other_half, final_half))
                        
                    final_img = Image.fromarray(final_array)
            
                    final_img.save('hy'+filename+'.png')
