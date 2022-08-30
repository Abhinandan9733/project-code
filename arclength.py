
from os import path
import os
import cv2
import numpy as np
import utilities as ut
import folderoperation as ft

dataList = []
meanIntensity = 0

INPUT_DIR = ft.select_folder()
IS_ODD = input("is Odd?")

for subdir, dirs, files in os.walk(INPUT_DIR):
    for file in files:
        if '.jpg' not in file:
            continue
        imgPath = path.join(subdir, file)
        image = cv2.imread(imgPath)
        meanIntensity = np.mean(image)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # thresh = cv2.threshold(gray, 245, 255, cv2.THRESH_OTSU + cv2.THRESH_BINARY)[1]
        # kernel = np.ones((3,3),np.uint8)
        # thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
        # cnts = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        # cnts = cnts[0] if len(cnts) == 2 else cnts[1]
        blur = cv2.GaussianBlur(gray, (3,3), cv2.BORDER_CONSTANT)
        ret, thresh = cv2.threshold(blur, 220, 255, cv2.THRESH_BINARY)
        cnts, hierarchies = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
        blank_image = np.ones((450,600,3), np.uint8)
        min_area = 10
        halfCnts = 0
    
        for c in cnts:
            area = cv2.contourArea(c)
            cords = ut.findMaxXYDistance(c,meanIntensity, blank_image, IS_ODD)
            print(cords)
            if meanIntensity > 20 and meanIntensity <25:
                if IS_ODD == "N":
                    halfCnts = ut.findMoltenpoolArea(c,cords['xAxisCords']['xMin'],cords['xAxisCords']['x'],cords['xAxisCords']['y'])
                else:
                    halfCnts = ut.findMoltenpoolArea(c,cords['xAxisCords']['x'],cords['xAxisCords']['xMax'],cords['xAxisCords']['y'])
                if area > min_area:
                    cv2.drawContours(blank_image,[c], 0, (255,0,0), 1)
            else:
                if area > min_area:
                    cv2.drawContours(blank_image,[c], 0, (255,0,0), 1)  
    
        # Draw line in y axis direction
        cv2.line(blank_image, (cords['yAxisCords']['xCord'],cords['yAxisCords']['yMin']), (cords['yAxisCords']['xCord'],cords['yAxisCords']['y']), (0,0,255), 1)
        line1 = [[cords['yAxisCords']['xCord'],cords['yAxisCords']['yMin']],[cords['yAxisCords']['xCord'],cords['yAxisCords']['y']]]
    
        # Draw line in x axis direction
        if meanIntensity > 20 and meanIntensity <25:
            if IS_ODD == "N":
                cv2.line(blank_image, (cords['xAxisCords']['xMin'],cords['xAxisCords']['y']), (cords['xAxisCords']['x'],cords['xAxisCords']['y']), (0,0,255), 1)
                line2 = [[cords['xAxisCords']['xMin'],cords['xAxisCords']['y']],[cords['xAxisCords']['x'],cords['xAxisCords']['y']]]
            else:
                cv2.line(blank_image, (cords['xAxisCords']['xMax'],cords['xAxisCords']['y']), (cords['xAxisCords']['x'],cords['xAxisCords']['y']), (0,255,0), 1)
                line2 = [[cords['xAxisCords']['xMax'],cords['xAxisCords']['y']],[cords['xAxisCords']['x'],cords['xAxisCords']['y']]]
    
        # y axis difference
        yDiff = abs(cords['yAxisCords']['yMin'] - cords['yAxisCords']['y'])
        if meanIntensity > 20 and meanIntensity <25:
            if IS_ODD == "N":
                xDiff = abs(cords['xAxisCords']['xMin'] - cords['xAxisCords']['x'])
            else:
                xDiff = abs(cords['xAxisCords']['xMax'] - cords['xAxisCords']['x'])
    
        # scale variable is used for scaling the pixel length with actual length
        scale = 0.057803
        arcLength = 0
        pointOfIntersection = []
        arcDiameter = 0
        MoltenpoolLength = 0
        MoltenpoolArea = 0
        text = ""
        if(meanIntensity > 20 and meanIntensity <25):
            pointOfIntersection = ut.findIntersectionPoint(line1,line2)
            arcLength = abs(cords['yAxisCords']['yMin']-pointOfIntersection["y"])*scale
            arcDiameter = (xDiff*scale)
            MoltenpoolLength = (abs(pointOfIntersection["y"]-cords["yAxisCords"]["y"])*scale)
            MoltenpoolArea = round(halfCnts*scale,2)
            text = f"""
                    X-Axis length {xDiff*scale}mm.\n
                    Y-Axis length {yDiff*scale}mm.\n
                    Y-Axis co-ordinates {line1}.\n
                    X-Axis co-ordinates {line2}.\n
                    point of intersection {pointOfIntersection}.\n \n
                    Arc Length : {arcLength} mm \n
                    Arc Diameter : {arcDiameter} mm \n
                    Molten-pool Length : {MoltenpoolLength} mm \n
                    Molten-pool Area : {MoltenpoolArea} sq. mm
                """
        else:
            arcLength = yDiff*scale
            text = f"""
                    Y-Axis length {yDiff*scale}mm.\n \n
                    Arc Length : {arcLength} mm
                """

        font = cv2.FONT_HERSHEY_SIMPLEX
        fontScale = 0.5
        color = (255, 0, 0)
        thickness = 1

        y0, dy = 200, 10
        for i, lines in enumerate(text.split('\n')):
            y = y0 + i*dy
            cv2.putText(blank_image,lines,(50,y), font, fontScale, color, thickness, cv2.LINE_AA)
        
        data = {
            'Arc Length': round(arcLength,3),
            'Arc Diameter': round(arcDiameter,3),
            'Molten-pool Length': round(MoltenpoolLength,3),
            'Molten-pool Area': round(MoltenpoolArea,3)
            }
        dataList.append(data)

        #cv2.imshow('blank_image with contours', blank_image)
    
        if cv2.waitKey(0) & 0xff == 27:
            cv2.destroyAllWindows()

    
ut.createExcelFile(r'D:\WAAM\output\WAAM-5\E5_L20.xlsx',dataList)
