import pandas as pd
import math

import data_rw
import data_struct
import data_align
import data_path

if __name__ == '__main__':
    datarw = data_rw.DataRW

    # 1. 初跑测厚仪数据与MES数据对齐
    # 1912
    thickness_datas_first_1912 = data_align.DataAlign.thick_MES_align(data_path.filepath_thick_first_1912, 
                                                                    data_path.filepath_MES_1912, 
                                                                    data_path.save_filepath_1912)
    batch_1912 = data_struct.BatchData(thickness_datas_first_1912[0],thickness_datas_first_1912[1],thickness_datas_first_1912[2],
                                    thickness_datas_first_1912[3],thickness_datas_first_1912[4],thickness_datas_first_1912[5],
                                    thickness_datas_first_1912[6],thickness_datas_first_1912[7],thickness_datas_first_1912[8],
                                    thickness_datas_first_1912[9], 295.5)
    # 0942
    thickness_datas_first_0942 = data_align.DataAlign.thick_MES_align(data_path.filepath_thick_first_0942, 
                                                                    data_path.filepath_MES_0942, 
                                                                    data_path.save_filepath_0942)
    batch_0942 = data_struct.BatchData(thickness_datas_first_0942[0],thickness_datas_first_0942[1],thickness_datas_first_0942[2],
                                    thickness_datas_first_0942[3],thickness_datas_first_0942[4],thickness_datas_first_0942[5],
                                    thickness_datas_first_0942[6],thickness_datas_first_0942[7],thickness_datas_first_0942[8],
                                    thickness_datas_first_0942[9], 72.0)
    # 1221
    thickness_datas_first_1221 = data_align.DataAlign.thick_MES_align(data_path.filepath_thick_first_1221, 
                                                                    data_path.filepath_MES_1221, 
                                                                    data_path.save_filepath_1221)
    batch_1221 = data_struct.BatchData(thickness_datas_first_1221[0],thickness_datas_first_1221[1],thickness_datas_first_1221[2],
                                    thickness_datas_first_1221[3],thickness_datas_first_1221[4],thickness_datas_first_1221[5],
                                    thickness_datas_first_1221[6],thickness_datas_first_1221[7],thickness_datas_first_1221[8],
                                    thickness_datas_first_1221[9], 54.0)
    # 1222
    thickness_datas_first_1222 = data_align.DataAlign.thick_MES_align(data_path.filepath_thick_first_1222, 
                                                                    data_path.filepath_MES_1222, 
                                                                    data_path.save_filepath_1222)
    batch_1222 = data_struct.BatchData(thickness_datas_first_1222[0],thickness_datas_first_1222[1],thickness_datas_first_1222[2],
                                    thickness_datas_first_1222[3],thickness_datas_first_1222[4],thickness_datas_first_1222[5],
                                    thickness_datas_first_1222[6],thickness_datas_first_1222[7],thickness_datas_first_1222[8],
                                    thickness_datas_first_1222[9], 30.0)
    # 2432
    thickness_datas_first_2432 = data_align.DataAlign.thick_MES_align(data_path.filepath_thick_first_2432, 
                                                                    data_path.filepath_MES_2432, 
                                                                    data_path.save_filepath_2432)
    batch_2432 = data_struct.BatchData(thickness_datas_first_2432[0],thickness_datas_first_2432[1],thickness_datas_first_2432[2],
                                    thickness_datas_first_2432[3],thickness_datas_first_2432[4],thickness_datas_first_2432[5],
                                    thickness_datas_first_2432[6],thickness_datas_first_2432[7],thickness_datas_first_2432[8],
                                    thickness_datas_first_2432[9], 39.5)
    # 1772
    thickness_datas_first_1772 = data_align.DataAlign.thick_MES_align(data_path.filepath_thick_first_1772, 
                                                                    data_path.filepath_MES_1772, 
                                                                    data_path.save_filepath_1772)
    batch_1772 = data_struct.BatchData(thickness_datas_first_1772[0],thickness_datas_first_1772[1],thickness_datas_first_1772[2],
                                    thickness_datas_first_1772[3],thickness_datas_first_1772[4],thickness_datas_first_1772[5],
                                    thickness_datas_first_1772[6],thickness_datas_first_1772[7],thickness_datas_first_1772[8],
                                    thickness_datas_first_1772[9], 66.0)
    # 1431
    thickness_datas_first_1431 = data_align.DataAlign.thick_MES_align(data_path.filepath_thick_first_1431, 
                                                                    data_path.filepath_MES_1431, 
                                                                    data_path.save_filepath_1431)
    batch_1431 = data_struct.BatchData(thickness_datas_first_1431[0],thickness_datas_first_1431[1],thickness_datas_first_1431[2],
                                    thickness_datas_first_1431[3],thickness_datas_first_1431[4],thickness_datas_first_1431[5],
                                    thickness_datas_first_1431[6],thickness_datas_first_1431[7],thickness_datas_first_1431[8],
                                    thickness_datas_first_1431[9], 48.0)
    # 1432
    thickness_datas_first_1432 = data_align.DataAlign.thick_MES_align(data_path.filepath_thick_first_1432, 
                                                                    data_path.filepath_MES_1432, 
                                                                    data_path.save_filepath_1432)
    batch_1432 = data_struct.BatchData(thickness_datas_first_1432[0],thickness_datas_first_1432[1],thickness_datas_first_1432[2],
                                    thickness_datas_first_1432[3],thickness_datas_first_1432[4],thickness_datas_first_1432[5],
                                    thickness_datas_first_1432[6],thickness_datas_first_1432[7],thickness_datas_first_1432[8],
                                    thickness_datas_first_1432[9], 24.0)

    # 2. 重跑数据与初跑数据对齐
    processed_data_1912 = data_align.DataAlign.thick_first_second(thickness_datas_first_1912, data_path.filepath_thick_second_1912, 3000.0, data_path.filepath_thick_processed_1912)
    processed_data_0942 = data_align.DataAlign.thick_first_second(thickness_datas_first_0942, data_path.filepath_thick_second_0942, 300.0, data_path.filepath_thick_processed_0942)
    processed_data_1221 = data_align.DataAlign.thick_first_second(thickness_datas_first_1221, data_path.filepath_thick_second_1221, 5000.0, data_path.filepath_thick_processed_1221)
    processed_data_1222 = data_align.DataAlign.thick_first_second(thickness_datas_first_1222, data_path.filepath_thick_second_1222, 5000.0, data_path.filepath_thick_processed_1222)
    processed_data_2432 = data_align.DataAlign.thick_first_second(thickness_datas_first_2432, data_path.filepath_thick_second_2432, 3000.0, data_path.filepath_thick_processed_2432)
    processed_data_1772 = data_align.DataAlign.thick_first_second(thickness_datas_first_1772, data_path.filepath_thick_second_1772, 2000.0, data_path.filepath_thick_processed_1772)
    processed_data_1431 = data_align.DataAlign.thick_first_second(thickness_datas_first_1431, data_path.filepath_thick_second_1431, 3000.0, data_path.filepath_thick_processed_1431)
    processed_data_1432 = data_align.DataAlign.thick_first_second(thickness_datas_first_1432, data_path.filepath_thick_second_1432, 15000.0, data_path.filepath_thick_processed_1432)