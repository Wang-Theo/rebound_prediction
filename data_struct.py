class BatchData:
    def __init__(self, batch_num, time, SJ_thickness_average, 
                 roll_length, speed, meter, gapDR, 
                 gapOP, pressureDR, pressureOP, 
                 time_gap):
        self.batch_num = batch_num # 批次膜卷号
        self.time = time # 时间
        self.SJ_thickness_average = SJ_thickness_average # 收卷厚度平均值
        self.roll_length = roll_length # 卷长
        self.speed = speed # 辊压速度(m/min)
        self.meter = meter # 辊压记米(m)
        self.gapDR = gapDR # 主轧传动侧主缸辊缝(um)
        self.gapOP = gapOP # 主轧操作侧主缸辊缝(um)
        self.pressureDR = pressureDR # 主轧传动侧主缸压力(t)
        self.pressureOP = pressureOP # 主轧操作侧主缸压力(t)
        self.time_gap = time_gap # 存放时间
        # self.CP_thickness_average = CP_thickness_average # 重跑厚度平均值

