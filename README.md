# LoanRiskScore_predictor
Applying different machine learning regression models to predict the **Loan Risk Score** from a variety of features.

## Getting Started

### Available Trained Models
- Multiple linear regression
- Support Vector regression
- Random Forest regression
## Dataset Features
- **ListingNumber**: The number that uniquely identifies the listing to the public as displayed on the website.
- **CreditGrade**: The Credit rating that was assigned at the time the listing went live. Applicable for listings pre-2009 period and will only be populated for those listings.
- **Term**:	The length of the loan expressed in months.
- **LoanStatus**: The current status of the loan: Cancelled, Chargedoff, Completed, Current, Defaulted, FinalPaymentInProgress, PastDue. The PastDue status will be accompanied by a delinquency bucket.
- **BorrowerAPR**: The Borrower's Annual Percentage Rate (APR) for the loan.
- **BorrowerRate**: The Borrower's interest rate for this loan.
- **ListingCategory**: The category of the listing that the borrower selected when posting their listing: 

|  CategoryName      | CategoryID |
|--------------------|------------|
| Not Available      | 0          |
| Debt Consolidation | 1          |
| Home Improvement   | 2          |
| Business           | 3          |
| Personal Loan      | 4          |
| Student Use        | 5          |
| Auto               | 6          |
| Other              | 7          |
| Baby & Adoption    | 8          |
| Boat               | 9          |
| Cosmetic procedure | 10         |
| Engagement Ring    | 11         |
| Green Loans        | 12         |
| Household Expenses | 13         |
| Large purchases    | 14         |
| Medical/Dental     | 15         |
| Motorcycle         | 16         |
| RV                 | 17         |
| Taxes              | 18         |
| Vacation           | 19         |
| Wedding Loans      | 20         |

- **BorrowerState**: The two letter abbreviation of the state of the address of the borrower at the time the Listing was created.
- **EmploymentStatus**:	The employment status of the borrower at the time they posted the listing.
- **EmploymentStatusDuration**:	The length in months of the employment status at the time the listing was created.
- **IsBorrowerHomeowner**: A Borrower will be classified as a homowner if they have a mortgage on their credit profile or provide documentation confirming they are a homeowner.
- **CreditScoreRangeLower**: The lower value representing the range of the borrower's credit score as provided by a consumer credit rating agency.
- **CreditScoreRangeUpper**: The upper value representing the range of the borrower's credit score as provided by a consumer credit rating agency.
- **RevolvingCreditBalance**: Dollars of revolving credit at the time the credit profile was pulled.
- **BankcardUtilization**: The percentage of available revolving credit that is utilized at the time the credit profile was pulled.
- **AvailableBankcardCredit**: The total available credit via bank card at the time the credit profile was pulled.
- **TotalTrades**:	Number of trade lines ever opened at the time the credit profile was pulled.
- **DebtToIncomeRatio**: The debt to income ratio of the borrower at the time the credit profile was pulled. This value is Null if the debt to income ratio is not available. This value is capped at `10.01` (any **DebtToIncomeRatio** > `1000%` will be returned as `1001%`).
- **IncomeRange**:	The income range of the borrower at the time the listing was created.
- **StatedMonthlyIncome**:	The monthly income the borrower stated at the time the listing was created.
- **TotalProsperPaymentsBilled**: Number of on time payments the borrower made on Prosper loans at the time they created this listing. This value will be null if the borrower had no prior loans.
- **LoanNumber**: Unique numeric value associated with the loan.
- **LoanOriginalAmount**: The origination amount of the loan.
- **LoanRiskScore**: A custom risk score built using historical Prosper data. The score ranges from 1-10, with 10 being the best, or lowest risk score. Applicable for loans originated after July 2009.
