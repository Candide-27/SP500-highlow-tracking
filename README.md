# SP500-highlow-tracking
Track stock volatility.

The Python script checks whether today's (at the date the script is run) High-Low gap of a S&P500 company's stock is larger than the average of that gap in the last 10 days.
S&P500 companies csv file derived from:https://datahub.io/core/s-and-p-500-companies-financials#resource-s-and-p-500-companies-financials_zip 

The output is an Excel file that includes the companies that satisfy the aforementioned condition and their market history regarding the current date's High, Low, Volume and the average of Volume and High-Low gap in the last 10 days. Including in the repository is the output file ran on October 30th, 2021.

The High-Low gap is a useful indicator of how volatile a stock price is. 

Packages used: pandas, numpy, yfinance, datetime 
