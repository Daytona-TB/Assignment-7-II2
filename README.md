# Assignment-7-II2
#Loan Data Visualization Project

#Purpose
This project performs data cleaning and generates insightful visualizations from a real-world loan dataset. The goal is to understand patterns related to loan amounts, interest rates, income levels, and default status using Matplotlib visualizations.

#Class Design & Implementation
The project is structured using:
  - pandas' for data loading and cleaning  
  - numpy' for statistical filtering  
  - matplotlib.pyplot' for plotting  

#Data Cleaning
Removed currency symbols (£, ,) from loan_amnt and customer_income using regex
Converted loan_amnt and customer_income to float type for numerical analysis
Dropped rows with missing values in essential columns:
loan_amnt, customer_income, loan_int_rate, Current_loan_status, loan_intent, loan_grade
Standardized Current_loan_status to uppercase for consistency
Trimmed top 5% of extreme values in loan_amnt, customer_income, and loan_int_rate
to reduce zoom distortion and improve visualization readability

#Limitations 
Outliers beyond the 95th percentile are excluded to focus on general trends
The project uses static plots only
No machine learning models or prediction analysis is included



#1 Loan Amount by Grade and Status
Type: Boxplot
X-axis: Loan grades (A–F), split by default status
Y-axis: Loan amount (£)
Purpose: To show the relationship between loan grade, amount, and likelihood of default

#2 Interest Rate by Loan Intent
Type: Boxplot
X-axis: Loan purpose (e.g., medical, education, personal)
Y-axis: Interest rate (%)
Purpose: To show how the purpose of a loan affects the rate offered

#3 Income Distribution by Loan Status
Type: Overlapping histogram
X-axis: Customer income (£)
Y-axis: Number of customers
Purpose: To show how income level is distributed among defaulting and non-defaulting borrowers


#Analysis of Visualizations
The visualizations reveal strong patterns in loan data tied to customer risk and loan performance. The first plot shows that lower-grade loans (grades D–F) are typically larger and far more likely to default compared to higher-grade loans (A–B), which tend to be smaller and more reliable. This suggests lenders are using the grading system effectively to manage risk.The second visualization shows that loan intents such as **education** and **personal use** are associated with higher interest rates, likely due to their higher risk of default, whereas intents like **medical** and **home improvement** have more moderate rates. The third graph clearly shows that customers with lower incomes are significantly more likely to default, while higher-income customers mostly maintain “no default” status. Together, these visualizations highlight how **loan grade**, **loan purpose**, and **income level** all correlate closely with default likelihood and borrowing conditions.
