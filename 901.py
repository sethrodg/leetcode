'''
Design an algorithm that collects daily price quotes for some stock and returns the span of that stock's price for the current day.

The span of the stock's price today is defined as the maximum number of consecutive days (starting from today and going backward) for which the stock price was less than or equal to today's price.
'''

#Stack solution
class StockSpanner:

    def __init__(self):
        self.stack = [] #[price, span]
        
    def next(self, price: int) -> int:
        
        span = 1
        while self.stack and price >= self.stack[-1][0]:
            span += self.stack[-1][1]
            self.stack.pop()
        
        self.stack.append([price, span])
        return span
  
#DP Array Solution (original solutoin I came to, same idea as stack but slightly worse space complexity)
class StockSpanner:

    def __init__(self):
        self.dp = []
        self.prices = []
        
    def next(self, price: int) -> int:
        self.dp.append(1)
        self.prices.append(price)
        
        i = len(self.dp)-1
        while i > 0:
            if self.prices[-1] < self.prices[i-1]:
                break
            else:
                self.dp[-1] += self.dp[i-1]
                i -= self.dp[i-1]
   
        return self.dp[-1]
