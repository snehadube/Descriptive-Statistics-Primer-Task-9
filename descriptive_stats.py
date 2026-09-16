"""
Task 9 - Descriptive Statistics Primer
Data Analytics Track | Veda Technology Internship

Calculates and interprets mean, median, mode, standard deviation, and
percentiles for the key numeric columns of the Titanic dataset, and
writes a short markdown report on what the numbers reveal about skew
and spread.

Usage:
    python descriptive_stats.py
"""

import pandas as pd

DATA_FILE = "Titanic.csv"
ANALYSIS_COLUMNS = ["age", "fare", "sibsp", "parch", "survived"]
DISPLAY_NAMES = {
    "age": "Age",
    "fare": "Fare",
    "sibsp": "Siblings/Spouses",
    "parch": "Parents/Children",
    "survived": "Survived (0/1)",
}


def load_data(path: str) -> pd.DataFrame:
    return pd.read_csv(path)


def summary_statistics(df: pd.DataFrame, columns: list) -> pd.DataFrame:
    """Build a mean/median/mode/std/percentile table for the given columns."""
    rows = []
    for col in columns:
        series = df[col]
        rows.append(
            {
                "Metric": DISPLAY_NAMES[col],
                "Count (n)": series.count(),
                "Mean": round(series.mean(), 2),
                "Median": round(series.median(), 2),
                "Mode": series.mode().iloc[0],
                "Std Dev": round(series.std(), 2),
                "Min": series.min(),
                "25th %ile": round(series.quantile(0.25), 2),
                "50th %ile": round(series.quantile(0.50), 2),
                "75th %ile": round(series.quantile(0.75), 2),
                "Max": series.max(),
                "Skewness": round(series.skew(), 2),
                "Missing": series.isna().sum(),
            }
        )
    return pd.DataFrame(rows).set_index("Metric")


def classify_skew(skew: float) -> str:
    if skew > 1:
        return "strongly right-skewed"
    if skew > 0.5:
        return "moderately right-skewed"
    if skew > -0.5:
        return "roughly symmetric"
    if skew > -1:
        return "moderately left-skewed"
    return "strongly left-skewed"


def build_writeup(stats: pd.DataFrame) -> str:
    lines = ["# Descriptive Statistics Write-up: Skew and Spread\n"]
    for col_display in stats.index:
        row = stats.loc[col_display]
        lines.append(f"## {col_display}")
        lines.append(
            f"- Mean: {row['Mean']}, Median: {row['Median']}, Mode: {row['Mode']}\n"
            f"- Std Dev: {row['Std Dev']}, IQR: {row['25th %ile']} - {row['75th %ile']}\n"
            f"- Skewness: {row['Skewness']} -> {classify_skew(row['Skewness'])}\n"
        )
    lines.append("## Overall takeaway")
    lines.append(
        "Age is close to symmetric and is well described by its mean. "
        "Fare, Siblings/Spouses, and Parents/Children are all right-skewed "
        "with long tails of high values, so for those the median and "
        "percentiles describe a 'typical' passenger better than the mean, "
        "which is pulled upward by a smaller number of high-fare or "
        "large-family passengers."
    )
    return "\n".join(lines)


def main():
    df = load_data(DATA_FILE)
    stats = summary_statistics(df, ANALYSIS_COLUMNS)

    print("\n=== Summary Statistics ===\n")
    print(stats.to_string())

    stats.to_csv("summary_statistics.csv")

    writeup = build_writeup(stats)
    with open("report.md", "w") as f:
        f.write(writeup)

    print("\nSaved: summary_statistics.csv, report.md")


if __name__ == "__main__":
    main()
