

import copy

import numpy as np
import importlib
import math
import Pollution_Origin
from Pollution_Origin import PollutionOrigin

import Pollution
importlib.reload(Pollution)
from Pollution import Pollution

importlib.reload(Pollution_Origin)

import PointClass
importlib.reload(PointClass)




class CalculatorOfPollutionsAroundOrigin:

    def __init__(self):
        pass


    def CalcDist(self, origin, xlim_m, ylim_m, time_sec, decreasingRatio, flowSpeed_ms):
        """汚染源周りの汚染濃度についての時間変化を計算するメソッド"""
        pollutionsDist = np.zeros((xlim_m, ylim_m))


        for x_i in range(xlim_m):
            for y_i in range(ylim_m):
                pollutionPoint = PointClass.Point(x_i, y_i)
                distanceFromOrigin_m = origin.Distance(pollutionPoint)

                t_ref = time_sec - distanceFromOrigin_m / flowSpeed_ms #何秒前の汚染源中心の濃度を参考にするか
                decAmount =  decreasingRatio * distanceFromOrigin_m
                pollutionsDist[x_i][y_i] = origin.History(t_ref) - decAmount

                #汚染源の影響が及ばない範囲
                if(pollutionsDist[x_i][y_i] < 0):
                    pollutionsDist[x_i][y_i] = 0

        return Pollution(pollutionsDist)


    def __CalculateAbsoluteDistance(self, xBegin, yBegin, xEnd, yEnd):

        diff = math.sqrt((xEnd - xBegin) * (xEnd - xBegin) + (yEnd- yBegin) * (yEnd - yBegin))

        return  diff
