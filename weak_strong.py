import os
import glob
import cv2
import numpy as np

i=0

for i, path in enumerate(glob.glob(r"D:\WAAM\output\WAAM-5\Arc images\L1\*.jpg")):
    image = cv2.imread(path, 0)
    
    intensity = np.mean(image)

    if intensity > 10 and intensity < 15:
        cv2.imwrite(os.path.join(r"D:\WAAM\output\WAAM-5\strong_weak\L1\weak\mage_%03i.jpg" %i), image)
        i += 1

    if intensity > 20 and intensity < 25:
        cv2.imwrite(os.path.join(r"D:\WAAM\output\WAAM-5\strong_weak\L1\strong\mage_%03i.jpg" %i), image)
        i += 1 

for i, path in enumerate(glob.glob(r"D:\WAAM\output\WAAM-5\Arc images\L2\*.jpg")):
    image = cv2.imread(path, 0)
    
    intensity = np.mean(image)

    if intensity > 10 and intensity < 15:
        cv2.imwrite(os.path.join(r"D:\WAAM\output\WAAM-5\strong_weak\L2\weak\mage_%03i.jpg" %i), image)
        i += 1

    if intensity > 20 and intensity < 25:
        cv2.imwrite(os.path.join(r"D:\WAAM\output\WAAM-5\strong_weak\L2\strong\mage_%03i.jpg" %i), image)
        i += 1 

for i, path in enumerate(glob.glob(r"D:\WAAM\output\WAAM-5\Arc images\L3\*.jpg")):
    image = cv2.imread(path, 0)
    
    intensity = np.mean(image)

    if intensity > 10 and intensity < 15:
        cv2.imwrite(os.path.join(r"D:\WAAM\output\WAAM-5\strong_weak\L3\weak\mage_%03i.jpg" %i), image)
        i += 1

    if intensity > 20 and intensity < 25:
        cv2.imwrite(os.path.join(r"D:\WAAM\output\WAAM-5\strong_weak\L3\strong\mage_%03i.jpg" %i), image)
        i += 1 

for i, path in enumerate(glob.glob(r"D:\WAAM\output\WAAM-5\Arc images\L4\*.jpg")):
    image = cv2.imread(path, 0)
    
    intensity = np.mean(image)

    if intensity > 10 and intensity < 15:
        cv2.imwrite(os.path.join(r"D:\WAAM\output\WAAM-5\strong_weak\L4\weak\mage_%03i.jpg" %i), image)
        i += 1

    if intensity > 20 and intensity < 25:
        cv2.imwrite(os.path.join(r"D:\WAAM\output\WAAM-5\strong_weak\L4\strong\mage_%03i.jpg" %i), image)
        i += 1 

for i, path in enumerate(glob.glob(r"D:\WAAM\output\WAAM-5\Arc images\L5\*.jpg")):
    image = cv2.imread(path, 0)
    
    intensity = np.mean(image)

    if intensity > 10 and intensity < 15:
        cv2.imwrite(os.path.join(r"D:\WAAM\output\WAAM-5\strong_weak\L5\weak\mage_%03i.jpg" %i), image)
        i += 1

    if intensity > 20 and intensity < 25:
        cv2.imwrite(os.path.join(r"D:\WAAM\output\WAAM-5\strong_weak\L5\strong\mage_%03i.jpg" %i), image)
        i += 1 

for i, path in enumerate(glob.glob(r"D:\WAAM\output\WAAM-5\Arc images\L6\*.jpg")):
    image = cv2.imread(path, 0)
    
    intensity = np.mean(image)

    if intensity > 10 and intensity < 15:
        cv2.imwrite(os.path.join(r"D:\WAAM\output\WAAM-5\strong_weak\L6\weak\mage_%03i.jpg" %i), image)
        i += 1

    if intensity > 20 and intensity < 25:
        cv2.imwrite(os.path.join(r"D:\WAAM\output\WAAM-5\strong_weak\L6\strong\mage_%03i.jpg" %i), image)
        i += 1 

for i, path in enumerate(glob.glob(r"D:\WAAM\output\WAAM-5\Arc images\L7\*.jpg")):
    image = cv2.imread(path, 0)
    
    intensity = np.mean(image)

    if intensity > 10 and intensity < 15:
        cv2.imwrite(os.path.join(r"D:\WAAM\output\WAAM-5\strong_weak\L7\weak\mage_%03i.jpg" %i), image)
        i += 1

    if intensity > 20 and intensity < 25:
        cv2.imwrite(os.path.join(r"D:\WAAM\output\WAAM-5\strong_weak\L7\strong\mage_%03i.jpg" %i), image)
        i += 1 

