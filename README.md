

# 🧾 Product Billing System in Python (with SQL)

This is a simple Python project that allows users to input a product code and quantity. The system retrieves product data from an SQL database and generates a customer invoice automatically.

## 🚀 Features

* Add and manage products in a SQL database
* Input product code and quantity
* Automatic calculation of total price
* Display of detailed invoice for the customer
* Basic stock quantity check (optional)

## 🛠️ Technologies Used

* **Python 3**
* **SQLite3** (or MySQL/PostgreSQL if you're using something else)
* Optional: `PrettyTable`, `pandas`, or any library for formatting output

## 📦 Installation

```bash
git clone https://github.com/your-username/product-billing-system.git
cd product-billing-system
pip install -r requirements.txt
```

> If you're using SQLite, no installation needed for the database.
> For MySQL/PostgreSQL, update your connection settings in the script.

## 📋 How it Works

1. **Admin** adds products to the database with:

   * `product_code`
   * `name`
   * `price`
   * `stock` (optional)

2. **Customer** inputs:

   * Product code
   * Quantity

3. **System**:

   * Retrieves product details
   * Multiplies price × quantity
   * Generates and prints an invoice

## 💻 Example

```
Enter product code: P002
Enter quantity: 3

--- Invoice ---
Product: Wireless Mouse
Quantity: 3
Unit Price: 10.00 $
Total: 30.00 $
Thank you for your purchase!
```

## 🧰 Database Schema (example)

**Table: products**

| id | code | name           | price | stock |
| -- | ---- | -------------- | ----- | ----- |
| 1  | P001 | USB Keyboard   | 15.00 | 20    |
| 2  | P002 | Wireless Mouse | 10.00 | 35    |

> You can manage this table manually, or create a basic admin interface to add/edit products.

## ✅ Optional Improvements

* GUI using `Tkinter` or `PyQt`
* Export invoice to PDF
* Reduce stock after purchase
* Add date/time of invoice
* Add client name or ID

## 📜 License

MIT © 2025


