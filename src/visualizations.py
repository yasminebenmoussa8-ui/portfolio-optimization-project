import matplotlib.pyplot as plt
import os
from pypfopt.efficient_frontier import EfficientFrontier
from pypfopt import plotting

def generate_efficient_frontier_chart(Mu, Sigma, mv_portfolio, ms_portfolio, output_dir="images"):
    """
    Plots the Markowitz Efficient Frontier and markers for key optimal portfolios.
    Saves output directly to an images repository.
    """
    os.makedirs(output_dir, exist_ok=True)
    
    ef_plot = EfficientFrontier(Mu, Sigma)
    fig, ax = plt.subplots(figsize=(10, 6))
    plotting.plot_efficient_frontier(ef_plot, ax=ax, show_assets=True)
    
    # Re-instantiate to compute individual portfolio performance scatter spots safely
    ef_1 = EfficientFrontier(Mu, Sigma)
    ef_1.min_volatility()
    ret_mv, vol_mv, _ = ef_1.portfolio_performance(risk_free_rate=0)
    ax.scatter(vol_mv, ret_mv, marker="*", color="green", s=250, label="Minimum Volatility", zorder=5)
    
    ef_2 = EfficientFrontier(Mu, Sigma)
    ef_2.max_sharpe(risk_free_rate=0)
    ret_ms, vol_ms, _ = ef_2.portfolio_performance(risk_free_rate=0)
    ax.scatter(vol_ms, ret_ms, marker="*", color="red", s=250, label="Max Sharpe Ratio", zorder=5)
    
    ax.set_title("Markowitz Efficient Frontier")
    ax.set_xlabel("Volatility")
    ax.set_ylabel("Expected returns")
    ax.legend()
    ax.grid(True)
    
    # Target path inside your systematic folder setup
    output_path = os.path.join(output_dir, "efficient_frontier.png")
    fig.savefig(output_path, dpi=300)
    plt.close(fig)
    print(f"Chart cleanly saved to: {output_path}")