for i, path in enumerate(glob.glob(r"D:\WAAM\output\WAAM-5\Arc images\L8\*.jpg")):
    image = cv2.imread(path, 0)
    
    intensity = np.mean(image)

    if intensity > 10 and intensity < 15:
        cv2.imwrite(os.path.join(r"D:\WAAM\output\WAAM-5\strong_weak\L8\weak\mage_%03i.jpg" %i), image)
        i += 1

    if intensity > 20 and intensity < 25:
        cv2.imwrite(os.path.join(r"D:\WAAM\output\WAAM-5\strong_weak\L8\strong\mage_%03i.jpg" %i), image)
        i += 1 

for i, path in enumerate(glob.glob(r"D:\WAAM\output\WAAM-5\Arc images\L9\*.jpg")):
    image = cv2.imread(path, 0)
    
    intensity = np.mean(image)

    if intensity > 10 and intensity < 15:
        cv2.imwrite(os.path.join(r"D:\WAAM\output\WAAM-5\strong_weak\L9\weak\mage_%03i.jpg" %i), image)
        i += 1

    if intensity > 20 and intensity < 25:
        cv2.imwrite(os.path.join(r"D:\WAAM\output\WAAM-5\strong_weak\L9\strong\mage_%03i.jpg" %i), image)
        i += 1 

for i, path in enumerate(glob.glob(r"D:\WAAM\output\WAAM-5\Arc images\L10\*.jpg")):
    image = cv2.imread(path, 0)
    
    intensity = np.mean(image)

    if intensity > 10 and intensity < 15:
        cv2.imwrite(os.path.join(r"D:\WAAM\output\WAAM-5\strong_weak\L10\weak\image_%03i.jpg" %i), image)
        i += 1

    if intensity > 20 and intensity < 25:
        cv2.imwrite(os.path.join(r"D:\WAAM\output\WAAM-5\strong_weak\L10\strong\image_%03i.jpg" %i), image)
        i += 1

for i, path in enumerate(glob.glob(r"D:\WAAM\output\WAAM-5\Arc images\L10\*.jpg")):
    image = cv2.imread(path, 0)
    
    intensity = np.mean(image)

    if intensity > 10 and intensity < 15:
        cv2.imwrite(os.path.join(r"D:\WAAM\output\WAAM-5\strong_weak\L10\weak\image_%03i.jpg" %i), image)
        i += 1

    if intensity > 20 and intensity < 25:
        cv2.imwrite(os.path.join(r"D:\WAAM\output\WAAM-5\strong_weak\L10\strong\image_%03i.jpg" %i), image)
        i += 1 

for i, path in enumerate(glob.glob(r"D:\WAAM\output\WAAM-5\Arc images\L12\*.jpg")):
    image = cv2.imread(path, 0)
    
    intensity = np.mean(image)

    if intensity > 10 and intensity < 15:
        cv2.imwrite(os.path.join(r"D:\WAAM\output\WAAM-5\strong_weak\L12\weak\image_%03i.jpg" %i), image)
        i += 1

    if intensity > 20 and intensity < 25:
        cv2.imwrite(os.path.join(r"D:\WAAM\output\WAAM-5\strong_weak\L12\strong\image_%03i.jpg" %i), image)
        i += 1 

for i, path in enumerate(glob.glob(r"D:\WAAM\output\WAAM-5\Arc images\L13\*.jpg")):
    image = cv2.imread(path, 0)
    
    intensity = np.mean(image)

    if intensity > 10 and intensity < 15:
        cv2.imwrite(os.path.join(r"D:\WAAM\output\WAAM-5\strong_weak\L13\weak\image_%03i.jpg" %i), image)
        i += 1

    if intensity > 20 and intensity < 25:
        cv2.imwrite(os.path.join(r"D:\WAAM\output\WAAM-5\strong_weak\L13\strong\image_%03i.jpg" %i), image)
        i += 1 

