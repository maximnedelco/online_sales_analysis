# Online Sales Analysis

A Python project for managing products and a customer cart in an online store.
Built to practice Git (branches, merges, conflicts) and OOP in Python.

## Classes
- **Product** (`product.py`): name, price, quantity. Methods: `display_info()`, `update_quantity()`.
- **ProductManager** (`product_manager.py`): list of products. Methods: `add_product()`, `remove_product()`, `display_products()`, `total_value()`.
- **Cart** (`cart.py`): `cart_items` list. Methods: `add_product()`, `total()`, `display_cart()`.

## Features
- Add, display, update and remove products
- Calculate total inventory value
- Add products to a cart, show its contents and total price

## Run
    python3 main.py

## Security
`config.json` (API keys) and screenshots are excluded via `.gitignore`.
