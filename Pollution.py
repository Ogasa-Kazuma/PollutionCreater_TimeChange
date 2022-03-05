

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import copy
from itertools import chain
import os.path



class Pollution:
    """濃度値分布モデルの保存、値調整、描画を行うクラス"""

    #コンストラクタ
    def __init__(self, pollutionPoints):
    #2次元リストをコンストラクタに渡してください
        self.__pollutionPoints = pollutionPoints

######パブリックメソッド#####################################################
##
##　パブリックメソッドにはクラス内からも外からもアクセスできます
##
############################################################################

    def GetPollution(self, x, y):
        """ある座標位置での濃度値を読み取る(時間軸は含まれないことに注意)"""
        return self.__pollutionPoints[x][y]

    def IsInRange(self, x, y):
        """指定した座標が濃度分布モデルの範囲内かどうかを判別する"""
        xlim, ylim  = self.__XY_Limits()
        #マイナス座標も範囲外
        isInRange = (x >= 0 and x < xlim and y >= 0 and y < ylim)
        return isInRange #True or False

    def Add(self, pollution):
        """濃度分布モデルどうしを足し合わせる"""
        xlim, ylim = self.__XY_Limits()

        #加算したモデルが、ベースとなるモデルより大きい場合、はみ出る部分は加算されないので注意
        for x_i in range(xlim):
            for y_i in range(ylim):
                if(pollution.IsInRange(x_i, y_i)):
                        #1つ1つの座標について、計算を行う
                        self.__pollutionPoints[x_i][y_i] += pollution.GetPollution(x_i, y_i)


        return self



    def View(self, graph_object, cmap = 'binary', alpha = 0.3, marker='o', norm=None, vmin=None, vmax=None, linewidths=None, edgecolors=None, data=None):
        """濃度分布の描画を行う"""
        #やたらメソッドの引数が多いですが、これはPythonの「デフォルト引数」機能を使っています（詳しくはWebで)
        #デフォルトの描画設定を、透明度(alpha) = 0.3, カラーマップをbinaryにしています。


        #描画できるように濃度分布モデルのデータを変換する
        xList, yList, pollutionList = self.__OrderToView()

        #matplotlibという描画ライブラリで散布図を描画
        #scatterは散布図を表します
        graph_object.scatter(xList, yList, c = pollutionList, cmap = cmap, alpha = alpha, marker = marker, norm = norm,\
                              vmin = vmin, vmax = vmax, linewidths = linewidths,\
                              edgecolors = edgecolors, data = data)

        #matplotlib、特にplt.show()は挙動が掴みづらいと思うので、調べて勉強することをおすすめします
        #plt.show()
        return graph_object #濃度分布をグラフオブジェクトに描いたあと、呼び出し元にグラフオブジェクトを返却します



    def Save(self, savePath):
        """データの保存を行う関数"""

        xlim, ylim = self.__XY_Limits()
        new_pollutions = []

        #濃度データを一次元リストに変換する
        for x_i in range(xlim):
            for y_i in range(ylim):
                pollution = self.__pollutionPoints[x_i][y_i]
                new_pollutions.append(pollution)



        ####### 変更するときは自己責任でお願いします, バックアップをとっておきましょう #####################
        ### 下手に変更すると濃度ファイルから濃度値を読み取れなくなります #################################
        indexNames = ["pollutions", "x", "y"]
        values = [new_pollutions, xlim, ylim]
        ###########################################################

        #保存にはPandasライブラリを使っています。データフレーム型という特殊な型を使っています（詳しくはWebで)
        datas = pd.DataFrame(index=[], columns=[])
        #保存するインデックス名前と値を対応づける
        for i in range(len(indexNames)):
            datalog = pd.DataFrame(index=[], columns=[])
            #単一の値（非リスト）だと保存できない。そのため、単一の値である場合はリストに変換する
            if(type(values[i]) == list):
                datalog[indexNames[i]] = values[i]
            else: #非リストの場合
                datalog[indexNames[i]] = [values[i]]

            datas = pd.concat([datas, datalog], axis = 1)

        #保存先は文字列型で指定する必要がある。ここれ一応文字列型に変換
        savePath = str(savePath)
        #ファイル芽、パス名から拡張子を取得
        not_used, ext = os.path.splitext(savePath)

        #拡張子によって保存用関数を選択
        if(ext == '.pkl'):
            datas.to_pickle(savePath)

        elif(ext == '.csv'):
            datas.to_csv(savePath)

        else:
            raise TypeError('pkl形式かcsv形式の保存にのみ対応しています')


##########################################################################################






###############　プライベートメソッド ########################################################
##
## プライベートメソッドには、クラス外からはアクセスできません
##
##########################################################################################


    def __OrderToView(self):
        xlim, ylim = self.__XY_Limits()

        new_x = []
        new_y = []
        new_pollutions = []

        for x_count in range(xlim):
            for y_count in range(ylim):
                    new_x.append(x_count)
                    new_y.append(y_count)
                    new_pollutions.append(self.__pollutionPoints[x_count][y_count])


        return new_x, new_y, new_pollutions


    def __XY_Limits(self):
        #2次元リストの各次元の長さを読み取ることでx, y座標の範囲を判定
        xlim = len(self.__pollutionPoints)
        ylim = len(self.__pollutionPoints[0])
        return xlim, ylim





    def __to_list(self):
        """濃度データを、保存しやすい構造に変換する"""
        xlim, ylim = self.__XY_Limits()

        new_x = []
        new_y = []
        new_pollutions = []

        for x_count in range(xlim):
            for y_count in range(ylim):
                new_x.append(x_count)
                new_y.append(y_count)
                new_pollutions.append(self.__pollutionPoints[x_count][y_count])

        return new_x, new_y, new_pollutions
