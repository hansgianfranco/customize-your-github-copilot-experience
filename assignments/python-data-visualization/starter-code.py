import pandas as pd
import matplotlib.pyplot as plt
import sys
from pathlib import Path


class DataVisualizer:
    def __init__(self, csv_file):
        """Initialize the visualizer with a CSV file."""
        try:
            self.df = pd.read_csv(csv_file)
        except FileNotFoundError:
            print(f"Error: File '{csv_file}' not found.")
            sys.exit(1)
        except Exception as e:
            print(f"Error reading CSV: {e}")
            sys.exit(1)

        self.file_stem = Path(csv_file).stem

    def create_line_chart(self, x_col, y_col, title=None):
        """Create a line chart."""
        plt.figure(figsize=(10, 6))
        plt.plot(self.df[x_col], self.df[y_col], marker="o", linestyle="-")
        plt.title(title or f"{y_col} over {x_col}")
        plt.xlabel(x_col)
        plt.ylabel(y_col)
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        output_file = f"{self.file_stem}_line.png"
        plt.savefig(output_file)
        plt.close()
        print(f"Saved: {output_file}")

    def create_bar_chart(self, x_col, y_col, title=None):
        """Create a bar chart."""
        plt.figure(figsize=(10, 6))
        plt.bar(self.df[x_col], self.df[y_col], color="steelblue")
        plt.title(title or f"{y_col} by {x_col}")
        plt.xlabel(x_col)
        plt.ylabel(y_col)
        plt.xticks(rotation=45, ha="right")
        plt.grid(True, alpha=0.3, axis="y")
        plt.tight_layout()
        output_file = f"{self.file_stem}_bar.png"
        plt.savefig(output_file)
        plt.close()
        print(f"Saved: {output_file}")

    def create_scatter_plot(self, x_col, y_col, title=None):
        """Create a scatter plot."""
        plt.figure(figsize=(10, 6))
        plt.scatter(self.df[x_col], self.df[y_col], alpha=0.6, s=100)
        plt.title(title or f"{y_col} vs {x_col}")
        plt.xlabel(x_col)
        plt.ylabel(y_col)
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        output_file = f"{self.file_stem}_scatter.png"
        plt.savefig(output_file)
        plt.close()
        print(f"Saved: {output_file}")

    def create_histogram(self, col, title=None, bins=20):
        """Create a histogram."""
        plt.figure(figsize=(10, 6))
        plt.hist(self.df[col], bins=bins, color="coral", edgecolor="black")
        plt.title(title or f"Distribution of {col}")
        plt.xlabel(col)
        plt.ylabel("Frequency")
        plt.grid(True, alpha=0.3, axis="y")
        plt.tight_layout()
        output_file = f"{self.file_stem}_histogram.png"
        plt.savefig(output_file)
        plt.close()
        print(f"Saved: {output_file}")

    def create_pie_chart(self, col, title=None):
        """Create a pie chart."""
        plt.figure(figsize=(8, 8))
        value_counts = self.df[col].value_counts()
        plt.pie(value_counts, labels=value_counts.index, autopct="%1.1f%%")
        plt.title(title or f"Distribution of {col}")
        plt.tight_layout()
        output_file = f"{self.file_stem}_pie.png"
        plt.savefig(output_file)
        plt.close()
        print(f"Saved: {output_file}")

    def display_summary_statistics(self):
        """Display summary statistics."""
        print("\nData Summary:")
        print(self.df.describe())
        print(f"\nShape: {self.df.shape}")
        print(f"Columns: {list(self.df.columns)}")


def main():
    if len(sys.argv) < 2:
        print("Usage: python starter-code.py <csv_file>")
        print("Example: python starter-code.py data.csv")
        sys.exit(1)

    csv_file = sys.argv[1]
    visualizer = DataVisualizer(csv_file)

    # Display summary
    visualizer.display_summary_statistics()

    # Example: Create visualizations with the first numeric columns
    numeric_cols = visualizer.df.select_dtypes(include=["number"]).columns.tolist()
    categorical_cols = visualizer.df.select_dtypes(include=["object"]).columns.tolist()

    if len(numeric_cols) >= 2:
        print("\nGenerating visualizations...")
        visualizer.create_line_chart(
            categorical_cols[0] if categorical_cols else numeric_cols[0],
            numeric_cols[0],
            "Line Chart",
        )
        visualizer.create_bar_chart(
            categorical_cols[0] if categorical_cols else numeric_cols[0],
            numeric_cols[1],
            "Bar Chart",
        )
        if len(numeric_cols) >= 2:
            visualizer.create_scatter_plot(numeric_cols[0], numeric_cols[1], "Scatter")
        visualizer.create_histogram(numeric_cols[0], "Histogram")

    if categorical_cols:
        visualizer.create_pie_chart(categorical_cols[0], "Pie Chart")

    print("\nVisualization complete!")


if __name__ == "__main__":
    main()
