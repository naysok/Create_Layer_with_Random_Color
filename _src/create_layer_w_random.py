import math
import random

import Rhino.Display as rd
import rhinoscriptsyntax as rs

def rgb_to_hsl(rgb):
    h, s, l  = list(rs.ColorRGBToHLS(rgb))
    hsl = rd.ColorHSL(h, s, l)
    # print("hls : {}, {}, {}".format(hsl.H, hsl.S, hsl.L))
    return [hsl.H, hsl.S, hsl.L]

def hsl_to_rgb(hsl):
    rgb = rd.ColorHSL.ToArgbColor(hsl)
    # print("rgb : {},{},{}".format(rgb.R, rgb.G, rgb.B))
    return [rgb.R, rgb.G, rgb.B]

def get_colors():
    
    layers_from_3dm = rs.LayerNames()
    
    hues = []
    
    ### Set Yellow (Unused << Selelcted-Color)
    hues.append(0.1666666716337204)
    
    ### Start-End
    hues.append(0.0)
    hues.append(1.0)
    
    for layer_name in layers_from_3dm:
        
        c = rs.LayerColor(layer_name)
        
        h, s, l = rgb_to_hsl(c)
        
        ## Black or White
        if (l < 0.2) or (0.8 < l):
            # print(layer_name)
            pass
        
        ### Other Colors
        else:
            # print(layer_name)
            # print(h, s, l)
            hues.append(h)
    
    return sorted(list(set(hues)))

def calc_difference(l):
    
    ds = []
    for i in xrange(len(l) - 1):
        ds.append(l[i+1] - l[i])
    return ds

def debug_hues():
    
    layers_from_3dm = rs.LayerNames()
    
    hues = []
    
    for layer_name in layers_from_3dm:
        
        c = rs.LayerColor(layer_name)
        
        h, s, l = rgb_to_hsl(c)
        
        rs.AddPoint(h,0,0)

def create_layer():
    
    ### Get Hue-Values
    colors = get_colors()
    # print(colors)
    
    ### Get Diff
    diff = calc_difference(colors)
    # print(diff)
    
    idx = diff.index(max(diff))
    # print(idx)
    
    new_hue = (colors[idx] + colors[idx + 1]) * 0.5
    # print(new_hue)
    
    new_rgb = hsl_to_rgb(rd.ColorHSL(new_hue, 0.5 + random.uniform(0, 0.5), 0.5 + random.uniform(-0.2, 0.2)))
    # print(new_rgb)
    
    rs.AddLayer(color=new_rgb)


count = 5

for i in range(count):
    create_layer()

# debug_hues()