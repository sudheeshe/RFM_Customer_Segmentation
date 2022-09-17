from sklearn.cluster import KMeans
from kneed import KneeLocator
from copy import copy
import pickle as pkl
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from Src.logger import AppLogger


class Train_KMean:
    """
    Description: This class helps to find the best KMean model.
    """

    def __init__(self):
        self.logger = AppLogger()
        self.file = open('Logs/KMeans_training_log.txt', 'a+')


    def train_model(self,data):

        """
        Description: This Method finds the optimal number of cluster (k) using Kneelocator and trains a final KMean algo with founded k.
        return: Dataframe
        """

        try:
            self.logger.log(self.file,
                            'Inside train_model method of stage_4 class >>> Started training of finding k.')

            temp_data = copy(data)

            wcss = dict()
            for k in range(1, 15):
                KM_model = KMeans(n_clusters=k, init='k-means++', max_iter=1000)
                KM_model.fit(temp_data)
                wcss[k] = KM_model.inertia_

            locate_elbow = KneeLocator(x=list(wcss.keys()), y=list(wcss.values()), curve='convex', direction='decreasing')
            k_value = locate_elbow.knee

            self.logger.log(self.file,
                            f'Inside train_model method of stage_4 class >>> k value is {str(k_value)}.')

            self.logger.log(self.file,
                            f'Inside train_model method of stage_4 class >>> Building KMean model with k value as {str(k_value)}.')
            final_kmean_model = KMeans(n_clusters=k_value, init= 'k-means++', max_iter= 1000)
            final_kmean_model.fit(temp_data)

            temp_data['cluster'] = final_kmean_model.labels_

            ## Model saving
            filename = 'Pickle/KMeans_model.pkl'
            pkl.dump(final_kmean_model, open(filename, 'wb'))

            self.logger.log(self.file, 'traing of final KMean model was successful, saving data to Data/Data_created_by_KMeans/dataset_from_KMeans.csv')
            self.logger.log(self.file, 'Leaving train_model method of stage_4 class')

            temp_data.to_csv('Data/Data_created_by_KMeans/dataset_from_KMeans.csv')


        except Exception as e:
            self.logger.log(self.file, str(e))



    def save_cluster_plot(self,data):

        """
        Description: This Method save interactive 3D plot of cluster.
        return: None
        """

        try:
            self.logger.log(self.file,
                            'Inside save_cluster_plot method of stage_4 class >>> Started creating the cluster plot')

            temp_data = copy(data)

            filename = 'Pickle/transformer.pkl'
            transformer = pkl.load(open(filename, 'rb'))
            self.logger.log(self.file,
                            'Inside save_cluster_plot method of stage_4 class >>> Loaded transformer.pkl successfully')

            df_inversed = pd.DataFrame(transformer.inverse_transform(temp_data[['Recency', 'Frequency', 'Monetary']]),
                                       index=temp_data.index, columns=['Recency', 'Frequency', 'Monetary'])

            final_df_inversed = pd.concat([df_inversed, temp_data['cluster']], axis=1, join='inner')

            self.logger.log(self.file,
                            'Inside save_cluster_plot method of stage_4 class >>> Dataframe created with original scale')

            fig = px.scatter_3d(final_df_inversed,
                                x='Recency',
                                y='Frequency',
                                z='Monetary',
                                color='cluster',
                                opacity=0.7,
                                color_discrete_sequence= px.colors.qualitative.G10)

            fig.update_layout(margin=dict(l=0, r=0, b=0, t=0))

            fig.write_html("Reports/Cluster_plot.html")

            self.logger.log(self.file,
                        'Inside save_cluster_plot method of stage_4 class >>> Saved the plot at Reports/Cluster_plot.html successfully.')

            self.logger.log(self.file, 'Leaving save_cluster_plot method of stage_4 class')


        except Exception as e:
            self.logger.log(self.file, str(e))