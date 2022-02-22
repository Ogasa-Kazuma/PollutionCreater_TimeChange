import math

class Point:

    def __init__(self, x, y):
        self.__x = x
        self.__y = y


    def GetX(self):
        return self.__x


    def GetY(self):
        return self.__y


    def distance(self, point):
        if(not type(point) == Point):
            raise TypeError("座標クラス以外とは距離を計算できません")

        start_x = self.GetX()
        last_x = point.GetX()
        start_y = self.GetY()
        last_y = point.GetY()

        distance = math.sqrt((last_x - start_x) ** (2) + (last_y - start_y) ** (2))

        return distance
