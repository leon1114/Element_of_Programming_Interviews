from typing import List

from test_framework import generic_test

def buy_and_sell_brute(prices : List[float]) -> float:
    # Brute force solution
    # iterate over element,
    #   iterate over following elements to find maximum profit
    max_profit = 0

    for i in range(0, len(prices)-1):
        buy = prices[i]
        for j in range(i+1, len(prices)):
            sell = prices[j]
            if (profit := sell - buy) > 0:
                if profit > max_profit:
                    max_profit = profit
    return max_profit # O(n^2)

def buy_and_sell(prices : List[float]) -> float:
    # this should be a O(n) or O(nlogn) solution
    # let's first go for the O(nlogn) solution -> sorting subarrays in every iteration? nope
    # O(n) solution
    # What we need to know is -> min cost before element i
    min_cost = prices[0]
    max_profit = 0
    for price in prices[1:]:
        profit = price - min_cost
        max_profit = profit if profit > max_profit else max_profit
        min_cost = price if price < min_cost else min_cost
    return max_profit

def buy_and_sell_stock_once(prices: List[float]) -> float:
    # profit = buy_and_sell_brute(prices)
    profit = buy_and_sell(prices)
    return profit

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock.py',
                                       'buy_and_sell_stock.tsv',
                                       buy_and_sell_stock_once))
