# Descriptive Statistics Write-up: Skew and Spread

## Age
- Mean: 29.7, Median: 28.0, Mode: 24.0
- Std Dev: 14.53, IQR: 20.12 - 38.0
- Skewness: 0.39 -> roughly symmetric

## Fare
- Mean: 32.2, Median: 14.45, Mode: 8.05
- Std Dev: 49.69, IQR: 7.91 - 31.0
- Skewness: 4.79 -> strongly right-skewed

## Siblings/Spouses
- Mean: 0.52, Median: 0.0, Mode: 0.0
- Std Dev: 1.1, IQR: 0.0 - 1.0
- Skewness: 3.7 -> strongly right-skewed

## Parents/Children
- Mean: 0.38, Median: 0.0, Mode: 0.0
- Std Dev: 0.81, IQR: 0.0 - 0.0
- Skewness: 2.75 -> strongly right-skewed

## Survived (0/1)
- Mean: 0.38, Median: 0.0, Mode: 0.0
- Std Dev: 0.49, IQR: 0.0 - 1.0
- Skewness: 0.48 -> roughly symmetric

## Overall takeaway
Age is close to symmetric and is well described by its mean. Fare, Siblings/Spouses, and Parents/Children are all right-skewed with long tails of high values, so for those the median and percentiles describe a 'typical' passenger better than the mean, which is pulled upward by a smaller number of high-fare or large-family passengers.
