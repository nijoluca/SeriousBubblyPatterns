def maxProfit(prices,n):
  profit=[0]*n
  max_profit=prices[n-1]
  for i in range(n-2,0,-1):
    if prices[i] > max_profit:
      max_profit=prices[i]
    profit[i]=max(profit[i+1],max_profit-prices[i])

  min_price=prices[0]
  for i in range(1,n):
    if prices[i] < min_price:
      min_price=prices[i]
    profit[i]=max(profit[i-1],(profit[i]+(prices[i]-min_price)))
  return profit[n-1]

prices=[2, 30, 15, 10, 8, 25, 80]
n=len(prices)
print(maxProfit(prices,n))
