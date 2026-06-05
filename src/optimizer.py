import pandas as pd
from pypfopt.efficient_frontier import EfficientFrontier
from pypfopt import risk_models, expected_returns

def optimize_portfolios(stock_prices_df):
    """
    Applies Markowitz Efficient Frontier optimization to extract 
    Minimum Volatility and Maximum Sharpe Ratio allocations.
    """
    # 1. Expected returns and covariance matrix calculation
    Mu = expected_returns.mean_historical_return(stock_prices_df)
    Sigma = risk_models.sample_cov(stock_prices_df)
    
    # 2. Optimize for Minimum Volatility
    ef_1 = EfficientFrontier(Mu, Sigma)
    raw_mv_weights = ef_1.min_volatility()
    mv_portfolio = pd.Series(raw_mv_weights)
    mv_portfolio.index.name = "tickers"
    # Extract only volatility (index 1 from performance tuple)
    mv_volatility = ef_1.portfolio_performance(verbose=False)[1] 
    
    # 3. Optimize for Maximum Sharpe Ratio
    ef_2 = EfficientFrontier(Mu, Sigma)
    raw_ms_weights = ef_2.max_sharpe(risk_free_rate=0)
    ms_portfolio = pd.Series(raw_ms_weights)
    # Extract Sharpe ratio (index 2 from performance tuple)
    ms_sharpe = ef_2.portfolio_performance(risk_free_rate=0)[2]
    
    return Mu, Sigma, mv_portfolio, mv_volatility, ms_portfolio, ms_sharpe