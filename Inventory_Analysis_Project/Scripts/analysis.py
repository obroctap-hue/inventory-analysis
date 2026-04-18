import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("inventory_report.csv")
clean = df[df["inventory"] > 0]

clean["damage_rate"] = clean["damaged"] / clean["inventory"]

# Calculate and plot damage rate
summary = clean.groupby("category")["damage_rate"].mean()
summary_percent_sort = summary.sort_values(ascending=False)*100
summary_percent_sort.plot(kind='bar')
plt.title("Damage Rate by Category (%)")
plt.xlabel("Category")
plt.ylabel("Damage Rate (%)")
plt.xticks(rotation=0) 
plt.savefig("damage_rate_chart.png")
plt.show()

#Calculate and plot total damage
impact = clean.groupby("category")["damaged"].sum()
impact.plot(kind='bar')
plt.title("Total Damaged Units by Category")
plt.xlabel("Category")
plt.ylabel("Units Damaged")
plt.xticks(rotation=0)
plt.savefig("total_damage_chart.png")
plt.show()

#Calculate damage rate and and graph top 5
clean["damage_rate"] = clean["damaged"] / clean["inventory"] #Create a new column for damage rate
top_items = clean.sort_values(by="damage_rate", ascending=False).head(5) #Sort damage rate descending and show only the top 5
top_items["damage_rate"] = top_items["damage_rate"] * 100 #Multiply by 100 for percentages
top_items.set_index("item")["damage_rate"].plot(kind="bar") # Set item as x axis, and damage rate as y axis
plt.title("Top 5 Items by Damage Rate (%)")
plt.xlabel("Item")
plt.ylabel("Damage Rate (%)")
plt.xticks(rotation = 45)
plt.savefig("top_5_damage_rate_items")
plt.show()
