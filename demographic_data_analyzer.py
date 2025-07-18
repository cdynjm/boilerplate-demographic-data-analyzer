import pandas as pd

def demographic_data_analyzer():
    # Load the data
    df = pd.read_csv('adult.data.csv')

    # How many of each race
    race_count = df['race'].value_counts()

    # Average age of men
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # % with Bachelors degree
    percentage_bachelors = round(
        (df[df['education'] == 'Bachelors'].shape[0] / df.shape[0]) * 100, 1
    )

    # Advanced education
    higher_education = df[
        df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    ]

    lower_education = df[
        ~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    ]

    # % higher education >50K
    higher_education_rich = round(
        (higher_education[higher_education['salary'] == '>50K'].shape[0] /
         higher_education.shape[0]) * 100, 1
    )

    # % lower education >50K
    lower_education_rich = round(
        (lower_education[lower_education['salary'] == '>50K'].shape[0] /
         lower_education.shape[0]) * 100, 1
    )

    # Min work hours
    min_work_hours = df['hours-per-week'].min()

    # % of rich among min workers
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = round(
        (num_min_workers[num_min_workers['salary'] == '>50K'].shape[0] /
         num_min_workers.shape[0]) * 100, 1
    )

    # Country with highest % of >50K
    country_salary = df.groupby('native-country')['salary'].value_counts(normalize=True).unstack()['>50K'] * 100
    highest_earning_country = country_salary.idxmax()
    highest_earning_country_percentage = round(country_salary.max(), 1)

    # Most popular occupation for rich in India
    india_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    top_IN_occupation = india_occupation['occupation'].value_counts().idxmax()

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
