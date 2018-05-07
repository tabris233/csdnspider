# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


# import RedisQueue

# p = RedisQueue('CSDN', host='localhost', port=6379, db=3)

class StudyscrapyPipeline(object):
    # def __init__(self):
        
    #     self.post = p
        
    def process_item(self, item, spider):
        # info = dict(item)
        # self.post.insert(info)
        fp = open(r'F:\Spider\Spider\studyscrapy\out.txt', 'a+')
        fp.write(item['title']+'\n')
        fp.write(item['time']+'\n')
        
        return item
