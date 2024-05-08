import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sbs
df = pd.read_csv("C:/Users/didie/Documents/retoAnalitica/arteDeLaAnalitica/twitter_dataset.csv")
print(df)
tweet_id=df.iloc[:, 0]
retweets=df.iloc[:, 3]
likes=df.iloc[:, 4]

plt.boxplot(tweet_id, vert=False, patch_artist=True, labels=["Tweet ID"])
plt.show()
plt.boxplot(retweets , vert=False, patch_artist=True, labels=["Retweets"])
plt.show()
plt.boxplot(likes , vert=False, patch_artist=True, labels=["Likes"])
plt.show()

plt.hist(tweet_id, label="Tweet ID")
plt.title("Tweet ID")
plt.show()
plt.hist(retweets, label="Retweets")
plt.title("Retweets")
plt.show()
plt.hist(likes, label="Likes")
plt.title("Likes")
plt.show()
dfcor=df[["Tweet_ID", "Retweets", "Likes"]].corr()

sbs.heatmap(dfcor, cmap="PuBu")
plt.show()