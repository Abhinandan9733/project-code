import os
import cv2
import glob



for i, path in enumerate(glob.glob(r"C:\Users\Abhi\Desktop\strong\*.jpg")):
    image = cv2.imread(path, 0)
    original = image.copy()
    gray = image.copy()
    blur = cv2.GaussianBlur(gray, (3,3), cv2.BORDER_CONSTANT)
    thresh = cv2.threshold(blur,0,255, cv2.THRESH_OTSU + cv2.THRESH_BINARY)[1]
    # kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
    # opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
    # dilate_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
    # dilate = cv2.dilate(opening, dilate_kernel, iterations=5)
    cnts = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]
    # cnts = sorted(cnts, key=cv2.contourArea, reverse=True)

    # for c in cnts:
    #     x,y,w,h = cv2.boundingRect(c)
    #     ROI = original[y:y+h, x:x+w]  
    #     cv2.imwrite(os.path.join(r"D:\WAAM\output\WAAM-1\ROI\L19\image_%05i.jpg" %i), ROI)
    #     break
    # i += 1

i=0
for j in cnts:
    M = cv2.moments(j)
    if M['m00'] != 0:
        cx = int(M['m10']/M['m00'])
        cy = int(M['m01']/M['m00'])
        cv2.drawContours(image, [j], -1, (0, 255, 0), 1)
        cv2.circle(image, (cx, cy), 3, (0, 0, 255), -1)
        # cv2.putText(image, "center", (cx - 20, cy - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1)
	    # print(f"x: {cx} y: {cy}")
        ROI = image[cy-100: cy+200, cx-125: cx+250]
        # ROI = original[cy-100:cy+100, cx-125:cx+125]
        cv2.imwrite(os.path.join(r"D:\WAAM\output\WAAM-3\filtered\length calculation\L5\ROI weak\image_%03i.jpg" %i), ROI)
        
        # cv2.imwrite(r"C:\Users\Abhi\Desktop\strong\image3.jpg", image)
    i += 1
