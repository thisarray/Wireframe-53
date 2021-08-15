from pgzero.builtins import Actor
from shapely.geometry import Polygon
from shapely.affinity import translate
from Listing03_ForegroundNames import foregroundNames
from Listing05_ForegroundMap import foregroundMap
from Listing07_ForegroundPolygons import foregroundPolygons

foregroundBiggestObjectHalfXSize = 206

class Foreground:
    def __init__(self):
        self.elements = []
        self.indexes = []
        self.mapElement = 0
        self.polygons = []
    def draw(self):
        for element in self.elements:
            element.draw()
    def update(self, globalTime):
        for i in reversed(range(len(self.elements))):
            self.elements[i].x -= 1
            if self.elements[i].x < -foregroundBiggestObjectHalfXSize:
                del self.elements[i]
                del self.indexes[i]
        if self.mapElement < len(foregroundMap):
            while foregroundMap[self.mapElement][1] < globalTime + 800 + foregroundBiggestObjectHalfXSize:
                self.indexes.append(foregroundMap[self.mapElement][0])
                self.elements.append(Actor(foregroundNames[foregroundMap[self.mapElement][0]], (foregroundMap[self.mapElement][1] - globalTime, foregroundMap[self.mapElement][2])))
                self.mapElement += 1
                if self.mapElement >= len(foregroundMap):
                    break
        self.polygons = []
        for i in range(len(self.indexes)):
            polygon = translate(Polygon(foregroundPolygons[self.indexes[i]]), self.elements[i].x, self.elements[i].y)
            self.polygons.append(polygon)
