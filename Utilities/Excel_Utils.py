import pandas as pd


class get_data_from_CSV:

    def get_travellers(self):
        try:
            df = pd.read_csv('traveller_information.csv')
            # print("excel utils: ", df)
            return df
        except Exception as ex:
            print("Read csv into data frame got and exception: ", ex)
