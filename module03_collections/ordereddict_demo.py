from collections import OrderedDict

class OrderedDictDemo:
    def demo(self):
        config = OrderedDict()
        config["db"] = "MySQL"
        config["host"] = "localhost"
        config["port"] = 3306
        config["user"] = "admin"
        print("Ordered Configuration:")
        for key, value in config.items():
            print(f"{key}: {value}")
