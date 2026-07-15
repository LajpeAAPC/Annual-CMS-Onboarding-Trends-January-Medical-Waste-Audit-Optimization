#Exploratory Data Analysis (EDA)
import pandas as pd
import numpy as np

data=pd.read_csv(r"C:\Users\Lajpe\Downloads\Medical-Equipment-Suppliers.csv")

data.head(10)
data.info()
data.describe()

<class 'pandas.core.frame.DataFrame'>
RangeIndex: 57197 entries, 0 to 57196
Data columns (total 17 columns):
 #   Column                  Non-Null Count  Dtype  
---  ------                  --------------  -----  
 0   provider_id             57197 non-null  int64  
 1   acceptsassignement      57197 non-null  bool   
 2   participationbegindate  57197 non-null  object 
 3   businessname            57197 non-null  object 
 4   practicename            57197 non-null  object 
 5   practiceaddress1        57197 non-null  object 
 6   practiceaddress2        12821 non-null  object 
 7   practicecity            57197 non-null  object 
 8   practicestate           57197 non-null  object 
 9   practicezip9code        57197 non-null  int64  
 10  telephonenumber         57197 non-null  int64  
 11  specialitieslist        56445 non-null  object 
 12  providertypelist        6752 non-null   object 
 13  supplieslist            57171 non-null  object 
 14  latitude                57197 non-null  float64
 15  longitude               57197 non-null  float64
 16  is_contracted_for_cba   57197 non-null  bool   
dtypes: bool(2), float64(2), int64(3), object(10)
memory usage: 6.7+ MB
provider_id	practicezip9code	telephonenumber	latitude	longitude
count	5.719700e+04	5.719700e+04	5.719700e+04	57197.000000	57197.000000
mean	2.136286e+07	4.650824e+08	1.485105e+12	37.496076	-89.971750
std	3.191091e+06	2.944270e+08	9.431909e+13	5.316228	15.403696
min	2.030322e+07	6.030000e+02	1.789888e+09	13.393044	-159.584854
25%	2.040013e+07	2.174215e+08	4.025528e+09	33.857070	-96.711840
50%	2.050016e+07	4.334296e+08	6.158834e+09	38.678480	-85.847000
75%	2.061583e+07	7.413228e+08	8.063569e+09	41.148556	-79.054350
max	3.436353e+07	9.992107e+08	9.047333e+15	64.858610	145.702290

# Convert the column to datetime
data['participationbegindate'] = pd.to_datetime(data['participationbegindate'])

# Check for missing values (optional)
data['participationbegindate'].isna().sum()

np.int64(0)

# O or no missing values. 
#Ready to export cleaned data to CSV or connect directly.
data.to_csv('cleaned_participation_data.csv', index=False)
