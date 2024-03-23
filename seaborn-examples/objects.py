import pandas as pd
import seaborn.objects as so
import seaborn as sns
from datetime import date
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


first_week = (
    crossings
    .loc[crossings.Month == "Apr", :]
    .sort_values(by='Date')
    .head(7)
)

# Multiple layers in a plot

(
    so.Plot(data=first_week, x="Day", y="Low Temp (°F)")
    .add(so.Line(color="black", linewidth=3, marker='o'))
    .add(so.Bar(color='green', fill=False, edgewidth=3))
    .add(so.Area(color="yellow"))
    .label(
        x='Day', y='Temperature',
        title='Minimum Temperature'
    )
    .show()
)


# Enhancing plots with Move and Stat object
(
    so.Plot(
        data=crossings, x="Month",
        y='High Temp (°F)', color='Day',
    )
    .add(
        so.Bar(),
        so.Agg(func='median'),
        so.Dodge(gap=0.1),
    )
    .label(
        x=None, y="Temperature",
        title='Median Temperature', color='Day'
    )
    .show()
)


# Separating a plot into subplots

(
    so.Plot(
        data=crossings, x='Month',
        y='High Temp (°F)', color='Day',
    )
    .facet(col='Month')
    .add(
        so.Bar(),
        so.Agg(func='median'),
        so.Dodge(gap=0.1),
    )
    .label(
        x=None, y='Temperature',
        title='Median Temperature', color='Day'
    )
    .show()
)

# Task 1: Redraw the min_temperature vs max_temperature scatterplot that you 
# created at the start of the article using objects. Also, make sure each marker 
# has a different color depending on the days that it represents. Finally, use a 
# star to represent each marker.
# (
#     sns.scatterplot(
#         data=crossings, x="Low Temp (°F)", y="High Temp (°F)",
#         hue="Month", size="Month", style="Month"
#     )
#     .set(
#         title="Minimum vs Maximum Temperature",
#         xlabel="Minimum Temperature",
#         ylabel="Maximum Temperature",
#     )
# )
# plt.show()

(
    so.Plot(
        data=crossings, x="Low Temp (°F)", y="High Temp (°F)",
        color='Month'
    )
    .add(
        so.Dot(marker='*')
    )
    .show()
)

# Task 2: Create a bar plot using objects showing the maximum and minimum
# bridge crossings for each of the four bridges.
melted_crossings.loc[:, ['Bridge', 'Crossings']].groupby(
    'Bridge').aggregate(['min', 'max'])

(
    so.Plot(
        data=melted_crossings, x='Bridge', y='Crossings',
        color='Bridge'
    ).
    add(
        so.Bar(color='yellow'),
        # so.Agg(func='min'),
        so.Agg(func='max'),
        legend=False
    )
    .add(
        so.Bar(color='red'),
        so.Agg(func='min'),
        legend=False
    )
    .label(
        x='Bridge', y='Crossings',
        title='Bridge Crossings',
    )
    .show()
)

# Task 3: Create a bar plot using objects analyzing the counts of breakfast
# cereal calories. The calories should be placed into ten equal-sized bins.
cereals_data = (
    pd.read_csv("../data/cereal.csv")
)
cereals_data.columns

(
    so.Plot(data=cereals_data, x='calories')
    .add(
        so.Bar(),
        so.Hist(bins=10, stat='probability')
    )
    .show()
)
