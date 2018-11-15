#!/usr/bin/env python
#-*- coding:utf-8 -*-

def min_coin_number(money, coins):
    if money == 0:
        return 0
    elif len(coins) == 0:
        return 10 ** 10
    min_coins, max_coin = coins[:-1], coins[-1]
    lst = [min_coin_number(money - max_coin * i, min_coins) + i for i in range(money / max_coin + 1)]
    print lst
    return min(lst)

def main():
    coins = [1, 3, 5]
    money = 11
    print min_coin_number(money, coins)

if __name__ == "__main__":
    main()
