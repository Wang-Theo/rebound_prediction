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
        MES_pressureDR_index = dataColumn.index("LAACA_PR004") # 主轧传动侧主缸压力(t)
        MES_pressureOP_index = dataColumn.index("LAACA_PR005") # 主轧操作侧主缸压力(t)
        # 各所需数据表头的数据
        MES_time = datas[dataColumn[MES_time_index]].values
        MES_speed = datas[dataColumn[MES_speed_index]].values
        MES_pressureDR = datas[dataColumn[MES_pressureDR_index]].values
        MES_pressureOP = datas[dataColumn[MES_pressureOP_index]].values
        # 返回一个二维列表
        return [MES_time, MES_speed, MES_pressureDR, MES_pressureOP]
    
    # 将数据保存到新的csv文件
    def data_writing_align_frist(datas_needed, save_file_path):
        # 创建空的DataFrame
        df = pd.DataFrame(columns=['batch_num', 'time', 'thickness_average', 'roll_length', 
                                    'speed', 'meter', 'gapDR', 'gapOP',
                                    'MES_pressureDR', 'MES_pressureOP'])
        # df = pd.DataFrame(columns=['批次膜卷号', '时间', '厚度平均值', '卷长', 
        #                            '辊压速度(m/min)', '辊压记米(m)', '主轧传动侧主缸辊缝(um)', 
        #                            '主轧操作侧主缸辊缝(um)', '主轧传动侧主缸压力(t)', '主轧操作侧主缸压力(t)'])
        # 将列表数据写入列
        df['batch_num'] = datas_needed[0]
        df['time'] = datas_needed[1]
        df['thickness_average'] = datas_needed[2]
        df['roll_length'] = datas_needed[3]
        df['speed'] = datas_needed[4]
        df['meter'] = datas_needed[5]
        df['gapDR'] = datas_needed[6]
        df['gapOP'] = datas_needed[7]
        df['MES_pressureDR'] = datas_needed[8]
        df['MES_pressureOP'] = datas_needed[9]
        # 保存为csv文件
        if not os.path.exists(save_file_path):
            df.to_csv(save_file_path, mode='a', index=None)
        else:
            df.to_csv(save_file_path, mode='a', index=None, header=False)

    # 将数据保存到新的csv文件
    def data_writing_align_second(datas_needed, save_file_path):
        # 创建空的DataFrame
        df = pd.DataFrame(columns=['batch_num', 'time', 'thickness_average', 'roll_length', 
                                    'speed', 'meter', 'gapDR', 'gapOP',
                                    'MES_pressureDR', 'MES_pressureOP', 'thickness_average_second', 
                                    'time_gap'])
        # 将列表数据写入列
        df['batch_num'] = datas_needed[0]
        df['time'] = datas_needed[1]
        df['thickness_average'] = datas_needed[2]
        df['roll_length'] = datas_needed[3]
        df['speed'] = datas_needed[4]
        df['meter'] = datas_needed[5]
        df['gapDR'] = datas_needed[6]
        df['gapOP'] = datas_needed[7]
        df['MES_pressureDR'] = datas_needed[8]
        df['MES_pressureOP'] = datas_needed[9]
        df['thickness_average_second'] = datas_needed[10]
        df['time_gap'] = datas_needed[11]
        # 保存为csv文件
        if not os.path.exists(save_file_path):
            df.to_csv(save_file_path, mode='a', index=None)
        else:
            df.to_csv(save_file_path, mode='a', index=None, header=False)

    # 分卷尾卷首，将数据保存到新的csv文件
    def data_writing_head_back(datas_needed, save_file_path_head, save_file_path_back):
        datas_head = []
        datas_back = []
        for i in range(len(datas_needed[0])):
            if(datas_needed[3][i]>1000000.0):
                divide_index = i
                break
        for i in range(len(datas_needed)):
            datas_head.append(datas_needed[i][:divide_index])
            datas_back.append(datas_needed[i][divide_index:])
        # 头部：创建空的DataFrame
        df_head = pd.DataFrame(columns=['batch_num', 'time', 'thickness_average', 'roll_length', 
                                    'speed', 'meter', 'gapDR', 'gapOP',
                                    'MES_pressureDR', 'MES_pressureOP', 'thickness_average_second', 
                                    'time_gap'])
        # 将列表数据写入列
        df_head['batch_num'] = datas_head[0]
        df_head['time'] = datas_head[1]
        df_head['thickness_average'] = datas_head[2]
        df_head['roll_length'] = datas_head[3]
        df_head['speed'] = datas_head[4]
        df_head['meter'] = datas_head[5]
        df_head['gapDR'] = datas_head[6]
        df_head['gapOP'] = datas_head[7]
        df_head['MES_pressureDR'] = datas_head[8]
        df_head['MES_pressureOP'] = datas_head[9]
        df_head['thickness_average_second'] = datas_head[10]
        df_head['time_gap'] = datas_head[11]
        # 保存为csv文件
        if not os.path.exists(save_file_path_head):
            df_head.to_csv(save_file_path_head, mode='a', index=None)
        else:
            df_head.to_csv(save_file_path_head, mode='a', index=None, header=False)

        # 尾部：创建空的DataFrame
        df_back = pd.DataFrame(columns=['batch_num', 'time', 'thickness_average', 'roll_length', 
                                    'speed', 'meter', 'gapDR', 'gapOP',
                                    'MES_pressureDR', 'MES_pressureOP', 'thickness_average_second', 
                                    'time_gap'])
        # 将列表数据写入列
        df_back['batch_num'] = datas_back[0]
        df_back['time'] = datas_back[1]
        df_back['thickness_average'] = datas_back[2]
        df_back['roll_length'] = datas_back[3]
        df_back['speed'] = datas_back[4]
        df_back['meter'] = datas_back[5]
        df_back['gapDR'] = datas_back[6]
        df_back['gapOP'] = datas_back[7]
        df_back['MES_pressureDR'] = datas_back[8]
        df_back['MES_pressureOP'] = datas_back[9]
        df_back['thickness_average_second'] = datas_back[10]
        df_back['time_gap'] = datas_back[11]
        # 保存为csv文件
        if not os.path.exists(save_file_path_back):
            df_back.to_csv(save_file_path_back, mode='a', index=None)
        else:
            df_back.to_csv(save_file_path_back, mode='a', index=None, header=False)

    def processed_data_reading(file_path):
            datas = pd.read_csv(file_path, encoding='gbk', on_bad_lines='skip')
            dataColumn = datas.columns.to_list()
            # 各所需数据的表头
            thickness_average_index = dataColumn.index("thickness_average")
            speed_index = dataColumn.index("speed")
            gapDR_index = dataColumn.index("gapDR")
            gapOP_index = dataColumn.index("gapOP")
            MES_pressureDR_index = dataColumn.index("MES_pressureDR")
            MES_pressureOP_index = dataColumn.index("MES_pressureOP")
            thickness_average_second_index = dataColumn.index("thickness_average_second")
            time_gap_index = dataColumn.index("time_gap")
            # 各所需数据表头的数据
            thickness_average = datas[dataColumn[thickness_average_index]].values
            speed = datas[dataColumn[speed_index]].values
            gapDR = datas[dataColumn[gapDR_index]].values
            gapOP = datas[dataColumn[gapOP_index]].values
            MES_pressureDR = datas[dataColumn[MES_pressureDR_index]].values
            MES_pressureOP = datas[dataColumn[MES_pressureOP_index]].values
            thickness_average_second = datas[dataColumn[thickness_average_second_index]].values
            time_gap = datas[dataColumn[time_gap_index]].values
            # 返回一个二维列表
            return [thickness_average, speed, gapDR, gapOP, MES_pressureDR, 
                    MES_pressureOP, thickness_average_second, time_gap]