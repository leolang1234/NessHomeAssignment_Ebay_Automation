# Ness Home Assignment — eBay Automation

End-to-end test automation for the eBay website, built with Playwright and Python as part of the Ness home assignment.

---

## Assignment Answers

### Question 1 — E2E Automation Flow

Demonstrate an end-to-end automation flow on the eBay website using Playwright with Python.

**Scenario steps:**
1. Login
2. Empty the cart
3. Update the shipping country
4. Search for products and filter by price
5. Add items to the cart
6. Validate the cart total

### Question 2 — Static Code Analysis

The file [`errors_in_the_static_code_section.html`](./errors_in_the_static_code_section.html) contains an interactive expand/collapse table listing all bugs found in the provided code snippet, along with a description of each error and a suggested fix.

---

## Tech Stack

| Tool | Purpose |
|---|---|
| Playwright (Python) | Browser automation |
| Pytest | Test framework |
| Page Object Model (POM) | Test architecture pattern |
| Allure Reports | Test reporting |
| Text Logger | Runtime debugging |
| JSON (data/) | Data-driven test inputs (no credentials stored) |

---

## Project Structure

```
NessHomeAssignment_Ebay_Automation/
├── pages/
│   ├── base_page.py          # Shared actions: logging, navigation, screenshots
│   ├── home_page.py
│   ├── login_page.py
│   ├── search_results_page.py
│   ├── product_page.py
│   └── cart_page.py
├── flows/
│   ├── login_flow.py
│   ├── search_flow.py
│   ├── add_to_cart_flow.py
│   └── cart_flow.py
├── tests/
│   └── test_smoke.py
├── utils/
│   ├── logger.py
│   └── data_utils.py
├── data/
│   └── test_data.json
├── conftest.py
├── pytest.ini
└── requirements.txt
```

**Layer responsibilities:**

- **`pages/`** — One class per page. Each inherits from `BasePage` which provides shared element actions, logging, and screenshot helpers.
- **`flows/`** — Business-level orchestration across multiple page objects (e.g. search → filter → add to cart).
- **`tests/`** — Pytest test scenarios that compose flows into full test cases.
- **`utils/`** — Shared helpers: structured logger and JSON data loader.
- **`data/`** — External test inputs kept separate from code.

---

## Prerequisites

- Python 3.10 or higher
- pip
- Google Chrome / Chromium
- Allure CLI ([installation guide](https://docs.qameta.io/allure/#_installing_a_commandline))

---

## Quick Start

```bash
# 1. Clone the repository
git clone https://github.com/leolang1234/NessHomeAssignment_Ebay_Automation.git

# 2. Navigate into the project folder
cd NessHomeAssignment_Ebay_Automation

# 3. Install Python dependencies
pip install -r requirements.txt

# 4. Install Playwright browsers
playwright install

# 5. Run tests and generate Allure results
pytest --username=your@email.com --password=yourpassword --alluredir=allure-results

# 6. Open the Allure report
allure serve allure-results
```

---

## Test Data

Static test inputs are configured in `data/test_data.json`. You can modify:

| Key | Description |
|---|---|
| `query` | Search term |
| `max_price` | Maximum item price filter |
| `limit` | Number of items to add to cart |
| `cart_url` | Direct URL to the eBay cart |

Credentials are **not** stored in the file. Pass them at runtime via command-line flags:

```bash
pytest --username=your@email.com --password=yourpassword
```

---

## Assumptions & Limitations

- Product availability and prices may vary over time.
- Prices are validated based on the currency displayed on the site at runtime.
- The test assumes the standard eBay UI with no A/B variations active.

---

## Notes

- Screenshots and log files are generated at runtime and excluded from version control.
- All screenshots are attached directly to the Allure report for easy debugging.
