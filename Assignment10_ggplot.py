"""Module 10 Assignment
Julie Haas
LIS 5937
Spring 2021"""

import pandas as pd
from ggplot import *

life_exp = pd.read_csv(r'LifeExpectancy_Census_Edited.csv')

p = ggplot(life_exp, aes(y='Life Expectancy', x='Year', color="Sex")) + geom_point()

print(p)
