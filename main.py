
############################ ライブラリ ###################################

#システム関連モジュール
import importlib
import sys
import os
from pathlib import Path

import PointClass
importlib.reload(PointClass)

sys.path.append(os.pardir + "/Python")
#描画モジュール
import matplotlib.pyplot as plt


#計算用モジュール
import random
import numpy as np
import math

#コンテナ管理用モジュール
from itertools import chain
import copy

#汚染源モジュール
import Pollution_Origin
from Pollution_Origin import PollutionOrigin


#汚染の時間変化計算モジュール
import Calculator_Of_Pollutions_Around_Origin
from Calculator_Of_Pollutions_Around_Origin import CalculatorOfPollutionsAroundOrigin
import Origin_History_Creater


#時間モジュール
import time
import datetime




import Pollution
importlib.reload(Pollution)
from Pollution import Pollution

#モジュールの内容の変更を適用
importlib.reload(Pollution_Origin)
importlib.reload(Calculator_Of_Pollutions_Around_Origin)

import Pollution_Origin_Data_Creater
importlib.reload(Pollution_Origin_Data_Creater)

importlib.reload(Origin_History_Creater)


#######################################################################



#########################################################################################
def main():


    #探索モデルのパラメータ
    fieldX = 100
    fieldY = 100
    searchingFirstTime = 1000
    searchingLastTime = 4000


#############汚染源を作成####################
    origins = list()
    historyCreater = Origin_History_Creater.OriginHistoryCreater()
    originCreater = Pollution_Origin_Data_Creater.PollutionOriginDataCreater()


    origin1 = originCreater.Create(x = 0, y = 80, startPollution = 100,\
                        maxTime = 4000, maxCycleTime = 20, maxChangePerSec = 1)

    origin2 = originCreater.Create(x = 0, y = 10, startPollution = 100,\
                        maxTime = 4000, maxCycleTime = 20, maxChangePerSec = 1)

    origins.append(origin1)
    origins.append(origin2)
##################################################




 ########################## 時間変化に応じた濃度分布を計算 #####################################

    decreasingRatio = 1 #汚染源中心からの距離と濃度の減少比
    flowSpeed_ms = 1 #流れの速度




    allPollutions = Pollution([[0 for y in range(fieldY)] for x in range(fieldX)])

    calculator = CalculatorOfPollutionsAroundOrigin()
        #1秒分の濃度分布変化を計算、保存
    for origin_i in origins:

        pollutionsDist = calculator.CalcDist(origin_i, fieldX, fieldY, 100, decreasingRatio, flowSpeed_ms)
        allPollutions.Add(pollutionsDist)
        #複数の汚染源を足し合わせる

    allPollutions.View()
    allPollutions.Save("DataLog/unko2.csv", 'csv')




################################################################################


if __name__ == "__main__":
    main()
