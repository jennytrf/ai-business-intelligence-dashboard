import pandas as pd

def load_data(path="data/business_data.csv"):
    df = pd.read_csv(path, parse_dates=["date"])
    return df

def calculate_kpis(df):
    df["revenue_growth"] = df["revenue"].pct_change() * 100
    df["churn_rate"] = (df["churned_customers"] / df["customers"]) * 100

    total_revenue = df["revenue"].sum()
    avg_growth = df["revenue_growth"].mean()
    avg_churn = df["churn_rate"].mean()

    return df, total_revenue, avg_growth, avg_churn
