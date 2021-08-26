import matplotlib.pyplot as plt
import matplotlib as mpl
import csv

x = []
y = []

countX = 0
headers = ""
with open('results.csv', 'r') as csvfile:
    lines = csv.reader(csvfile, delimiter=',')
    headers = next(lines, None)
    for row in lines:
        z = []
        countY = 0
        for values in row:
            if countY == 0:
                x.append(values)
                countY += 1
            else:
                if 1 < countY < 6 or 9 <= countY <= 10:
                    z.append(float(values))
                    countY += 1
                elif 11 <= countY <= 12:
                    z.append(float(values)/1000000)
                    countY += 1
                else:
                    countY += 1
        y.append(z)
        countX += 1


def color_selector(argument):
    switcher = {
        0: "b",
        1: "g",
        2: "r",
        3: "c",
        4: "m",
        5: "y",
        6: "b",
        7: "w"
    }
    return switcher.get(argument, "w")


headersValues = ["Duration(s)", "Ping(ms)", "Upload(Mbps)", "Download(Mbps)", "Avg Duration(s)", "Avg Ping(ms)",
                 "Avg Upload(Mbps)", "Avg Download(Mbps)"]
maxY = 0
minY = 10000000
count = 0

plt.figure(facecolor='grey')
ax = plt.axes()
ax.set_facecolor("grey")
labels_color = 'black'
mpl.rcParams['text.color'] = labels_color
mpl.rcParams['axes.labelcolor'] = labels_color
# mpl.rcParams['axes.grid.color'] = labels_color
mpl.rcParams['xtick.color'] = labels_color
mpl.rcParams['ytick.color'] = labels_color
for indexY in range(len(y[0])):
    a = []
    b = []
    for indexX in range(len(x)):
        a.append(x[indexX])
        b.append(y[indexX][indexY])
    plt.plot(a, b, '-', color=color_selector(indexY), marker='x', lw=1, label=headersValues[indexY])

for indexX in range(len(x)):
    for indexY in range(len(y[indexX])):
        xVal = x[indexX]
        yVal = y[indexX][indexY]
        if yVal > maxY:
            maxY = yVal
        elif yVal < minY:
            minY = yVal

plt.xlim(-1, len(x) + 0.2)
plt.ylim(0, round(maxY, 0) + (0.1 * maxY))
plt.xticks(rotation=90)
plt.minorticks_on()
plt.xlabel('Date')
plt.ylabel('Measure Value')
plt.title('Speedtest statistics', fontsize=10)
plt.legend(title='Measures')
plt.grid()
plt.show()
