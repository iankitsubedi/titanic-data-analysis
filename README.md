# Titanic Data Analysis

An exploratory data analysis of the Titanic passenger dataset using Python with **Matplotlib**, **Seaborn**, and **Pandas**. This project features multiple visualizations to understand passenger demographics, survival patterns, and relationships between various factors.

## Dataset

The dataset (`tested.csv`) contains passenger information from the Titanic. The analysis focuses on:
- **Age** – Age of passenger
- **Sex** – Gender (Male/Female)
- **SibSp** – Number of siblings/spouses aboard
- **Survived** – Survival status (0 = Did Not Survive, 1 = Survived)

> Note: Irrelevant columns (PassengerId, Pclass, Parch, Ticket, Fare, Cabin, Embarked) were dropped, and rows with missing age data were removed.

## Visualizations

### 1. **Histogram: Age Distribution by Gender**
Shows the distribution of passenger ages, color-coded by gender using Seaborn's histplot.

### 2. **Scatter Plot: Age vs Siblings/Spouses**
Displays the relationship between passenger age and number of siblings/spouses aboard with jittered points for clarity.

### 3. **Seaborn Scatter Plot: Survival by Age and Siblings**
Interactive scatter plot showing how age and number of siblings/spouses relate to survival status.

### 4. **Bar Chart: Survival Count by Gender**
Compares survival rates between male and female passengers with color-coded bars.

### 5. **Bar Chart: Siblings/Spouses Distribution**
Shows how many passengers had 0, 1, 2, or more siblings/spouses aboard.

### 6. **Pie Chart: Survival Distribution**
Overall percentage breakdown of survivors vs non-survivors.

### 7. **Pie Chart: Gender Distribution**
Proportion of male and female passengers on the Titanic.

### 8. **Line Plot: Age vs Siblings Trend**
Seaborn line plot showing the trend between age and number of siblings/spouses.

## Technologies Used

- **Python 3.x**
- **Pandas** – Data manipulation and cleaning
- **Matplotlib** – Basic plotting and visualization
- **Seaborn** – Advanced statistical visualizations
- **NumPy** – Numerical operations and jittering

## Installation & Usage

1. **Clone the repository:**
```bash
git clone https://github.com/iankitsubedi/titanic-data-analysis.git
cd titanic-data-analysis
```

2. **Install required packages:**
```bash
pip install pandas matplotlib seaborn numpy
```

3. **Run the analysis:**
```bash
python main.py
```

## Key Insights

The visualizations reveal:
- Age and gender distribution of passengers
- Survival patterns based on gender (females had higher survival rates)
- Relationship between family size (siblings/spouses) and survival
- Overall survival statistics from the Titanic disaster

## Files

- `main.py` – Main Python script with all visualizations
- `tested.csv` – Titanic dataset
- `README.md` – Project documentation

## Future Improvements

- Add more statistical analysis
- Include passenger class (Pclass) analysis
- Create interactive visualizations with Plotly
- Add correlation heatmap

## License

This project is open source and available for educational purposes.

## Author

Ankit Subedi
GitHub: [@iankitsubedi](https://github.com/iankitsubedi)
