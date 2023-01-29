# TradingView - Short Put Option Backtest
This is my very first project right after finishing a Python3 course on codecademy. 

Strategy explain:
Short 6 months / 1 year put option contract ~5% below current stock price weekly to profit from theta decay in a bull / stagnation market.

Historical stock price and market holiday data was downloaded as csv files. Stock price data needs to be modified because option expiration day is always
the last day of the week, therefore, holiday is added to make sure every Friday exist for the algorithm. 
The algorithm takes 2 inputs: stock ticker symbol (how you name the stock data file) and option contract duration. Return how often a put option
falls in the money at expiration. 

Technology used:
- Python3 

