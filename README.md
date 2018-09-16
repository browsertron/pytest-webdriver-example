# pytest-webdriver-example
This repo shows the fastest way to run WebDriver with pytest

## Prerequisites

  - Python 3.6+
  - Pipenv

## Getting Started

```bash
# Clone the repo
git clone git@github.com:browsertron/pytest-webdriver-example.git
cd pytest-webdriver-example

pipenv install

# Generate Tests
pipenv run generate
```

## Running Tests

### Locally

```bash
# The app server is started for you in the background with `pipenv run app`
pipenv run test
```

## Generate Tests

To create large test suites, we generate tests. The template `tests/webdriver.template.py` has one template parameter `{{num}}`. If you change the template or `tests/conftest.py`, or want a larger test suite, run `pipenv run generate`.

```bash
# Generate the desired number of tests (the default is 20)
pipenv run generate 25
```

# Modifications

* This example uses [`pytest-parallel`](https://github.com/browsertron/pytest-parallel) to run tests concurrently. You can change the level of concurrency (`--tests-per-worker`) in `tasks.py`.
* `selenium` for Python doesn't use thread-safe requests by default, so running all the tests in the same thread with `pytest-parallel` causes flakiness. To ensure thread safety, `tests/webdriver_monkey_patch.py` should be imported in `tests/conftest.py` until the official package supports thread-safe requests.

## License
MIT
