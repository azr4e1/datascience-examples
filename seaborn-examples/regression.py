import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import date
from sklearn.linear_model import LinearRegression

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
    sns.regplot(
        data=crossings, x='Low Temp (°F)',
        y='High Temp (°F)', ci=95,
    )
    .set(
        title='Regrssion Analysis of Temperatures',
        xlabel='Minimum Temperature',
        ylabel='Maximum Temperature'
    )
)
plt.show()

x = crossings.loc[:, ['Low Temp (°F)']]
y = crossings.loc[:, 'High Temp (°F)']
model = LinearRegression()
model.fit(x, y)

r_squared = f"R-Squared: {model.score(x, y):.2f}"
best_fit = (
    f"y = {model.coef_[0]:.4f}x"
    f"{model.intercept_:+.4f}"
)

ax = sns.regplot(
        data=crossings, x='Low Temp (°F)',
        y='High Temp (°F)', line_kws={"label": f"{best_fit}\n{r_squared}"},
)
ax.set_xlabel("Minimum Temperature")
ax.set_title("Regression Analysis of Temperatures")
ax.set_ylabel("Maximum Temperature")
ax.legend()
plt.show()
