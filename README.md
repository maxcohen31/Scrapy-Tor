# Scrapy/Tor Web Scraper using Privoxy
Web scraper using Scrapy framework along with Tor network.
When we combine Scrapy with Tor, we can have more control over our crawler privacy. We already know that Scrapy can work with proxy server however since Scrapy doesn’t work directly with SOCKS proxy, things can work out if we can introduce a http proxy server as an intermediate between Scrapy and Tor which can also speak to Tor using SOCKS. SOCKS protocol is a lower level protocol than http and it is more transparent in a sense that it doesn’t add extra info like http-header.

## Site
luxuryestate.com

## Tools
**TOR**: Is an abbreviation of "The Onion Project", a project that seeks to create a low latency distributed communication network above the Internet layer so that the data of the users who use it will be never reveal, thus maintaining a private and anonymous network.

**Stem**: is a Python controller library for TOR.

**Privoxy**: Privoxy is a non-caching web proxy with advanced filtering capabilities for enhancing privacy, modifying web page data and HTTP headers, controlling access, and removing ads and other obnoxious Internet junk. Privoxy has a flexible configuration and can be customized to suit individual needs and tastes. It has application for both stand-alone systems and multi-user networks.

## Port
● `9051` :  If ControlPort is set ( with this port, in torrc file), Tor will accept connections on this port and allow those connections to control the Tor process using the Tor Control Protocol. 
Unless you also specify one or more of HashedControlPassword or CookieAuthentication, setting this option will cause Tor to allow any process on the local host to control it. This option is required for many Tor controllers; most use the value of 9051.

## Setup a virtual enviroment
```bash
virtualenv housespider ; source bin/activate
pip install scrapy 
pip install stem
pip install scrapy-fake-useragent
pip install request
```

# Start Tor and Privoxy services
```bash
service tor start
service privoxy start
```

## Directory Structure
```bash
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
```
## Go to the project directory

```bash
  cd Scrapy-Tor
  cd housespider/housespider/spiders/
```

## Run the crawler - Run IP checker
```bash
  python3 luxury_spider.py
  python3 check_ip.py
```
## TODO
- ItemLoader
