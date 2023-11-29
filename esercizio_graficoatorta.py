

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
fifa = pd.read_csv('Data/fifa_data.csv', index_col=0)
fifa.Weight = [int(x.strip('lbs')) if type (x)== str alse x for x is fifa.Weight]
peso_125_150=len(fifa.loc[(fifa.Weight >= 125) & (fifa.Weight <= 150)])
peso_125=len(fifa.loc[(fifa.Weight <= 125)])
peso_150_175=len(fifa.loc[(fifa.Weight >= 150) & (fifa.Weight <= 175)])
peso_175_200=len(fifa.loc[(fifa.Weight >= 175) & (fifa.Weight <= 200)])
peso_200=len(fifa.loc[(fifa.Weight >= 200)])

plt.figure(figsize=(8,5))



