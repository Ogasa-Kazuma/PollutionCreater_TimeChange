
import importlib

import PointClass
importlib.reload(PointClass)

import random

class PollutionOriginDataCreater:

    def __init__(self):
        pass

    def Create(self, x, y, startPollution, maxTime, maxCycleTime, maxChangePerSec):

        #リストと明示した方がよい
        pollutionHistory = [startPollution]
        t = 0

        while(t < maxTime):
            #濃度履歴の最大時間まで濃度の増減を繰り返す
            cycleTime = self.__DecideCycleTime(t, maxTime, maxCycleTime)
            pollutionHistory = self.__IncreasePollution(pollutionHistory, cycleTime, maxChangePerSec)
            pollutionHistory = self.__DecreasePollution(pollutionHistory, cycleTime, maxChangePerSec)
            t += cycleTime * 2

        #なんか分かりづらい
        origin = self.Origin(PointClass.Point(x, y), pollutionHistory)

        return origin



    def __DecideCycleTime(self, nowTime, maxTime, maxCycleTime):
        """濃度履歴の最大時間を超えてしまわないようサイクルタイムを調整"""
        cycleTime = random.randint(0, maxCycleTime + 1)
        nextFinishTime = nowTime + cycleTime

        if(nextFinishTime > maxTime):
            cycleTime -= nextFinishTime - maxTime
            return cycleTime

        return cycleTime



    def __IncreasePollution(self, history, cycleTime, maxChangePerSec):
        """1サイクルでの濃度変化量を計算"""
        for t_i in range(0, cycleTime):

            history.append(history[-1] + random.uniform(0, maxChangePerSec))

        return history



    def __DecreasePollution(self, history, cycleTime, maxChangePerSec):
        """1サイクルでの濃度変化量を計算"""
        for t_i in range(0, cycleTime):

            history.append(history[-1] - random.uniform(0, maxChangePerSec))

        return history



    #内部クラス
    class Origin:


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
