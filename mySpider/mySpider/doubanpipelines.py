from cmdb.models import DouBanMovie
import pymysql

class DoubanPipeline(object):
    name="douban"
    author_name = "author"
    insertSql = "insert into cmdb_doubanmovie(title, score, content, info) values ('${title}','${score}','${content}','${info}')"
    def __init__(self, settings):
        self.settings = settings
    def process_item(self, item, spider):
        if spider.name == "douban":
            sqltext = self.insertSql.format(title=pymysql.escape_string(item['title']),
            score=pymysql.escape_string(item['score']),
            content=pymysql.escape_string(item['content']),
            info=pymysql.escape_string(item['info']))
            self.cursor.execute(sqltext)
        else:
            spider.log("Undefined name:%s" % spider.name)
        return item
    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings)
    def open_spider(self, spider):
        self.connect=pymysql.connect(host=self.settings.get("MYSQL_HOST"),
                                     db=self.settings.get("MYSQL_DBNAME"),
                                     user=self.settings.get("MYSQL_USER"),
                                     passwd=self.settings.get("MYSQL_PASSWD"))
        self.cursor = self


