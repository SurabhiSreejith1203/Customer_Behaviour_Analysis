import pandas as pd
df=pd.read_csv('customer_shopping_behavior.csv')
# print(df.head())#show values of 1st 5 rows
# print(df.info())#shows attributes
# print(df.describe(include='all'))#if include not mention it only shows numerical values 
# print(df.isnull().sum())
df['Review Rating']=df['Review Rating'].fillna(df.groupby('Category')['Review Rating'].transform('median'))
# print(df.isnull().sum())
df.columns=df.columns.str.strip().str.lower().str.replace(' ','_')
df=df.rename(columns={'purchase_amount_(usd)': 'purchase_amount'})
#print(df.columns)
# Create new column of age group
df['age_group'] = pd.qcut(df['age'], q=4, labels=['Young', 'Adult', 'Middle_Aged', 'Senior'])
#create column purchase_freq_days
freq_map={'Annually':365,'Bi-Weekly':14,'Every 3 Months':90,'Fortnightly':14,'Monthly':30,'Quarterly':90,'Weekly':7}
df['purchase_freq_days']=df['frequency_of_purchases'].map(freq_map)
# print(df[['age','age_group','frequency_of_purchases','purchase_freq_days']].head(10))
print((df['discount_applied']==df['promo_code_used']).all())
df= df.drop(columns='promo_code_used')
print('promo_code_used' in df.columns)
from sqlalchemy import create_engine
engine = create_engine('postgresql+psycopg2://postgres:Surabhi%401203@localhost:5432/customer_behaviour')
df.to_sql('customer', engine, if_exists='replace', index=False)
print('done')