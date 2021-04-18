#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#


"""
in order to run this or almost any other Python script
the user needs to be able to load/install 3rd-party Python modules/packages from the internet

There are many ways to do this, we will propose one way:

Install Python IDE/DEbugger calles Spyder as a part of bigger package called Anaconda

Firtst download and install Anaconda from   https://www.anaconda.com/products/individual

and then launch Anaconda and install Spyder in-app from

https://docs.spyder-ide.org/current/installation.html

After that following https://stackoverflow.com/questions/10729116/adding-a-module-specifically-pymorph-to-spyder-python-ide
run command

pip install pandas_datareader

if you need to load/install other Python 3rd-party pankages, then tun
pip install "name of package"
example
pip install numpy
pip install pandas

This scripts downloads and prints daily OHLCV data for the following 4 instruments

- Stock: Microsoft
- ETF: Russell 2000 Growth
- Mutual fund: Vanguard 500 Index fund
- Currency BTC-USD
"""

from pandas_datareader import data as pdr


def test_yfinance():
    for symbol in ['MSFT', 'IWO', 'VFINX', 'BTC-USD']:
        print(">>", symbol, end=' ... ')
        data = pdr.get_data_yahoo(symbol, start='2020-09-25', end='2020-10-02')
        print(data)


if __name__ == "__main__":
    test_yfinance()
