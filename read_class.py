import pandas as pd

class FILES:
    def __init__(self):
        pass

    def Read_data(self,file_name):
        visa_df=pd.read_csv(file_name)
        return visa_df

if __name__=="__main__":
    FILES.Read_data(file_name)
    print("Data read successfully")