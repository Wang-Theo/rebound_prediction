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
    # 0942
    thickness_datas_first_0942 = data_align.DataAlign.thick_MES_align(data_path.filepath_thick_first_0942, 
                                                                    data_path.filepath_MES_0942, 
                                                                    data_path.save_filepath_0942)
    # 1221
    thickness_datas_first_1221 = data_align.DataAlign.thick_MES_align(data_path.filepath_thick_first_1221, 
                                                                    data_path.filepath_MES_1221, 
                                                                    data_path.save_filepath_1221)
    # 1222
    thickness_datas_first_1222 = data_align.DataAlign.thick_MES_align(data_path.filepath_thick_first_1222, 
                                                                    data_path.filepath_MES_1222, 
                                                                    data_path.save_filepath_1222)
    # 2432
    thickness_datas_first_2432 = data_align.DataAlign.thick_MES_align(data_path.filepath_thick_first_2432, 
                                                                    data_path.filepath_MES_2432, 
                                                                    data_path.save_filepath_2432)
    # 1772
    thickness_datas_first_1772 = data_align.DataAlign.thick_MES_align(data_path.filepath_thick_first_1772, 
                                                                    data_path.filepath_MES_1772, 
                                                                    data_path.save_filepath_1772)
    # 1431
    thickness_datas_first_1431 = data_align.DataAlign.thick_MES_align(data_path.filepath_thick_first_1431, 
                                                                    data_path.filepath_MES_1431, 
                                                                    data_path.save_filepath_1431)
    # 1432
    thickness_datas_first_1432 = data_align.DataAlign.thick_MES_align(data_path.filepath_thick_first_1432, 
                                                                    data_path.filepath_MES_1432, 
                                                                    data_path.save_filepath_1432)

    # 2. 重跑数据与初跑数据对齐
    # processed_data_1912 = data_align.DataAlign.thick_first_second(thickness_datas_first_1912, data_path.filepath_thick_second_1912, 3000.0, data_path.filepath_thick_processed_1912, 295.5)
    # processed_data_0942 = data_align.DataAlign.thick_first_second(thickness_datas_first_0942, data_path.filepath_thick_second_0942, 300.0, data_path.filepath_thick_processed_0942, 72.0)
    # processed_data_1221 = data_align.DataAlign.thick_first_second(thickness_datas_first_1221, data_path.filepath_thick_second_1221, 5000.0, data_path.filepath_thick_processed_1221, 54.0)
    # processed_data_1222 = data_align.DataAlign.thick_first_second(thickness_datas_first_1222, data_path.filepath_thick_second_1222, 5000.0, data_path.filepath_thick_processed_1222, 30.0)
    # processed_data_2432 = data_align.DataAlign.thick_first_second(thickness_datas_first_2432, data_path.filepath_thick_second_2432, 3000.0, data_path.filepath_thick_processed_2432, 39.5)
    # processed_data_1772 = data_align.DataAlign.thick_first_second(thickness_datas_first_1772, data_path.filepath_thick_second_1772, 2000.0, data_path.filepath_thick_processed_1772, 66.0)
    # processed_data_1431 = data_align.DataAlign.thick_first_second(thickness_datas_first_1431, data_path.filepath_thick_second_1431, 3000.0, data_path.filepath_thick_processed_1431, 48.0)
    # processed_data_1432 = data_align.DataAlign.thick_first_second(thickness_datas_first_1432, data_path.filepath_thick_second_1432, 15000.0, data_path.filepath_thick_processed_1432, 24.0)

    processed_data_1912 = data_align.DataAlign.thick_first_second(thickness_datas_first_1912, data_path.filepath_thick_second_1912, 3000.0, data_path.filepath_thick_processed_all, 295.5)
    processed_data_0942 = data_align.DataAlign.thick_first_second(thickness_datas_first_0942, data_path.filepath_thick_second_0942, 300.0, data_path.filepath_thick_processed_all, 72.0)
    processed_data_1221 = data_align.DataAlign.thick_first_second(thickness_datas_first_1221, data_path.filepath_thick_second_1221, 5000.0, data_path.filepath_thick_processed_all, 54.0)
    processed_data_1222 = data_align.DataAlign.thick_first_second(thickness_datas_first_1222, data_path.filepath_thick_second_1222, 5000.0, data_path.filepath_thick_processed_all, 30.0)
    processed_data_2432 = data_align.DataAlign.thick_first_second(thickness_datas_first_2432, data_path.filepath_thick_second_2432, 3000.0, data_path.filepath_thick_processed_all, 39.5)
    processed_data_1772 = data_align.DataAlign.thick_first_second(thickness_datas_first_1772, data_path.filepath_thick_second_1772, 2000.0, data_path.filepath_thick_processed_all, 66.0)
    processed_data_1431 = data_align.DataAlign.thick_first_second(thickness_datas_first_1431, data_path.filepath_thick_second_1431, 3000.0, data_path.filepath_thick_processed_all, 48.0)
    processed_data_1432 = data_align.DataAlign.thick_first_second(thickness_datas_first_1432, data_path.filepath_thick_second_1432, 15000.0, data_path.filepath_thick_processed_all, 24.0)