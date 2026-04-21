import pandas as pd
from sqlalchemy import create_engine

# load dataset (FIXED 🔥)
df = pd.read_csv(
    'data/raw_data.csv',
    sep='\t',          # ✅ MOST IMPORTANT CHANGE
    encoding='latin1',
    engine='python'
)

#====================================#
# 1. Basic info
#====================================#
print("Loaded Successfully ✅")
print(df.head())
print("Shape:", df.shape)


#=====================================#
# 2. Remove duplicates
#=====================================#
df = df.drop_duplicates()

#=====================================#
# 3. Missing values handle
#=====================================#
df = df.dropna()

#====================================#
# 4. Column cleaning
#====================================#
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

#====================================#
# 5. Feature Engineering
#====================================#
if 'sales' in df.columns and 'profit' not in df.columns:
    df['profit'] = df['sales'] * 0.2 

#=================================#
# 6. Convert date
#=================================#
if 'order_date' in df.columns:
    df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')

#=================================#
# 7. Save clean data
#=================================#
df.to_csv('data/fixed_data.csv', index=False)

print("✅ Fixed file saved")

df = pd.read_csv('data/fixed_data.csv')

engine = create_engine("mysql+pymysql://datauser:1234@localhost/ecommerce")

df.to_sql('sales', con=engine, if_exists='replace', index=False)

print("✅ Data uploaded successfully")