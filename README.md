# instagram-automation

## Dependencies

Download Chrome and matching Chromedriver:

1. https://googlechromelabs.github.io/chrome-for-testing/#stable
2. `unzip` the Chromedriver

Setup env:

```bash
python3 -m venv env
env/bin/pip install -r requirements.txt
```

## Example usage

Run:

```bash
env/bin/python3 webdriver.py \
    --chromedriver chromedriver-linux64/chromedriver \
    --chrome_version 122.0.6261.111
```
