import pandas as pd
import seaborn.objects as so

# When you build a plot using seaborn objects, the first object that you use is 
# Plot. This object references the DataFrame whose data you’re plotting, as well 
# as the specific columns within it whose data you’re interested in seeing.

# a Plot object is only a background for your plot. To see some content, you need 
# to build it up by adding one or more Mark objects to your Plot object. The Mark 
# object is the base class of a whole range of subclasses, with each representing 
# a different part of your data visualization.

crossings = pd.read_csv("../data/cycle_crossings.csv")
crossings.head()
crossings.dtypes
crossings.Date = pd.to_datetime(crossings.Date, format="%m/%d")
crossings['month'] = pd.Categorical(crossings['Date'].apply(lambda x: x.strftime("%b")))

(
    so.Plot(
        data=crossings, x="Low Temp (°F)", y="High Temp (°F)",
        color="month",
    )
    .add(so.Dot(), marker="month")
    .facet(col="month")
    .layout(size=(15, 5))
    .label(
        title="Minimum vs Maximum Temperature",
        xlabel="Minimum Temperature",
        ylabel="Maximum Temperature",
        color=str.capitalize,
    )
    .show()
)
