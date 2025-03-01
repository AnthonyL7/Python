import pandas as pd
#import matplotlib.pyplot as plt
#import seaborn as sns

xl = pd.ExcelFile("/Users/anthony/Documents/Python/Analysis/TableauSalesData.xlsx")
SalesData = xl.parse('Orders')
print(SalesData.head(10))