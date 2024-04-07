import pandas as pd
import math

import data_rw

class DataAlign:
    def __init__(self):
        pass

    def thick_MES_align(filepath_thick_first, filepath_MES, save_filepath):
        datarw = data_rw.DataRW

        # 数据读取
        thickness_datas_first_1912 = datarw.thicktester_data_reading(filepath_thick_first)
        MES_datas = datarw.MES_data_reading(filepath_MES)

        # 测厚仪和MES数据对齐
        # 测厚仪：时间 [1]，主轧传动侧主缸压力(t) [8] ，主轧操作侧主缸压力(t) [9]
        # MES：时间 [0]，主轧传动侧主缸压力(t) [2] ，主轧操作侧主缸压力(t) [3]
        for i in range(len(thickness_datas_first_1912[0])):
            thickness_datas_first_1912[8].append("0")
            thickness_datas_first_1912[9].append("0")

        MES_indexes = []
        MES_begin = 1
        MES_end = 1
        thicktester_indexes = []
        thicktester_begin = 0
        thicktester_end = 0
        while(MES_end < len(MES_datas[0])):
            if(MES_datas[0][MES_begin] == MES_datas[0][MES_end]):
                MES_end += 1
            else:
                MES_indexes.append(MES_end-1)
                MES_begin = MES_end
            if(MES_end == (len(MES_datas[0])-1)):
                MES_indexes.append(len(MES_datas[0])-1)

        while(thicktester_end < len(thickness_datas_first_1912[0])):
            if(thickness_datas_first_1912[1][thicktester_begin] == thickness_datas_first_1912[1][thicktester_end]):
                thicktester_end += 1
            else:
                thicktester_indexes.append(thicktester_end-1)
                thicktester_begin = thicktester_end
            if(thicktester_end == (len(thickness_datas_first_1912[0])-1)):
                thicktester_indexes.append(len(thickness_datas_first_1912[0])-1)
                                
        i = 0
        j = 0
        mark = 0
        while((i<len(thicktester_indexes)) & (j<len(MES_indexes))):
            if ((i == 0) | (j == 0)):
                if(thickness_datas_first_1912[1][thicktester_indexes[i]] == MES_datas[0][MES_indexes[j]]):
                    mark = 1
                    radio = MES_indexes[j] / (thicktester_indexes[i]+1)
                    for m in range(thicktester_indexes[i]+1):
                        thickness_datas_first_1912[8][m] = MES_datas[2][math.ceil((m+1)*radio)]
                        thickness_datas_first_1912[9][m] = MES_datas[3][math.ceil((m+1)*radio)]
                else:
                    i+=1
                    mark = 0
            else:
                if(thickness_datas_first_1912[1][thicktester_indexes[i]] == MES_datas[0][MES_indexes[j]]):
                    mark = 1
                    radio = (MES_indexes[j]-MES_indexes[j-1]) / (thicktester_indexes[i]-thicktester_indexes[i-1])
                    for m in range(thicktester_indexes[i-1]+1, thicktester_indexes[i]+1):
                        thickness_datas_first_1912[8][m] = MES_datas[2][math.ceil((m-thicktester_indexes[i-1])*radio+MES_indexes[j-1])]
                        thickness_datas_first_1912[9][m] = MES_datas[3][math.ceil((m-thicktester_indexes[i-1])*radio+MES_indexes[j-1])]
                else:
                    i+=1
                    mark = 0
            if(mark == 1):
                i+=1
                j+=1

        # 数据存储
        datarw.data_writing(thickness_datas_first_1912, save_filepath)

        return thickness_datas_first_1912