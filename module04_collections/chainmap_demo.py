from collections import ChainMap

class ChainMapDemo:
    def demo(self):
        from collections import ChainMap
        dic1 = {'a': 1, 'b': 2, 'c': 3,'y':90}
        dic2 = {'x': -1, 'y': -2, 'z': -3,'a':56}
        dic3 = {4: 4.2, 5: 9.0, 2: 6.1}
        cMap = ChainMap(dic1, dic2, dic3)
        print(f"The type of the {cMap} is {type(cMap)}")
        for k, v in cMap.items():
            print(f"{k}: {v}")

if __name__ == "__main__":
    print("\n=== ChainMap Demo ===")
    ChainMapDemo().demo()