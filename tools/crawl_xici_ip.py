# -*- coding: utf-8 -*-
# @File  : crawl_xici_ip.py
# @Author: LaoJu
# @Date  : 2019/2/10
# @Desc  :

import requests
from scrapy.selector import Selector
import MySQLdb

conn = MySQLdb.connect(host="118.24.117.85", user="root", passwd="616632", db="article_spider", charset="utf8")
cursor = conn.cursor()


def crawl_ips():
    # 爬取西刺的免费IP
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    }

    # 遍历爬取3000页
    for i in range(3000):
        re = requests.get("https://www.xicidaili.com/nn/{0}".format(i), headers=headers)

        selector = Selector(text=re.text)
        all_trs = selector.css("#ip_list tr")

        ip_list = []
        # 提取IP
        for tr in all_trs[1:]:  # 去掉表头的tr
            # 提取速度
            speed_str = tr.css(".bar::attr(title)").extract()[0]
            if speed_str:
                # 去掉"秒"字
                speed = float(speed_str.split("秒")[0])

            all_texts = tr.css("td::text").extract()
            ip = all_texts[0]
            port = all_texts[1]
            proxy_type = all_texts[5]

            ip_list.append((ip, port, proxy_type, speed))

        # 把每一页存入数据库
        for ip_info in ip_list:
            cursor.execute(
                # values传递字符串要用单引号
                "INSERT INTO proxy_ip(ip,port,speed,proxy_type) VALUES('{0}','{1}',{2},'{3}') ".format(ip_info[0],
                                                                                                       ip_info[1],
                                                                                                       ip_info[3],
                                                                                                       ip_info[2], )
            )

            conn.commit()


class GetIP(object):

    def delete_ip(self, ip):
        #从数据库删除ip
        delete_sql = """
            delete from proxy_ip WHERE ip='{0}'
        """.format(ip)
        cursor.execute(delete_sql)
        conn.commit()
        return True

    def judge_ip(self, ip, port,proxy_type):
        # 判断IP是否可用
        http_url = "http://www.jobbole.com/"
        # proxy_url = "{0}://{1}:{2}".format(proxy_type.lower(),ip, port)
        try:
            proxy_dict = {
                # "http": proxy_url,
                "http": "http://43.245.218.156:50312",

            }
            response = requests.get(http_url, proxies=proxy_dict)

        except Exception as e:
            print("invalid ip and port")
            self.delete_ip(ip)
            return False
        else:
            code = response.status_code
            if code >= 200 and code <= 300:
                print("effective ip")
                return True
            else:
                print("invalid ip and port")
                self.delete_ip(ip)
                return False

    def get_random_ip(self):
        # 从数据库随机取一个可用IP
        random_sql = """
            select ip,port,proxy_type from proxy_ip order BY RAND() limit 1
        """
        result = cursor.execute(random_sql)
        for ip_info in cursor.fetchall():
            ip = ip_info[0]
            port = ip_info[1]
            proxy_type = ip_info[2]

            self.judge_ip(ip,port,proxy_type)


# print(crawl_ips())

get_ip = GetIP()
# get_ip.get_random_ip()
get_ip.judge_ip(1,2,3)

