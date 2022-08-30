
import os
from os import path
import cv2
import numpy as np
import folderoperation as ft

INPUT_DIR = ft.select_folder()

for subdir, dirs, files in os.walk(INPUT_DIR):
    for file in files:
        if '.jpg' not in file:
            continue
        imgPath = path.join(subdir, file)
        filename = imgPath.split("\\")[-1]
        image = cv2.imread(imgPath, 0)
        intensity = np.mean(image)
    
        if intensity > 2:
            OUTPUT_DIR = subdir + '/output'
            if not os.path.exists(OUTPUT_DIR):
                os.makedirs(OUTPUT_DIR)
            cv2.imwrite(os.path.join(OUTPUT_DIR, filename), image)
