# Task 9 — Descriptive Statistics Primer

**Track:** Data Analytics | **Program:** Veda Technology Internship | **Level 1, Day 9**

## Objective
Build intuition for when to use each descriptive statistic (mean, median,
mode, standard deviation, percentiles) and what it reveals about a
distribution's skew and spread.

## Dataset
[Titanic dataset](https://www.kaggle.com/datasets/yasserh/titanic-dataset)
(891 passenger records, `Titanic.csv`).

## Columns analyzed
- `age` — passenger age
- `fare` — ticket fare
- `sibsp` — siblings/spouses aboard
- `parch` — parents/children aboard
- `survived` — survival flag (0 = No, 1 = Yes)

## Approach
1. **Python + Pandas** (`descriptive_stats.py`) — computes count, mean,
   median, mode, standard deviation, min/max, 25th/50th/75th percentiles,
   and skewness for each column, and writes them out to
   `summary_statistics.csv` plus an interpretive `report.md`.
2. **Excel** (`Titanic_Descriptive_Statistics.xlsx`) — the same summary
   table rebuilt with live Excel formulas (`AVERAGE`, `MEDIAN`, `MODE`,
   `STDEV`, `PERCENTILE`, `SKEW`) over the raw data tab, so it
   recalculates if the data changes, plus a written skew/spread analysis.

## How to run
```bash
pip install pandas
python descriptive_stats.py
```
Outputs `summary_statistics.csv` and `report.md` in the same folder.

## Key findings
| Column | Mean | Median | Skewness | Interpretation |
|---|---|---|---|---|
| Age | 29.70 | 28.00 | 0.39 | Roughly symmetric |
| Fare | 32.20 | 14.45 | 4.79 | Strongly right-skewed |
| Siblings/Spouses | 0.52 | 0.00 | 3.70 | Strongly right-skewed |
| Parents/Children | 0.38 | 0.00 | 2.75 | Strongly right-skewed |
| Survived | 0.38 | 0.00 | 0.48 | Roughly symmetric (38% survival rate) |

**Takeaway:** Age is close to symmetric, so its mean is a fair summary.
Fare, Siblings/Spouses, and Parents/Children are all right-skewed with
long tails — for these, the median and percentiles describe a "typical"
passenger better than the mean, which is inflated by a smaller number of
high-fare or large-family passengers. See `report.md` for the full
write-up.

## Files
- `Titanic.csv` — raw dataset
- `descriptive_stats.py` — Pandas analysis script
- `summary_statistics.csv` — generated stats table
- `report.md` — generated skew & spread write-up
- `Titanic_Descriptive_Statistics.xlsx` — Excel version with live formulas

---
*Submitted for the Veda Technology Data Analytics Internship, Task 9.*
