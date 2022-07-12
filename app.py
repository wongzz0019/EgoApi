# 定义全局变量
import os.path

# 项目根目录
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# ego微商服务器域名
BASE_URL = "http://www.myego.com:13140"
# 注意令牌可能会失效，使用code之后，获取的令牌，手动获取
TOKEN = "bd8f3599604107c0deebe15d84a"
HEADERS = {"Content-Type": "application/json"}
# code是手动从微信小程序前端获取的
CODE = "013zDSZm0UibDn1wz125s4d56"