
############################ ライブラリ ###################################

#システム関連モジュール
import importlib
import sys
import os
from pathlib import Path

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
import Origin_Creater

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

importlib.reload(Origin_Creater)

importlib.reload(Origin_History_Creater)

#######################################################################



#########################################################################################
def main():

    #データ保存用のディレクトリを作成
    dirMaker = Directory_Maker.DirectoryMaker()
    dailyNameDirMaker = Daily_Name_Directory_Maker.DailyNameDirectoryMaker(dirMaker)
    saveDir = dailyNameDirMaker.MkDir("DataLog")

    #探索モデルのパラメータ
    fieldX = 100
    fieldY = 100
    searchingFirstTime = 1000
    searchingLastTime = 4000

    pollutions = np.zeros((fieldX, fieldY))




#############汚染源を作成####################
    origins = list()
    historyCreater = Origin_History_Creater.OriginHistoryCreater()
    originCreater = Origin_Creater.OriginCreater(Pollution_Origin.PollutionOrigin, historyCreater)

    origin1 = originCreater.Create(dict(x = 0, y = 80, startHistory = 100,\
                        t_max = 4000, maxCycleTime = 20, changePerSec = 1))
    origin2 = originCreater.Create(dict(x = 0, y = 10, startHistory = 100,\
                        t_max = 4000, maxCycleTime = 20, changePerSec = 1))
    origins.append(origin1)
    origins.append(origin2)
##################################################




 ########################## 時間変化に応じた濃度分布を計算 #####################################

    decreasingRatio = 1 #汚染源中心からの距離と濃度の減少比
    flowSpeed_ms = 1 #流れの速度




    allPollutions = Pollution([[0 for y in range(fieldY)] for x in range(fieldX)])
        #1秒分の濃度分布変化を計算、保存
    for origin_i in origins:
        calculator = CalculatorOfPollutionsAroundOrigin(origin_i)
        pollutionsDist = calculator.CalcDist(fieldX, fieldY, 1000, decreasingRatio, flowSpeed_ms)
        allPollutions.Add(pollutionsDist)
        #複数の汚染源を足し合わせる

    allPollutions.View()




################################################################################


if __name__ == "__main__":
    main()
