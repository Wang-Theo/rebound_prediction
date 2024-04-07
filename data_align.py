import pandas as pd
import math
import time

import data_rw

class DataAlign:
    def __init__(self):
        pass
    
    # 去除没有重跑厚度和轧制力的数据行
    def datas_cleasing(processed_datas):
        batch_num = []
        time = []
        thickness_average = []
        roll_length = []
        speed = []
        meter = []
        gapDR = []
        gapOP = []
        MES_pressureDR = []
        MES_pressureOP = []
        thickness_average_second = []
        index = 0
        for i in range(len(processed_datas[0])):
            if((float(processed_datas[8][i]) == 0.0) 
               | (float(processed_datas[9][i]) == 0.0) 
               | (float(processed_datas[10][i]) == 0.0)):
                continue
            else:
                batch_num.append(processed_datas[0][i])
                time.append(processed_datas[1][i])
                thickness_average.append(processed_datas[2][i])
                roll_length.append(processed_datas[3][i])
                speed.append(processed_datas[4][i])
                meter.append(processed_datas[5][i])
                gapDR.append(processed_datas[6][i])
                gapOP.append(processed_datas[7][i])
                MES_pressureDR.append(processed_datas[8][i])
                MES_pressureOP.append(processed_datas[9][i])
                thickness_average_second.append(processed_datas[10][i])
        return [batch_num, time, thickness_average, roll_length, 
                speed, meter, gapDR, gapOP, MES_pressureDR,
                MES_pressureOP, thickness_average_second]
    
    # 初跑测厚仪数据与MES数据对齐
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
            if(MES_datas[0][MES_begin][0:16] == MES_datas[0][MES_end][0:16]):
                MES_end += 1
            else:
                MES_indexes.append(MES_end-1)
                MES_begin = MES_end
            if(MES_end == (len(MES_datas[0])-1)):
                MES_indexes.append(len(MES_datas[0])-1)

        while(thicktester_end < len(thickness_datas_first_1912[0])):
            if(thickness_datas_first_1912[1][thicktester_begin][0:16] == thickness_datas_first_1912[1][thicktester_end][0:16]):
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
                if(thickness_datas_first_1912[1][thicktester_indexes[i]][0:16] == MES_datas[0][MES_indexes[j]][0:16]):
                    mark = 1
                    if(i==0 & j ==0):
                        radio = MES_indexes[j] / (thicktester_indexes[i]+1)
                        for m in range(thicktester_indexes[i]+1):
                            thickness_datas_first_1912[8][m] = MES_datas[2][math.ceil((m+1)*radio)]
                            thickness_datas_first_1912[9][m] = MES_datas[3][math.ceil((m+1)*radio)]
                    elif(i==0 & j !=0):
                        radio = (MES_indexes[j]-MES_indexes[j-1]) / (thicktester_indexes[i]+1)
                        for m in range(thicktester_indexes[i]+1):
                            thickness_datas_first_1912[8][m] = MES_datas[2][math.ceil((m+1)*radio+MES_indexes[j-1])]
                            thickness_datas_first_1912[9][m] = MES_datas[3][math.ceil((m+1)*radio+MES_indexes[j-1])]
                    elif(i!=0 & j ==0):
                        radio = (MES_indexes[j]) / (thicktester_indexes[i]-thicktester_indexes[i-1])
                        for m in range(thicktester_indexes[i-1]+1, thicktester_indexes[i]+1):
                            thickness_datas_first_1912[8][m] = MES_datas[2][math.ceil((m-thicktester_indexes[i-1])*radio)]
                            thickness_datas_first_1912[9][m] = MES_datas[3][math.ceil((m-thicktester_indexes[i-1])*radio)]
                elif((i!=len(thicktester_indexes)-1) & (j!=len(MES_indexes)-1)):
                    if(len(MES_datas[0][1]) == 15):
                        thick_time = time.strptime(thickness_datas_first_1912[1][thicktester_indexes[i+1]][10:16], "%H:%M")
                        MES_time = time.strptime(MES_datas[0][MES_indexes[j+1]][10:16],"%H:%M")
                    elif(len(MES_datas[0][1]) == 19):
                        thick_time = time.strptime(thickness_datas_first_1912[1][thicktester_indexes[i+1]][11:16], "%H:%M")
                        MES_time = time.strptime(MES_datas[0][MES_indexes[j+1]][11:16],"%H:%M")
                    if(thick_time < MES_time):
                        i+=1
                    else:
                        j+=1
                    mark = 0
            else:
                if(thickness_datas_first_1912[1][thicktester_indexes[i]][0:16] == MES_datas[0][MES_indexes[j]][0:16]):
                    mark = 1
                    radio = (MES_indexes[j]-MES_indexes[j-1]) / (thicktester_indexes[i]-thicktester_indexes[i-1])
                    for m in range(thicktester_indexes[i-1]+1, thicktester_indexes[i]+1):
                        thickness_datas_first_1912[8][m] = MES_datas[2][math.ceil((m-thicktester_indexes[i-1])*radio+MES_indexes[j-1])]
                        thickness_datas_first_1912[9][m] = MES_datas[3][math.ceil((m-thicktester_indexes[i-1])*radio+MES_indexes[j-1])]
                elif((i!=len(thicktester_indexes)-1) & (j!=len(MES_indexes)-1)):
                    if(len(MES_datas[0][1]) == 15):
                        thick_time = time.strptime(thickness_datas_first_1912[1][thicktester_indexes[i+1]][10:16], "%H:%M")
                        MES_time = time.strptime(MES_datas[0][MES_indexes[j+1]][10:16],"%H:%M")
                    elif(len(MES_datas[0][1]) == 19):
                        thick_time = time.strptime(thickness_datas_first_1912[1][thicktester_indexes[i+1]][11:16], "%H:%M")
                        MES_time = time.strptime(MES_datas[0][MES_indexes[j+1]][11:16],"%H:%M")
                    if(thick_time < MES_time):
                        i+=1
                    else:
                        j+=1
                    mark = 0
                else:
                    break
            if(mark == 1):
                i+=1
                j+=1

        # 数据存储
        datarw.data_writing_align_frist(thickness_datas_first_1912, save_filepath)

        return thickness_datas_first_1912
    
    # 重跑数据与初跑数据对齐
    # 初跑的卷尾是重跑的卷头，重跑的尾部废弃26米
    def thick_first_second(batch_datas_first, filepath_thick_second, meter_discard, save_filepath, time_gap):
        datarw = data_rw.DataRW
        # 数据读取
        thickness_datas_second = datarw.thicktester_data_reading(filepath_thick_second)

        # 初跑：卷长[3]
        # 重跑：卷长[3]，厚度平均值[2]
        # 1. 初跑数据去除废弃料
        # 1) 初跑头部废弃26米
        batch_datas_first_ = []
        head_discard_index = 0
        for i in range(len(batch_datas_first[0])):
            if(batch_datas_first[3][i]>26000.0):
                head_discard_index = i
                break
        for i in range(len(batch_datas_first)):
            batch_datas_first_.append(batch_datas_first[i][head_discard_index:])
        for i in range(len(batch_datas_first_[0])):
            batch_datas_first_[3][i] = batch_datas_first_[3][i] - 26000.0
        # 2) 初跑尾部废弃工人所给米数
        batch_datas_first_discarded = []
        end_index = 0
        length = batch_datas_first_[3][-1]
        for i in range(len(batch_datas_first_[0])):
            if((length - batch_datas_first_[3][i])<meter_discard):
                end_index = i-1
                break
        for i in range(len(batch_datas_first_)):
            batch_datas_first_discarded.append(batch_datas_first_[i][:end_index])

        #! 卷长没清零
        if(thickness_datas_second[3][0] > 10000):
            start_meter = thickness_datas_second[3][0]
            for i in range(len(thickness_datas_second[3])):
                thickness_datas_second[3][i] = thickness_datas_second[3][i] - start_meter

        # 2. 按照卷长对齐
        batch_datas_first_discarded.append([])
        for i in range(len(batch_datas_first_discarded[0])):
            batch_datas_first_discarded[10].append(0)
        for i in range(len(batch_datas_first_discarded[3])):
            for j in range(len(thickness_datas_second[3])):
                if(thickness_datas_second[3][j] > batch_datas_first_discarded[3][i]):
                    radio = (batch_datas_first_discarded[3][i]-thickness_datas_second[3][j-1])/(thickness_datas_second[3][j] - thickness_datas_second[3][j-1])
                    batch_datas_first_discarded[10][i] = radio*(thickness_datas_second[2][j] - thickness_datas_second[2][j-1]) + thickness_datas_second[2][j-1]
                    break
        # 3. 数据清洗
        batch_datas_first_discarded = DataAlign.datas_cleasing(batch_datas_first_discarded)
        batch_datas_first_discarded.append([])
        for i in range(len(batch_datas_first_discarded[0])):
            batch_datas_first_discarded[11].append(time_gap)
        # 数据存储
        datarw.data_writing_align_second(batch_datas_first_discarded, save_filepath)
        return batch_datas_first_discarded
        
