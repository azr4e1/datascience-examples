import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import date

# Functional style intereface contains a set of plotting functions for creating different plot types. The functional interface classifies its plotting functions into several braod types. The three most common types are:

# 1. relplot(): relational plot -> scatterplot(), lineplot()
# 2. displot(): distribution plot -> histplot(), kdeplot(), ecdfplot(), rugplot()
# 3. catplot(): categorical plot -> stripplot(), swarmplot(), boxplot(), violinplot(), boxenplot(), pointplot(), barplot(), countplot()

# plots can be figure level or axes level. A figure level function allows you to draw multiple subplots, with each showing a different category of data. The parameters you specify in the figure-level function apply to each subplot

# An axes level function allows you to draw a single plot. Any parameter you provide to an axes level function apply only to the single plot produced by that function.

# The `hue` parameter allows you to add different colors to different categories of data on a plot. To use it, you pass in the name of the column that you wish to apply coloring to.

# The relational plotting functions also support style and size parameters that allow you to apply different styles and sizes to each point as well. These can further clarify your plot.

crossings = pd.read_csv("../data/cycle_crossings.csv")
crossings.head()
crossings.dtypes
crossings.Date = pd.to_datetime(crossings.Date, format="%m/%d")
crossings['month'] = crossings['Date'].apply(lambda x: x.strftime("%b"))

# axes level function
(
    sns.scatterplot(
        data=crossings, x="Low Temp (°F)", y="High Temp (°F)",
        hue="month",#  size="month", style="month"
    )
    .set(
        title="Minimum vs Maximum Temperature",
        xlabel="Minimum Temperature",
        ylabel="Maximum Temperature",
    )
)

plt.show()

# figure level function
# The row or col parameters allow you to specify the row or column data Series that will be displayed in each subplot. Setting the column parameter will place each of your subplots in their own columns, while setting the row parameter will give you a separate row for each of them.
(
    sns.relplot(
        data=crossings, x="Low Temp (°F)", y="High Temp (°F)",
        kind="scatter", hue="month", row="month",
    )
    .set(
        xlabel="Minimum Temperature",
        ylabel="Maximum Temperature",
        title="Minimum vs Maximum Temperature",
    )
    .legend.set_title("Month")
)

plt.show()
