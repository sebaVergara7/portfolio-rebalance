# 📊 Portfolio Rebalance

A modular Python project that calculates the total value of an investment portfolio and determines how to rebalance it according to a target allocation.

---

## 📌 Description

This project models a basic investment portfolio composed of individual stocks. It calculates the portfolio's total value and determines the dollar adjustments needed to match a target allocation. The code is structured for clarity, modularity, and testability, making it ideal for educational purposes, technical interviews, or as a foundation for more advanced financial tools.

---

## 🚀 Technologies Used

- **Language**: Python 3.10+
- **Testing**: Pytest
- **Structure**: Modular design with `src/` and `tests/` folders

---

## 🛠 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/portfolio-rebalance.git
cd portfolio-rebalance
```

### 2. Create and Activate a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 📁 Project Structure

```code
portfolio-rebalance/
├── src/                  # Core logic
│   ├── __init__.py       # Package initializer
│   ├── stock.py          # Stock class
│   └── portfolio.py      # Portfolio class
├── tests/                # Unit tests
│   └── test_portfolio.py
├── examples/             # Executable usage examples
│   └── basic_usage.py
├── pytest.ini            # Pytest configuration
├── requirements.txt      # Dependencies
├── README.md             # Project documentation
└── .gitignore
```

---

## 🧪 Testing

To run the test suite:

```bash
python -m pytest
```

Or with verbose output:

```bash
python -m pytest -v
```

---

## ▶️ Example Usage

Run the example script to see the portfolio valuation and rebalance output:

```bash
python -m examples.basic_usage
```

Expected output:

```code
Total portfolio value: 15000
Rebalance actions (in dollars): {'META': 1000, 'AAPL': -1000}
```

---

## 🧠 Design Decisions

- Modular structure: Separates domain logic (Stock, Portfolio) from usage and testing.
- Explicit typing: Uses Python type hints for clarity and maintainability.
- Test-first mindset: Includes unit tests to validate core functionality.

---

## ⚠️ Known Limitations

- Prices are hardcoded and do not reflect real-time market data.
- No support for fractional shares or transaction fees.
- No persistent storage or external API integration.

## 💡 Possible Future Improvements

- Integrate real-time stock prices via a market API.
- Add support for fractional shares and fees.
- Implement rebalance suggestions in terms of share quantities.
- Extend to support ETFs, mutual funds, or crypto assets.

---

Let me know if you'd like to include badges (e.g. build status, Python version), author credits, or links to your GitHub profile to polish it further.

## 📖 Appendix – LLM Usage Log This project was developed with the support of Microsoft Copilot for documentation and presentation tasks. The design, implementation, and technical decisions were mine; Copilot helped accelerate repetitive tasks such as writing docstrings and structuring the README. You can find the detailed log of relevant conversations here: [docs/LLM_USAGE_LOGS.md](docs/LLM_USAGE_LOGS.md)


