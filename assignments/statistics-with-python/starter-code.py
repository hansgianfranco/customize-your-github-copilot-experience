import pandas as pd
import numpy as np
from scipy import stats
import sys
from pathlib import Path


class StatisticalAnalyzer:
    def __init__(self, csv_file):
        """Initialize analyzer with a CSV file."""
        try:
            self.df = pd.read_csv(csv_file)
        except FileNotFoundError:
            print(f"Error: File '{csv_file}' not found.")
            sys.exit(1)
        except Exception as e:
            print(f"Error reading CSV: {e}")
            sys.exit(1)

        self.file_stem = Path(csv_file).stem

    def get_descriptive_statistics(self):
        """Calculate descriptive statistics for numeric columns."""
        numeric_cols = self.df.select_dtypes(include=[np.number]).columns
        stats_dict = {}

        for col in numeric_cols:
            data = self.df[col].dropna()
            stats_dict[col] = {
                "mean": data.mean(),
                "median": data.median(),
                "mode": data.mode().values[0] if not data.mode().empty else None,
                "std": data.std(),
                "variance": data.var(),
                "min": data.min(),
                "max": data.max(),
                "q1": data.quantile(0.25),
                "q3": data.quantile(0.75),
                "iqr": data.quantile(0.75) - data.quantile(0.25),
                "count": len(data),
            }

        return stats_dict

    def detect_outliers(self, column_name):
        """Detect outliers using IQR method."""
        data = self.df[column_name].dropna()
        q1 = data.quantile(0.25)
        q3 = data.quantile(0.75)
        iqr = q3 - q1
        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr

        outliers = data[(data < lower_bound) | (data > upper_bound)]
        return {
            "lower_bound": lower_bound,
            "upper_bound": upper_bound,
            "outliers": outliers.tolist(),
            "count": len(outliers),
        }

    def correlation_analysis(self):
        """Calculate correlation matrix for numeric columns."""
        numeric_df = self.df.select_dtypes(include=[np.number])
        correlation_matrix = numeric_df.corr()
        return correlation_matrix

    def handle_missing_values(self, strategy="drop"):
        """Handle missing values in the dataset."""
        if strategy == "drop":
            return self.df.dropna()
        elif strategy == "fill_mean":
            numeric_cols = self.df.select_dtypes(include=[np.number]).columns
            df_copy = self.df.copy()
            for col in numeric_cols:
                df_copy[col].fillna(df_copy[col].mean(), inplace=True)
            return df_copy
        return self.df

    def t_test(self, column, population_mean=0):
        """Perform a one-sample t-test."""
        data = self.df[column].dropna()
        t_statistic, p_value = stats.ttest_1samp(data, population_mean)
        return {"t_statistic": t_statistic, "p_value": p_value}

    def group_analysis(self, group_column, numeric_column):
        """Analyze numeric data grouped by a categorical column."""
        grouped = self.df.groupby(group_column)[numeric_column].agg(
            ["mean", "median", "std", "count"]
        )
        return grouped

    def generate_report(self):
        """Generate a comprehensive statistical report."""
        report = "=" * 60 + "\n"
        report += "STATISTICAL ANALYSIS REPORT\n"
        report += "=" * 60 + "\n\n"

        # Dataset overview
        report += "DATASET OVERVIEW:\n"
        report += f"Shape: {self.df.shape}\n"
        report += f"Columns: {list(self.df.columns)}\n"
        report += f"Missing values:\n{self.df.isnull().sum()}\n\n"

        # Descriptive statistics
        report += "DESCRIPTIVE STATISTICS:\n"
        report += "-" * 60 + "\n"
        desc_stats = self.get_descriptive_statistics()
        for col, stats_data in desc_stats.items():
            report += f"\n{col}:\n"
            for key, value in stats_data.items():
                report += f"  {key}: {value:.4f if isinstance(value, float) else value}\n"

        # Outlier detection
        report += "\n\nOUTLIER DETECTION (IQR Method):\n"
        report += "-" * 60 + "\n"
        numeric_cols = self.df.select_dtypes(include=[np.number]).columns
        for col in numeric_cols:
            outlier_info = self.detect_outliers(col)
            report += f"\n{col}:\n"
            report += f"  Outlier bounds: [{outlier_info['lower_bound']:.4f}, {outlier_info['upper_bound']:.4f}]\n"
            report += f"  Number of outliers: {outlier_info['count']}\n"

        # Correlation analysis
        report += "\n\nCORRELATION MATRIX:\n"
        report += "-" * 60 + "\n"
        corr_matrix = self.correlation_analysis()
        report += corr_matrix.to_string()
        report += "\n"

        return report

    def display_report(self):
        """Display and save the report."""
        report = self.generate_report()
        print(report)

        # Save report
        report_file = f"{self.file_stem}_analysis_report.txt"
        with open(report_file, "w") as f:
            f.write(report)
        print(f"\nReport saved to: {report_file}")


def main():
    if len(sys.argv) < 2:
        print("Usage: python starter-code.py <csv_file>")
        print("Example: python starter-code.py data.csv")
        sys.exit(1)

    csv_file = sys.argv[1]
    analyzer = StatisticalAnalyzer(csv_file)
    analyzer.display_report()


if __name__ == "__main__":
    main()
