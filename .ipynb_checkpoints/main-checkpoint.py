from src.data_loader import fetch_stock_prices
from src.optimizer import optimize_portfolios
from src.visualizations import generate_efficient_frontier_chart
from src.report_generator import create_pdf_report

def main():
    print("==================================================")
    print("   Portfolio Analytics Automation Engine Launch   ")
    print("==================================================\n")
    
    # Step 1: Input Matrix Definition
    target_tickers = ["AAPL", "MSFT", "GOOGL", "NVDA"]
    
    # Step 2: Extract Data Pipelines
    raw_data = fetch_stock_prices(target_tickers)
    
    # Step 3: Run Quantitative Optimizations 
    Mu, Sigma, mv_weights, mv_vol, ms_weights, ms_sharpe = optimize_portfolios(raw_data)
    
    print("\n[Optimization Metrics Derived Successfully]")
    print(f"Minimum Volatility achieved: {mv_vol:.4f}")
    print(f"Maximum Sharpe Ratio achieved: {ms_sharpe:.4f}\n")
    
    # Step 4: Map Visual Layout Modeling
    generate_efficient_frontier_chart(Mu, Sigma, mv_weights, ms_weights)
    
    # Step 5: Automate Corporate Reporting Compilation
    create_pdf_report(mv_weights, ms_weights)
    
    print("\n==================================================")
    print("        Workflow Pipeline Run Terminated          ")
    print("==================================================")

if __name__ == "__main__":
    main()