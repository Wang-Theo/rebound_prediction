import pandas as pd
import numpy as np
from sklearn import neighbors
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.preprocessing import MinMaxScaler
from sklearn.feature_selection import SelectKBest,f_regression
from sklearn import metrics
from sklearn.model_selection import cross_val_score

import learning_model
import data_path
import data_rw

if __name__ == '__main__':
    # 相关性分析
    # learning_model.LearningModel.correlation_analysis(data_path.filepath_thick_processed_1912, '1912')
    # learning_model.LearningModel.correlation_analysis(data_path.filepath_thick_processed_0942, '0942')
    # learning_model.LearningModel.correlation_analysis(data_path.filepath_thick_processed_1221, '1221')
    # learning_model.LearningModel.correlation_analysis(data_path.filepath_thick_processed_1222, '1222')
    # learning_model.LearningModel.correlation_analysis(data_path.filepath_thick_processed_2432, '2432')
    # learning_model.LearningModel.correlation_analysis(data_path.filepath_thick_processed_1772, '1772')
    # learning_model.LearningModel.correlation_analysis(data_path.filepath_thick_processed_1431, '1431')
    # learning_model.LearningModel.correlation_analysis(data_path.filepath_thick_processed_1432, '1432')
    # learning_model.LearningModel.correlation_analysis(data_path.filepath_thick_processed_all, '_all')
    # learning_model.LearningModel.correlation_analysis(data_path.filepath_thick_processed_head, '_head')
    # learning_model.LearningModel.correlation_analysis(data_path.filepath_thick_processed_back, '_back')

    # 数据集
    head_datas = pd.read_csv(data_path.filepath_thick_processed_head, encoding='gbk', on_bad_lines='skip')
    back_datas = pd.read_csv(data_path.filepath_thick_processed_back, encoding='gbk', on_bad_lines='skip')
    # kNN模型训练
    y_test_head, y_pred_head, k_best_head, kfold_score_head = learning_model.LearningModel.knn_training(head_datas)
    y_test_back, y_pred_back, k_best_back, kfold_score_back = learning_model.LearningModel.knn_training(back_datas)
    # 评价
    print("头部预测指标结果：") # 前1000米
    print("k:", k_best_head)
    print("R_2:", metrics.r2_score(y_test_head,y_pred_head))
    print("MAE:", metrics.mean_absolute_error(y_test_head, y_pred_head))
    print("交叉验证kfold MAE:", kfold_score_head)
    print("\n")
    print("尾部预测指标结果：")
    print("k:", k_best_back)
    print("R_2:", metrics.r2_score(y_test_back,y_pred_back))
    print("MAE:", metrics.mean_absolute_error(y_test_back, y_pred_back))
    print("交叉验证kfold MAE:", kfold_score_back)
    #绘图展示预测效果
    plt.subplot(2, 1, 1)
    plt.title("Head Part Prediction")
    y_pred_head.sort()
    y_test_head.values.sort()
    x = np.arange(1,(len(y_pred_head)+1))
    plt.plot(x, y_test_head, 'r', label='y_test')
    plt.plot(x, y_pred_head, 'b', label='y_pred')
    plt.legend()

    plt.subplot(2, 1, 2)
    plt.title("Back Part Prediction")
    y_pred_back.sort()
    y_test_back.values.sort()
    x = np.arange(1,(len(y_pred_back)+1))
    plt.plot(x, y_test_back, 'r', label='y_test')
    plt.plot(x, y_pred_back, 'b', label='y_pred')
    plt.legend()
    plt.show()