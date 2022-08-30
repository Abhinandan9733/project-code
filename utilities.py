
import cv2
import numpy as np
from scipy.optimize import curve_fit
import xlsxwriter
 
def findHorizontalLineCords(points):
    xMin = 9999
    y = 0 
    x = 0
    for point in points:
        if(point[0][0] < xMin):
            xMin = point[0][0]
            y = point[0][1]
    
    filteredPoints = list(filter(lambda p:p[0][0] == xMin, points))

    diff = 0
    for ft in filteredPoints:
        for p in points:
            if (ft[0][1] == p[0][1] and ft[0][0] != p[0][0]):
                if (abs(ft[0][0] - p[0][0]) >= diff):
                    diff = abs(ft[0][0] - p[0][0])
                    x = p[0][0]
                    y = p[0][1]

    # for fp in filtedPoints:
    #     if(fp[0][1] > y):
    #         y = fp[0][1]

    # for point in points:
    #     if(point[0][1] == y and point[0][0] != xMin):
    #         x = point[0][0]
    

    return {"xMin":xMin,"x":x,"y":y}

def findHorizontalLineCordsOdd(points):
    xMax = 0
    y = 0 
    x = 0
    for point in points:
        if(point[0][0] > xMax):
            xMax = point[0][0]
            y = point[0][1]
    
    filteredPoints = list(filter(lambda p:p[0][0] == xMax, points))

    diff = 0
    for ft in filteredPoints:
        for p in points:
            if (ft[0][1] == p[0][1] and ft[0][0] != p[0][0]):
                if (abs(ft[0][0] - p[0][0]) > diff):
                    diff = abs(ft[0][0] - p[0][0])
                    x = p[0][0]
                    y = p[0][1]
    
    return {"xMax":xMax,"x":x,"y":y}

def findVerticalLineCords(points):
    yMin = 9999
    xCord = 0
    y = 0

    for point in points:
        if(point[0][1] < yMin):
            yMin = point[0][1] 
            xCord = point[0][0]
    
    filteredPoints = list(filter(lambda p:p[0][1] == yMin, points))

    diff = 0
    for ft in filteredPoints:
        for p in points:
            if (ft[0][0] == p[0][0] and ft[0][1] != p[0][1]):
                if (abs(ft[0][1] - p[0][1]) > diff):
                    diff = abs(ft[0][1] - p[0][1])
                    xCord = p[0][0]
                    y = p[0][1]

    # for fp in filtedPoints:
    #     if(fp[0][0] > xCord):
    #         xCord = fp[0][0]

    # for point1 in points:
    #     if((point1[0][0] == xCord) and (point1[0][1] != yMin)) :
    #         y = point1[0][1]
    return {"yMin":yMin,"xCord":xCord,"y":y}
 
# Difference of x-axis and y-axis
def findMaxXYDistance(points,meanIntensity, image, IS_ODD):
    if (meanIntensity > 20 and meanIntensity <25):
        if IS_ODD == "N":
            xAxisCords = findHorizontalLineCords(points)
        else:
            xAxisCords = findHorizontalLineCordsOdd(points)

        # ellipse = drawEllipse(points, xAxisCords["xMin"], xAxisCords["x"], xAxisCords["y"])
        # cv2.ellipse(image,ellipse,(0,255,0),2)
        # curveFitting(curveFittingRule, xData, yData)
        yAxisCords = findVerticalLineCords(points)
        return { "xAxisCords":xAxisCords, "yAxisCords":yAxisCords }
    else:
        yAxisCords = findVerticalLineCords(points)
        return { "yAxisCords":yAxisCords }

# For finding out the intersection point for two line
def findIntersectionPoint(line1, line2):
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])
 
    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]
 
    div = det(xdiff, ydiff)
    if div == 0:
       raise Exception('lines do not intersect')
 
    d = (det(*line1), det(*line2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    return {'x':x, 'y':y}
 
# Calculation of Molten-pool Area
def findMoltenpoolArea(points,x1,x2,y):
    i = 0
    j = 0
    str = 0
    end = 0
    for point in points:
        i = i + 1
        if(point[0][0] == x1 and point[0][1] ==y):
            str = i
    for point1 in points:
        j = j + 1
        if(point1[0][0] == x2 and point1[0][1] ==y):
            end = j
    return cv2.contourArea(points[str:end])
 
# Creating excel file
def createExcelFile(fileName,dataList=[]):
    strongArcArray = list(filter(lambda data : data['Arc Diameter'] != 0, dataList))
    weakArcArray = list(filter(lambda data : data['Arc Diameter'] == 0, dataList))
    workbook = xlsxwriter.Workbook(fileName)
    worksheet = workbook.add_worksheet()
    
    worksheet.write('A2', 'Arc Length under Weak arc (mm)')
    worksheet.write('B2', 'Arc Length under Strong arc (mm)')
    worksheet.write('C2', 'Average Arc Length (mm)')
    # worksheet.write('D2', 'Arc Diameter (mm)')
    # worksheet.write('E2', 'Molten-pool Length (mm)')
    # worksheet.write('F2', 'Molten-pool Area (sq. mm)')
    i = 2
    for data in strongArcArray:
        worksheet.write(i,1,str(data['Arc Length']))
        worksheet.write(i,3,str(data['Arc Diameter']))
        worksheet.write(i,4,str(data['Molten-pool Length']))
        worksheet.write(i,5,str(data['Molten-pool Area']))
        i += 1

    j = 2
    for data in weakArcArray:
        worksheet.write(j,0,str(data['Arc Length']))
        j += 1
    
    workbook.close()

def curveFitting(func, xData, yData):
    #Perform the curve-fit
    popt, pcov = curve_fit(func, xData, yData)
    print(popt)
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print(pcov)
    #x values for the fitted function
    # xFit = np.arange(0.0, 5.0, 0.01)
    # print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    # print(xFit)

def curveFittingRule(x, a, b):
    return a * np.exp(b * x)

def findMoltenpoolAreaPoints(points,x1,x2,y):
    i = 0
    j = 0
    str = 0
    end = 0
    for point in points:
        i = i + 1
        if(point[0][0] == x1 and point[0][1] ==y):
            str = i
    for point1 in points:
        j = j + 1
        if(point1[0][0] == x2 and point1[0][1] ==y):
            end = j
    filteredPoints = points[str:end]
    # xData = np.array(list(map(findXData, filteredPoints)))
    # yData = np.array(list(map(findYData, filteredPoints)))
    return filteredPoints
    # print(xData)
    # print(yData)

def findXData(point):
    return point[0][0]

def findYData(point):
    return point[0][1]

def drawEllipse(points,x1,x2,y):
    i = 0
    j = 0
    str = 0
    end = 0
    for point in points:
        i = i + 1
        if(point[0][0] == x1 and point[0][1] ==y):
            str = i
    for point1 in points:
        j = j + 1
        if(point1[0][0] == x2 and point1[0][1] ==y):
            end = j
    # print(points[str:end])
    # print(str)
    # print("+++++++++++++++++++++++++++++++++++++++++++++")
    # print(end)
    # ellipse = cv2.fitEllipse(points)
    # return ellipse