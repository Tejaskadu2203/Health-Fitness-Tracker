import numpy as np
import pandas as pd
#Date from start to 6 more dates
date=pd.date_range(start='2025-01-01',periods=500,freq='D')

#Steps guessing randomly between 2000-10000
steps=np.random.randint(2000,20000,size=500)

#Random Calories between 1500-4000
calories=np.random.randint(1500,4000,size=500)

#Sleep Cycle
sleep_cycle=np.round(np.random.uniform(5,9,size=500),1)

#Creating a DataFrame
df=pd.DataFrame({
    'Dates':date,
    'Steps':steps,
    "Calories":calories,
    'sleep_cycle':sleep_cycle
})
print(df)
