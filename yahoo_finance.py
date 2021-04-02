import yfinance as yf


def stock_available(symbol):
    ticker = yf.Ticker(symbol)
    stockInfo = ticker.info

    if len(stockInfo) > 1:
        return True
    else:
        return False


def yahoo_finance_summary(symbol):
    ticker = yf.Ticker(symbol)
    stockInfo = ticker.info

    summary = {
        'zip': stockInfo['zip'],
        'phone': stockInfo['phone'],
        'sector': stockInfo['sector'],
        'website': stockInfo['website'],
        'city': stockInfo['city'],
        'country': stockInfo['country'],
        'shortName': stockInfo['shortName'],
        'exchangeTimezoneShortName': stockInfo['exchangeTimezoneShortName'],
        'symbol': stockInfo['symbol'],
        'market': stockInfo['market'],
        'logo_url': stockInfo['logo_url'],
        'currency': stockInfo['currency'],
        'regularMarketPrice': stockInfo['regularMarketPrice'],
    }
    return summary


def yahoo_finance_financial(symbol):
    ticker = yf.Ticker(symbol)
    stockInfo = ticker.info
    financial = {
        'previousClose': stockInfo['previousClose'],
        'regularMarketOpen': stockInfo['regularMarketOpen'],
        'twoHundredDayAverage': stockInfo['twoHundredDayAverage'],
        'trailingAnnualDividendYield': stockInfo['trailingAnnualDividendYield'],
        'payoutRatio': stockInfo['payoutRatio'],
        'volume24Hr': stockInfo['volume24Hr'],
        'regularMarketDayHigh': stockInfo['regularMarketDayHigh'],
        'navPrice': stockInfo['navPrice'],
        'averageDailyVolume10Day': stockInfo['averageDailyVolume10Day'],
        'totalAssets': stockInfo['totalAssets'],
        'regularMarketPreviousClose': stockInfo['regularMarketPreviousClose'],
        'fiftyDayAverage': stockInfo['fiftyDayAverage'],
        'trailingAnnualDividendRate': stockInfo['trailingAnnualDividendRate'],
        'open': stockInfo['open'],
        'toCurrency': stockInfo['toCurrency'],
        'averageVolume10days': stockInfo['averageVolume10days'],
        'expireDate': stockInfo['expireDate'],
        'yield': stockInfo['yield'],
        'algorithm': stockInfo['algorithm'],
        'dividendRate': stockInfo['dividendRate'],
        'exDividendDate': stockInfo['exDividendDate'],
        'beta': stockInfo['beta'],
        'circulatingSupply': stockInfo['circulatingSupply'],
        'startDate': stockInfo['startDate'],
        'regularMarketDayLow': stockInfo['regularMarketDayLow'],
        'priceHint': stockInfo['priceHint'],
        'currency': stockInfo['currency'],
        'trailingPE': stockInfo['trailingPE'],
        'regularMarketVolume': stockInfo['regularMarketVolume'],
        'lastMarket': stockInfo['lastMarket'],
        'maxSupply': stockInfo['maxSupply'],
        'openInterest': stockInfo['openInterest'],
        'marketCap': stockInfo['marketCap'],
        'volumeAllCurrencies': stockInfo['volumeAllCurrencies'],
        'strikePrice': stockInfo['strikePrice'],
        'averageVolume': stockInfo['averageVolume'],
        'priceToSalesTrailing12Months': stockInfo['priceToSalesTrailing12Months'],
        'dayLow': stockInfo['dayLow'],
        'ask': stockInfo['ask'],
        'ytdReturn': stockInfo['ytdReturn'],
        'askSize': stockInfo['askSize'],
        'volume': stockInfo['volume'],
        'fiftyTwoWeekHigh': stockInfo['fiftyTwoWeekHigh'],
        'forwardPE': stockInfo['forwardPE'],
        'fromCurrency': stockInfo['fromCurrency'],
        'fiveYearAvgDividendYield': stockInfo['fiveYearAvgDividendYield'],
        'fiftyTwoWeekLow': stockInfo['fiftyTwoWeekLow'],
        'bid': stockInfo['bid'],
        'tradeable': stockInfo['tradeable'],
        'dividendYield': stockInfo['dividendYield'],
        'bidSize': stockInfo['bidSize'],
        'dayHigh': stockInfo['dayHigh'],
        'exchange': stockInfo['exchange'],
        'annualHoldingsTurnover': stockInfo['annualHoldingsTurnover'],
        'enterpriseToRevenue': stockInfo['enterpriseToRevenue'],
        'beta3Year': stockInfo['beta3Year'],
        'profitMargins': stockInfo['profitMargins'],
        'enterpriseToEbitda': stockInfo['enterpriseToEbitda'],
        '52WeekChange': stockInfo['52WeekChange'],
        'morningStarRiskRating': stockInfo['morningStarRiskRating'],
        'forwardEps': stockInfo['forwardEps'],
        'revenueQuarterlyGrowth': stockInfo['revenueQuarterlyGrowth'],
        'sharesOutstanding': stockInfo['sharesOutstanding'],
        'fundInceptionDate': stockInfo['fundInceptionDate'],
        'annualReportExpenseRatio': stockInfo['annualReportExpenseRatio'],
        'bookValue': stockInfo['bookValue'],
        'sharesShort': stockInfo['sharesShort'],
        'sharesPercentSharesOut': stockInfo['sharesPercentSharesOut'],
        'fundFamily': stockInfo['fundFamily'],
        'lastFiscalYearEnd': stockInfo['lastFiscalYearEnd'],
        'heldPercentInstitutions': stockInfo['heldPercentInstitutions'],
        'netIncomeToCommon': stockInfo['netIncomeToCommon'],
        'trailingEps': stockInfo['trailingEps'],
        'lastDividendValue': stockInfo['lastDividendValue'],
        'SandP52WeekChange': stockInfo['SandP52WeekChange'],
        'priceToBook': stockInfo['priceToBook'],
        'heldPercentInsiders': stockInfo['heldPercentInsiders'],
        'nextFiscalYearEnd': stockInfo['nextFiscalYearEnd'],
        'mostRecentQuarter': stockInfo['mostRecentQuarter'],
        'shortRatio': stockInfo['shortRatio'],
        'sharesShortPreviousMonthDate': stockInfo['sharesShortPreviousMonthDate'],
        'floatShares': stockInfo['floatShares'],
        'enterpriseValue': stockInfo['enterpriseValue'],
        'threeYearAverageReturn': stockInfo['threeYearAverageReturn'],
        'lastSplitDate': stockInfo['lastSplitDate'],
        'lastSplitFactor': stockInfo['lastSplitFactor'],
        'legalType': stockInfo['legalType'],
        'lastDividendDate': stockInfo['lastDividendDate'],
        'morningStarOverallRating': stockInfo['morningStarOverallRating'],
        'earningsQuarterlyGrowth': stockInfo['earningsQuarterlyGrowth'],
        'dateShortInterest': stockInfo['dateShortInterest'],
        'pegRatio': stockInfo['pegRatio'],
        'lastCapGain': stockInfo['lastCapGain'],
        'shortPercentOfFloat': stockInfo['shortPercentOfFloat'],
        'sharesShortPriorMonth': stockInfo['sharesShortPriorMonth'],
        'impliedSharesOutstanding': stockInfo['impliedSharesOutstanding'],
        'category': stockInfo['category'],
        'fiveYearAverageReturn': stockInfo['fiveYearAverageReturn'],
        'regularMarketPrice': stockInfo['regularMarketPrice'],
    }
    return financial


