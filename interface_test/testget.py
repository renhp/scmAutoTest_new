# 测试get请求事例
import json

import requests
import unittest


class TestClass(unittest.TestCase):

    def testGet(self):
        # header部分的配置
        headers = {
            'User-Agent': 'hlj-android/3.3.1',
            'Host': 'customer-api.helijia.com',
            'Connection': 'Keep-Alive',
            'Accept-Encoding': 'gzip'
        }

        # cookies部分的配置
        cookies = dict(
            beacon_id='MTAxLjI1MS4xOTUuMTE5LTE0',
            search_test='1',
            search_r='32'
        )

        # get请求的构造
        res = requests.get(
            "http://www.baidu.com",
            headers=headers,
            cookies=cookies
        )

        print(res.text)
        print(res.status_code)
        print(res.url)
        # rj = json.loads(res.text)  # 如果是json的话，将返回文本转换为json格式

        # self.assertTrue("url" in res.text)
        self.assertTrue("http://www.baidu.com", res.url)

if __name__ == "__main__":
    unittest.main()



