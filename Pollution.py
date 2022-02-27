
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import copy
from itertools import chain

class Pollution:

    def __init__(self, pollutionPoints):
        self.__pollutionPoints = pollutionPoints


    def GetPollution(self, x, y):
        return self.__pollutionPoints[x][y]

    def IsInRange(self, x, y):
        xlim, ylim  = self.__XY_Limits()
        isInRange = (x >= 0 and x < xlim and y >= 0 and y < ylim)
        return isInRange

    def Add(self, pollution):

        xlim, ylim = self.__XY_Limits()
        for x_i in range(xlim):
            for y_i in range(ylim):
                if(pollution.IsInRange(x_i, y_i)):
                        self.__pollutionPoints[x_i][y_i] += pollution.GetPollution(x_i, y_i)


        return self



    def View(self, cmap = 'binaly'):

        xList, yList, pollutionList = self.__OrderToView()
        #matplotlibという描画ライブラリで散布図を描画
        ax = plt.figure().add_subplot(111)
        ax.scatter(xList, yList, c = pollutionList, cmap = 'binary', alpha = 0.3)
        plt.show()
        return None


    def __XY_Limits(self):
        xlim = len(self.__pollutionPoints)
        ylim = len(self.__pollutionPoints[0])
        return xlim, ylim


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
        xlim = len(self.__pollutionPoints)
        ylim = len(self.__pollutionPoints[0])
        return xlim, ylim


    def Save(self, savePath, format, start_t, end_t):
        """データの保存を行う関数"""

        xlim, ylim = self.__XY_Limits()
        new_pollutions = []

        for x_i in range(xlim):
            for y_i in range(ylim):
                pollution = self.__pollutionPoints[x_i][y_i]
                new_pollutions.append(pollution)


        x, y = self.__XY_Limits()
        indexNames = ["pollutions", "x", "y", "start_t", "end_t"]
        values = [new_pollutions, x, y, start_t, end_t]

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


        savePath = str(savePath)

        if(format == 'pkl'):
            datas.to_pickle(savePath)

        if(format == 'csv'):
            datas.to_csv(savePath)


    def __to_list(self):

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
