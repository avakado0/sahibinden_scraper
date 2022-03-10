# sahibinden_scraper
This scraper written with Scrapy scrapes major Turkish e-commerce web site sahibinden.com which has bot protection system for web scrapers.

In order to bypass the bot detection system 3 methods are used

1) Delay between requests with a random multiplier
2) Use of user agent rotation where in each request a different user agent info is sent to the page
3) Use of rotating proxies middleware. Free proxies from Turkey are used rotatingly which distracts the web page from detecting.
