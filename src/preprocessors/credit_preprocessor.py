import pandas as pd


class CreditPreprocessor:

    def preprocess(self, df: pd.DataFrame) -> pd.DataFrame:
        df = self._remove_duplicate_profiles(df)
        df = self._create_credit_score_range(df)
        df = self._impute_credit_limit(df)
        df = self._cap_outstanding_debt(df)
        df = self._recalculate_credit_utilisation(df)
        return df


    # 1️ Remove duplicate cust_id (keep latest valid)

    def _remove_duplicate_profiles(self, df):
        df = df.drop_duplicates(subset="cust_id", keep="last")
        return df


    # 2️ Create credit score range bands

    def _create_credit_score_range(self, df):
        bins = [300, 450, 500, 550, 600, 650, 700, 750, 800]
        labels = [f"{start}-{end-1}" for start, end in zip(bins, bins[1:])]
        df["credit_score_range"] = pd.cut(
            df["credit_score"],
            bins=bins,
            labels=labels,
            include_lowest=True,
            right=False
        )
        return df


    # 3️ Impute missing credit_limit using range-wise mode

    def _impute_credit_limit(self, df):
        df["credit_limit"] = (
            df.groupby("credit_score_range")["credit_limit"]
            .transform(lambda x: x.fillna(x.mode()[0] if not x.mode().empty else x.median()))
        )
        return df


    # 4️ Cap outstanding_debt at credit_limit

    def _cap_outstanding_debt(self, df):
        df.loc[
            df["outstanding_debt"] > df["credit_limit"],
            "outstanding_debt"
        ] = df["credit_limit"]
        return df


    # 5️ Recalculate credit utilisation for consistency

    def _recalculate_credit_utilisation(self, df):
        df["credit_utilisation"] = (
            df["outstanding_debt"] / df["credit_limit"]
        )
        return df
