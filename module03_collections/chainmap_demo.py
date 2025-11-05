from collections import ChainMap

class ChainMapDemo:
    def demo(self):
        defaults = {"theme": "light", "show_line_numbers": True}
        user_settings = {"theme": "dark","k":9}
        system_settings = {"show_line_numbers": False,"k":10}
        combined = ChainMap(user_settings, system_settings, defaults)
        print("Final Settings (with priority):")
        for k, v in combined.items():
            print(f"{k}: {v}")

if __name__ == "__main__":
    print("\n=== ChainMap Demo ===")
    ChainMapDemo().demo()