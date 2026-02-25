import pandas as pd
from sqlalchemy import create_engine
from src.config import Config

class DataExporter:
    def __init__(self):
        self.engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)

    def export_table(self, df: pd.DataFrame, table_name: str):
        try:
            df.to_sql(
                name=table_name,
                con=self.engine,
                if_exists="replace",
                index=False
            )
            print(f"✔ Exported {table_name} to MySQL (schema: e_master_card)")
        except Exception as e:
            print(f"Error exporting table {table_name}: {e}")
            raise