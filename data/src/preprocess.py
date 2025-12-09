import pandas as pd

def preprocess_data(path="data/sample_data.csv"):
    # Read the sample CSV file
    df = pd.read_csv(path)

    # Calculate simple metrics
    df["daily_change"] = df["kpi"].pct_change()
    threshold = df["kpi"].std()
    df["is_anomaly"] = df["kpi"].diff().abs() > threshold

    # Create a small summary dictionary
    summary = {
        "average_kpi": float(df["kpi"].mean()),
        "max_kpi": float(df["kpi"].max()),
        "min_kpi": float(df["kpi"].min()),
        "anomalies": df[df["is_anomaly"]].to_dict(orient="records")
    }

    return summary

# This will run when you execute the script
if __name__ == "__main__":
    print(preprocess_data())
