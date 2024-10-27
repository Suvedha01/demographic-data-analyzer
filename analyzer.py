import pandas as pd
data = pd.read_csv('your_dataset.csv')
def race_count():
    return data['race'].value_counts()

def average_age_men():
    return round(data[data['sex'] == 'Male']['age'].mean(), 1)

def percentage_bachelors():
    return round((data['education'] == "Bachelors").mean() * 100, 1)

def percentage_high_education_rich():
    advanced_education = ['Bachelors', 'Masters', 'Doctorate']
    return round((data[data['education'].isin(advanced_education)]['salary'] == '>50K').mean() * 100, 1)

def percentage_low_education_rich():
    advanced_education = ['Bachelors', 'Masters', 'Doctorate']
    return round((data[~data['education'].isin(advanced_education)]['salary'] == '>50K').mean() * 100, 1)

def minimum_hours():
    return data['hours-per-week'].min()

def percentage_min_workers_rich():
    min_hours = minimum_hours()
    return round((data[data['hours-per-week'] == min_hours]['salary'] == '>50K').mean() * 100, 1)

def highest_earning_country():
    countries = data[data['salary'] == '>50K']['native-country'].value_counts(normalize=True) * 100
    highest_country = countries.idxmax()
    highest_percentage = countries.max()
    return highest_country, round(highest_percentage, 1)

def top_IN_occupation():
    return data[(data['native-country'] == 'India') & (data['salary'] == '>50K')]['occupation'].mode()[0]

if __name__ == "__main__":
    print(race_count())
    print(average_age_men())
    print(percentage_bachelors())
    print(percentage_high_education_rich())
    print(percentage_low_education_rich())
    print(minimum_hours())
    print(percentage_min_workers_rich())
    print(highest_earning_country())
    print(top_IN_occupation())

