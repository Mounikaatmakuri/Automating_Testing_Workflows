## This is the simple calculator python app

This repository demonstrates a basic CI/CD pipeline using **GitHub Actions** to automate Python testing, linting, and deployment tasks.

## ⚙️ Features

- ✅ Python Unit Testing with `pytest`
- ✅ Syntax and lint checking using `flake8`
- ✅ GitHub Actions for CI/CD automation
- ✅ Error handling and modular structure

## 🚀 How It Works

Every time you **push** or create a **pull request** to the `main` branch, GitHub Actions will:

1. Set up a Python environment
2. Install dependencies (`requirements.txt`)
3. Run tests from the `tests/` folder
4. Check for syntax errors using `flake8`

## 🧪 Run Locally

To run the tests on your machine:

```bash
# Create a virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Run tests
pytest

# Run linter
flake8 .
