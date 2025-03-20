class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        n = len(prices)
        d = [[0] * 2 for _ in range(n)]
        # d[i][k] i　是天数，k是当天结束后持有1或者不持有0股票
        d[0][0] = 0
        d[0][1] = -prices[0] - fee
        for i in range(1, n):
             d[i][0] = max(d[i-1][0], d[i-1][1] + prices[i]) # 到底是要继续持有股票还是卖出股票
             d[i][1] = max(d[i-1][1], d[i-1][0] - prices[i] - fee) # 能不能以更低的价格买下当前股票
             # 可怕
        return d[n-1][0]


    def maxProfit2(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            # we treat the stock price as a pattern of low -- high -- low -- high ...
            # And every time we see a potential max_profit we add it
            if price < min_price:
                min_price = price
            if price - min_price - fee > 0:
                max_profit += price - min_price - fee
                min_price = price - fee # Since we have already calculated a fee in previous transaction

        return max_profit 