# 📚 Open Library — E2E Test Automation

Automated end-to-end tests for [Open Library](https://openlibrary.org) using **Playwright** and **Python**, following the **Page Object Model (POM)** pattern.

---

## 🧪 What does this project test?

| Test | Type | Description |
|------|------|-------------|
| `test_search_book_by_title` | 🟢 Smoke | Searches "Harry Potter" and validates results are returned |
| `test_search_with_no_results` | 🔵 Regression | Searches a random string and validates no results are shown |
| `test_search_with_empty_inputs` | 🔵 Regression | Searches with blank spaces and validates no results are shown |

---

## 🏗️ Project Structure

```
open-library-playwright-python/
│
├── pages/                  # Page Object Model
│   ├── home_page.py        # Open Library home page
│   └── results_page.py     # Search results page
│
├── tests/                  # Test cases
│   └── test_search.py      # Search functionality tests
│
├── conftest.py             # Fixtures (browser setup)
├── pytest.ini              # pytest configuration
├── requirements.txt        # Project dependencies
└── .github/
    └── workflows/          # GitHub Actions CI pipeline
```

---

## ⚙️ Technologies

![Python](https://img.shields.io/badge/Python-3.12+-blue)
![Playwright](https://img.shields.io/badge/Playwright-latest-green)
![pytest](https://img.shields.io/badge/pytest-latest-orange)

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/ivonny88/open-library-playwright-python.git
cd open-library-playwright-python
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
playwright install chromium
```

### 3. Run the tests

**All tests:**
```bash
pytest
```

**Headed mode (visible browser):**
```bash
pytest --headed
```

**Only smoke tests:**
```bash
pytest -m smoke
```

**Only regression tests:**
```bash
pytest -m regression
```

**With HTML report:**
```bash
pytest --html=report.html --self-contained-html
```

---

## 🧩 Design Pattern: Page Object Model (POM)

This project separates test logic from page interactions. Each page of the application has its own class:

- **`HomePage`** — handles navigation and search input
- **`ResultsPage`** — handles result validation

This makes tests easier to read, maintain and scale.

---

## 🔄 CI/CD

Tests run automatically on every push via **GitHub Actions**. The browser runs in headless mode in CI, and in headed mode locally (auto-detected via the `CI` environment variable in `conftest.py`).

---

## 👩‍💻 Author

**Fátima Ocaña** — QA Engineer | Manual & Automation Testing  
[LinkedIn](https://www.linkedin.com/feed/) · [GitHub](https://github.com/ivonny88)
