import pandas as pd
from sqlalchemy import create_engine
from src.config import Config

class DataLoader:
    def __init__(self):
        self.engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)

    def load_table(self, table_name:str) -> pd.DataFrame:
        try:
            query = f"SELECT * FROM {table_name}"
            df = pd.read_sql(query, self.engine)
            print(f"{table_name} loaded successfully. shape: {df.shape}")
            return df
        except Exception as e:
            print(f"Error loading table: {table_name}:{e}")
            raise