# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import redis
import RedisQueue

redis_db = redis.Redis(host='localhost', port=6379, db=4)
redis_data_dict = "f_uuids"

# q = 

class StudyscrapyPipeline(object):
    
    def __init__(self):
        # self.q = RedisQueue(name='CSDN', host='localhost', port=6379, db=3)
        if redis_db.hlen(redis_data_dict) == 0:
            pass

    # s = set()
    def process_item(self, item, spider):
        fp = open(r'F:\Spider\Spider\studyscrapy\out.txt', 'a+')
        if redis_db.hexists(redis_data_dict, item['title']):
            print('数据已存入队列 <--')
            pass
        else:
            fp.write(item['title']+', '+item['time']+'\n')
            redis_db.hset(redis_data_dict,item['title'],item['time'])
            print('title: {0},time: {1} 存入队列成功'.format(item['title'],item['time']))
            
        return item
