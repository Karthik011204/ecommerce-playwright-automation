# E-Commerce Playwright Automation Framework

## Features

- Playwright Python UI automation
- Pytest framework
- Page Object Model
- HTML reports
- Test tagging
- Screenshots on failure
- Cross-browser execution
- API testing using Requests and Postman
- GitHub Actions CI/CD

## Install

```bash
pip install -r requirements.txt
playwright install
```

## Run all tests

```bash
pytest
```

## Run smoke tests

```bash
pytest -m smoke
```

## Run regression tests

```bash
pytest -m regression
```

## Run in cross browser

```bash
set BROWSER=chromium
pytest

set BROWSER=firefox
pytest
```

## Run with HTML report

```bash
pytest --html=reports/report.html --self-contained-html
```

## Run parallel

```bash
pytest -n 2
```

## Notes

Demo Web Shop is used for UI automation. ReqRes is used for API testing because Demo Web Shop does not expose public REST APIs.
