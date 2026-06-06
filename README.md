# Automated portfolio optimization

A Python-based portfolio construction tool using Modern Portfolio Theory (MPT).
The application retrieves market data, computes the Markowitz Efficient Frontier, optimizes asset allocations, and generates a concise report in PDF format.
- Automated Data Pipeline: Fetches historical market data dynamically via Yahoo Finance.
- Calculates optimal weights for the Maximum Sharpe Ratio and Minimum Volatility portfolios.
- Generates and saves a clean, modern plot of the Efficient Frontier.
- Compiles results and charts into a polished PDF report using ReportLab.
### Fully modular code structure decoupled from Jupyter Notebooks.

## Project Structure :
```text
Portfolio optimisation/
main.py                   Production entry point (orchestrates the workflow)
  src/                     Core application modules
      data_loader.py         Handles market data ingestion
      optimizer.py           Executes MPT mathematical optimization
      visualizations.py      Plots the Efficient Frontier chart
      report_generator.py    Compiles and styles the final PDF report
  IMAGES/                  Stored visualization outputs
  reports/                 Stored PDF artifacts
