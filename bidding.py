import pandas as pd
from datetime import date

year = int(date.today().strftime("%Y")[2:])

terms = ["T1", "T2", "T3A", "T3B"]

new_names = ["term", "session", "bidding_window", "course_code", "description", "section", "vacancy", "opening_vacancy", "before_process_vacancy", "dice", "after_process_vacancy", "enrolled_students", "median_bid", "min_bid", "instructor", "school"]

old_names = ["Term", "Session", "Bidding Window", "Course Code", "Description", "Section", "Vacancy", "Opening Vacancy",	"Before Process Vacancy", "D.I.C.E", "After Process Vacancy", "Enrolled Students", "Median Bid", "Min Bid", "Instructor", "School/Department"]

df = pd.DataFrame(columns=old_names)

col_names = dict()

for i in range(len(new_names)):
    col_names[old_names[i]] = new_names[i]

for year in range(15, year):
    for i in terms: 
        df = df.append(pd.read_excel("20{}-{}_{}.xls".format(year, year+1, i)), ignore_index = True)

print("done")

df.rename(columns = col_names,inplace=True)

df.to_csv('overall.csv')

if __name__ == "__main__":
    print(df.head())