import scrapy
import click
class LozaSpider(scrapy.Spider):
    name = "img"
    URL='https://loza.vn'
    start_urls = [
      "https://loza.vn/ao-so-mi-nu"
      # "https://loza.vn/quan-cong-so-nu",
      # "https://loza.vn/vay-dam",
      # "https://loza.vn/chan-vay",
      # "https://loza.vn/vest-nu",
      # "https://loza.vn/ao-khoac-nu",
      # "https://loza.vn/set-do",
      # "https://loza.vn/thoi-trang-dao-pho"
    ]

    def parse(self, response):

        for item_link in response.css("div.col-6 a.image-cover::attr(href)").extract():
            cover_link=self.URL+item_link
            self.log("-------------------------------------------------------------")
            self.log("cover_link :" + cover_link)
            yield scrapy.Request(cover_link, callback=self.parse_single_item)

    def parse_single_item(self, response):
        for link in response.css('div.box-image a img').xpath('@src').extract():
            img_link = link.replace("thumbnail/200x280", "image/1000x")
            yield scrapy.Request(img_link, callback=self.parse_img)

    def parse_img(self, response):
        # self.log("link : " + response.url.split('/')[-1])
        with open("img/%s" % response.url.split('/')[-1].split('?')[-2], 'wb') as f:
            f.write(response.body)

    # def parse_img(self, response):
    #     page = response.url.split("/")[-1]
    #     filename = 'img-%s' % page
    #     with open(filename, 'wb') as f:
    #         f.write(response.body)
    #     self.log('Saved file %s' % filename)