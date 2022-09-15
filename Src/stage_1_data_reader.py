import pandas as pd
from Src.logger import AppLogger

class ReadData:

    """
    Description: This Module helps to read the data
    """

    def __init__(self):
        self.logger = AppLogger()
        self.file = open('Logs/Data_reading_log.txt', 'a+')

    def read_data(self, data):

        """
        Description: This method read the data in csv format
        return: DataFrame
        """

        try:
            self.logger.log(self.file,
                            'Inside read_data method of stage_1 class >>> Started reading the given csv data.')

            dataframe = pd.read_csv(data, on_bad_lines='skip', parse_dates=['InvoiceDate'], encoding='latin1')
            self.logger.log(self.file, 'Data read successfully. Returning dataframe')
            self.logger.log(self.file, 'Leaving read_data method of stage_1 class')

            return dataframe

        except Exception as e:
            self.logger.log(self.file, str(e))
