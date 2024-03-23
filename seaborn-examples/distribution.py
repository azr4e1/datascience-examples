import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

cereals_data = (
    pd.read_csv("../data/cereal.csv")
)

# histogram
(
    sns.histplot(data=cereals_data, x='rating', bins=10)
    .set(title='Cereal Ratings Distribution')
)
plt.show()

# kde plot (kernel density estimation)
(
    sns.kdeplot(data=cereals_data, x='rating')
    .set(title='Cereal Ratings KDE Curve')
)

# rugplot
(
    sns.rugplot(data=cereals_data, x='rating',
                height=0.2, color='black')
    .set(title='Cereal Ratings Rug Plot')
)
plt.show()

# Task 1: Produce a single histogram showing cereal ratings distribution such 
# that there’s a separate bar for each manufacturer. Keep to the same ten bins.
(
    sns.histplot(data=cereals_data, x='rating', bins=10, hue='mfr', multiple='dodge')
    .set(title='Cereal Ratings Distribution')
)
plt.show()

# Task 2: See if you can superimpose a KDE plot onto your original ratings 
# histogram using only one function.
(
    sns.histplot(data=cereals_data, x='rating', bins=10, kde=True)
    .set(title='Cereal Ratings Distribution')
)
plt.show()

# Task 3: Update your answer to Task 1 such that each manufacturer’s calorie data 
# appears on a separate plot along with its own KDE curve.
# fig, (ax1, ax2) = plt.subplots(2, 1)
# (
#     sns.histplot(data=cereals_data, x='rating', bins=10, hue='mfr', ax=ax1, multiple='dodge')
#     .set(title='Cereal Ratings Distribution')
# )
# (
#     sns.histplot(data=cereals_data, x='calories', bins=10, hue='mfr', ax=ax2, kde=True, multiple='dodge')
#     .set(title='Cereal Calories Distribution')
# )
# plt.show()
sns.displot(
    data=cereals_data, x='rating',
    bins=10, hue='mfr',
    kde=True, col='mfr'
)
plt.show()

