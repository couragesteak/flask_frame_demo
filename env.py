class Env:
    def __init__(self):
        # 运行环境（可修改）
        # self.app_env = "dev"
        # self.app_env = "test"
        self.app_env = "pro"

        # 环境对应路径 （可修改）
        self.app_path_dev = "D:/dev/cs/flask_frame_demo"
        self.app_path_test = "D:/dev/cs/flask_frame_demo"
        self.app_path_pro = "D:/dev/cs/flask_frame_demo"

    def get_app_env(self):
        return self.app_env

    def get_app_path(self):
        if self.app_env == "pro":
            return self.app_path_pro
        if self.app_env == "test":
            return self.app_path_test
        if self.app_env == "dev":
            return self.app_path_dev
        return self.app_path_dev
