import scrapy
from lmscraper.items import LmscraperItem
from scrapy.pipelines.images import ImagesPipeline

class LeroyMerlinSpider(scrapy.Spider):
    name = 'leroy_merlin'
    start_urls = ['https://leroymerlin.ru/catalogue/kraski-dlya-vnutrennih-rabot/']

    def parse(self, response):
        item = LmscraperItem()
        for products in response.css('div.phytpj4_plp'):
            item['name'] = products.css('span.t9jup0e_plp.p1h8lbu4_plp::text').get()
            item['price'] = products.css('p.t3y6ha_plp.xc1n09g_plp.p1q9hgmc_plp::text').get().replace('\xa0','')
            item['link'] = products.css('a.bex6mjh_plp.b1f5t594_plp.iypgduq_plp.nf842wf_plp').attrib['href']

            yield item

        def parseImages(self, response):
            for elem in response.xpath("//*[@id='root']/main/div[5]/div[2]/div/section/div[3]/section/div[1]/div[1]/a/span/picture/img"):
                img_url = elem.xpath("@src").extract_first()
                yield ImageItem(image_urls=[img_url])

        next_page = response.css('a.bex6mjh_plp.s15wh9uj_plp.l7pdtbg_plp.r1yi03lb_plp.sj1tk7s_plp').attrib['href']
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

    