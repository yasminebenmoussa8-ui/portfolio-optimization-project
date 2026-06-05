import fpdf
from fpdf.enums import XPos, YPos
import os

class PortfolioReport(fpdf.FPDF):
    def header(self):
        self.set_font("Helvetica", "B", 18)
        self.set_text_color(30, 64, 175)  # Modern Blue
        self.cell(0, 12, "Portfolio Optimization Report", new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="C")
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font("Helvetica", "I", 8)
        self.set_text_color(160, 174, 192)  # Light Grey
        self.cell(0, 10, f"Page {self.page_no()}/{{nb}}", align="C")

def create_pdf_report(mv_portfolio, ms_portfolio, output_dir="reports"):
    """
    Constructs a stylized multi-page PDF performance execution overview.
    """
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "Portfolio_Report.pdf")
    
    try:
        print("Beginning PDF compilation pipeline...")
        pdf = PortfolioReport()
        pdf.alias_nb_pages()
        pdf.add_page()

        pdf.set_font("Helvetica", "", 11)
        pdf.set_text_color(45, 55, 72)

        texte_intro = (
            "This report presents the results of our portfolio optimization "
            "applied on selected tickers (AAPL, GOOGL, MSFT, NVDA). "
            "The results have been computed with Python using PyPortfolioOpt.\n\n"
        )
        pdf.multi_cell(0, 6, texte_intro)
        pdf.ln(4)

        # SECTION 1 : Minimum Volatility
        pdf.set_font("Helvetica", "B", 13)
        pdf.set_text_color(30, 64, 175)
        pdf.cell(0, 10, "1. Portfolio Minimum Volatility", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        pdf.set_text_color(45, 55, 72)

        for ticker, weight in mv_portfolio.items():
            pdf.set_font("Helvetica", "", 11)
            pdf.cell(40, 7, f"   - {ticker} : ", new_x=XPos.RIGHT, new_y=YPos.TOP)
            pdf.set_font("Helvetica", "B", 11)
            pdf.cell(30, 7, f"{weight*100:.2f} %", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

        pdf.ln(8)

        # SECTION 2 : Max Sharpe
        pdf.set_font("Helvetica", "B", 13)
        pdf.set_text_color(30, 64, 175)
        pdf.cell(0, 10, "2. Portfolio Max Sharpe", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        pdf.set_text_color(45, 55, 72)

        for ticker, weight in ms_portfolio.items():
            pdf.set_font("Helvetica", "", 11)
            pdf.cell(40, 7, f"   - {ticker} : ", new_x=XPos.RIGHT, new_y=YPos.TOP)
            pdf.set_font("Helvetica", "B", 11)
            pdf.cell(30, 7, f"{weight*100:.2f} %", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
            
        # Section 3: Efficient Frontier Graph
        pdf.add_page()
        pdf.set_font("Helvetica", "B", 13)
        pdf.set_text_color(30, 64, 175)
        pdf.cell(0, 10, "3. Efficient Frontier", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        
        # Points to the saved folder structure path directly
        pdf.image("images/efficient_frontier.png", x=15, y=40, w=170)

        pdf.output(output_path)
        print(f"✅ SUCCESS: Elegant PDF report compiled at: {output_path}")

    except Exception as e:
        print(f"❌ COMPILATION ERROR: {e}")