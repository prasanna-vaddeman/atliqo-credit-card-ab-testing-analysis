import pandas as pd
class CustomerPreprocessor:

    def preprocess(self, df):
        df = self._clean_income(df)
        df = self._clean_age(df)
        df = self._create_age_group(df)
        return df

    def _clean_income(self, df):
        df.loc[df['annual_income'] < 100, 'annual_income'] = None
        df['annual_income'] = (
            df.groupby('occupation')['annual_income']
            .transform(lambda x: x.fillna(x.median()))
        )
        return df

    def _clean_age(self, df):
        df.loc[(df['age'] < 15) | (df['age'] > 80), 'age'] = None
        df['age'] = (
            df.groupby('occupation')['age']
            .transform(lambda x: x.fillna(x.median()))
        )
        return df

    def _create_age_group(self, df):
        bins = [17, 25, 48, 65]
        labels = ["18-25", "26-48", "49-65"]
        df['age_group'] = pd.cut(df['age'], bins=bins, labels=labels)
        return df
