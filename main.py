#this is the main program with classes

from read_class import FILES
from tables_class import TABLE_DATA
from bar_class import CHART

file_name=r"C:\Users\Saurabh.Dugar\Documents\NareshIT\Data_Files\Visadataset.csv"
df=FILES().Read_data(file_name)
keys,values=TABLE_DATA().DATA_TABLES(df)
CHART().BAR_CHART(keys,values)
print(keys,values)

