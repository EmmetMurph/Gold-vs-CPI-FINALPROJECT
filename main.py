#Preparation
import pandas as pd, matplotlib.pyplot as plt
gold = pd.read_csv('Gold_prices.csv' , parse_dates=['Date'], index_col='Date' )
gold = gold.asfreq('M')
gold_USD = pd.DataFrame(gold, columns=['USD (PM)']).fillna(method='ffill')
gold1_USD = gold_USD.sort_index(ascending=False)
gold_final = gold1_USD['2018-01-01':'2023-01-01']
print(gold_final.head())
inflation = pd.read_csv('Inflation_USA.csv', parse_dates=['Date'], index_col='Date')
inflation_USA = pd.DataFrame(inflation, columns=['CPI'])
inflation_final = inflation_USA.sort_index(ascending=False)
print(inflation_final.head())
Gold_Inflation = pd.concat([gold_final, inflation_final], axis=1)
print(Gold_Inflation.head())
#Analysis
gold_last = Gold_Inflation['USD (PM)'].iat[0]
gold_first = Gold_Inflation['USD (PM)'].iat[-1]
def gold_difference(gold_last, gold_first):
    if gold_last > gold_first:
        diff = gold_last - gold_first
        final = diff/gold_first*100
    return final
print("The difference between the first recorded gold price and last recorded gold price is %", gold_difference(gold_last, gold_first))
CPI_last = Gold_Inflation['CPI'].iat[0]
CPI_first = Gold_Inflation['CPI'].iat[-1]
def CPI_difference(CPI_last, CPI_first):
    if CPI_last > CPI_first:
        diff = CPI_last - CPI_first
        final = diff/CPI_first*100
        return final
print("The difference between first recorded CPI price and last recorded CPI price is %",CPI_difference(CPI_last, CPI_first))
Gold_Inflation['Monthly Change (USD)'] = Gold_Inflation['USD (PM)'].pct_change().mul(100)
Gold_Inflation['Monthly Change (CPI)'] = Gold_Inflation['CPI'].pct_change().mul(100)
Gold_Inflation.plot(subplots=True, linestyle='dashdot')
plt.show()
x = Gold_Inflation['Monthly Change (CPI)']
y = Gold_Inflation['Monthly Change (USD)']
plt.scatter(x,y, c=y, cmap='plasma')
plt.axvline(0, c='Grey', ls='dashdot')
plt.axhline(0, c='Grey', ls='dashdot')
plt.xlabel('Monthly Change (CPI)')
plt.ylabel('Monthly Change (USD)')
plt.title('Correlation between % Monthly Change in Gold and the CPI')
plt.colorbar()
plt.show()
a = Gold_Inflation['USD (PM)']
b = Gold_Inflation['CPI']
plt.scatter(b,a, c=a, cmap='plasma')
plt.xlabel('Monthly Price (CPI)')
plt.ylabel('Monthly Price (USD)')
plt.title('Correlation between Monthly Price of Gold and the CPI')
plt.colorbar()
plt.show()