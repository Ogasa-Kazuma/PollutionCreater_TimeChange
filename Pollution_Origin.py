
import importlib
import PointClass
importlib.reload(PointClass)

class PollutionOrigin:


    def __init__(self, point, history):

        print(type(point))
        if(not type(point) == PointClass.Point):
            raise ValueError('座標オブジェクトを引数に指定してください')

        self.__point = point
        self.__history = history

    def Distance(self, point_away_from_origin):
        #learn
        if(not type(point_away_from_origin) == PointClass.Point):
            raise ValueError('座標オブジェクトを引数に指定してください')
        return self.__point.distance(point_away_from_origin)

    def History(self, time):
        if(time < 0):
            return 0
        #learn
        return self.__history[int(time)]
