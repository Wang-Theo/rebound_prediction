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
    head_datas = data_rw.DataRW.processed_data_reading(data_path.filepath_thick_processed_head)
    back_datas = data_rw.DataRW.processed_data_reading(data_path.filepath_thick_processed_back)

    