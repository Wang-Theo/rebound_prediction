import pandas as pd
import numpy as np
from sklearn import neighbors
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.preprocessing import MinMaxScaler
from sklearn.feature_selection import SelectKBest,f_regression
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score

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

    # 数据训练
    head_datas = pd.read_csv(data_path.filepath_thick_processed_head, encoding='gbk', on_bad_lines='skip')
    back_datas = pd.read_csv(data_path.filepath_thick_processed_back, encoding='gbk', on_bad_lines='skip')
    # 对所有自变量数据作标准化处理
    transfer = MinMaxScaler(feature_range=(0, 1))
    head_datas_scaler = pd.DataFrame(transfer.fit_transform(head_datas[['thickness_average','speed','gapDR','gapOP',
                                              "MES_pressureDR", "MES_pressureOP"]]))
    back_datas_scaler = pd.DataFrame(transfer.fit_transform(back_datas[['thickness_average','speed','gapDR','gapOP',
                                              "MES_pressureDR", "MES_pressureOP"]]))
    head_datas_scaler = np.append(head_datas_scaler,head_datas[['time_gap']],axis=1)
    back_datas_scaler = np.append(back_datas_scaler,back_datas[['time_gap']],axis=1)
    # 拆分训练集和测试集
    X_train, X_test = model_selection.train_test_split(head_datas_scaler, 
                                                        test_size = 0.25, random_state = 100)
    y_train, y_test = model_selection.train_test_split(head_datas[['thickness_average_second']], 
                                                        test_size = 0.25, random_state = 100)

    # 设置待测试的不同k值
    #训练
    kNN_reg = neighbors.KNeighborsRegressor()
    kNN_reg.fit(X_train, y_train)
    #预测
    y_pred = kNN_reg.predict(X_test)


    # 评价
    print("均方差：", np.sqrt(mean_squared_error(y_test, y_pred))) #计算均方差根判断效果
    print("均方误差（MSE）：", r2_score(y_test,y_pred)) #计算均方误差（MSE）回归损失，越接近于1拟合效果越好

    #绘图展示预测效果
    y_pred.sort()
    y_test.values.sort()
    x = np.arange(1,len(y_pred)+1)
    Pplot = plt.scatter(x,y_pred)
    Tplot = plt.scatter(x,y_test)
    plt.legend(handles=[Pplot,Tplot],labels=['y_pred','y_test'],linestyle='-')
    plt.show()