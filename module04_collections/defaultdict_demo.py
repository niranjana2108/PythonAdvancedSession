from collections import defaultdict

class DefaultDictDemo:
    def demo(self):
        dDic = defaultdict(lambda: 0)
        dDic[1] = 2
        dDic[3] = 4
        dDic[5] = 6
        print(dDic[1])
        print(dDic[7])


if __name__ == "__main__":
    print("\n=== DefaultDict Demo ===")
    DefaultDictDemo().demo()