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
   - Enter a quantity
   - Repeat as many times as you like
   - Type "no" when asked if you want to check another stock, to see your session summary

## Example

Enter your preferred stock: 
AAPL ($180), TSLA ($250), MSFT ($420): aapl
Enter the quantity to check: 12
Total investment value: $ 2160
Do you want to check another stock? (yes/no): no
Total invested this session: $2160

Each run appends to `portfolio_results.txt`, so your history builds up over time rather than being overwritten.

## Concepts used

- Dictionaries (stock_prices) for storing hardcoded stock data
- while loops for repeated input and session control
- if / elif / else for branching logic
- try / except for handling invalid number input
- File handling (with open(...) as file:, append mode, .write())
- The datetime module for timestamping log entries
- String building and formatting (+, str(), .join(), list .append())

## Notes

This project was built incrementally while learning — starting from basic input/output and file writing, then layering on error handling, timestamps, a dynamic stock list, and a session summary.
