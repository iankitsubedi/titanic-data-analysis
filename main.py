import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

df = pd.read_csv("tested.csv")

# Getting the required info from the csv file
df = df.drop(columns=['PassengerId','Pclass','Parch','Ticket','Fare','Cabin','Embarked'])
df = df.dropna(subset=['Age'])
df["Sex"] = df["Sex"].replace({"male": "Male",
                               "female":"Female"})

df =df.drop_duplicates()

# Histogram
sns.histplot(data = df , x = "Age" , hue="Sex")
plt.xlabel("Age")
plt.ylabel("No of people")
plt.title("Histogram between Age and No of people")
plt.show()  

# Scatter plot
plt.scatter(df['Age'], df['SibSp'] + np.random.normal(0, 0.05, len(df)), 
            alpha=0.5, color='purple', edgecolor='black')
plt.xlabel("Age")
plt.ylabel("No of Siblings/Spouses")
plt.title("Scatterplot of Age and No of Siblings/Spouses")
plt.yticks(range(df['SibSp'].max() + 1))
plt.grid(alpha=0.3)
plt.show()

# More Scatter plot
df['Survived'] = df['Survived'].astype(bool)
sns.scatterplot(data=df , x = 'Age' , y = 'SibSp' , hue="Survived" , alpha = 0.5)
plt.title("Relation")
plt.show()

# Bar chart: Survival by Gender
survival_by_gender = df.groupby('Sex')['Survived'].value_counts().unstack()
survival_by_gender.plot(kind='bar', color=['#ff6b6b', '#4ecdc4'], edgecolor='black')
plt.xlabel("Gender")
plt.ylabel("Count")
plt.title("Survival Count by Gender")
plt.legend(['Did Not Survive', 'Survived'])
plt.xticks(rotation=0)
plt.show()


# Bar chart: Number of Siblings/Spouses
sibsp_counts = df['SibSp'].value_counts().sort_index()
plt.bar(sibsp_counts.index, sibsp_counts, color='orange', edgecolor='black')
plt.xlabel("Number of Siblings/Spouses")
plt.ylabel("Count")
plt.title("Distribution of Siblings/Spouses on Board")
plt.show()

# Pie chart for Survival Rate
survival_counts = df['Survived'].value_counts()
plt.pie(survival_counts, labels=['Did Not Survive', 'Survived'], 
        autopct='%1.1f%%', startangle=90, colors=['#ff6b6b', '#4ecdc4'])
plt.title("Survival Distribution")
plt.show()

# Pie chart for Gender Distribution
sex_counts = df['Sex'].value_counts()
plt.pie(sex_counts, labels=sex_counts.index, 
        autopct='%1.1f%%', startangle=90, colors=['#95e1d3', '#f38181'])
plt.title("Gender Distribution")
plt.show()

#line plot
sns.set_style("whitegrid")
sns.lineplot(data= df , x = 'Age' , y = 'SibSp' , color = "blue")
plt.title("Line plot betwen Age and No of siblings")
plt.show()
