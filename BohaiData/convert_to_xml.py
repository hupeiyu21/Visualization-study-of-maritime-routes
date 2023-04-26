import pandas as pd
import numpy as np
from rdp import rdp
import os
import time
from tqdm import tqdm

#%%
# 容器
Node_pos = []
Node_geo = []
File_list = []
All_File_Data = []

# 参数
rdp_index = 1000
#%%
def ReadAllCsvFile(path):
    files = os.listdir(path)

    csv_file_paths = []

    for file in files:
        if file.endswith('.csv'):
            csv_file_paths.append(os.path.join(path, file))

    return csv_file_paths
#%%
def GetLonLat(path):
    df = pd.read_csv(path)
    value=df[['LON','LAT']] / 600000.0
    lat = value['LAT'].values.tolist()
    lon = value['LON'].values.tolist()
    return lat,lon
#%%
def Geographic2WebMmercator(lat, lon):
    R =  6378137.0
    x = np.radians(lon) * R
    y = np.log(np.tan(np.pi / 4 + np.radians(lat) / 2)) * R
    return x, y

def WebMercator2Geographic(list_x, list_y):
    R =  6378137.0
    for i in list_x:
        lat_new = np.degrees(2 * np.arctan(np.exp (list_y[i] / R)) - np.pi / 2.0)
        lon_new = np.degrees(list_x[i] / R)
    for i in range(len(lat_new)):
        Node_geo.append([lat_new[i],lon_new[i]])
    return Node_geo

#%%
def GetData(path):
    lat,lon = GetLonLat(path)
    x,y = Geographic2WebMmercator(lat,lon)
    for i in range(len(lat)):
        Node_pos.append([x[i],y[i]])
    return Node_pos
#%%
def GetAllData(File_list):
    for i in File_list:
        All_File_Data.append(GetAfterRDPData(i))

    return All_File_Data
#%%
def Gen(array,a,b,count):

    dir = "../BohaiData/result"  # Replace with desired directory
    filename1 = "file_node{}.txt".format(count)
    filename2 = "file_edge{}.txt".format(count)

    file_path1 = os.path.join(dir, filename1)
    file_path2 = os.path.join(dir, filename2)

    with open(file_path1, "w") as f:
        for i,arr in enumerate(array):
            f.write("    <node id=\"%d\">"%a)
            f.write('\r\n')
            f.write("          <data key=\"x\">%f</data>"%array[i][0])
            f.write('\r\n')
            f.write("          <data key=\"tooltip\">s</data>")
            f.write('\r\n')
            f.write("          <data key=\"y\">%f</data>"%array[i][1])
            f.write('\r\n')
            f.write("    </node>")
            f.write('\r\n')
            a += 1

    with open(file_path2, "w") as f:
        for i , arr in enumerate(array):
            f.write("    <edge id=\"%d\" source=\"%d\" target=\"%d\">"%(b,b,b+1))
            f.write('\r\n')
            f.write("    </edge>")
            f.write('\r\n')
            b += 1
            if(i == len(array) - 2):
                f.write("    <edge id=\"%d\" source=\"%d\" target=\"%d\">" % (b, b, b))
                f.write('\r\n')
                f.write("    </edge>")
                f.write('\r\n')
                b += 1
                break

        f.write('\r\n')

    print("finished%d %d"%(a,b))

if __name__ == '__main__':
    # 得到经过rdp之后的二维数组
    file_list = ReadAllCsvFile("Data/bohai")
    index = 0
    count = 0
    for i in file_list:
        data = np.array(GetData(i))
        Gen(data,index,index,count)
        index += len(data) + 1
        count += 1

# if __name__ == '__main__':
#     # 得到经过rdp之后的二维数组
#     data = np.array(GetData('../BohaiData/Data/Bohai/205387000.csv'))
#     Gen(data,0,0)