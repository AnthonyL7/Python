years_code_list = ['1','2','3','4','2','1','3','2','5','6','7','8','9','10','12','14','15','21','13','20', 'More than 50 years']
years_code_cleaned = [int(years) for years in years_code_list if years != 'More than 50 years']

junior_developers = len([dev for dev in years_code_cleaned if dev < 5])
print(junior_developers)