for i, path in enumerate(glob.glob(r"D:\WAAM\output\WAAM-5\Arc images\L14\*.jpg")):
    image = cv2.imread(path, 0)
    
    intensity = np.mean(image)

    if intensity > 10 and intensity < 15:
        cv2.imwrite(os.path.join(r"D:\WAAM\output\WAAM-5\strong_weak\L14\weak\image_%03i.jpg" %i), image)
        i += 1

    if intensity > 20 and intensity < 25:
        cv2.imwrite(os.path.join(r"D:\WAAM\output\WAAM-5\strong_weak\L14\strong\image_%03i.jpg" %i), image)
        i += 1 

for i, path in enumerate(glob.glob(r"D:\WAAM\output\WAAM-5\Arc images\L15\*.jpg")):
    image = cv2.imread(path, 0)
    
    intensity = np.mean(image)

    if intensity > 10 and intensity < 15:
        cv2.imwrite(os.path.join(r"D:\WAAM\output\WAAM-5\strong_weak\L15\weak\image_%03i.jpg" %i), image)
        i += 1

    if intensity > 20 and intensity < 25:
        cv2.imwrite(os.path.join(r"D:\WAAM\output\WAAM-5\strong_weak\L15\strong\image_%03i.jpg" %i), image)
        i += 1 

for i, path in enumerate(glob.glob(r"D:\WAAM\output\WAAM-5\Arc images\L15\*.jpg")):
    image = cv2.imread(path, 0)
    
    intensity = np.mean(image)

    if intensity > 10 and intensity < 15:
        cv2.imwrite(os.path.join(r"D:\WAAM\output\WAAM-5\strong_weak\L15\weak\image_%03i.jpg" %i), image)
        i += 1

    if intensity > 20 and intensity < 25:
        cv2.imwrite(os.path.join(r"D:\WAAM\output\WAAM-5\strong_weak\L15\strong\image_%03i.jpg" %i), image)
        i += 1 

for i, path in enumerate(glob.glob(r"D:\WAAM\output\WAAM-5\Arc images\L17\*.jpg")):
    image = cv2.imread(path, 0)
    
    intensity = np.mean(image)

    if intensity > 10 and intensity < 15:
        cv2.imwrite(os.path.join(r"D:\WAAM\output\WAAM-5\strong_weak\L17\weak\image_%03i.jpg" %i), image)
        i += 1

    if intensity > 20 and intensity < 25:
        cv2.imwrite(os.path.join(r"D:\WAAM\output\WAAM-5\strong_weak\L17\strong\image_%03i.jpg" %i), image)
        i += 1 

for i, path in enumerate(glob.glob(r"D:\WAAM\output\WAAM-5\Arc images\L18\*.jpg")):
    image = cv2.imread(path, 0)
    
    intensity = np.mean(image)

    if intensity > 10 and intensity < 15:
        cv2.imwrite(os.path.join(r"D:\WAAM\output\WAAM-5\strong_weak\L18\weak\image_%03i.jpg" %i), image)
        i += 1

    if intensity > 20 and intensity < 25:
        cv2.imwrite(os.path.join(r"D:\WAAM\output\WAAM-5\strong_weak\L18\strong\image_%03i.jpg" %i), image)
        i += 1 
    
for i, path in enumerate(glob.glob(r"D:\WAAM\output\WAAM-5\Arc images\L19\*.jpg")):
    image = cv2.imread(path, 0)
    
    intensity = np.mean(image)

    if intensity > 10 and intensity < 15:
        cv2.imwrite(os.path.join(r"D:\WAAM\output\WAAM-5\strong_weak\L19\weak\image_%03i.jpg" %i), image)
        i += 1

    if intensity > 20 and intensity < 25:
        cv2.imwrite(os.path.join(r"D:\WAAM\output\WAAM-5\strong_weak\L19\strong\image_%03i.jpg" %i), image)
        i += 1 

for i, path in enumerate(glob.glob(r"D:\WAAM\output\WAAM-5\Arc images\L20\*.jpg")):
    image = cv2.imread(path, 0)
    
    intensity = np.mean(image)

    if intensity > 10 and intensity < 15:
        cv2.imwrite(os.path.join(r"D:\WAAM\output\WAAM-5\strong_weak\L20\weak\image_%03i.jpg" %i), image)
        i += 1

    if intensity > 20 and intensity < 25:
        cv2.imwrite(os.path.join(r"D:\WAAM\output\WAAM-5\strong_weak\L20\strong\image_%03i.jpg" %i), image)
        i += 1 