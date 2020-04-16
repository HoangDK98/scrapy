import scrapy
import pymysql
# import cv2


class my_Spider(scrapy.Spider):

    name = 'info'             # this is namespider
    BASE_URL = 'https://mywork.com.vn'
    start_urls =[
        'https://mywork.com.vn'
        ]

# # conect to database mysql
#     try:
#         db = pymysql.connect(host="localhost",  # your host, usually localhost
#                              user="root",  # your username
#                              passwd="",  # your password
#                              db="scrapyinfo")
#     except:
#         print("Connect to database failse")
#
#     mycursor = db.cursor()


    def parse(self, response):
        for link1 in response.css('div.company_name p.j_title a::attr(href)').extract():
        # for link1 in response.css('div.company_name p.j_title a::attr(title)').extract():
            link2 = self.BASE_URL + link1
            yield scrapy.Request(link2, callback=self.parse_item)
            # yield {'link2':link2}
    def parse_item(self, response):
        # ---------------------------scrapy job------------------------------------
        for job in response.css('div.col-md-7 h1.main-title'):
            job1=job.css('span::text').extract_first().strip()
            if job1=="hot":
                job2=str(job.css('span::text').extract()).strip()
            else:
                job2=job1
        # ---------------------------scrapy name company------------------------------------

        for name_company in response.css('div.col-md-7 a.capitalize'):
            name_company1=name_company.css('span::text').extract_first().strip()
            # yield {'hi: ' : name_company1}
        # ---------------------------scrapy salary------------------------------------
        for salary in response.css('div.col-md-7 p span.text_red'):
            salary1=str(salary.css('.text_red::text').extract_first()).strip()
        #---------------------------scrapy require------------------------------------
        for necessary in response.css('div.job_detail_general'):
            necessary1 = str(necessary.css('strong::text').extract()).strip()
            necessary2 = str(necessary.css('p::text').extract()).strip()
            necessary3=necessary1+necessary2
        yield {"công viêc : ": job2,"tên ct :":name_company1,"lương : ":salary1,'necessary : ':necessary3}

        # for job_description in response.css('div.mw-box-item'):
        #     job_description1=str(job_description.css('.mw-box-item::text').extract())
        #     yield {"hihi : ": job_description1}



        # for benefit in response.css('div.col-md-7 p span.text_red'):
        #     benefit1=str(benefit.css('.text_red::text').extract_first()).strip()
        # for job_requirements in response.css('div.col-md-7 p span.text_red'):
        #     job_requirements1=str(job_requirements.css('.text_red::text').extract_first()).strip()

        # yield {"công viêc : ": job2,"tên ct :":name_company1,"lương : ":salary1}
        # self.mycursor.execute("INSERT INTO findwork("+cols+") VALUES (%s,%s,%s)",(vals))
        # self.db.commit()

        # -----------------------scrapy require-------------------------------------
        # for require in response.css('div.col-md-7 p span.text_red'):
        #     require1 = str(require.css('.text_red::text').extract_first()).strip()
        #     yield {"": require1}
        #     # self.insert_database('findwork', 'require', require1)

#---------Way run terminal : scrapy crawl 'namespider' . if you want to write file turn yield and run add '-o 'namefile.csv'---------'






