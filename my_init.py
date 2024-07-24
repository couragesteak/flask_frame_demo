from env import Env
from src.main.util.util_log import Logger

app_path = Env().get_app_path()
# 程序日志
logger = Logger(f"{app_path}/log/app.log")
