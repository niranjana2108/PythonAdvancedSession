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

        grades = defaultdict(list)
        grades['math'].append(95)
        grades['science'].append(88)
        grades['english'].append(92)
        print(grades['social'])
        print(grades)


if __name__ == "__main__":
    print("\n=== DefaultDict Demo ===")
    DefaultDictDemo().demo()