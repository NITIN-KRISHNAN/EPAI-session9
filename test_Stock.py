import Stock
from collections import namedtuple

stock_market = Stock.create_stock_market()


def test_stock_types():
    assert type(stock_market) == Stock.StockMarket
    assert type(stock_market._0) == Stock.StockExt


def test_create_stock_market():
    assert len(stock_market) == Stock.NUM_COMPANIES


def test_weights_add_to_one():
    assert round(sum(Stock.get_random_weights(Stock.NUM_COMPANIES))) == 1
    weight = 0
    for stock in stock_market:
        weight += stock.weight
    assert round(weight) == 1


def test_random_stock_sanity():
    stock = Stock.get_random_stock()
    assert 100 <= stock.open < 10000
    assert stock.high >= stock.low
    assert stock.low <= stock.close <= stock.high
    assert 0 <= stock.low
    assert 0 <= stock.close


def test_all_stock_sanity():
    stock_market = Stock.create_stock_market()
    for stock in stock_market:
        assert 100 <= stock.open < 10000
        assert stock.high >= stock.low
        assert stock.low <= stock.close <= stock.high
        assert 0 <= stock.low
        assert 0 <= stock.close


def test_index_sanity():
    index = Stock.calculate_index(Stock.create_stock_market())
    assert index.high >= index.low
    assert index.low <= index.close <= index.high
    assert 0 <= index.low
    assert 0 <= index.close


def test_index_calculation():
    StockMarketExt = namedtuple("StockMarket", list(range(2)), rename=True)
    stock_market_abridged = StockMarketExt(*(Stock.StockExt('Rodriguez','Rod2' , 1372, 1418,  1248, 1257, 0.36),
                                       Stock.StockExt('Freeman', 'Fre41', 7391, 8694, 7213, 7293, 0.64)))
    index = Stock.calculate_index(stock_market_abridged)
    assert round(index.high,2) == round((1418*.36 + 8694*.64),2)\
           and round(index.open,2) == round((1372*.36 + 7391*.64),2)\
           and round(index.low,2) == round((1248*.36 + 7213*.64),2)\
           and round(index.close,2) == round((1257*.36 + 7293*.64),2)


def test_unique_stock_ticker():
    symbols = set()
    names = set()
    for stock in stock_market:
        symbols.add(stock.symbol)
        names.add(stock.name)
    assert len(symbols) == len(names) == Stock.NUM_COMPANIES


def test_upper_circuits():
    for stock in stock_market:
        assert stock.high <= 1.2 * stock.open
        assert stock.close <= 1.2 * stock.open


def test_lower_circuits():
    for stock in stock_market:
        assert stock.low >= 0.2 * stock.open
        assert stock.close >= 0.2 * stock.open