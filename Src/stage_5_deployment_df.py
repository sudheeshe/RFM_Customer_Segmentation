from Src.logger import AppLogger
import pandas as pd
from copy import copy


class DeploymentData:

    def __init__(self):
        self.logger = AppLogger()
        self.file = open('Logs/Deployment_data_log.txt', 'a+')


    def cluster_name_mapper(x):

        """
        Description: This method helps to map the cluster to a meaningful name
        Note: Please not the cluster number changes when we re-run the kernal,
              so always check the clour code and change the cluster name if needed

        """
        purple = 1
        yellow = 3
        light_orange = 2
        blue = 0

        if x == yellow:
            return 'About_to_Churn_Customer'

        elif x == blue:
            return 'New_Customer'

        elif x == light_orange:
            return 'Churned_Customer'

        elif x == purple:
            return 'Loyal_Customer'


    def create_deployment_data(self):

        """
        Description: This method creates deployment_data and save at Data/Deployment_data location
        returns:Dataframe
        """

        try:
            self.logger.log(self.file,
                            'Inside create_deployment_data of stage_5 class >>> Started creating the deployment_data')

            data_path = 'Data/Data_created_by_KMeans/dataset_from_KMeans.csv'

            temp_data = pd.read_csv(data_path, index_col='CustomerID')

            df = pd.DataFrame(temp_data['cluster'])

            df['Type_of_customers'] = df['cluster'].apply(DeploymentData.cluster_name_mapper)

            df.drop(labels=['cluster'], axis='columns', inplace=True)

            self.logger.log(self.file,
                            'Inside create_deployment_data of stage_5 class >>> created the deployment_data saving as csv')
            df.to_csv('Data/Deployment_data/dataset_for_prediction.csv')

            self.logger.log(self.file,
                            'Inside create_deployment_data of stage_5 class >>> deployment_data saved @ Data/Deployment_data/dataset_for_prediction.csv')
            self.logger.log(self.file, 'Leaving create_deployment_data of stage_5 class')

            return df

        except Exception as e:
            self.logger.log(self.file, str(e))