def yahoo_finance_company(symbol):
    ticker = yf.Ticker(symbol)
    stockInfo = ticker.info
    company = {
        'zip': stockInfo['zip'],
        'phone': stockInfo['phone'],
        'sector': stockInfo['sector'],
        'longBusinessSummary': stockInfo['longBusinessSummary'],
        'city': stockInfo['city'],
        'state': stockInfo['state'],
        'country': stockInfo['country'],
        'website': stockInfo['website'],
        'maxAge': stockInfo['maxAge'],
        'address1': stockInfo['address1'],
        'industry': stockInfo['industry'],
        'shortName': stockInfo['shortName'],
        'longName': stockInfo['longName'],
        'exchangeTimezoneName': stockInfo['exchangeTimezoneName'],
        'exchangeTimezoneShortName': stockInfo['exchangeTimezoneShortName'],
        'isEsgPopulated': stockInfo['isEsgPopulated'],
        'gmtOffSetMilliseconds': stockInfo['gmtOffSetMilliseconds'],
        'quoteType': stockInfo['quoteType'],
        'symbol': stockInfo['symbol'],
        'messageBoardId': stockInfo['messageBoardId'],
        'market': stockInfo['market'],
        'logo_url': stockInfo['logo_url'],
        'fullTimeEmployees': stockInfo['fullTimeEmployees'],
        'companyOfficers': stockInfo['companyOfficers'],
    }
    return company

print(stock_available('divash'))