import pandas as pd
from datetime import date
import seaborn as sns
import matplotlib.pyplot as plt

crossings = pd.read_csv("../data/cycle_crossings.csv")
crossings.head()
crossings.dtypes
crossings.Date = pd.to_datetime(crossings.Date, format="%m/%d")
crossings.Date = crossings['Date'].apply(lambda x: date(2017, x.month, x.day))
crossings['Month'] = pd.Categorical(crossings['Date'].apply(lambda x: x.strftime("%b")))

melted_crossings = crossings.melt(id_vars=['Date', 'Day', 'Month'], value_vars=[
                                  'Brooklyn Bridge', 'Manhattan Bridge',
                                  'Williamsburg Bridge', 'Queensboro Bridge'],
                                  var_name='Bridge',
                                  value_name='Crossings')

(
    sns.barplot(
        data=melted_crossings,
        x="Day", y='Crossings',
        hue='Bridge',
        errorbar=None,
        estimator='sum',
    )
)

plt.show()

wednesday_crossings = crossings.loc[
    crossings['Day'] == 'Wednesday', :
]

(
    sns.boxplot(
        data=wednesday_crossings, x='Day',
        y='Williamsburg Bridge', hue='Month'
    )
)

plt.show()

# Task 1: See if you can create multiple barplots for the weekend data only, with 
# each day on a separate plot but in the same row. Each subplot should show the 
# highest number of crossings for each bridge.

weekends_crossings = melted_crossings.loc[
    melted_crossings.Day.isin(['Saturday', 'Sunday']), :
]

(
    sns.catplot(
        data=weekends_crossings, x='Bridge', y='Crossings',
        hue='Day', col='Day', estimator='max', kind='bar',
        errorbar=None,
    )
)
plt.show()

# Task 2: See if you can draw three boxplots in a row containing separate monthly 
# crossings for the Brooklyn Bridge for Wednesdays only.
(
    sns.boxplot(
        data=wednesday_crossings, x='Day', y='Brooklyn Bridge',
        hue='Month'
    )
)
plt.show()
