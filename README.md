# boss

I use descriptive statistics and machine learning algorithms (linear regression and regression trees) to plan bid prices for modules. The python file 'bidding.py' appends the BOSS excel files across terms as found at https://oasis.smu.edu.sg/Pages/RO/All_students/BOSS-Overall-Results.aspx into a single csv file for easier analysis. It merges all term excel sheets into a single csv starting from the year 2015 up til the contemporary year.

The jupyter notebook 'analysis' covers the actual analysis where I first clean the data, filter it for the relevant modules, professors, bidding windows and terms as required. After which, I use boxplots, scatterplots, lineplots, linear and tree regression to analyze the data. The explanatory covariates are the vacancies for a class and the number of sections available while the dependent covariates (depending on the model and plot) are the median or min bid or the vacancies after the bidding window.

Here's a list of all the variables used in the models:

| Variable               | Description                                                                                   |
|------------------------|-----------------------------------------------------------------------------------------------|
| term                   | {Term 1/2/3A/3B}                                                                              |
| session                | Academic Year Session                                                                         |
| bidding_window         | Bidding Round and Window {R1 W1, R1 W2, R1A W1, R1A W1, R1A W2, R1B W1, R1B W2, R2 W1, R2 W2} |
| course_code            | Course Code                                                                                   |
| description            | Course Title                                                                                  |
| section                | Section of the class {G1, G2...}                                                              |
| vacancy                | Total vacancies in the class                                                                  |
| opening_vacancy        | Vacancies in R1W1                                                                             |
| before_process_vacancy | Vacancies before bidding window                                                               |
| dice                   | Number of people who diced the module (dropped it in favour of another module)                |
| after_process_vacancy  | Vacancies after bidding window                                                                |
| enrolled_students      | Number of enrolled students in class                                                          |
| median_bid             | The median bid for the bidding window for the class                                           |
| min_bid                | The min bid for the bidding window for the class                                              |
| instructor             | The instructor for the class                                                                  |
| school                 | The school offering the course {e.g. SOE}                                                     |
| year                   | The academic year in which the course was offered                                             |


The model which performed the best is the Random Forest with a R2 score of 65%. Limitations for the model likely stem from the large number of one hot encoded features in the model rather than numerical features. In the future, I'd like to explore other algorithms like CatBoosting and additional feature engineering such as section or course grouping counts to see whether they can improve model performance.
