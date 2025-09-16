from fitness import *
import numpy as np
import pandas as pd
#Average Values
print('Average Steps',df['Steps'].mean())
print('Average Sleep',df['sleep_cycle'].mean())

#Maximum CALORIES
print("Maximum Calories",df['Calories'].max())

#Day with less than 6 hours sleep
print(df[df['sleep_cycle']<6])

df['Sleep Quality']=np.where(df['sleep_cycle']>=7,'Good Sleep','Poor Sleep')

#Modifying Activity Level
df['Activity Level']=pd.cut(df['Steps'],bins=[0,5000,10000,20000],labels=['LOW','MODERATE','HIGH'])

#Modifying Calorie Level 
df['Calorie Level']=pd.cut(df['Calories'],bins=[0,2000,3000,4000],labels=['LOW CALORIE INTAKE','MODERATE CALORIE INTAKE','HIGH CALORIE INTAKE'])

df.to_csv('fitness_dataset.csv')


