# pytest-webdriver-example
This repo shows the fastest way to run WebDriver with pytest

## Prerequisites

  - Python 3.6+
  - Pipenv
  - a tunnel - [ngrok](https://ngrok.com/), [localtunnel](https://localtunnel.github.io/www/), [serveo](https://serveo.net/)

## Getting Started

```bash
# Clone the repo
git clone git@github.com:browsertron/pytest-webdriver-example.git
cd pytest-webdriver-example

pipenv install

# Generate Tests
pipenv run generate
```

## Run tests

```bash
# The app server is started for you in the background with `pipenv run app`
pipenv run test
```

## Run tests remotely

Large suites can be run much quicker when the browsers are created remotely. To configure remote execution:

1) Add a REMOTE_WEBDRIVER environment variable. This snippet uses Browsertron, but you can use any remote service you like.
    ```bash
    ~/.bash_profile
    export REMOTE_WEBDRIVER='https://token:YOUR_TOKEN@grid.browsertron.com/wd/hub'
    ```
2) Start a tunnel with ngrok, localtunnel, or serveo against port 8000
    ```bash
    ngrok http 8000
    ```
3) In another terminal, start the tests
    ```bash
    pipenv run test --remote --url=YOUR_TUNNEL_URL
    ```

## Generate Tests

To create large test suites, we generate tests from templates in `tests/`. The template `tests/webdriver.template.py` has one template parameter `{{num}}`. If you change any template, or want a larger test suite, run `pipenv run generate`.

```bash
# Generate the desired number of tests (the default is 20)
pipenv run generate 25
```

## Modifications

* This example uses [`pytest-parallel`](https://github.com/browsertron/pytest-parallel) to run tests concurrently. You can change the level of concurrency (`--tests-per-worker`) in `tasks.py`.
* `selenium` for Python doesn't use thread-safe requests by default, so running all the tests in the same thread with `pytest-parallel` causes flakiness. To ensure thread safety, `tests/webdriver_monkey_patch.py` is imported in `tests/conftest.py` until the official package supports thread-safe requests.

## License
MIT
