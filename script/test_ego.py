# 导包
import pytest
import logging

import unittest
import app
from api.ego_api import EgoApi
from config.yaml_load import load_yaml


class TestEgo(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # 实例化封装EgoApi类
        cls.ego_api = EgoApi()

    def setup(self):
        app.HEADERS['token'] = "bd8f3599604107c0deebe15d84a"

    def test_get_banner_success(self):
        # 使用实例化的ego_api发送获取轮播图的接口请求
        response = self.ego_api.get_banner()
        # 打印响应数据
        logging.info("获取轮播图的测试结果为:{}".format(response.json()))
        # 断言结果
        assert response.status_code == 200  # 断言响应状态码是不是200
        assert "首页轮播图" == response.json().get("description")

    def test_get_theme_success(self):
        response = self.ego_api.get_theme("1,2,3")
        logging.info("测试获取的专题栏位为:{}".format(response.json()))
        assert response.status_code == 200
        logging.info('response.json()[0].get("description")的结果为：{}'.format(response.json()[0].get("description")))
        assert response.json()[0].get("description") == '美味水果世界'  # 断言返回数据中的description

    def test_get_recent_goods(self):
        response = self.ego_api.get_recent_goods()
        logging.info("测试获取最近新品接口：{}".format(response.json()))
        assert response.status_code == 200
        logging.info('response.json()[0].get("name"):{}'.format(response.json()[0].get("name")))
        assert response.json()[0].get("name") == '芹菜 半斤'

    def test_get_goods_category(self):
        # 发送获取商品分类的接口请求
        response = self.ego_api.get_product_category()
        logging.info("获取商品分类为：{}".format(response.json()))
        assert response.json()[0].get('name') == '果味'

    # @pytest.mark.parametrize('data', load_yaml('../data/data.yaml'))
    def test_get_category_any_goods(self):
        # 发送获取商品分类下的商品接口请求
        response = self.ego_api.by_category('1')
        logging.info("获取商品分类下的商品接口请求结果为:{}".format(response.json()))
        assert response.status_code == 200
        assert response.json()[0].get("name") == "梨花带雨 3个"

    def test_get_goods_detail(self):
        # 发送获取商品详情的接口请求
        response = self.ego_api.get_product_detail("32")
        logging.info("获取商品详情接口的结果为：{}".format(response.json()))
        assert response.status_code == 200
        assert response.json().get("name") == "土豆 半斤"

    def test_get_token(self):
        # 发送获取token的接口请求
        response = self.ego_api.get_token(app.HEADERS,
                                          {"code":"013zDSZm0UibDn1wz125s4d56"})
        logging.info("获取的token为：{}".format(response.json()))
        assert response.status_code == 200
        logging.info("response.json().get('token'):{}".format(response.json().get("token")))
        assert response.json().get("token") # 断言获取的token是否存在

    def test_verify_token(self):
        # 发送验证token的接口请求
        response = self.ego_api.verify_token(app.HEADERS)
        logging.info("验证的结果为:{}".format(response.json()))
        assert response.status_code == 200
        assert response.json().get("isValid") # 断言响应数据中有没有isValid

    def test_get_user_orderlist(self):
        # 发送获取用户订单列表的接口请求
        response = self.ego_api.get_user_orderlist(app.HEADERS, "page=1")
        logging.info("获取用户订单列表的结果为：{}".format(response.json()))
        assert response.status_code == 200
        assert response.json().get('data')[0].get('snap_name') == '夏日芒果'


#
# if __name__ == '__main__':
#     pytest.main(['-s', 'test_ego.py'])
