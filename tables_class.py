class TABLE_DATA:

    def __init__(self):
        pass

    def DATA_TABLES(self,df):
        keys=df['continent'].value_counts().keys()
        values=df['continent'].value_counts().values
        print(keys,values)
        print("Value counts of the feature continent:",df['continent'].value_counts())
        return keys,values

if __name__ == "__main__":
    TABLE_DATA.DATA_TABLES(df)