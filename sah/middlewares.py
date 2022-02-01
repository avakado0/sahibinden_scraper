# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from scrapy.downloadermiddlewares.useragent import UserAgentMiddleware
import random, logging



class UserAgentRotatorMiddleware(UserAgentMiddleware):
    user_agents_list = [
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36 OPR/A941241C5628D",
        "Mozilla/5.0 (Linux; U; Android 9; en-in; Redmi 7 Build/PKQ1.181021.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/79.0.3945.147 Mobile Safari/537.36 XiaoMi/MiuiBrowser/12.9.3-gn",
        "Mozilla/5.0 (Linux; Android 10; V2029 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.101 Mobile Safari/537.36 GSA/12.22.8.23.arm64",
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36 Ionic/2.16.8",
        "Mozilla/5.0 (Linux; Android 10; JSN-L21 Build/HONORJSN-L21; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.101 Mobile Safari/537.36 GSA/12.22.8.23.arm64",
        "Mozilla/5.0 (Linux; Android 9; BQ-5731L) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 10; HRY-LX1T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Mobile Safari/537.36 Atom/1.4.1.54",
        "Safari/537.36 Ionic/2.16.8",
        "Mozilla/5.0 (Linux; Android 10; JSN-L21 Build/HONORJSN-L21; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.101 Mobile Safari/537.36 GSA/12.22.8.23.arm64",
        "Mozilla/5.0 (Linux; Android 9; BQ-5731L) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 10; HRY-LX1T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Mobile Safari/537.36 Atom/1.4.1.54",
        "Mozilla/5.0 (Windows NT 6.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/8C268E",
        "Mozilla/5.0 (Windows NT 6.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/BB3E2C",
        "Mozilla/5.0 (Linux; U; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4183.127 Mobile Safari/537.36 OPR/55.1.2254.56965",
        "Mozilla/5.0 (Linux; arm_64; Android 10; MAR-LX1H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.216 YaBrowser/21.5.1.107.00 SA/3 Mobile Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4545.0 Safari/537.36",
        "Mozilla/5.0 (Linux; Android 10; HD1905) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.91 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 9; arm_64; BV6900) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 YaBrowser/20.7.1.60.00 SA/3 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 8.1.0; DUA-L22 Build/HONORDUA-L22; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.101 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 10; ASUS_Z00LD) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.210 Mobile Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2653.75 Safari/537.36",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.2; .NET CLR 2.5.36082)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.2; .NET CLR 2.2.22499)",
        "Mozilla/5.0 (Linux; arm; Android 11; SM-A115F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.216 YaApp_Android/21.51.1 YaSearchBrowser/21.51.1 BroPP/1.0 SA/3 TA/7.1 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; arm_64; Android 9; ZTE Blade V10 Vita RU) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 YaBrowser/21.3.4.59.00 SA/3 TA/7.1 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 7.0; SM-J730F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; arm_64; Android 9; PAR-LX1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 YaApp_Android/21.50.1 YaSearchBrowser/21.50.1 BroPP/1.0 SA/3 TA/7.1 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; arm_64; Android 10; HRY-LX1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.216 YaApp_Android/21.51.1 YaSearchBrowser/21.51.1 BroPP/1.0 SA/3 TA/7.1 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; U; Android 7.1.2; uk-ua; Redmi 4A Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/79.0.3945.147 Mobile Safari/537.36 XiaoMi/MiuiBrowser/12.10.5-go",
        "Mozilla/5.0 (Linux; Android 7.1.1; SM-A7100) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; arm_64; Android 9; SM-G955F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.216 YaBrowser/21.5.1.107.00 SA/3 TA/7.1 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; arm; Android 6.0.1; SM-G532F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 YaApp_Android/21.34.1 YaSearchBrowser/21.34.1 BroPP/1.0 SA/3 TA/7.1 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; arm; Android 6.0.1; SM-G532F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 YaApp_Android/21.34.1 YaSearchBrowser/21.34.1 BroPP/1.0 SA/3 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; arm; Android 10; SM-J400F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.216 YaApp_Android/21.51.1 YaSearchBrowser/21.51.1 BroPP/1.0 SA/3 TA/7.1 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; arm_64; Android 10; Redmi Note 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 YaBrowser/21.3.4.59.00 SA/3 TA/7.1 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; arm_64; Android 10; Redmi Note 9 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.216 YaBrowser/21.5.1.107.00 SA/3 TA/7.1 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; arm_64; Android 10; JSN-L21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.216 YaApp_Android/21.51.1 YaSearchBrowser/21.51.1 BroPP/1.0 SA/3 TA/7.1 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 8.0.0; WAS-TL10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 8.0.0; SM-J400F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.88 Mobile Safari/537.36",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 YaBrowser/21.5.2.927.10 SA/3 TA/6.1 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (Linux; Android 7.0; SM-G570F Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.101 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; arm_64; Android 9; FIG-LX1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 YaBrowser/21.3.1.128.00 SA/3 TA/7.1 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; arm_64; Android 9; Mi 9 Lite) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.216 YaBrowser/21.5.1.107.00 SA/3 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; arm_64; Android 9; Mi 9 Lite) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.216 YaBrowser/21.5.1.107.00 SA/3 TA/7.1 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; arm_64; Android 10; Redmi Note 9S) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.216 YaBrowser/21.5.1.107.00 SA/3 TA/7.1 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; arm_64; Android 9; SM-A307FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.216 YaApp_Android/21.51.1 YaSearchBrowser/21.51.1 BroPP/1.0 SA/3 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; arm_64; Android 9; SM-A307FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.216 YaApp_Android/21.51.1 YaSearchBrowser/21.51.1 BroPP/1.0 SA/3 TA/7.1 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; arm_64; Android 10; SM-A750FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.216 YaBrowser/21.5.1.107.00 SA/3 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; arm_64; Android 10; SM-A750FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.216 YaBrowser/21.5.1.107.00 SA/3 TA/7.1 Mobile Safari/537.36"

        ]
    def __init__(self, user_agent=""):
        self.user_agent = user_agent
    def process_request(self, request, spider):
        try:
            self.user_agent = random.choice(self.user_agents_list)
            request.headers.setdefault('User-Agent', self.user_agent)
        except IndexError:
            logging.error("USER_AGENT alınamadı...")    
            




# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter


class SahSpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class SahDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
