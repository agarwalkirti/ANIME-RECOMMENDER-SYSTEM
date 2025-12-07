import pandas as pd

class AnimeDataLoader:
    def __init__(self,original_csv:str,processed_csv:str):
        self.original_csv = original_csv
        self.processed_csv = processed_csv

    def load_and_process(self):
        df = pd.read_csv(self.original_csv, encoding='utf-8',on_bad_lines='skip').dropna()
        required_cols = {'Name','Genres','sypnopsis'}
        # inspection check if required column is missing then raise exception
        missing = required_cols - set(df.columns) 
        if missing:
            raise ValueError(missing," Missing column in CSV file")
        
        df['combined_info'] = (
            "Title: " + df["Name"] + " Overview: " + df["sypnopsis"] + " Genres: "+df['Genres']
        )
        # creating combined_info dataframe and save it into processed_csv in same path as of original csv
        df[['combined_info']].to_csv(self.processed_csv, index=False,encoding='utf-8')

        return self.processed_csv




        