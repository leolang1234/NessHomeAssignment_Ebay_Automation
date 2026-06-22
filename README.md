# Ness Home Assigment

## Overview

This is my suggested answers to the Ness home assigment
Answer to question 1:
Demonstrate an E2E automation flow on the eBay website using Playwright with Python.
The scenario's steps
  1. Login
  2. Empty Cart 
  3. update the currency
  4. searching products, filtering by price ,adding items to the cart
  5. validating the cart total.

Answer to question 2:
The file errors_in_the_static_code_section.html.
A Basic expand collapse table to describe the errors found and how to fix them

The project is built using:

- Playwright (Python)
- Pytest
- Page Object Model (POM)
- Data-Driven approach
- Allure Reports for test reporting
- Text Logger to help with debugging
- Claude Code

---

## Prerequisites

Before running the project, make sure you have:

- Python3 (version 3.10 or higher)
- PIP3
- Google Chrome / Chromium installed
- Allure CLI installed

---

## How to Run Locally

```bash
# 1) Clone the repository
git clone https://github.com/leolang1234/NessHomeAssignment_Ebay_Automation.git

# 2) Navigate into the project folder
cd NessHomeAssignment_Ebay_Automation

# 3) Install requirements
pip install -r requirements.txt

# 4) Install Playwright browsers
playwright install

# 5) Run tests and generate Allure results
pytest --alluredir=allure-results

# 6) Open the Allure report
allure serve allure-results
```

---

## Test Data (Data-Driven)

Test inputs are configured in `data/test_data.json`.

You can change values like:

- query
- max_price
- limit
- Login User Name and password

---

## Architecture

The project follows the Page Object Model (POM) pattern with an additional flow layer:

- `pages/`  
  Contains page classes (HomePage, ProductPage, CartPage).  
  Each class is responsible for a single page and its actions.

- `flows/`  
  Contains business flows that orchestrate multiple page objects  
  (e.g. search flow, add-to-cart flow, cart validation flow).

- `tests/`  
  Contains test scenarios written with pytest.

- `utils/`  
  Shared helpers such as data loading and parsing.

- `data/`  
  External test data files (JSON).

This structure improves readability, maintainability, and scalability.

---

## Assumptions and Limitations

- No user login is performed (Guest checkout only).
- Prices are validated based on the displayed currency on the site.
- Product availability and prices may change over time.
- The test assumes standard eBay UI.

---

## Notes

- Screenshots and reports are generated during runtime and are excluded from version control.
- All screenshots are attached directly to the Allure report.
