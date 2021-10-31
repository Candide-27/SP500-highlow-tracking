# SP500-highlow-tracking
Track stock volatility.

Being a useful indicator of the stock price volatility, High-Low gap represents the price range of the security.
The Python script checks whether today's (at the date the script is run) High-Low gap of a S&P500 company's stock is larger than the average of that gap in the last 10 days.
S&P500 companies csv file is retrieved from: https://datahub.io/core/s-and-p-500-companies-financials#resource-s-and-p-500-companies-financials_zip 

The output is an Excel file that includes the companies that satisfy the aforementioned condition and their market history regarding the current date's High, Low, Volume and the average of Volume and High-Low gap in the last 10 days. 

Packages used: pandas, numpy, yfinance, datetime 
