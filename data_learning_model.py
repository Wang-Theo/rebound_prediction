import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

import data_path
class LearningModel:
    def __init__(self):
        pass
    def correlation_analysis(file_path, name):
        data = pd.read_csv(file_path)
        df = pd.DataFrame(data)
        columns=['thickness_average', 'speed', 'gapDR', 'gapOP',
                'MES_pressureDR', 'MES_pressureOP', 'thickness_average_second', 
                'time_gap']
        cor = df[columns].corr(method='spearman',numeric_only = True)

        sns.heatmap(cor,
                    annot=True,  # 显示相关系数的数据
                    center=0.5,  # 居中
                    fmt='.2f',  # 只显示两位小数
                    linewidth=0.5,  # 设置每个单元格的距离
                    linecolor='black',  # 设置间距线的颜色
                    vmin=0, vmax=1,  # 设置数值最小值和最大值
                    xticklabels=True, yticklabels=True,  # 显示x轴和y轴
                    square=True,  # 每个方格都是正方形
                    cbar=True,  # 绘制颜色条
                    cmap='coolwarm_r',  # 设置热力图颜色
                    )
        plt.savefig("./corralation_images/rebound_prediction_correlation" +name +".png",dpi=1000) # 保存图片

if __name__ == '__main__':
    # LearningModel.correlation_analysis(data_path.filepath_thick_processed_1912, '1912')
    # LearningModel.correlation_analysis(data_path.filepath_thick_processed_0942, '0942')
    # LearningModel.correlation_analysis(data_path.filepath_thick_processed_1221, '1221')
    # LearningModel.correlation_analysis(data_path.filepath_thick_processed_1222, '1222')
    # LearningModel.correlation_analysis(data_path.filepath_thick_processed_2432, '2432')
    # LearningModel.correlation_analysis(data_path.filepath_thick_processed_1772, '1772')
    # LearningModel.correlation_analysis(data_path.filepath_thick_processed_1431, '1431')
    # LearningModel.correlation_analysis(data_path.filepath_thick_processed_1432, '1432')
    # LearningModel.correlation_analysis(data_path.filepath_thick_processed_all, '_all')
    # LearningModel.correlation_analysis(data_path.filepath_thick_processed_head, '_head')
    LearningModel.correlation_analysis(data_path.filepath_thick_processed_back, '_back')
