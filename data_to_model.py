import csv
from pyproj import Geod
import copy
import os

# sensor sample rate(hz)
interval = 50

wgs84_geod = Geod(ellps='WGS84')  # Distance will be measured on this ellipsoid - more accurate than a spherical method


# Get distance between pairs of lat-lon points
def Distance(lat1, lon1, lat2, lon2):
    az12, az21, dist = wgs84_geod.inv(lon1, lat1, lon2, lat2)  # Yes, this order is correct
    return [az12, dist]


input_path = '/Users/amitaflalo/Desktop/deepnav/data/raw/'
# os.remove('/Users/amitaflalo/Desktop/deepnav/data/raw/.DS_Store')

for filename in os.listdir(input_path):

    with open(input_path + filename, newline='') as csvfile:
        data = list(csv.reader(csvfile))

    # calibrate start
    for i in range(10):
        if data[i][0] != data[i + 1][0] or data[i][1] != data[i + 1][1]:
            data = data[i + 1:][:]
            break

    # cuts data until starts moving
    for i in range(0, 10000, interval):
        azi1, dist1 = Distance(data[i][0], data[i][1], data[i + interval][0], data[i + interval][1])
        azi2, dist2 = Distance(data[i + interval][0], data[i + interval][1], data[i + interval * 2][0],
                               data[i + interval * 2][1])
        if abs(azi1 - azi2) < 10 and dist1 + dist2 > 10:
            azi2 = azi2 % 360
            data[i + interval * 2][8], data[i + interval * 2][9] = azi2, dist2
            data = data[i + interval * 2:][:]
            break

    # calibrate the end
    l = len(data)
    end = l % interval
    data = data[0:l - end + 1][:]

    # fill empty
    for i in range(0, len(data)):
        if len(data[i]) < 8:
            data[i] = data[-1]
            print('fix--' + str(filename) + 'line:' + str(i))

    # azimuth calc
    for i in range(interval, len(data), interval):
        tmp_azi, tmp_dis = Distance(data[i - interval][0], data[i - interval][1], data[i][0], data[i][1])
        tmp_azi = tmp_azi % 360
        data[i][8], data[i][9] = tmp_azi, tmp_dis

    datacopy = copy.deepcopy(data)

    # azimuth difference (x2 - x1)
    for i in range(interval, len(data), interval):
        data[i][8] = (datacopy[i][8] - datacopy[i - interval][8])

    # distance Difference meters/sec
    for i in range(interval, len(data), interval):
        data[i][9] = (datacopy[i][9] - datacopy[i - interval][9])

    path = '/Users/amitaflalo/Desktop/deepnav/data/train/'

    try:
        with open(path + filename, 'x', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)
    except:
        os.remove(path + filename)

        with open(path + filename, 'x', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)
