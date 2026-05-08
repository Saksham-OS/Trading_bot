# Binance Futures Trading Bot

A Python-based Binance Futures Trading Bot developed as part of an internship assignment.

## Features

* Market Order Placement
* Limit Order Placement
* Stop-Limit Order Placement
* Binance Testnet API Integration
* Command Line Interface (CLI)
* Input Validation
* Error Handling
* Logging System
* Secure API Key Handling using .env

## Technologies Used

* Python
* Binance API
* python-binance
* python-dotenv
* argparse
* logging

## How to Run

### Install dependencies

pip install -r requirements.txt

### Configure .env file

Add your Binance Testnet API Key and Secret

### Run Example

python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001

## Project Purpose

This project demonstrates Python development, API integration, exception handling, modular code structure, and practical trading bot implementation.
