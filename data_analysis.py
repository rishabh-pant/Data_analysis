import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('internship.csv')

# print(df.head())
# print(df.describe())

# mv=df.isnull().sum()
# print(mv)

# avg=df['age'].mean()
# print(avg)

# uv=df['age'].nunique
# print(f"uv {uv}")

eng_emp = df[df['department'] == 'Engineering']
print(eng_emp)

max_salary = df['salary'].max()
max_salary_emp = df[df['salary'] == max_salary]
print(max_salary_emp)

min_salary = df['salary'].min()
min_salary_emp = df[df['salary'] == min_salary]
print(min_salary_emp)

dep_count = df['department'].value_counts()
print(dep_count)

sort_d = df.sort_values(by='age', ascending=False)
print(sort_d)

sort = df.sort_values(by='age', ascending=True)
print(sort)

df['experience'] = df['age'].apply(lambda x: 'senior' if x >= 30 else 'junior')
print(df)

plt.figure(figsize=(8, 6))
plt.pie(dep_count, labels=dep_count.index, autopct='%1.1f%%', startangle=140) # type: ignore
plt.title('department')
plt.show()