import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")
plt.style.use("fivethirtyeight")


USAhousing = pd.read_csv('death.csv')
print(USAhousing.head())
print(USAhousing.info())
print(USAhousing.describe())
print(USAhousing.columns)


# Test to see we loaded the data correctly
print(USAhousing[' FIPS'])

