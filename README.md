# Titanic Dataset Visualization

This repository contains Python code for visualizing the Titanic dataset using **Matplotlib** and **Pandas**. The visualizations help explore relationships between passenger demographics, survival rates, and family aboard.

## Dataset

The dataset (`tested.csv`) contains the following columns:  

- `PassengerId` – Unique ID for each passenger  
- `Survived` – Survival status (0 = No, 1 = Yes)  
- `Pclass` – Passenger class (1 = 1st, 2 = 2nd, 3 = 3rd)  
- `Name` – Passenger name  
- `Sex` – Gender  
- `Age` – Age of passenger  
- `SibSp` – Number of siblings/spouses aboard  
- `Parch` – Number of parents/children aboard  
- `Ticket` – Ticket number  
- `Fare` – Fare paid  
- `Cabin` – Cabin number  
- `Embarked` – Port of embarkation  

> In the visualizations, only relevant columns (`Age`, `Sex`, `SibSp`, `Survived`) are used.

## Visualizations

1. **Histogram of Age** – Shows the distribution of passenger ages on board.  

2. **Scatter Plot: Age vs Siblings/Spouses (`SibSp`)** – Shows relationship between passenger age and number of siblings/spouses.  

3. **Bar Chart: Survival by Gender** – Shows the count of survivors and non-survivors for male and female passengers.  

4. **Bar Chart: Number of Siblings/Spouses** – Shows distribution of passengers based on the number of siblings/spouses aboard.  

5. **Pie Chart: Survival Rate** – Shows overall survival vs non-survival percentage.  

6. **Pie Chart: Gender Distribution** – Shows proportion of male and female passengers.  

## How to Run

1. Clone this repository:  
```bash
git clone https://github.com/your-username/titanic-visualization.git
