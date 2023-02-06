from ultralytics import YOLO
import argparse
import cv2
import numpy as np
from squares import Squares
from fen import FEN

# Loading the models
pieces_model = YOLO('pieces_yolov8.pt')
only_board_model = YOLO('only_board_yolov8.pt')
rank_file_model = YOLO('board_yolov8.pt')

# Function to calculate the matrix of each piece
# each piece has [name, x, y], so that (x, y) the refrence point of that piece
def calculatePiecesMatrix(pieces_result):
    def findClassName(cls):
        className = ''
        if cls == 0:
            className = 'b'
        elif cls == 1:
            className = 'k'
        elif cls == 2:
            className = 'n'
        elif cls == 3:
            className = 'p'
        elif cls == 4:
            className = 'q'
        elif cls == 5:
            className = 'r'
        elif cls == 6:
            className = 'B'
        elif cls == 7:
            className = 'K'
        elif cls == 8:
            className = 'N'
        elif cls == 9:
            className = 'P'
        elif cls == 10:
            className = 'Q'
        elif cls == 11:
            className = 'R'
        return className
    pieces = []
    for box in pieces_result[0].boxes:
        if box.conf < 0.3:
            continue
        coordinates = box.xywh
        x = coordinates[0][0].item()
        y = coordinates[0][1].item()
        w = coordinates[0][2].item()
        h = coordinates[0][3].item()
        ref_x = x
        ref_y = y + h/4
        className = findClassName(box.cls.item())
        piece = np.array([className, int(ref_x), int(ref_y)])
        pieces.append(piece)
    return pieces

# rectify the image based on the four corners
def rectify_image(img, pt1, pt2, pt3, pt4):
    # Warping the image:
    srcTri = np.array( [pt1, pt2, pt3, pt4] ).astype(np.float32)
    dstTri = np.array( [[0, 0], [img.shape[0], 0], [0, img.shape[1]], [img.shape[0], img.shape[1]]] ).astype(np.float32)
    matrix = cv2.getPerspectiveTransform(srcTri, dstTri)
    warp_dst = cv2.warpPerspective(img, matrix, (img.shape[1], img.shape[0]))
    matrix = matrix.astype(np.float32)
    #cv2.imwrite('rectified_img.jpg', warp_dst)
    return matrix, warp_dst

def updatePiecesMatrix(pieces, matrics):
    # calculate the refrence points of the pieces on the rectified image
    for piece in pieces:
        point = np.array([[[piece[1], piece[2]]]]).astype(np.float32)
        transformed_point = cv2.perspectiveTransform(point, matrics)
        x_new = transformed_point[0, 0, 0]
        y_new = transformed_point[0, 0, 1]
        piece[1] = int(x_new)
        piece[2] = int(y_new)
    return pieces

def calculateFourCorners(only_board_result):
    # calculate two points randomly from line in the edge
    pointsl1 = [point for point in only_board_result[0].masks.segments[0] if point[0] * 640 <= 320 and point[1] * 640 in range(200, 300)]
    pointsl2 = [point for point in only_board_result[0].masks.segments[0] if point[0] * 640 <= 320 and point[1] * 640 in range(400, 500)]
    pointsr1 = [point for point in only_board_result[0].masks.segments[0] if point[0] * 640 >= 320 and point[1] * 640 in range(200, 300)]
    pointsr2 = [point for point in only_board_result[0].masks.segments[0] if point[0] * 640 >= 320 and point[1] * 640 in range(400, 500)]
    pointsu1 = [point for point in only_board_result[0].masks.segments[0] if point[0] * 640 in range(150, 300) and point[1] * 640 <= 320]
    pointsu2 = [point for point in only_board_result[0].masks.segments[0] if point[0] * 640 in range(400, 500) and point[1] * 640 <= 320]
    pointsd1 = [point for point in only_board_result[0].masks.segments[0] if point[0] * 640 in range(100, 300) and point[1] * 640 >= 320]
    pointsd2 = [point for point in only_board_result[0].masks.segments[0] if point[0] * 640 in range(400, 600) and point[1] * 640 >= 320]

    pointsu1 = only_board_result[0].masks.segments[0][0]
    pointsu2 = np.array([pointsu1[0]*640 + 300, pointsu1[1]*640])

    blank = np.zeros((640, 640, 3), dtype='uint8')

    ### main function to draw lines between two points
    def drawLine(image,p1,p2):
        ### function to find slope 
        def slope(p1,p2):
            x1,y1=p1
            x2,y2=p2
            if x2!=x1:
                return((y2-y1)/(x2-x1))
            else:
                return 'NA'
        x1,y1=p1
        x2,y2=p2
        ### finding slope
        m=slope(p1,p2)
        ### getting image shape
        h,w=image.shape[:2]

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
            px,py=x1,0
            qx,qy=x1,h
        cv2.line(image, (int(px), int(py)), (int(qx), int(qy)), (255, 255, 255), 1)
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

    left_line = drawLine(blank, (pointsl1[0][0]*640, pointsl1[0][1]*640), (pointsl2[0][0]*640, pointsl2[0][1]*640))
    right_line = drawLine(blank, (pointsr1[0][0]*640, pointsr1[0][1]*640), (pointsr2[0][0]*640, pointsr2[0][1]*640))
    #up_line = drawLine(blank, (pointsl1[0][0]*640, pointsl1[0][1]*640), (pointsl2[0][0]*640, pointsl2[0][1]*640))
    up_line = drawLine(blank, (pointsu1[0]*640, pointsu1[1]*640), (pointsu2[0], pointsu2[1]))
    down_line = drawLine(blank, (pointsd1[0][0]*640, pointsd1[0][1]*640), (pointsd2[0][0]*640, pointsd2[0][1]*640))

    # calculate the four corners
    point_leftup = line_intersection(left_line, up_line)
    point_leftdown = line_intersection(left_line, down_line)
    point_rightup = line_intersection(right_line, up_line)
    point_rightdown = line_intersection(right_line, down_line)

    cv2.circle(blank, point_rightup, 5, (0, 0, 255), -1)
    cv2.circle(blank, point_rightdown, 5, (0, 0, 255), -1)
    cv2.circle(blank, point_leftup, 5, (0, 0, 255), -1)
    cv2.circle(blank, point_leftdown, 5, (0, 0, 255), -1)

    return point_leftup, point_rightup, point_leftdown, point_rightdown

