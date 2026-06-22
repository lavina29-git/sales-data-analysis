import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv('train.csv')
print("Dataset loaded! Shape:", df.shape)

# Data Cleaning
df.dropna(inplace=True)
print("After cleaning:", df.shape[0], "rows")

# Chart 1 - Sales by Category
df.groupby('Category')['Sales'].sum().plot(kind='bar')
plt.title('Sales by Category')
plt.xlabel('Category')
plt.ylabel('Total Sales')
plt.tight_layout()
plt.savefig('chart1_sales_by_category.png')
plt.clf()
print("Chart 1 saved!")

# Chart 2 - Sales by Region
df.groupby('Region')['Sales'].sum().plot(kind='bar', color='green')
plt.title('Sales by Region')
plt.xlabel('Region')
plt.ylabel('Total Sales')
plt.tight_layout()
plt.savefig('chart2_sales_by_region.png')
plt.clf()
print("Chart 2 saved!")

# Chart 3 - Monthly Sales Trend
df['Order Date'] = pd.to_datetime(df['Order Date'], dayfirst=True)
df['Month'] = df['Order Date'].dt.to_period('M')
df.groupby('Month')['Sales'].sum().plot()
plt.title('Monthly Sales Trend')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.tight_layout()
plt.savefig('chart3_monthly_trend.png')
plt.clf()
print("Chart 3 saved!")

print("All charts saved successfully!")
