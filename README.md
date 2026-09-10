# CodeAlpha_StockPortfolioTracker

A simple command-line Python program that calculates the total value of a stock investment, using a hardcoded dictionary of stock prices. Built as Task 2 of the CodeAlpha Python Programming Internship.

## What it does

The program asks the user to pick a stock (from a small predefined list) and a quantity, then calculates and displays the total investment value. Every lookup — valid or invalid — is logged with a timestamp to a `.txt` file, and a running session total is shown and saved once the user is done.

## Features

- Displays available stocks and their prices directly in the input prompt
- Calculates total investment value (quantity × price)
- Logs every lookup (including invalid stock symbols) to `portfolio_results.txt`, with a timestamp
- Handles invalid input gracefully (e.g. typing letters instead of a number for quantity) without crashing
- Tracks and displays a running session total across multiple lookups
- Lets the user check multiple stocks in one session before exiting

## How to run

1. Make sure Python 3 is installed.
2. Run the script:
   python stock_portfolio_tracker.py
3. Follow the prompts:
   - Enter a stock symbol (AAPL, TSLA, or MSFT)
   -