def run(input='retest2.jpg', model='only_board'):
    detect_board = False
    input = str(input)
    model = str(model)
    board = Squares() 
    fen_obj = FEN()

    # if the input is a photo
    if input.endswith('.png') or input.endswith('jpg'):
        img = cv2.imread(input)
        img = cv2.resize(img, (640, 640))

        pieces_result = pieces_model.predict(input)

        # calculate pieces matrix
        pieces = calculatePiecesMatrix(pieces_result)

        if model == 'only_board':
            only_board_result = only_board_model.predict(img)
            board.model = 'only_board'

            # calculate the four corners
            pt1, pt2, pt3, pt4 = calculateFourCorners(only_board_result)

            # calculate rectified image
            matrics, rec_img = rectify_image(img, pt1, pt2, pt3, pt4)

            # update pieces matrix
            up_pieces = updatePiecesMatrix(pieces, matrics)

            board.img = rec_img
            fen_obj.pieces = up_pieces
            fen_obj.squares = board
            matrix = fen_obj.calculateMartix()
            fen = fen_obj.calculateFen(matrix)
            print(fen)
            
        # TODO
        else:
            rank_file_result = rank_file_model.predict(img)
            board.model = 'rank_file'
            board.img = img

    # if the input is a video or '0' for webcam
    else:
        cap = cv2.VideoCapture(source=input)
        while True:
            ret, frame = cap.read()
            frame = cv2.resize(frame, (640, 640))

            # if can't read frame
            if not ret:
                print("Can't receive frame (stream end?). Exiting ...")
                break
            #---------------------------------------
            # if there is a movement:
            #   move = True
            #   continue
            # if there is no movement after a movement:
            #   move = False
            #   
            #---------------------------------------
            pieces_result = pieces_model.predict(frame)
            # calculate pieces matrix
            pieces = calculatePiecesMatrix(pieces_result)

            # detecting the board for the first time
            if not detect_board:
                if model == 'only_board':
                    only_board_result = only_board_model.predict(frame)
                    board.model = 'only_board'

                    # calculate the four corners
                    pt1, pt2, pt3, pt4 = calculateFourCorners(only_board_result)

                    # calculate rectified image
                    matrics, rec_img = rectify_image(img, pt1, pt2, pt3, pt4)

                    # update pieces matrix
                    up_pieces = updatePiecesMatrix(pieces, matrics)

                    board.img = rec_img
                    fen_obj.pieces = up_pieces
                    fen_obj.squares = board
                    matrix = fen_obj.calculateMartix()
                    fen = fen_obj.calculateFen(matrix)
                else:
                    rank_file_result = rank_file_model.predict(frame)
                detect_board = True
            if cv2.waitKey(1) == ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', help='image or video path, 0 for webcam', default='retest2.jpg')
    parser.add_argument('--model', help='(only_board) or (rank_file)', default='only_board')
    args = parser.parse_args()
    return args

def main(args):
    run(**vars(args))

if __name__== "__main__":
    args = parse_args()
    main(args)
