import pandas as pd
import numpy as np
import datetime
from copy import copy
from Src.logger import AppLogger
from sklearn.preprocessing import PowerTransformer
from sklearn.impute import KNNImputer
import pickle as pkl



class FeatureEngineering:

    """
    Description: This class helps in replace outlier with nan,
                 Imputation with KNNImputer
                 Yeo_Johnson transformation of data
    """

    def __init__(self):

        self.logger = AppLogger()
        self.file = open('Logs/FeatureEngg_logs.txt','a+')

    def replace_outlier_with_nan(self,data,column_name, percentile_min=0.01, percentile_max=0.99):

        """
        Description: Method replaces outliers with np.Nan Outlier is calculated based on the minimum and maximum percentile given
        return: Dataframe
        """

        try:
            self.logger.log(self.file,
                            'Inside replace_outlier_with_nan method of stage_3 class >>> Started replacing of outliers with np.Nan.')

            temp_df = copy(data)

            mini = temp_df[column_name].quantile(percentile_min)
            maxi = temp_df[column_name].quantile(percentile_max)

            temp_df[column_name] = temp_df[column_name].replace(temp_df[column_name].loc[temp_df[column_name] < mini].values, np.NaN)
            temp_df[column_name] = temp_df[column_name].replace(temp_df[column_name].loc[temp_df[column_name] > maxi].values, np.NaN)

            self.logger.log(self.file, 'Replacing outliers with np.NaN was successful, returning dataframe.')
            self.logger.log(self.file, 'Leaving replace_outlier_with_nan method of stage_3 class')

            return temp_df

        except Exception as e:
            self.logger.log(self.file, str(e))


    def imputer(self,data):

        """
        Description: This Method imputes outliers, internally uses KNNImputer.
        return: Dataframe
        """

        try:
            self.logger.log(self.file,
                            'Inside imputer method of stage_3 class >>> Started Imputation of outliers using KNNImputer.')
            temp_df = copy(data)

            imputer = KNNImputer(n_neighbors=3)

            output = imputer.fit_transform(temp_df) #output will be an array

            #Converting output to dataframe
            final_data = pd.DataFrame(output, index=temp_df.index,
                                               columns=temp_df.columns)

            self.logger.log(self.file, 'Imputation of outliers using KNNImputer was successful, returning dataframe.')
            self.logger.log(self.file, 'Leaving imputer method of stage_3 class')

            return final_data

        except Exception as e:
            self.logger.log(self.file, str(e))


    def yeo_johnson_transformer(self, data):

        """
        Description: Method transforms data. internally uses Yeo_Johnson_transformation
        return: Dataframe
        """

        try:
            self.logger.log(self.file,
                            'Inside yeo_johnson_transformer method of stage_3 class >>> Started applying yeo_johnson transformation.')

            temp_df = copy(data)

            transformer = PowerTransformer(method='yeo-johnson')
            output = transformer.fit_transform(temp_df)

            final_data = pd.DataFrame(output, index=temp_df.index, columns=temp_df.columns)

            filename = 'Pickle/transformer.pkl'
            pkl.dump(transformer, open(filename, 'wb'))

            self.logger.log(self.file, 'Transformation of data using yeo_johnson was successful, returning dataframe.')
            self.logger.log(self.file, 'Saved the transformer as transformer.pkl in Pickle folder')
            self.logger.log(self.file, 'Leaving yeo_johnson_transformer method of stage_3 class')

            return final_data

        except Exception as e:
            self.logger.log(self.file, str(e))
