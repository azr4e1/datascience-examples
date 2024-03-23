import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

tips = sns.load_dataset("tips")

# with seaborn
(
    sns.barplot(
        data=tips, x="day", y="tip",
        estimator="mean", errorbar=None,
    )
    .set(title="Daily Tips ($)")
)

# (
#     sns.histplot(
#         data=tips, x="total_bill",
#     )
#     .set(title="Daily Tips ($)")
# )

plt.show()

# with matplotlib
average_daily_tip = (
    tips
    .groupby("day")["tip"]
    .mean()
)

days = ["Thur", "Fri", "Sat", "Sun"]
daily_averages = []
for day in days:
    daily_averages.append(average_daily_tip[day])

fig, ax = plt.subplots()
plt.bar(x=days, height=daily_averages)
ax.set_xlabel("day")
ax.set_ylabel("tip")
ax.set_title("Daily Tips ($)")

plt.show()
