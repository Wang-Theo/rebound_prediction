import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn import model_selection
from sklearn import neighbors
from sklearn import metrics
from sklearn.linear_model import LinearRegression
import joblib

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
    # 交叉验证
    def kfold_val_score(model, x_train, y_train):
        kfold_head = model_selection.cross_val_score(model , x_train , y_train , 
                                    cv=5, scoring = "neg_mean_absolute_error")
        return kfold_head

    def knn_training(datas, name):
        # 对所有自变量数据作标准化处理
        transfer = MinMaxScaler(feature_range=(0, 1))
        datas_scaler = pd.DataFrame(transfer.fit_transform(datas[['thickness_average','speed','gapDR','gapOP',
                                                "MES_pressureDR", "MES_pressureOP"]]))
        X = np.append(datas_scaler,datas[['time_gap']],axis=1)
        Y = datas[['thickness_average_second']]
        # 拆分训练集和测试集
        X_train, X_test = model_selection.train_test_split(X, test_size = 0.25, random_state = 2000)
        y_train, y_test = model_selection.train_test_split(Y, test_size = 0.25, random_state = 2000)
        R2s = []
        MAEs = []
        for k in range(1, 31):
            #训练
            kNN_reg = neighbors.KNeighborsRegressor(k)
            kNN_reg.fit(X_train, y_train)
            #预测
            y_pred = kNN_reg.predict(X_test)
            # 评价指标
            R2 = metrics.r2_score(y_test,y_pred)
            MAE = metrics.mean_absolute_error(y_test, y_pred)
            R2s.append(R2)
            MAEs.append(MAE)
        # 找MAE最小
        # min_elem = MAEs[0]
        # min_index = 0
        # for i in range(1, len(MAEs)):
        #     if MAEs[i] < min_elem:
        #         min_elem = MAEs[i]
        #         min_index = i
        #             #训练
        # k_best = min_index + 1
        # 找R2最大
        max_elem = R2s[0]
        max_index = 0
        for i in range(1, len(R2s)):
            if R2s[i] > max_elem:
                max_elem = R2s[i]
                max_index = i
        # 训练
        k_best = max_index + 1
        kNN_reg_best = neighbors.KNeighborsRegressor(k_best)
        kNN_reg_best.fit(X_train, y_train)
        joblib.dump(kNN_reg_best, "./trained_models/" + name + "_knn_trained_model.m")
        # 预测
        y_pred = kNN_reg_best.predict(X_test)
        # 交叉验证
        kfold_score = -LearningModel.kfold_val_score(kNN_reg_best, X_train, y_train)
        return y_test, y_pred, k_best, kfold_score
    
    def linear_regression_training(datas, name):
        # 对所有自变量数据作标准化处理
        transfer = MinMaxScaler(feature_range=(0, 1))
        datas_scaler = pd.DataFrame(transfer.fit_transform(datas[['thickness_average','speed','gapDR','gapOP',
                                                "MES_pressureDR", "MES_pressureOP"]]))
        X = np.append(datas_scaler,datas[['time_gap']],axis=1)
        Y = datas[['thickness_average_second']]
        # 拆分训练集和测试集
        X_train, X_test = model_selection.train_test_split(X, test_size = 0.25, random_state = 6000)
        y_train, y_test = model_selection.train_test_split(Y, test_size = 0.25, random_state = 6000)
        # 训练
        linear_reg = LinearRegression(fit_intercept=True).fit(X_train,y_train)
        joblib.dump(linear_reg, "./trained_models/" + name + "_linear_trained_model.m")
        # 预测
        y_pred = linear_reg.predict(X_test)
        # 交叉验证
        kfold_score = -LearningModel.kfold_val_score(linear_reg, X_train, y_train)
        return y_test, y_pred, kfold_score