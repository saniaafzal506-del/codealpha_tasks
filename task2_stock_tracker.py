# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 03:11:03 2026

@author: Administrator
"""

portfolio = {}

def add_stock():
    name = input("Stock ka naam: ").upper()
    shares = int(input("Kitne shares: "))
    price = float(input("1 share ki price: "))
    portfolio[name] = {"shares": shares, "price": price}
    print(f"✅ {name} add ho gaya!")

def show_portfolio():
    if not portfolio:
        print("Portfolio khaali hai!")
        return

    total = 0
    print("\n--- Aapka Portfolio ---")
    for stock, data in portfolio.items():
        value = data["shares"] * data["price"]
        total += value
        print(f"{stock}: {data['shares']} shares x ${data['price']} = ${value}")
    print(f"Total Investment: ${total}\n")

while True:
    print("1. Stock Add karo")
    print("2. Portfolio Dekho")
    print("3. Exit")

    choice = input("Option chuno 1-3: ")

    if choice == "1":
        add_stock()
    elif choice == "2":
        show_portfolio()
    elif choice == "3":
        print("Bye! Portfolio save nahi hua, next task me file handling seekhen ge")
        break
    else:
        print("Ghalat option!")