#!/usr/bin/python

import argparse


def find_max_profit(prices):
    # try number 1
    #
    # print(prices)
    # if prices[0] > prices[1]:
    #     max_price = prices[0]
    #     max_price_index = 0
    #     min_price = prices[1]
    #     min_price_index = 1
    # else:
    #     max_price = prices[1]
    #     max_price_index = 1
    #     min_price = prices[0]
    #     min_price_index = 0
    # print(max_price, min_price)
    # for i in range(0, len(prices)):
    #     if prices[i] > max_price:
    #         max_price = prices[i]
    #         max_price_index = i
    #     elif prices[i] < min_price and min_price_index > max_price_index:
    #         if max_price_index == 0:
    #             max_price = prices[i + 1]
    #             max_price_index = i + 1
    #         else:
    #             max_price = prices[min_price_index - 1]
    #             max_price_index = min_price_index - 1
    #         min_price = prices[i]
    #         min_price_index = i
    # print('end', max_price, min_price)
    # return max_price - min_price
    #
    # try number 2
    max = prices[1] - prices[0]
    for i in prices:
        for j in prices[prices.index(i) + 1:]:
            if j - i > max:
                max = j - i

    return max


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))


"""
find biggest number
find smallest number
subtract smallest number from biggest number
return result
"""
