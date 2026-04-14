# BDD_SauceLab_2

Minimal pytest + Playwright test suite for Sauce Demo (https://www.saucedemo.com).

Prerequisites
- Python 3.8+
- pip
- (optional) virtualenv/venv

Install

```bash
python -m pip install -r requirements.txt
python -m playwright install
```

Run tests

Use the default `base_url` from `conftest.py` or set `BASE_URL` to override.

```bash
pytest tests/e2e -q
```

Notes
- Tests use the `pytest-playwright` plugin and the `page` fixture.
- If you need to run a single test file: `pytest tests/e2e/test_login.py -q`.
