from collections import defaultdict

class DefaultDictDemo:
    def demo(self):
        logs = [("error", "404"), ("info", "startup"), ("error", "500"), ("info", "connected")]
        log_dict = defaultdict(list)
        for level, message in logs:
            log_dict[level].append(message)
        print("Grouped Logs:")
        for level, messages in log_dict.items():
            print(f"{level}: {messages}")
