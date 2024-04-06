# 数据的读取写入
import pandas as pd
import os

class DataRW:
    def __init__(self):
        pass

    # 从测厚仪的csv文件读取所需的原始数据列，存入返回list
    def thicktester_data_reading(file_path):
        datas = pd.read_csv(file_path, encoding='gbk', on_bad_lines='skip')
        dataColumn = datas.columns.to_list()
        # 各所需数据的表头
        batch_num_index = dataColumn.index("批次膜卷号")
        time_index = dataColumn.index("时间")
        thickness_average_index = dataColumn.index("厚度平均值")
        roll_length_index = dataColumn.index("卷长")
        speed_index = dataColumn.index("辊压速度(m/min)")
        meter_index = dataColumn.index(" 辊压记米(m)")
        gapDR_index = dataColumn.index("主轧传动侧主缸辊缝(um)")
        gapOP_index = dataColumn.index(" 主轧操作侧主缸辊缝(um)")
        # 各所需数据表头的数据
        batch_num = datas[dataColumn[batch_num_index]].values
        time = datas[dataColumn[time_index]].values
        thickness_average = datas[dataColumn[thickness_average_index]].values
        roll_length = datas[dataColumn[roll_length_index]].values
        speed = datas[dataColumn[speed_index]].values
        meter = datas[dataColumn[meter_index]].values
        gapDR = datas[dataColumn[gapDR_index]].values
        gapOP = datas[dataColumn[gapOP_index]].values
        # 返回一个二维列表
        return [batch_num, time, thickness_average, roll_length, 
                speed, meter, gapDR, gapOP, [], []]
    
    # 从MES的csv文件读取所需的原始数据列，存入返回list
    def MES_data_reading(file_path):
        datas = pd.read_csv(file_path, encoding='gbk', on_bad_lines='skip')
        dataColumn = datas.columns.to_list()
        # 各所需数据的表头
        MES_time_index = dataColumn.index("Datetime") # 时间
        MES_speed_index = dataColumn.index("LAACA_PR001") # 辊压速度
        MES_pressureDR_index = dataColumn.index("LAACA_PR002") # 主轧传动侧主缸压力(t)
        MES_pressureOP_index = dataColumn.index("LAACA_PR003") # 主轧操作侧主缸压力(t)
        # 各所需数据表头的数据
        MES_time = datas[dataColumn[MES_time_index]].values
        MES_speed = datas[dataColumn[MES_speed_index]].values
        MES_pressureDR = datas[dataColumn[MES_pressureDR_index]].values
        MES_pressureOP = datas[dataColumn[MES_pressureOP_index]].values
        # 返回一个二维列表
        return [MES_time, MES_speed, MES_pressureDR, MES_pressureOP]
    
    # 将数据保存到新的csv文件
    def data_writing(datas_needed, save_file_path):
        # 创建空的DataFrame
        df = pd.DataFrame(columns=['批次膜卷号', '时间', '厚度平均值', '卷长', 
                                   '辊压速度(m/min)', '辊压记米(m)', '主轧传动侧主缸辊缝(um)', 
                                   '主轧操作侧主缸辊缝(um)', '主轧传动侧主缸压力(t)', '主轧操作侧主缸压力(t)'])
        # 将列表数据写入列
        df['批次膜卷号'] = datas_needed[0]
        df['时间'] = datas_needed[1]
        df['厚度平均值'] = datas_needed[2]
        df['卷长'] = datas_needed[3]
        df['辊压速度(m/min)'] = datas_needed[4]
        df['辊压记米(m)'] = datas_needed[5]
        df['主轧传动侧主缸辊缝(um)'] = datas_needed[6]
        df['主轧操作侧主缸辊缝(um)'] = datas_needed[7]
        df['主轧传动侧主缸压力(t)'] = datas_needed[8]
        df['主轧操作侧主缸压力(t)'] = datas_needed[9]
        # 保存为csv文件
        if not os.path.exists(save_file_path):
            df.to_csv(save_file_path, mode='a', index=None)
        else:
            df.to_csv(save_file_path, mode='a', index=None, header=False)