# 📘 Assignment: Python Data Visualization

## 🎯 Objective

Learn data visualization techniques using matplotlib or plotly to create charts, graphs, and interactive visualizations that tell stories with data.

## 📝 Tasks

### 🛠️ Create a Data Visualization Dashboard

#### Description
Build a Python script that reads data from CSV or JSON files and creates multiple visualizations to explore and communicate insights. The script should generate various chart types and save them as images or interactive HTML files.

#### Requirements
Completed program should:

- Read data from a CSV file containing at least 3-4 columns.
- Create at least 4 different types of visualizations:
  - Line chart (for trends over time or categories).
  - Bar chart (for comparisons).
  - Scatter plot (for relationships between variables).
  - Pie chart or histogram (for distributions).
- Customize visualizations with titles, labels, legends, and color schemes.
- Handle missing or invalid data gracefully.
- Save visualizations as static images (PNG/JPG) or interactive HTML files.
- Provide filtering or sorting options for the visualizations.
- Include summary statistics (mean, median, count) displayed on charts where relevant.
- Bonus: Create an interactive dashboard using Plotly or similar library.

Example usage:

```bash
python starter-code.py sales_data.csv
# Generates: sales_line.png, sales_bar.png, sales_scatter.png, sales_distribution.html
```

Data example (CSV):

```
Date,Product,Sales,Region
2024-01-01,Widget A,150,North
2024-01-02,Widget B,200,South
...
```

Starter code: see `starter-code.py` in this folder.
