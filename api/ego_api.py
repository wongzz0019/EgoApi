# 封装被测系统的接口

# 使用requests
import requests

import app


class EgoApi:

    def __init__(self):
        self.banner_url = app.BASE_URL + "/api/v1/banner/1"
        self.theme_url = app.BASE_URL + "/api/v1/theme"
        self.recent_goods_url = app.BASE_URL + "/api/v1/product/recent"
        self.token_url = app.BASE_URL + "/api/v1/token/user"
        self.address_url = app.BASE_URL + "/api/v1/address"
        self.verify_token_url = app.BASE_URL + "/api/v1/token/verify"
        self.orderlist_url = app.BASE_URL + "/api/v1/order/by_user"
        self.create_order_url = app.BASE_URL + "/api/v1/order"
        self.query_order_url = app.BASE_URL + "/api/v1/order"
        self.category_url = app.BASE_URL + "/api/v1/category/all"
        self.by_category_url = app.BASE_URL + "/api/v1/product/by_category"
        self.product_detail_url = app.BASE_URL + "/api/v1/product"

    # 获取轮播图
    def get_banner(self):
        return requests.get(url=self.banner_url)

    # 获取专题栏位
    def get_theme(self, ids):
        # url = self.banner_url + "?" + ids
        # return requests.get(url=self.theme_url, params=ids)
        return requests.get(url=self.theme_url, params={"ids": ids})

    # 获取最近新品
    def get_recent_goods(self):
        return requests.get(url=self.recent_goods_url)

    # 获取令牌
    def get_token(self, headers, json):
        return requests.post(url=self.token_url, headers=headers, json=json)

    # 获取地址
    def get_address(self, headers):
        return requests.get(url=self.address_url, headers=headers)

    # 验证令牌是否有效
    def verify_token(self, json):
        return requests.post(url=self.verify_token_url, json=json)

    # 封装获取用户订单列表(需要token验证，token在headers中)   params= 参数自动加？  传入参数时要这样写 "page=1"
    def get_user_orderlist(self, headers,  page):
        return requests.get(url=self.orderlist_url, params=page, headers=headers)

    # 封装创建订单接口
    def create_order(self, headers, json):
        return requests.post(url=self.create_order_url, headers=headers, json=json)

    # 封装查看订单接口
    def query_order(self, headers, order_id):
        query_order_url = self.query_order_url + "/" + order_id
        return requests.get(url=query_order_url, headers=headers)

    # 获取商品分类
    def get_product_category(self):
        return requests.get(url=self.category_url)

    # 获取商品分类下的某个商品
    def by_category(self, params):
        return requests.get(url=self.by_category_url, params={"id":params})

    # 获取商品信息
    def get_product_detail(self, product_id):
        url = self.product_detail_url + "/" + product_id
        return requests.get(url=url)



if __name__ == '__main__':
    ego_api = EgoApi()  # 实例化类对象
    response = ego_api.get_banner()  # 调用类中的方法（轮播图接口）
    print(response.json())  # 打印轮播图的结果


    # response = ego_api.get_theme("ids=1,2,3")
    response = ego_api.get_theme("1,2,3")
    print(response.json())


    response = ego_api.get_recent_goods()
    print("最近新品:", response.json())


    response = ego_api.get_token(app.HEADERS, {"code": app.CODE})
    print("获取的令牌为：", response.json())


    print('更新前的app.HEADERS:', app.HEADERS)
    app.HEADERS['token'] = '7654asd465d2sd1fds5465f'
    print('更新之后的app.HEADERS:', app.HEADERS)
    response = ego_api.get_address(app.HEADERS)
    print("使用令牌后，获取地址的信息为：", response.json())


    response = ego_api.verify_token({"token": "bd8f3599604107c0deebe15d84a"})
    print("验证令牌的结果为：", response.json())


    app.HEADERS['token'] = '7654asd465d2sd1fds5465f'  # 更新token
    response = ego_api.get_user_orderlist(app.HEADERS, "page=1")
    print("获取用户订单列表为：", response.json())


    app.HEADERS['token'] = '7654asd465d2sd1fds5465f'  # 若token失效就更新token
    response = ego_api.create_order(app.HEADERS, {"products":[{"product_id":8,"count":1},{"product_id":10,"count":2}]})
    print("创建订单的结果为：", response.json())


    app.HEADERS['token'] = '7654asd465d2sd1fds5465f'  # 若token失效就更新token
    response = ego_api.query_order(app.HEADERS, "110")
    print("查看订单为：",response.json())


    response = ego_api.get_product_category()
    print("商品分类为:", response.json())


    response = ego_api.by_category("5")
    print("商品分类下某个商品为：", response.json())

    response = ego_api.get_product_detail("11")
    print("商品信息为：", response.json())