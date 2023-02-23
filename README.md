# WebScraping
This Python script connects to Google and retrieves the top 20 trending keywords for the specified countries. The resulting data is stored in an Excel workbook, with a separate sheet for each country. The workbook is saved to the specified file path.

Setup

This script requires the trend and pandas libraries to be installed. If you do not have these installed, you can install them by running:

Copy code
pip install pytrends pandas
Usage

Open the script in your preferred Python editor or environment.
Modify the countries list to include the countries you want to retrieve trending keywords for.
Modify the file_path variable to specify the location where you want to save the Excel workbook.
Run the script.
Output

The script will create an Excel workbook with the name GlobalTrends_<date>.xlsx, where <date> is the current date in the format dd.mm.yyyy. The workbook will contain a separate sheet for each country in the countries list. Each sheet will contain the top 20 trending keywords for that country.

Disclaimer

This script relies on the pytrends library to connect to Google and retrieve the trending keywords. Google may block your IP address if it detects automated requests. Use this script at your own risk.
