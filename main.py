from Src.stage_1_data_reader import ReadData
from Src.stage_2_RMF_table_gen import RMF_TableGenerator
from Src.stage_3_feature_engineering import FeatureEngineering
from Src.stage_4_model_training import Train_KMean
from Src.stage_5_deployment_df import DeploymentData
import os.path


try:

    if os.path.isfile('Data/Deployment_data/dataset_for_prediction.csv'):

        print("Prediction file already present @ Data/Deployment_data folder....!!!")
        print("Please try with it....!!!")

    else:

        ## Reading the data
        data = ReadData()
        data_frame = data.read_data('Data/Raw_data/data.csv')

        ## Creating RMF table
        rmf = RMF_TableGenerator()
        RMF_df = rmf.create_rmf_table(data_frame)


        ## Applying Feature Engg
        FE = FeatureEngineering()

        ## Replacing outliers with Nan
        df_with_nan = FE.replace_outlier_with_nan(RMF_df, 'Recency')
        df_with_nan = FE.replace_outlier_with_nan(df_with_nan, 'Frequency')
        df_with_nan = FE.replace_outlier_with_nan(df_with_nan, 'Monetary')

        ## Applying KNNImputer
        df_after_imputation = FE.imputer(df_with_nan)

        ## Applying Yeo_Johnson transformation
        df_transformed = FE.yeo_johnson_transformer(df_after_imputation)

        ## Training the KMean model
        model = Train_KMean()
        df_from_Kmeans = model.train_model(df_transformed)
        model.save_cluster_plot(df_from_Kmeans)


        ## Creating the Deployment data
        dply_data = DeploymentData()
        dply_df = dply_data.create_deployment_data()


        print(dply_df.head(20))
        print(dply_df.info())
        print(dply_df.shape)

except Exception as e:
    print(e)

