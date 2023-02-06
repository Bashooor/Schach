import numpy as np
import cv2

# class for the squares.
# img is the photo (rectified photo or original photo) based on the choosen model
# model is a string with ('rank_file') for the model (rank_file_model)
# Otherwise using the other model (only_board_model) as default
class Squares:

    def __init__(self, img, model):
        self.img = img
        self.model = model

    def getModel(self):
        return self.model
    
    ### main function to draw lines between two points
    def drawLine(self, p1, p2):
        ### function to find slope 
        def slope(p1, p2):
            x1, y1 = p1
            x2, y2 = p2
            if x2 != x1:
                return((y2-y1)/(x2-x1))
            else:
                return 'NA'
        x1, y1 = p1
        x2, y2 = p2
        ### finding slope
        m = slope(p1, p2)
        ### getting image shape
        h, w = self.img.shape[:2]

        if m!='NA':
            ### here we are essentially extending the line to x=0 and x=width
            ### and calculating the y associated with it
            ##starting point
            px=0
            py=-(x1-0)*m+y1
            ##ending point
            qx=w
            qy=-(x2-w)*m+y2
        else:
        ### if slope is zero, draw a line with x=x1 and y=0 and y=height
            px, py = x1, 0
            qx, qy = x1, h
        cv2.line(self.img, (int(px), int(py)), (int(qx), int(qy)), (255, 255, 255), 1)
        line = [[int(px), int(py)], [int(qx), int(qy)]]
        return line
        
    def line_intersection(line1, line2):
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
        return int(x), int(y)
    
    # calculate intersection points and squares
    point1_r1 = (0, 560)
    point2_r1 = (640, 560)
    point3_r1 = (0, 640)
    point4_r1 = (640, 640)
    point1_r2 = (0, 400)
    point2_r2 = (640, 400)
    point3_r2 = (0, 480)
    point4_r2 = (640, 480)
    point1_r3 = (0, 240)
    point2_r3 = (640, 240)
    point3_r3 = (0, 320)
    point4_r3 = (640, 320)
    point1_r4 = (0, 80)
    point2_r4 = (640, 80)
    point3_r4 = (0, 160)
    point4_r4 = (640, 160)
    point1_f1 = (80, 0)
    point2_f1 = (80, 640)
    point3_f1 = (160, 0)
    point4_f1 = (160, 640)
    point1_f2 = (240, 0)
    point2_f2 = (240, 640)
    point3_f2 = (320, 0)
    point4_f2 = (320, 640)
    point1_f3 = (400, 0)
    point2_f3 = (400, 640)
    point3_f3 = (480, 0)
    point4_f3 = (480, 640)
    point1_f4 = (560, 0)
    point2_f4 = (560, 640)
    point3_f4 = (640, 0)
    point4_f4 = (640, 640)
    #--------------------------------------------------------

    # if the second model (rank_model_model) has been choosen
    # TODO
    if getModel() == 'rank_file':
        point1_r1 = (0, 560)
        point2_r1 = (640, 560)
        point3_r1 = (0, 640)
        point4_r1 = (640, 640)
        point1_r2 = (0, 400)
        point2_r2 = (640, 400)
        point3_r2 = (0, 480)
        point4_r2 = (640, 480)
        point1_r3 = (0, 240)
        point2_r3 = (640, 240)
        point3_r3 = (0, 320)
        point4_r3 = (640, 320)
        point1_r4 = (0, 80)
        point2_r4 = (640, 80)
        point3_r4 = (0, 160)
        point4_r4 = (640, 160)
        point1_f1 = (80, 0)
        point2_f1 = (80, 640)
        point3_f1 = (160, 0)
        point4_f1 = (160, 640)
        point1_f2 = (240, 0)
        point2_f2 = (240, 640)
        point3_f2 = (320, 0)
        point4_f2 = (320, 640)
        point1_f3 = (400, 0)
        point2_f3 = (400, 640)
        point3_f3 = (480, 0)
        point4_f3 = (480, 640)
        point1_f4 = (560, 0)
        point2_f4 = (560, 640)
        point3_f4 = (640, 0)
        point4_f4 = (640, 640)
    #----------------------------------------
    line1_r1 = drawLine(point1_r1, point2_r1)
    line2_r1 = drawLine(point3_r1, point4_r1)

    line1_r2 = drawLine(point1_r2, point2_r2)
    line2_r2 = drawLine(point3_r2, point4_r2)

    line1_r3 = drawLine(point1_r3, point2_r3)
    line2_r3 = drawLine(point3_r3, point4_r3)

    line1_r4 = drawLine(point1_r4, point2_r4)
    line2_r4 = drawLine(point3_r4, point4_r4)

    line1_f1 = drawLine(point1_f1, point2_f1)
    line2_f1 = drawLine(point3_f1, point4_f1)

    line1_f2 = drawLine(point1_f2, point2_f2)
    line2_f2 = drawLine(point3_f2, point4_f2)

    line1_f3 = drawLine(point1_f3, point2_f3)
    line2_f3 = drawLine(point3_f3, point4_f3)

    line1_f4 = drawLine(point1_f4, point2_f4)
    line2_f4 = drawLine(point3_f4, point4_f4)

    line_r1_r4 = drawLine(point1_r1, point3_r4)
    line_f1_f4 = drawLine(point1_f1, point3_f4)
    #------------------------------------------
    # Intersection points:
    #----------------------------------------------
    p11 = line_intersection(line_f1_f4, line_r1_r4)
    p12 = line_intersection(line_f1_f4, line1_f1)
    p13 = line_intersection(line_f1_f4, line2_f1)
    p14 = line_intersection(line_f1_f4, line1_f2)
    p15 = line_intersection(line_f1_f4, line2_f2)
    p16 = line_intersection(line_f1_f4, line1_f3)
    p17 = line_intersection(line_f1_f4, line2_f3)
    p18 = line_intersection(line_f1_f4, line1_f4)
    p19 = line_intersection(line_f1_f4, line2_f4)

    p21 = line_intersection(line1_r4, line_r1_r4)
    p22 = line_intersection(line1_r4, line1_f1)
    p23 = line_intersection(line1_r4, line2_f1)
    p24 = line_intersection(line1_r4, line1_f2)
    p25 = line_intersection(line1_r4, line2_f2)
    p26 = line_intersection(line1_r4, line1_f3)
    p27 = line_intersection(line1_r4, line2_f3)
    p28 = line_intersection(line1_r4, line1_f4)
    p29 = line_intersection(line1_r4, line2_f4)

    p31 = line_intersection(line2_r4, line_r1_r4)
    p32 = line_intersection(line2_r4, line1_f1)
    p33 = line_intersection(line2_r4, line2_f1)
    p34 = line_intersection(line2_r4, line1_f2)
    p35 = line_intersection(line2_r4, line2_f2)
    p36 = line_intersection(line2_r4, line1_f3)
    p37 = line_intersection(line2_r4, line2_f3)
    p38 = line_intersection(line2_r4, line1_f4)
    p39 = line_intersection(line2_r4, line2_f4)

    p41 = line_intersection(line1_r3, line_r1_r4)
    p42 = line_intersection(line1_r3, line1_f1)
    p43 = line_intersection(line1_r3, line2_f1)
    p44 = line_intersection(line1_r3, line1_f2)
    p45 = line_intersection(line1_r3, line2_f2)
    p46 = line_intersection(line1_r3, line1_f3)
    p47 = line_intersection(line1_r3, line2_f3)
    p48 = line_intersection(line1_r3, line1_f4)
    p49 = line_intersection(line1_r3, line2_f4)

    p51 = line_intersection(line2_r3, line_r1_r4)
    p52 = line_intersection(line2_r3, line1_f1)
    p53 = line_intersection(line2_r3, line2_f1)
    p54 = line_intersection(line2_r3, line1_f2)
    p55 = line_intersection(line2_r3, line2_f2)
    p56 = line_intersection(line2_r3, line1_f3)
    p57 = line_intersection(line2_r3, line2_f3)
    p58 = line_intersection(line2_r3, line1_f4)
    p59 = line_intersection(line2_r3, line2_f4)

    p61 = line_intersection(line1_r2, line_r1_r4)
    p62 = line_intersection(line1_r2, line1_f1)
    p63 = line_intersection(line1_r2, line2_f1)
    p64 = line_intersection(line1_r2, line1_f2)
    p65 = line_intersection(line1_r2, line2_f2)
    p66 = line_intersection(line1_r2, line1_f3)
    p67 = line_intersection(line1_r2, line2_f3)
    p68 = line_intersection(line1_r2, line1_f4)
    p69 = line_intersection(line1_r2, line2_f4)

    p71 = line_intersection(line2_r2, line_r1_r4)
    p72 = line_intersection(line2_r2, line1_f1)
    p73 = line_intersection(line2_r2, line2_f1)
    p74 = line_intersection(line2_r2, line1_f2)
    p75 = line_intersection(line2_r2, line2_f2)
    p76 = line_intersection(line2_r2, line1_f3)
    p77 = line_intersection(line2_r2, line2_f3)
    p78 = line_intersection(line2_r2, line1_f4)
    p79 = line_intersection(line2_r2, line2_f4)

    p81 = line_intersection(line1_r1, line_r1_r4)
    p82 = line_intersection(line1_r1, line1_f1)
    p83 = line_intersection(line1_r1, line2_f1)
    p84 = line_intersection(line1_r1, line1_f2)
    p85 = line_intersection(line1_r1, line2_f2)
    p86 = line_intersection(line1_r1, line1_f3)
    p87 = line_intersection(line1_r1, line2_f3)
    p88 = line_intersection(line1_r1, line1_f4)
    p89 = line_intersection(line1_r1, line2_f4)

    p91 = line_intersection(line2_r1, line_r1_r4)
    p92 = line_intersection(line2_r1, line1_f1)
    p93 = line_intersection(line2_r1, line2_f1)
    p94 = line_intersection(line2_r1, line1_f2)
    p95 = line_intersection(line2_r1, line2_f2)
    p96 = line_intersection(line2_r1, line1_f3)
    p97 = line_intersection(line2_r1, line2_f3)
    p98 = line_intersection(line2_r1, line1_f4)
    p99 = line_intersection(line2_r1, line2_f4)
    #------------------------------------------
    # Squares:
    #----------------------------------
    a1 = np.array([p81, p82, p92, p91])
    a2 = np.array([p71, p72, p82, p81])
    a3 = np.array([p61, p62, p72, p71])
    a4 = np.array([p51, p52, p62, p61])
    a5 = np.array([p41, p42, p52, p51])
    a6 = np.array([p31, p32, p42, p41])
    a7 = np.array([p21, p22, p32, p31])
    a8 = np.array([p11, p12, p22, p21])

    b1 = np.array([p82, p83, p93, p92])
    b2 = np.array([p72, p73, p83, p82])
    b3 = np.array([p62, p63, p73, p72])
    b4 = np.array([p52, p53, p63, p62])
    b5 = np.array([p42, p43, p53, p52])
    b6 = np.array([p32, p33, p43, p42])
    b7 = np.array([p22, p23, p33, p32])
    b8 = np.array([p12, p13, p23, p22])

    c1 = np.array([p83, p84, p94, p93])
    c2 = np.array([p73, p74, p84, p83])
    c3 = np.array([p63, p64, p74, p73])
    c4 = np.array([p53, p54, p64, p63])
    c5 = np.array([p43, p44, p54, p53])
    c6 = np.array([p33, p34, p44, p43])
    c7 = np.array([p23, p24, p34, p33])
    c8 = np.array([p13, p14, p24, p23])

    d1 = np.array([p84, p85, p95, p94])
    d2 = np.array([p74, p75, p85, p84])
    d3 = np.array([p64, p65, p75, p74])
    d4 = np.array([p54, p55, p65, p64])
    d5 = np.array([p44, p45, p55, p54])
    d6 = np.array([p34, p35, p45, p44])
    d7 = np.array([p24, p25, p35, p34])
    d8 = np.array([p14, p15, p25, p24])

    e1 = np.array([p85, p86, p96, p95])
    e2 = np.array([p75, p76, p86, p85])
    e3 = np.array([p65, p66, p76, p75])
    e4 = np.array([p55, p56, p66, p65])
    e5 = np.array([p45, p46, p56, p55])
    e6 = np.array([p35, p36, p46, p45])
    e7 = np.array([p25, p26, p36, p35])
    e8 = np.array([p15, p16, p26, p25])

    f1 = np.array([p86, p87, p97, p96])
    f2 = np.array([p76, p77, p87, p86])
    f3 = np.array([p66, p67, p77, p76])
    f4 = np.array([p56, p57, p67, p66])
    f5 = np.array([p46, p47, p57, p56])
    f6 = np.array([p36, p37, p47, p46])
    f7 = np.array([p26, p27, p37, p36])
    f8 = np.array([p16, p17, p27, p26])

    g1 = np.array([p87, p88, p98, p97])
    g2 = np.array([p77, p78, p88, p87])
    g3 = np.array([p67, p68, p78, p77])
    g4 = np.array([p57, p58, p68, p67])
    g5 = np.array([p47, p48, p58, p57])
    g6 = np.array([p37, p38, p48, p47])
    g7 = np.array([p27, p28, p38, p37])
    g8 = np.array([p17, p18, p28, p27])

    h1 = np.array([p88, p89, p99, p98])
    h2 = np.array([p78, p79, p89, p88])
    h3 = np.array([p68, p69, p79, p78])
    h4 = np.array([p58, p59, p69, p68])
    h5 = np.array([p48, p49, p59, p58])
    h6 = np.array([p38, p39, p49, p48])
    h7 = np.array([p28, p29, p39, p38])
    h8 = np.array([p18, p19, p29, p28])