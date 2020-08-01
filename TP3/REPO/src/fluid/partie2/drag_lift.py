import matplotlib.pyplot as plt
import csv

time = []
drag = []
lift= []

with open('../../../data/stokes_part2/P2P1/np_4/fluid.measures.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        time.append(row[0])
        drag.append(row[1])
        lift.append(row[2])

plt.plot(time,drag, label='drag')
# plt.plot(time,lift, label='lift')
plt.xlabel('time (s)')
plt.ylabel('drag')
plt.ylim(-10000, 10000)
plt.legend()
plt.show()