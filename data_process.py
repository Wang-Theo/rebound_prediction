import pandas as pd
import math

import data_rw
import data_struct

datarw = data_rw.DataRW

# 文件路径
filepath_thick_first_1912 = "./datas/first_round/Thickness/E3E2BC1912.csv"
filepath_MES_1912 = "./datas/first_round/MES/MES_E3E2BC1912.CSV"
save_filepath_1912 = "./datas/first_round/datas_aligned/A_E3E2BC1912.csv"
filepath_thick_second_1912 = "./datas/second_round/Thickness/sec_E3E2BC1912.csv"

# 数据读取
thickness_datas_first_1912 = datarw.thicktester_data_reading(filepath_thick_first_1912)
MES_datas = datarw.MES_data_reading(filepath_MES_1912)

# 测厚仪和MES数据对齐
# 测厚仪：时间 [1]
# MES：时间 [0]，主轧传动侧主缸压力(t) [2] ，主轧操作侧主缸压力(t) [3]
for i in range(len(thickness_datas_first_1912[0])):
    thickness_datas_first_1912[8].append(0)
    thickness_datas_first_1912[9].append(0)

for i in range(1, min(len(thickness_datas_first_1912[0]),len(MES_datas[0]))):

# for i in range(1, len(thickness_datas_first_1912[0])):
#     if((float(thickness_datas_first_1912[8][i]) == 0.0)):
#         for j in range(2, len(MES_datas[0])):
#             if(float(MES_datas[1][j])/1000 > float(thickness_datas_first_1912[5][i])):
#                 if((float(MES_datas[1][j])/1000 - float(MES_datas[1][j-1])/1000) == 0):
#                     break
#                 else:
#                     radio = (float(thickness_datas_first_1912[5][i]) - float(MES_datas[1][j-1])/1000) / (float(MES_datas[1][j])/1000 - float(MES_datas[1][j-1])/1000)
#                     if(radio>0):
#                         thickness_datas_first_1912[8][i] = abs(float(MES_datas[2][j])-float(MES_datas[2][j-1])) * radio + float(MES_datas[2][j-1])
#                 break

# 收卷与重跑数据对齐


batch_1912 = data_struct.BatchData(thickness_datas_first_1912[0],thickness_datas_first_1912[1],thickness_datas_first_1912[2],
                                   thickness_datas_first_1912[3],thickness_datas_first_1912[4],thickness_datas_first_1912[5],
                                   thickness_datas_first_1912[6],thickness_datas_first_1912[7],thickness_datas_first_1912[8],
                                   thickness_datas_first_1912[9], 295.5)


# 数据存储
datarw.data_writing(thickness_datas_first_1912, save_filepath_1912)