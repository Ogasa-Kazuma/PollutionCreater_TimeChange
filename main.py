
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




#汚染の時間変化計算モジュール
import Calculator_Of_Pollutions_Around_Origin
from Calculator_Of_Pollutions_Around_Origin import CalculatorOfPollutionsAroundOrigin

importlib.reload(Calculator_Of_Pollutions_Around_Origin)

#時間モジュール
import time
import datetime




import Pollution
importlib.reload(Pollution)
from Pollution import Pollution

#モジュールの内容の変更を適用


import Pollution_Origin_Data_Creater
importlib.reload(Pollution_Origin_Data_Creater)

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






    calculator = CalculatorOfPollutionsAroundOrigin()
        #1秒分の濃度分布変化を計算、保存

    for t_i in range(1, 100):
        allPollutions = Pollution([[0 for y in range(fieldY)] for x in range(fieldX)])
        for origin_i in origins:
            pollutionsDist = calculator.CalcDist(origin_i, fieldX, fieldY, t_i, decreasingRatio, flowSpeed_ms)
            allPollutions.Add(pollutionsDist)
        allPollutions.Save("DataLog/unko2.pkl", 'pkl')
            #複数の汚染源を足し合わせる
        #allPollutions.View()






################################################################################


if __name__ == "__main__":
    main()
