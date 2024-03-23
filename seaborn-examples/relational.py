import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import date

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

sns.set_theme(style='darkgrid')

(
    sns.lineplot(data=crossings, x='Date', y='Brooklyn Bridge')
    .set(
        title='Brooklyn Bridge Daily Crossings',
        xlabel=None,
    )
)
plt.xticks(rotation=45)
plt.show()


# Task 1: Using an appropriate dataset, produce a single line plot showing the 
# crossings for all bridges from April to June.
(
    sns.lineplot(data=melted_crossings[['Date', 'Crossings']].groupby('Date').sum(), x='Date', y='Crossings', estimator='sum')
    .set(
        title='Daily crossings on all bridges',
        xlabel='Day'
    )
)
plt.xticks(rotation=45)
plt.show()

# Task 2: Clarify your solution to Task 1 by creating a separate subplot for each 
# bridge.
(
    sns.relplot(
        data=melted_crossings, x='Date', y='Crossings', hue='Bridge', row='Bridge',
        kind='line'
    )
    .set(
        title='Daily Crossings across all bridges',
        xlabel='Day'
    )
)
plt.xticks(rotation=45)
plt.show()
