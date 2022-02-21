

import importlib
import Pickle_Reader
import matplotlib.pyplot as plt
import copy

importlib.reload(Pickle_Reader)


pklReader = Pickle_Reader.PickleReader()


pollutionLog = pklReader.Read("/home/kazuma/研究/PollutionCreate/DataLog/2022年/1月/3日/22時/49分/16秒/500.pkl")

print(pollutionLog)


xlim = int(pollutionLog["x"][0])
ylim = int(pollutionLog["y"][0])
first_t = int(pollutionLog["start_t"][0])
last_t = int(pollutionLog["end_t"][0])

time_step = 25

first_t = 1000
last_t = 1151

for time_i in range(first_t, last_t, time_step):

    new_x = list()
    new_y = list()




    for x_i in range(0, xlim, 1):
        for y_i in range(0, ylim, 1):

            new_x.append(x_i)
            new_y.append(y_i)


    #path = "/home/kazuma/研究/PollutionCreate/DataLog/2022年/1月/3日/22時/49分/16秒/" + str(time_i) + ".pkl"
    path = "/home/kazuma/研究/PollutionCreate/DataLog/2022年/1月/3日/22時/49分/16秒/" + str(time_i) + ".pkl"
    pollutionLog = pklReader.Read(path)
    plns = copy.deepcopy(pollutionLog["pollutions"])
    plns = plns.values.tolist()
    maxPln = max(plns)


    for i in range(len(plns)):
        plns[i] = plns[i] / maxPln




    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_aspect('equal')
    ax.set_xlabel("x [m]")
    ax.set_ylabel("y [m]")
    ax.scatter(new_x, new_y, s= 20,  c = plns, cmap = 'binary')
    plt.show()

    if(time_i == 1000 or time_i == 1025 or time_i == 1050 or time_i == 1075 or time_i == 1100 or time_i == 1125 or time_i == 1150):
        file = "Pic_Pollution/thesis/" + "little_time_change_" + str(time_i) + ".png"
        fig.savefig(file, dpi = 300)
