# Inventory Damage Analysis

## Overview ##

Drawing on my experience in inventory control, this project analyzes inventory data to identify damage trends across item categories and highlight opportunities to reduce future damage claims.

---

## Objectives ##

* Clean and validate inventory data
* Calculate damage rate (`damaged / inventory`)
* Identify high-risk categories and items
* Visualize key performance metrics

---

## Tools & Technologies ##

* Python
* pandas
* matplotlib

---

## Project Structure ##

```
inventory-analysis/
│
├── data/
│   └── inventory_report.csv
│
├── scripts/
│   └── analysis.py
│
├── output/
│   ├── damage_rate_by_category.png
│   ├── total_damaged_units_by_category.png
│   └── top_5_items_by_damage_rate.png
│
└── README.md
```

---

## Methodology ##

1. Data Cleaning
   * Removed records with invalid inventory values (≤ 0)
2. Feature Engineering
   * Created a `damage_rate` metric to standardize comparisons
3. Aggregation
   * Calculated average damage rate by category
   * Summed total damaged units by category
4. Visualization
   * Generated bar charts to highlight trends and outliers

---

## Key Insights ##
* The **Fruit category** has the highest damage rate (~6.5%), significantly higher than other categories
* The **Snack category** has the lowest damage rate (~4.2%)
* Certain items, like bananas, contribute disproportionately to total damage, indicating targeted improvement opportunities

---

## Outputs ##
* Damage rate by category (bar chart)
* Total damaged units by category (bar chart)
* Top 5 items by damage rate

---

## How to Run ##
1. Clone the repository
2. Navigate to the project folder
3. Run the script: python scripts/analysis.py

---

## Future Improvements ##
* Incorporate larger and more realistic datasets
* Add time-based analysis (trends over time)
* Build an interactive dashboard (e.g., Power BI or Streamlit)

