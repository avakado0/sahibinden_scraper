# Scrapy settings for sah project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https:False//docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'sah'

SPIDER_MODULES = ['sah.spiders']
NEWSPIDER_MODULE = 'sah.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False
#HTTPERROR_ALLOWED_CODES  =[404,429]
# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 10
#RANDOMIZE_DOWNLOAD_DELAY = True


# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs

#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 4

#ROTATING_PROXY_PAGE_RETRY_TIMES=10
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = True

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
   'authority': 'www.sahibinden.com',
   'accept': 'text/html, */*; q=0.01',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
        #'Cookie': 'vid=508; cdid=zkKg6hEKiU7d2dL061f5af83; nwsh=std; showPremiumBanner=false; MS1=https://www.sahibinden.com/; OptanonConsent=isGpcEnabled=0&datestamp=Sun+Jan+30+2022+23%3A28%3A19+GMT%2B0300+(GMT%2B03%3A00)&version=6.22.0&isIABGlobal=false&hosts=&consentId=d9b0f7b7-79d2-4452-9d2e-06b8adcd2297&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0004%3A1&AwaitingReconsent=false; _gcl_au=1.1.439176278.1643491206; __ssid=75a5e0e1f635f093614a72ef847b825; _fbp=fb.1.1643491207010.1913364210; _ga_CVPS3GXE1Z=GS1.1.1643574501.7.0.1643574502.59; _ga=GA1.2.408402920.1643491208; _gid=GA1.2.1183097106.1643491208; __gads=ID=256b6d491bc7321f-22b191b22fcd0072:T=1643491208:S=ALNI_MaqwVSBF2NcGlEBFhR71lAR1Xx-Gw; cto_bundle=6qF_RV8ybkpTSmdWVVpnWHpiV21xcnF2cGRsS1lWSDU3TEJFJTJCVmpwckp5WjBnd0hPU3pzeEklMkZQS241VWtWQThudTNRdGtyckVKd3VHbVdvcml6WkpQbFdvdnFIRjlLcExRanpxM0ZEV2RjY0Z6MERiYmhGS1BRRngyRU01VnZ5QWROV2tlZkxQS28lMkYzWlBXUXhTck9yOEZQd0ElM0QlM0Q; segIds=; st=a6330c14864804d82bfc3ed6bc9a64769246df2051666b30d2bc431cdec494de45ae441c919b51107aeec4e6eb8529ce31fe635dbc2e434b7; dp=1366*768-landscape; geoipCity=bursa; geoipIsp=turksat; _dc_gtm_UA-235070-1=1',
        'scheme': 'https',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'max-age=0'
        
}
#DOWNLOAD_TIMEOUT = 15080.93.212.44:3155
#ROTATING_PROXY_CLOSE_SPIDER=True  #When True, spider is stopped if there are no alive proxies. If False (default), then when there is no alive proxies all dead proxies are re-checked.
# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'sah.middlewares.SahSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
     'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
     'sah.middlewares.UserAgentRotatorMiddleware' : 400,
    # 'sah.middlewares.ProxyFunctions' : 399,
     'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 100,
     
      #'rotating_proxies.middlewares.RotatingProxyMiddleware': 1,
      'rotating_proxies.middlewares.BanDetectionMiddleware': 2
#     #'rentier_rotating_proxies.middlewares.RotatingProxyMiddleware': 100,
    #'rentier_rotating_proxies.middlewares.BanDetectionMiddleware': 101
    
}
#DOWNLOAD_DELAY = 5
#ROTATING_PROXY_LIST_PATH = "/home/draco/docs/scraping/scrapyyy/thomas/proxies_reorg.txt"
#NUMBER_OF_PROXIES_TO_FETCH = 30
#DNS_TIMEOUT = 10

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
    
   
#     'sah.pipelines.MongodbPipeline' :200

# }
# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
AUTOTHROTTLE_ENABLED = True
# The initial download delay
AUTOTHROTTLE_START_DELAY = 4
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 15
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
