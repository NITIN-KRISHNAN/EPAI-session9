from faker import Faker
from collections import namedtuple
import random

faker = Faker()

NUM_COMPANIES = 100
Stock = namedtuple("Stock", "name, symbol, open, high, low, close")
Stock.__doc__ = "This namedtuple represents a stock and its daily change"
Stock.name.__doc__ = "Stock name"
Stock.symbol.__doc__ = "Stock symbol used on ticker"
Stock.open.__doc__ = "Day's Opening price of the stock"
Stock.high.__doc__ = "Day's High price of the stock"
Stock.low.__doc__ = "Day's low price of the stock"
Stock.close.__doc__ = "Day's Closing price of the stock"

StockExt = namedtuple("StockExt", Stock._fields + ("weight", ))
StockExt.__doc__ = "This namedtuple extends a stock and adds the weightage of the stock in the index"
StockExt.weight.__doc__ = "Represents the weightage of the stock in the index"

StockMarket = namedtuple("StockMarket", list(range(NUM_COMPANIES)), rename=True)
StockMarket.__doc__ = "This namedtuple represents the stock market which comprises of many stocks "

Index = namedtuple("Index", 'open, high, low, close')
Index.__doc__ = "This namedtuple represents the daily movement of the index"
Index.open.__doc__ = "Day's opening price of the index"
Index.high.__doc__ = "Day's high price of the index"
Index.low.__doc__ = "Day's low price of the index"
Index.close.__doc__ = "Day's close price of the index"


def create_stock_market() -> StockMarket:
    """
    Function to create random stocks
    :return: namedtuple representing the stock market which comprises of many stocks
    """
    weights = get_random_weights(NUM_COMPANIES)
    stock_list = list()
    for weight in weights:
        stock = get_random_stock()
        stock_ext = StockExt._make(stock + (weight,))
        stock_list.append(stock_ext)
    stock_market = StockMarket(*stock_list)
    return stock_market


def get_random_weights(num) -> list:
    """
    Functions to create index weightage distribution
    :param num: number of stocks in the market
    :return: list of weights of stocks in the index
    """
    random_list = [random.random() for i in range(num)]
    sum_random_list = sum(random_list)
    random_list = [num / sum_random_list for num in random_list]
    return random_list


def get_random_stock() -> Stock:
    """
    Function to create random stock and its day's price movement using faker lib
    :return: randomly generated Stock
    """
    name = faker.company()
    open_ = random.uniform(100, 10000)
    high = random.uniform(open_, 1.2 * open_)
    low = random.uniform(0.8 * open_, open_)
    close = random.uniform(low, high)
    stock  = Stock(name, name[:3] + str(random.randint(0,100)), open_, high, low, close)
    return stock


def calculate_index(stock_market) -> Index:
    """
    Function to calculate the index's price movement
    :param stock_market: namedtuple representing the stock market which comprises of many stocks
    :return: index namedtuple which contains the index's price movement (open, high, low, close)
    """
    open_ = sum(stock_ext.weight * stock_ext.open for stock_ext in stock_market)
    low = sum(stock_ext.weight * stock_ext.low for stock_ext in stock_market)
    high = sum(stock_ext.weight * stock_ext.high for stock_ext in stock_market)
    close = sum(stock_ext.weight * stock_ext.close for stock_ext in stock_market)
    return Index(open_, high, low, close)