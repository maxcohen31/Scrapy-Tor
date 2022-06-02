# Scrapy/Tor Web Scraper
Web scraper using Scrapy framework along with Tor network

## Setup a virtual enviroment
```bash
virtualenv amazonscraper ; source bin/activate
pip install scrapy
```
## Directory Structure
.
├── README.md
└── Scrapy-With-Tor
    └── housespider
        ├── housespider
        │   ├── __init__.py
        │   ├── items.py
        │   ├── middlewares.py
        │   ├── pipelines.py
        │   ├── __pycache__
        │   │   ├── __init__.cpython-39.pyc
        │   │   ├── items.cpython-39.pyc
        │   │   ├── middlewares.cpython-39.pyc
        │   │   └── settings.cpython-39.pyc
        │   ├── settings.py
        │   └── spiders
        │       ├── check_ip.py
        │       ├── __init__.py
        │       ├── luxury_properties.csv
        │       ├── luxury_spider.py
        │       └── __pycache__
        │           ├── check_ip.cpython-39.pyc
        │           ├── ifconfig.cpython-39.pyc
        │           ├── __init__.cpython-39.pyc
        │           ├── luxury_spider.cpython-39.pyc
        │           └── tryip.cpython-39.pyc
        └── scrapy.cfg

## Go to the project directory

```bash
  cd Amazon-book-scraper
  cd housespider/housespider/spiders/
```

## Run the crawler - Run IP checker
```bash
  python3 luxury_spider.py
  python3 check_ip.py
```
## TODO
- ItemLoader
