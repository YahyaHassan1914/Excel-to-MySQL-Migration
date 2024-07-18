import pandas as pd

# Load the Excel file
# Load the Excel file (specify the sheet name if there's more than one sheet)
df = pd.read_excel('items.xlsx')

# Display the DataFrame
print(df)

items = df['Item']
print(items)

high_price_items = df[df['Price'] > 2.0]
print(high_price_items)

df.to_excel('new_items.xlsx', index=False)