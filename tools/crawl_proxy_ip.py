# -*- coding: utf-8 -*-
# @File  : crawl_proxy_ip.py
# @Author: LaoJu
# @Date  : 2019/2/12
# @Desc  :

import requests
import re
from scrapy.selector import Selector
import MySQLdb

conn = MySQLdb.connect(host="118.24.117.85", user="root", passwd="616632", db="article_spider", charset="utf8")
cursor = conn.cursor()


def crawl_ips():
    # 从https://raw.githubusercontent.com/fate0/proxylist/master/proxy.list爬取IP
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    }

    response = requests.get("https://raw.githubusercontent.com/fate0/proxylist/master/proxy.list", headers=headers)

    re_str = response.text
    ip_list = []
    for one_ip in re_str.split("\n"):
        if one_ip != None:
            match_ip = re.match('.*"host":\s"(.+?)",', one_ip)
            if match_ip:
                ip = match_ip.group(1)
            else:
                continue
            match_port = re.match('.*"port":\s?(.+?),', one_ip)
            if match_port:
                port = match_port.group(1)
            else:
                continue
            match_type = re.match('.*"type":\s?"(.+?)",', one_ip)
            if match_type:
                proxy_type = match_type.group(1)
            else:
                continue

            ip_list.append((ip, port, proxy_type))

    for ip_info in ip_list:
        cursor.execute(
            # values传递字符串要用单引号
            "INSERT INTO new_proxy_ip(ip,port,proxy_type) VALUES('{0}','{1}','{2}') ".format(ip_info[0],
                                                                                             ip_info[1],
                                                                                             ip_info[2])
        )

        conn.commit()


class GetIP(object):

    def delete_ip(self, ip):
        # 从数据库删除ip
        delete_sql = """
            delete from new_proxy_ip WHERE ip='{0}'
        """.format(ip)
        cursor.execute(delete_sql)
        conn.commit()
        return True

    def judge_ip(self, ip, port, proxy_type):
        # 判断IP是否可用
        http_url = "http://www.baidu.com/"
        proxy_url = "{0}://{1}:{2}".format(proxy_type.lower(), ip, port)
        try:
            proxy_dict = {
                "http": proxy_url,
                # "http": "http://43.245.218.156:50312",

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
            select ip,port,proxy_type from new_proxy_ip order BY RAND() limit 1
        """
        # random_sql = """
        #             select ip,port,proxy_type from new_proxy_ip WHERE ip='43.245.218.156'
        #         """
        result = cursor.execute(random_sql)
        for ip_info in cursor.fetchall():
            ip = ip_info[0]
            port = ip_info[1]
            proxy_type = ip_info[2]

            judge_re = self.judge_ip(ip, port, proxy_type)
            if judge_re:
                return "{0}://{1}:{2}".format(proxy_type.lower(), ip, port)
            else:
                return self.get_random_ip()


if __name__ == "__main__":
    get_ip = GetIP()
    get_ip.get_random_ip()
    # get_ip.judge_ip(1,2,3)
