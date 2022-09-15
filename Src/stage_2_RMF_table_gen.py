import pandas as pd
import numpy as np
import datetime
from copy import copy
from Src.logger import AppLogger


class RMF_TableGenerator:

    """
    Description: This module helps to create RMF table from the input data.
                 This class drops the records where CustomerID is Null
                 This class removes Negative values in Quantity column and UnitPrice column.
                 This class considers only United_Kingdom other countries are dropped internally
                 This class creates a new colum TotalPrice by taking product of Quantity & UnitPrice
    """

    def __init__(self):
        self.logger = AppLogger()
        self.file = open('Logs/RMF_table_creation_logs.txt', 'a+')
        self.current_date = datetime.datetime(2011,12,10)

    def create_rmf_table(self,data):

        """
        Description: This method helps to create RMF table from the input data.
                     This method drops the records where CustomerID is Null
                     This method removes Negative values in Quantity column and UnitPrice column.
                     This method considers only United_Kingdom other countries are dropped internally
                     This method creates a new colum TotalPrice by taking product of Quantity & UnitPrice

        return: DataFrame
        """

        try:
            self.logger.log(self.file,
                            'Inside create_rmf_table method of stage_2 class >>> Started creating RMF table.')

            data = data.loc[(data['Country'] == 'United Kingdom')]
            self.logger.log(self.file,
                            'Inside create_rmf_table method of stage_2 class >>> Removed other countries keeping only United Kingdom.')

            data.dropna(subset=['CustomerID'], how='all',inplace=True, axis = 'index')
            self.logger.log(self.file,
                            'Inside create_rmf_table method of stage_2 class >>> Dropped all Null records where CustomerID was null .')

            data = data[(data['Quantity'] > 0) & (data['UnitPrice'] > 0)]
            self.logger.log(self.file,
                            'Inside create_rmf_table method of stage_2 class >>> Dropped all Null records where Quantity & UnitPrice was negative .')

            data['TotalPrice'] = np.round((data['Quantity'] * data['UnitPrice']), 1)
            self.logger.log(self.file,
                            'Inside create_rmf_table method of stage_2 class >>> Created TotalPrice column.')

            RMF_data = data.groupby('CustomerID').agg(
                {'InvoiceDate': lambda x: (self.current_date - x.max()).days,
                 'InvoiceNo': lambda x: len(x),
                 "TotalPrice": lambda x: x.sum()})

            RMF_data = RMF_data.rename(columns={'InvoiceDate': 'Recency','InvoiceNo':'Frequency', 'TotalPrice':'Monetary'})

            self.logger.log(self.file, "RMF_table created successfully.")
            self.logger.log(self.file, 'Leaving create_rmf_table method of stage_2 class')

            return RMF_data

        except Exception as e:
            self.logger.log(self.file, str(e))
