# 执行测试套件的入口
# 导包
import unittest

import HtmlTestRunner

import app
from script.test_ego import TestEgo

# 创建测试套件
suite = unittest.TestSuite()
# 将测试用例添加到测试套件
suite.addTest(unittest.makeSuite(TestEgo))
# 定义测试用例报告的名称
reportname = app.BASE_URL + "/report/mini_ego.html"
# 使用HTMLTestRunner生成测试报告
with open(reportname, mode="wb") as f:
    # 实例化HTMLTestRunner
    runner = HtmlTestRunner.HTMLTestRunner(f, verbosity=2, report_title="Ego商城接口测试报告")
    # 使用runner运行测试套件
    runner.run(suite)
