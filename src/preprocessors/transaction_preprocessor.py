import pandas as pd
import numpy as np


class TransactionPreprocessor:

    def preprocess(self, df: pd.DataFrame) -> pd.DataFrame:
        df = self._fill_platform_nulls(df)
        df = self._handle_zero_transactions(df)
        df = self._handle_outliers(df)
        return df


    # 1️ Fill missing platform using global mode

    def _fill_platform_nulls(self, df):
        df["platform"] = df["platform"].fillna(df["platform"].mode()[0])
        return df


    # 2️ Replace zero transaction amounts

    def _handle_zero_transactions(self, df):

        mask = (
            (df["platform"] == "Amazon") &
            (df["product_category"] == "Electronics") &
            (df["payment_type"] == "Credit Card") &
            (df["tran_amount"] == 0)
        )

        median_value = (
            df.loc[
                (df["platform"] == "Amazon") &
                (df["product_category"] == "Electronics") &
                (df["payment_type"] == "Credit Card") &
                (df["tran_amount"] > 0),
                "tran_amount"
            ].median()
        )

        df.loc[mask, "tran_amount"] = median_value

        return df


    # 3️ Handle Outliers using Category-wise Mean

    def _handle_outliers(self, df):

        df["tran_amount"] = df["tran_amount"].astype(float)

        Q1 = df["tran_amount"].quantile(0.25)
        Q3 = df["tran_amount"].quantile(0.75)
        IQR = Q3 - Q1

        upper = Q3 + 2 * IQR

        tran_mean_per_category = (
            df.groupby("product_category")["tran_amount"].mean()
        )

        outliers = df[df["tran_amount"] > upper]

        df.loc[
            outliers.index,
            "tran_amount"
        ] = outliers["product_category"].map(tran_mean_per_category)

        return df
