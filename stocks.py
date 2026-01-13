import time

# Colors
BLUE = '\033[94m'
YELLOW = '\033[93m'
BOLD = '\033[1m'
RESET = '\033[0m'

def run_tracker():
    prices = {"AAPL": 180, "TSLA": 250, "GOOGL": 145, "MSFT": 400, "NVDA": 500}
    portfolio = []
    
    print(f"{BLUE}{BOLD}======================================")
    print("      STOCK PORTFOLIO TRACKER")
    print(f"======================================{RESET}")
    print(f"Available Market: {', '.join(prices.keys())}")

    while True:
        symbol = input(f"\n{YELLOW}Enter Ticker (or 'exit'): {RESET}").upper()
        if symbol == 'EXIT': break
        
        if symbol in prices:
            try:
                qty = int(input(f"Shares of {symbol}: "))
                val = qty * prices[symbol]
                portfolio.append({"symbol": symbol, "qty": qty, "price": prices[symbol], "total": val})
                print(f"✅ Added {symbol}")
            except ValueError:
                print("❌ Please enter a number for quantity.")
        else:
            print(f"❌ {symbol} not found in our database.")

    # Generate Report UI
    total_inv = sum(item['total'] for item in portfolio)
    report = f"\n{BOLD}{'TICKER':<10} | {'QTY':<5} | {'PRICE':<8} | {'SUBTOTAL'}{RESET}\n"
    report += "-" * 40 + "\n"
    for item in portfolio:
        report += f"{item['symbol']:<10} | {item['qty']:<5} | ${item['price']:<7} | ${item['total']:,}\n"
    report += "-" * 40
    report += f"\n{BOLD}TOTAL PORTFOLIO VALUE: ${total_inv:,.2f}{RESET}"

    print(report)

    # Save to file
    save = input("\nSave report to file? (y/n): ").lower()
    if save == 'y':
        print("Saving", end="")
        for _ in range(3):
            time.sleep(0.4)
            print(".", end="", flush=True)
        
        with open("portfolio.txt", "w") as f:
            f.write(report.replace(BOLD, "").replace(BLUE, "").replace(YELLOW, "").replace(RESET, ""))
        print(f"\n{GREEN}File 'portfolio.txt' created successfully!{RESET}")

if __name__ == "__main__":
    run_tracker()