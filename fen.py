import cv2
import numpy as np

class FEN:

    def __init__(self, pieces, squares):
        self.pieces = pieces
        self.squares = squares
    
    def calculateMartix(self):
        matrix = [['*', '*', '*', '*', '*', '*', '*', '*'],
          ['*', '*', '*', '*', '*', '*', '*', '*'],
          ['*', '*', '*', '*', '*', '*', '*', '*'],
          ['*', '*', '*', '*', '*', '*', '*', '*'],
          ['*', '*', '*', '*', '*', '*', '*', '*'],
          ['*', '*', '*', '*', '*', '*', '*', '*'],
          ['*', '*', '*', '*', '*', '*', '*', '*'],
          ['*', '*', '*', '*', '*', '*', '*', '*']]
        for piece in self.pieces:
            name = piece[0]
            point = (int(piece[1]), int(piece[2]))
            # find where the piece is:
            # rank 8:
            if cv2.pointPolygonTest(np.array([self.squares.p11, self.squares.p19, self.squares.p29, self.squares.p21]), point, False) >= 0:
                if cv2.pointPolygonTest(self.squares.a8, point, False) >= 0:
                    matrix[0][0] = name
                elif cv2.pointPolygonTest(self.squares.b8, point, False) >= 0:
                    matrix[0][1] = name
                elif cv2.pointPolygonTest(self.squares.c8, point, False) >= 0:
                    matrix[0][2] = name
                elif cv2.pointPolygonTest(self.squares.d8, point, False) >= 0:
                    matrix[0][3] = name
                elif cv2.pointPolygonTest(self.squares.e8, point, False) >= 0:
                    matrix[0][4] = name
                elif cv2.pointPolygonTest(self.squares.f8, point, False) >= 0:
                    matrix[0][5] = name
                elif cv2.pointPolygonTest(self.squares.g8, point, False) >= 0:
                    matrix[0][6] = name
                else:
                    matrix[0][7] = name

            # rank 7:
            elif cv2.pointPolygonTest(np.array([self.squares.p21, self.squares.p29, self.squares.p39, self.squares.p31]), point, False) >= 0:
                if cv2.pointPolygonTest(self.squares.a7, point, False) >= 0:
                    matrix[1][0] = name
                elif cv2.pointPolygonTest(self.squares.b7, point, False) >= 0:
                    matrix[1][1] = name
                elif cv2.pointPolygonTest(self.squares.c7, point, False) >= 0:
                    matrix[1][2] = name
                elif cv2.pointPolygonTest(self.squares.d7, point, False) >= 0:
                    matrix[1][3] = name
                elif cv2.pointPolygonTest(self.squares.e7, point, False) >= 0:
                    matrix[1][4] = name
                elif cv2.pointPolygonTest(self.squares.f7, point, False) >= 0:
                    matrix[1][5] = name
                elif cv2.pointPolygonTest(self.squares.g7, point, False) >= 0:
                    matrix[1][6] = name
                else:
                    matrix[1][7] = name

            # rank 6:
            elif cv2.pointPolygonTest(np.array([self.squares.p31, self.squares.p39, self.squares.p49, self.squares.p41]), point, False) >= 0:
                if cv2.pointPolygonTest(self.squares.a6, point, False) >= 0:
                    matrix[2][0] = name
                elif cv2.pointPolygonTest(self.squares.b6, point, False) >= 0:
                    matrix[2][1] = name
                elif cv2.pointPolygonTest(self.squares.c6, point, False) >= 0:
                    matrix[2][2] = name
                elif cv2.pointPolygonTest(self.squares.d6, point, False) >= 0:
                    matrix[2][3] = name
                elif cv2.pointPolygonTest(self.squares.e6, point, False) >= 0:
                    matrix[2][4] = name
                elif cv2.pointPolygonTest(self.squares.f6, point, False) >= 0:
                    matrix[2][5] = name
                elif cv2.pointPolygonTest(self.squares.g6, point, False) >= 0:
                    matrix[2][6] = name
                else:
                    matrix[2][7] = name

            # rank 5:
            elif cv2.pointPolygonTest(np.array([self.squares.p41, self.squares.p49, self.squares.p59, self.squares.p51]), point, False) >= 0:
                if cv2.pointPolygonTest(self.squares.a5, point, False) >= 0:
                    matrix[3][0] = name
                elif cv2.pointPolygonTest(self.squares.b5, point, False) >= 0:
                    matrix[3][1] = name
                elif cv2.pointPolygonTest(self.squares.c5, point, False) >= 0:
                    matrix[3][2] = name
                elif cv2.pointPolygonTest(self.squares.d5, point, False) >= 0:
                    matrix[3][3] = name
                elif cv2.pointPolygonTest(self.squares.e5, point, False) >= 0:
                    matrix[3][4] = name
                elif cv2.pointPolygonTest(self.squares.f5, point, False) >= 0:
                    matrix[3][5] = name
                elif cv2.pointPolygonTest(self.squares.g5, point, False) >= 0:
                    matrix[3][6] = name
                else:
                    matrix[3][7] = name

            # rank 4:
            elif cv2.pointPolygonTest(np.array([self.squares.p51, self.squares.p59, self.squares.p69, self.squares.p61]), point, False) >= 0:
                if cv2.pointPolygonTest(self.squares.a4, point, False) >= 0:
                    matrix[4][0] = name
                elif cv2.pointPolygonTest(self.squares.b4, point, False) >= 0:
                    matrix[4][1] = name
                elif cv2.pointPolygonTest(self.squares.c4, point, False) >= 0:
                    matrix[4][2] = name
                elif cv2.pointPolygonTest(self.squares.d4, point, False) >= 0:
                    matrix[4][3] = name
                elif cv2.pointPolygonTest(self.squares.e4, point, False) >= 0:
                    matrix[4][4] = name
                elif cv2.pointPolygonTest(self.squares.f4, point, False) >= 0:
                    matrix[4][5] = name
                elif cv2.pointPolygonTest(self.squares.g4, point, False) >= 0:
                    matrix[4][6] = name
                else:
                    matrix[4][7] = name

            # rank 3:
            elif cv2.pointPolygonTest(np.array([self.squares.p61, self.squares.p69, self.squares.p79, self.squares.p71]), point, False) >= 0:
                if cv2.pointPolygonTest(self.squares.a3, point, False) >= 0:
                    matrix[5][0] = name
                elif cv2.pointPolygonTest(self.squares.b3, point, False) >= 0:
                    matrix[5][1] = name
                elif cv2.pointPolygonTest(self.squares.c3, point, False) >= 0:
                    matrix[5][2] = name
                elif cv2.pointPolygonTest(self.squares.d3, point, False) >= 0:
                    matrix[5][3] = name
                elif cv2.pointPolygonTest(self.squares.e3, point, False) >= 0:
                    matrix[5][4] = name
                elif cv2.pointPolygonTest(self.squares.f3, point, False) >= 0:
                    matrix[5][5] = name
                elif cv2.pointPolygonTest(self.squares.g3, point, False) >= 0:
                    matrix[5][6] = name
                else:
                    matrix[5][7] = name
            
            # rank 2:
            elif cv2.pointPolygonTest(np.array([self.squares.p71, self.squares.p79, self.squares.p89, self.squares.p81]), point, False) >= 0:
                if cv2.pointPolygonTest(self.squares.a2, point, False) >= 0:
                    matrix[6][0] = name
                elif cv2.pointPolygonTest(self.squares.b2, point, False) >= 0:
                    matrix[6][1] = name
                elif cv2.pointPolygonTest(self.squares.c2, point, False) >= 0:
                    matrix[6][2] = name
                elif cv2.pointPolygonTest(self.squares.d2, point, False) >= 0:
                    matrix[6][3] = name
                elif cv2.pointPolygonTest(self.squares.e2, point, False) >= 0:
                    matrix[6][4] = name
                elif cv2.pointPolygonTest(self.squares.f2, point, False) >= 0:
                    matrix[6][5] = name
                elif cv2.pointPolygonTest(self.squares.g2, point, False) >= 0:
                    matrix[6][6] = name
                else:
                    matrix[6][7] = name

            # rank 1:
            elif cv2.pointPolygonTest(np.array([self.squares.p81, self.squares.p89, self.squares.p99, self.squares.p91]), point, False) >= 0:
                if cv2.pointPolygonTest(self.squares.a1, point, False) >= 0:
                    matrix[7][0] = name
                elif cv2.pointPolygonTest(self.squares.b1, point, False) >= 0:
                    matrix[7][1] = name
                elif cv2.pointPolygonTest(self.squares.c1, point, False) >= 0:
                    matrix[7][2] = name
                elif cv2.pointPolygonTest(self.squares.d1, point, False) >= 0:
                    matrix[7][3] = name
                elif cv2.pointPolygonTest(self.squares.e1, point, False) >= 0:
                    matrix[7][4] = name
                elif cv2.pointPolygonTest(self.squares.f1, point, False) >= 0:
                    matrix[7][5] = name
                elif cv2.pointPolygonTest(self.squares.g1, point, False) >= 0:
                    matrix[7][6] = name
                else:
                    matrix[7][7] = name
        return matrix
    def calculateFen(matrix):
        fen = ''
        for i, rank in enumerate(matrix):
            empty = 0
            for j, square in enumerate(rank):
                if square == '*':
                    empty += 1
                if j == 7:
                    fen += str(empty)
                elif empty != 0:
                    fen += str(empty) + square
                    empty = 0
                else:
                    fen += square
            if i < 7:
                fen += '/'
            fen += ' w KQkq - 0 1'
        return fen
