
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# خواندن داده‌ها
customers = pd.read_csv('customers.csv')
sales = pd.read_csv('sales.csv')

# تبدیل ستون تاریخ به datetime
sales['date'] = pd.to_datetime(sales['date'])

# اضافه کردن ستون ماه فروش
sales['month'] = sales['date'].dt.to_period('M')

# ۱. مجموع فروش کل
total_sales = sales['amount'].sum()

# ۲. میانگین مبلغ فروش
average_sales = sales['amount'].mean()

# ۳. مشتریانی که بیش از ۳ بار خرید کرده‌اند = مشتریان وفادار
loyal_customers = sales['customer_id'].value_counts()
loyal_customers = loyal_customers[loyal_customers >= 3]

# ۴. گروه‌بندی بر اساس ماه برای رسم نمودار فروش ماهانه
monthly_sales = sales.groupby('month')['amount'].sum()

# ۵. پر فروش‌ترین محصول
top_product = sales['product_name'].value_counts().idxmax()

# ۶. رسم نمودار فروش ماهانه
plt.figure(figsize=(10, 5))
monthly_sales.plot(kind='line', marker='o')
plt.title('Monthly Sales')
plt.xlabel('Month')
plt.ylabel('Total Sales Amount')
plt.grid(True)
plt.tight_layout()
plt.show()

# ۷. نمودار دایره‌ای مشتریان وفادار
plt.figure(figsize=(6, 6))
loyal_customers.plot(kind='pie', autopct='%1.1f%%')
plt.title('Loyal Customers (3+ purchases)')
plt.ylabel('')
plt.tight_layout()
plt.show()

# ۸. نمودار تعداد فروش به ازای هر محصول
plt.figure(figsize=(8, 5))
sns.countplot(data=sales, x='product_name', order=sales['product_name'].value_counts().index)
plt.title('Product Sales Count')
plt.xlabel('Product')
plt.ylabel('Count')
plt.tight_layout()
plt.show()

# ۹. نمایش خلاصه‌ای از تحلیل
summary = f"""
📊 تحلیل داده‌های فروش:

- مجموع فروش کل: {total_sales:.2f} دلار
- میانگین مبلغ هر خرید: {average_sales:.2f} دلار
- تعداد مشتریان وفادار (۳ خرید یا بیشتر): {len(loyal_customers)} نفر
- پرفروش‌ترین محصول: {top_product}
"""

print(summary)
