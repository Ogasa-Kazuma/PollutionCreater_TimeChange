
############################ ライブラリ ###################################

#システム関連モジュール
import importlib
import sys
import os
from pathlib import Path

import PointClass
importlib.reload(PointClass)

sys.path.append(os.pardir + "/Python")
sys.path.append(os.pardir)
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


def CreateGraphObject():
    fig = plt.figure()
    graph_object = fig.add_subplot(111)
    return graph_object





#########################################################################################
def main():



    #濃度分布モデルのサイズ
    fieldX = 100
    fieldY = 100


#############汚染源と汚染源の濃度履歴を作成####################
    #ここで行っていることの意味は論文を参考にしてください
    #汚染源の位置において、どの時刻でどのような濃度だったか、という履歴を作成します。
    originCreater = Pollution_Origin_Data_Creater.PollutionOriginDataCreater()

    #maxCycleTimeは、濃度が上がるか、下がるかのサイクルの最大秒数の調整をします(サイクルは最大秒数を上限としてランダムに決定します)
    #maxChangePerSecは、一秒で最大どれくらい濃度変化があるかを設定します（ランダムに設定します）
    origin1 = originCreater.Create(x = 0, y = 80, startPollution = 100,\
                        maxTime = 4000, maxCycleTime = 20, maxChangePerSec = 1)

    origin2 = originCreater.Create(x = 0, y = 10, startPollution = 100,\
                        maxTime = 4000, maxCycleTime = 20, maxChangePerSec = 1)

    #２つの汚染源をまとめる
    originList = [origin1, origin2]
##################################################




 ########################## 時間変化に応じた濃度分布を計算 #####################################


    decreasingRatio = 1 #汚染源中心からの距離と濃度の減少比
    flowSpeed_ms = 1 #流れの速度

    #汚染源周辺の濃度分布を計算するオブジェクト
    calculator = CalculatorOfPollutionsAroundOrigin()

    #ファイル名に目印をつける
    fileHeadName = input()

    #1秒分の濃度分布変化を計算、保存
    #timeは汚染物質の排出が始まってからの時間を示す
    time_start = 0
    time_last = 100

    for t_i in range(time_start, time_last):
        #全体の濃度分布を格納するためのPollutionオブジェクトを生成(この時点では空)
        allPollutions = Pollution([[0 for y in range(fieldY)] for x in range(fieldX)])

        for origin_i in originList: #汚染源一つ一つの周辺の濃度分布を計算

            #1つの汚染源周辺の濃度分布を計算
            pollutionsDist = calculator.CalcDist(origin_i, fieldX, fieldY, t_i, decreasingRatio, flowSpeed_ms)
            #上記で計算した、一つの汚染源周辺の濃度分布を、複数の汚染源周辺の濃度分布（全体モデル）に加算
            allPollutions.Add(pollutionsDist)

        #上書きに注意
        #1秒ずつ保存。ファイル名は秒数にちなんだものにする
        #他のフォルダ（探索者フォルダ）に保存しているので注意
        allPollutions.Save("../Searcher_TimeChange/PollutionFiles/" + fileHeadName + str(t_i) + ".pkl")


        #表示される濃度値は「相対濃度」であり、白いところが0とは限らないので注意
        #描画はメモリを食うし、時間がかかるのであくまで結果確認用として使ってください（実行時に警告も出ると思います)
        graph_object = CreateGraphObject()
        allPollutions.View(graph_object)


################################################################################


if __name__ == "__main__":
    main()
