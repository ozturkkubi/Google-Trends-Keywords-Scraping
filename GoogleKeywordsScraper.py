from pytrends.request import TrendReq
import pandas as pd
import datetime

pytrend = TrendReq() #to connect Python to Google

countries = ['insert location here'] #insert location names here
trending_keywords = []

for country in countries:
    df = pytrend.trending_searches(pn=country)
    trending_keywords.append(df.head(20))

result = pd.concat(trending_keywords, keys=countries)
result.reset_index(level=0, inplace=True)
result.reset_index(level=0, inplace=True)
result.columns = ['keyword_rank', 'country', 'keyword']
result['keyword_rank'] += 1

date = datetime.datetime.now().strftime("%d.%m.%Y")
file_name = "GlobalTrends_" + date + ".xlsx"
file_path = "insert file path here" + file_name  #insert your file path here

# Create an Excel Workbook
writer = pd.ExcelWriter(file_path, engine='openpyxl')

# Create a sheet for each country
for country in countries:
    result_country = result[result['country'] == country]
    result_country.to_excel(writer, sheet_name=country.capitalize().replace("_", " "), index=False)

# Save the workbook
writer.save()
