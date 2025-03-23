import numpy as np
import pandas as pd
import seaborn as sns

df = pd.read_csv("data/happiness_survey_data.csv")
sns.histplot(df.happiness_score)

sns.boxplot(x=df.happiness_score)

q25, q50, q75 = np.percentile(df.happiness_score, (25, 50, 75))

iqr = q75 - q25

min_happy = q25 - 1.5*iqr
max_happy = q75 + 1.5*iqr
min_happy, q25, q50, q75, max_happy

df[df.happiness_score < 2.1885]

mean_happy = np.mean(df.happiness_score)
sd_happy = np.std(df.happiness_score)
mean_happy, sd_happy
[happy for happy in df.happiness_score if (
    happy < mean_happy - 2.5 * sd_happy) or (happy > mean_happy + 2.5 * sd_happy)]
