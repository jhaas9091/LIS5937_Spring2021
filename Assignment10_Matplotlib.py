"""Module 10 Assignment
Julie Haas
LIS 5937
Spring 2021"""

import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv (
    r"C:\Users\jbae1\OneDrive\UCF MLIS\LIS5937 - Python for Data Sci Prof\Week 10\Assign10\LifeExpectancy_Edited2.csv")

df_x = pd.DataFrame(data, columns=['Year'])
df_y = pd.DataFrame(data, columns=['Life Expectancy'])
#print(df_x, df_y)

plt.title("Life Expectancy at Birth in U.S. [2017-2060]")
plt.ylabel('Life Expectancy [in years]')
plt.xlabel('Birth Year')

plt.plot(df_x,df_y)
plt.show()
plt.clf()
