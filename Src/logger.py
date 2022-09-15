from datetime import datetime
import os


class AppLogger:

    def make_log_folder(self, log_folder_name):
        try:
            if not os.path.isdir(log_folder_name):
                os.makedirs(log_folder_name)
        except Exception as e:
            return e

    def log(self,file_name, log_message):
        self.now = datetime.now()
        self.current_time =self.now.strftime('%H:%M:%S')
        self.date =self.now.date()

        file_name.write(str(self.date) + "/" + str(self.current_time) + "\t\t" + log_message + "\n")