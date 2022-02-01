import scrapy
import time
import random
#rom scrapy.utils.response import open_in_browser
class KurtulusSpider(scrapy.Spider):
    name = 'besiktas'
    allowed_domains = ['sahibinden.com']
    #start_urls = ['https://www.sahibinden.com/kiralik-daire?pagingOffset=40&address_quarter=22780&address_quarter=22781&address_district=4892&address_district=2023&address_district=2034&address_district=2033&address_district=2032&address_district=2031&address_district=2030&address_district=999051&address_district=2037&address_district=2026&address_district=999096&address_district=2036&address_district=2024&address_district=2035&address_district=4624&address_district=999029&address_town=427&address_city=34']
    
    def start_requests(self):
        ilk_link = 'https://www.sahibinden.com/kiralik-daire?pagingOffset=760&address_district=1952&address_district=1950&address_district=999113&address_district=1949&address_district=1948&address_district=1947&address_district=1946&address_district=1945&address_district=999027&address_district=1944&address_town=418&address_city=34'
        link_on = 'https://www.sahibinden.com/kiralik-daire?'
        deger = "pagingOffset="
        link_arka = '&address_district=1952&address_district=1950&address_district=999113&address_district=1949&address_district=1948&address_district=1947&address_district=1946&address_district=1945&address_district=999027&address_district=1944&address_town=418&address_city=34'
        sh = 0
        while True:
            
            
            sh += 1
            if sh == 1:
                link = ilk_link
                yield scrapy.Request(link, callback = self.parse)
            elif sh ==40:
                break
            else:
                link = link_on + deger + str((sh-1)*20) + link_arka
                print("Sayfa" +str(sh) +"açılıyor.")
               # randf = random.uniform(0.7, 1.2)
                #time.sleep(4.5*randf) 
                yield scrapy.Request(link, callback = self.parse)
    

    def parse(self, response):
        # nexttime.sleep(1) _page_p    ilan = entry.xpath('.//td[@class="searchResultsTitleValue leafContent"]/a/text()').get().strip()
        #         alan = entry.xpath('.//td[@class="searchResultsAttributeValue"][1]/text()').get().strip()
        #         odalar = entry.xpath('.//td[@class="searchResultsAttributeValue"][2]/text()').get().strip()
        #         fiyat = entry.xpath('.//td[@class="searchResultsPriceValue"]/div/text()').get().strip()
        #         mahalle = entry.xpath('.//td[@class="searchResultsLocationValue"]/text()').get().strip()
        #         art = response.xpath('//li/a[@class="prevNextBut"]/@href').get()
        # #print(response.body)
        
        data2 =response.xpath("//tbody/tr[@class='searchResultsItem     ']")
        data = response.xpath("//div[contains(@class,'content')]/ul/li")
        if data:

            for entry in data:
                try:
                    ilan = entry.xpath(".//h3/text()").get().strip()
                    fiyat = entry.xpath(".//h5/text()").get().strip()
                    mahalle = entry.xpath(".//h4/text()").get().strip()
                    link = entry.xpath(".//a/@href").get()
                except AttributeError:
                    print("Veri alınamadı.")

                #aşağıdaki değerler response'un içinde olmadığı için çıkarıldı.

                #alan = entry.xpath('.//td[@class="searchResultsAttributeValue"][1]/text()').get().strip()
                #odalar = entry.xpath('.//td[@class="searchResultsAttributeValue"][2]/text()').get().strip()
                

                try:
                    
                    yield {
                        'ilan': ilan,
                        #'alan': alan,
                        #'odalar': odalar,
                        'fiyat' : fiyat,
                        'mahalle': mahalle,
                        'user-agent': response.request.headers.get('User-Agent').decode('utf-8'),
                        'link' : link
                        
                    }
                except:
                    print("HATA KODU 1...")
        elif data2:
            for entry in data:
                ilan = entry.xpath('.//td[@class="searchResultsTitleValue leafContent"]/a/text()').get().strip()
                alan = entry.xpath('.//td[@class="searchResultsAttributeValue"][1]/text()').get().strip()
                odalar = entry.xpath('.//td[@class="searchResultsAttributeValue"][2]/text()').get().strip()
                fiyat = entry.xpath('.//td[@class="searchResultsPriceValue"]/div/text()').get().strip()
                mahalle = entry.xpath('.//td[@class="searchResultsLocationValue"]/text()').get().strip()

            try:

                yield {
                        'ilan': ilan,
                        'alan': alan,
                        'odalar': odalar,
                        'fiyat' : fiyat,
                        'mahalle': mahalle,
                        'user-agent': response.request.headers.get('User-Agent').decode('utf-8'),
                        'link' : link                
                }
            except:
                print("HATA KODU 2...")
        else:
            print("HATA KODU 3...")

          
        #if next_page_part is None:
        #    exit
            
           # yield scrapy.FormRequest(url=next_page,callback=self.parse,headers=formdata,dont_filter=False)
            

            
            

        