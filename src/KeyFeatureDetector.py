import cv2 as cv
import numpy as np
import math

class KeyFeatureDetector():

    def __init__(self):
        self._image = None
        self._image_gray = None
        self._corners = np.array(list())
        self._angle = np.array(list())
        self._vertices = np.array(list())
        self._facts = []

    def _reset(self):
        self.__init__()

    def _read_file(self,file):
        self._image = cv.imread(file)
        self._image_gray = cv.cvtColor(self._image, cv.COLOR_BGR2GRAY)

    def _detect_corner(self):
        self._corners = np.array(list())
        self._angle = np.array(list())
        self._vertices = np.array(list())
        if(True):
            ret,thresh = cv.threshold(self._image_gray,150,255,cv.THRESH_BINARY)
            contours, hierarchy = cv.findContours(thresh,cv.RETR_TREE,cv.CHAIN_APPROX_NONE)

            contour = contours[0]
            size = cv.contourArea(contour)
            rect = cv.minAreaRect(contour)

            peri = cv.arcLength(contour, True)
            self._corners = cv.approxPolyDP(contour, 0.001 * peri, True)
            self._image = cv.drawContours(self._image, [self._corners], 0, (0,255,0), 3)
            
            # Detect Angle Magnitude
            for i in range(0,self._corners.shape[0]):

                vA = self._corners[i] - self._corners[(i-1)%self._corners.shape[0]]
                vB = self._corners[i] - self._corners[(i+1)%self._corners.shape[0]]

                dotProduct = vA[0].dot(vB[0])
                magVA = np.linalg.norm(vA[0])
                magVB = np.linalg.norm(vB[0])
                
                angleMag = math.degrees(np.arccos(dotProduct/(magVA*magVB)))
                self._angle = np.append(self._angle,angleMag)

    def _find_vertices(self):
        for i in range(0,self._corners.shape[0]):
            v = self._corners[i] - self._corners[(i+1)%self._corners.shape[0]]

            magV = np.linalg.norm(v[0])

            self._vertices = np.append(self._vertices,magV)

    def _get_corners(self):
        return self._corners
    
    def _get_angles(self):
        return self._angle

    def _get_image(self):
        return self._image
    
    def _show_image(self):
        print(self._corners)
        print(self._angle)
        print(self._vertices)
        cv.imshow('image', self._image)
        cv.waitKey(0)
        cv.destroyAllWindows

    def _get_facts(self):
        return self._facts

    def _extract_fact(self):

        self._facts = []
        # Jumlah Sudut
        self._facts.append("(jumlahsudut " + str(len(self._corners)) + ")")

        # Jumlah Sudut Sama,Jumlah siku, Jumlah Tumpul, Jumlah Lancip
        jumlah_sudut_sama_terbanyak = 0
        jumlah_sudut_sama = 0
        jumlah_siku = 0
        jumlah_tumpul = 0
        jumlah_lancip = 0
        for sudut in self._angle:
            jumlah_sudut_sama = 0
            for x in self._angle:
                if x == sudut:
                    jumlah_sudut_sama = jumlah_sudut_sama + 1
            
            if jumlah_sudut_sama_terbanyak < jumlah_sudut_sama:
                jumlah_sudut_sama_terbanyak = jumlah_sudut_sama

            if sudut == 90:
                jumlah_siku = jumlah_siku + 1
            elif sudut < 90:
                jumlah_lancip = jumlah_lancip + 1
            else :
                jumlah_tumpul = jumlah_tumpul + 1
        
        self._facts.append("(jumlahsudutsama " + str(jumlah_sudut_sama_terbanyak) + ")")
        self._facts.append("(jumlahsudutsiku " + str(jumlah_siku) + ")")
        self._facts.append("(jumlahsudutlancip " + str(jumlah_lancip) + ")")
        self._facts.append("(jumlahsuduttumpul " + str(jumlah_tumpul) + ")")

        # Jumlah Sisi Sama
        jumlah_sisi_sama = 0
        jumlah_sisi_sama_terbanyak = 0
        for sisi in self._vertices:
            jumlah_sisi_sama = 0
            for x in self._vertices:
                if x == sisi:
                    jumlah_sisi_sama = jumlah_sisi_sama + 1
            
            if jumlah_sisi_sama_terbanyak < jumlah_sisi_sama:
                jumlah_sisi_sama_terbanyak = jumlah_sisi_sama
        
        self._facts.append("(jumlahsisisama " + str(jumlah_sisi_sama_terbanyak) + ")")

        print(self._facts)
        return self._facts


if __name__ == "__main__":
    Detector = KeyFeatureDetector('shapes/segitiga_tumpul.png')
    Detector._read_file()
    Detector._detect_corner()
    Detector._show_image()