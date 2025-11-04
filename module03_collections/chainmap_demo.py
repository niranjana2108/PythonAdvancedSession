from collections import ChainMap

class ChainMapDemo:
    def demo(self):
        defaults = {"theme": "light", "show_line_numbers": True}
        user_settings = {"theme": "dark"}
        system_settings = {"show_line_numbers": False}
        combined = ChainMap(user_settings, system_settings, defaults)
        print("Final Settings (with priority):")
        for k, v in combined.items():
            print(f"{k}: {v}")
