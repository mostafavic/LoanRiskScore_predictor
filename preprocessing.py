import pandas as pd
from random import choice
from util import *
from math import ceil
#Load loan data
data = pd.read_csv('LoanRiskScore.csv')

# Fill the columns with null values with the mean value of the whole column
categories = ['LoanOriginalAmount', 'LoanRiskScore', 'BorrowerAPR', 'TotalTrades', 'RevolvingCreditBalance', 'BankcardUtilization', 'AvailableBankcardCredit', 'BorrowerRate', 'EmploymentStatusDuration', 'DebtToIncomeRatio', 'CreditScoreRangeLower', 'CreditScoreRangeUpper', 'StatedMonthlyIncome']
for category in categories:
    categoryMean = ceil(data[category].mean())
    data[category] = data[category].fillna(categoryMean)
    print(f"{category}: {data[category].isna().sum()}.")


# Get all unique credit grades list
allCreditGrades = data['CreditGrade'].unique()
# Remove Null from the unique credit grades list
allCreditGrades = [x for x in allCreditGrades if x == x]
# Run through all credit grades with a null value and random choice a credit grade from unique credit grades list
for index, row in data.iterrows():
    if pd.isnull(row['CreditGrade']):
        creditGrade = choice(allCreditGrades)
        data.loc[index, 'CreditGrade'] = creditGrade
 
# Remove Duplicate ListNumbers
filteredData = data.drop_duplicates(subset="ListingNumber")

# Removing all RiskScores > 10
filteredData.drop(filteredData[filteredData['LoanRiskScore'] > 10].index, inplace=True)

# Removing BorrowerState null values
filteredData.drop(filteredData[pd.isnull(filteredData['BorrowerState'])].index, inplace=True)

# Fill 0 to TotalProsperPaymentsBilled if null
filteredData['TotalProsperPaymentsBilled'].fillna(0, inplace=True)

# Write the new Preprocessed LoanRiskScore.csv file
filteredData.to_csv('LoanRiskScoreProcessed.csv', index=False)