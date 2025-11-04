from module03_collections.namedtuple_demo import NamedTupleDemo
from module03_collections.deque_demo import DequeDemo
from module03_collections.counter_demo import CounterDemo
from module03_collections.ordereddict_demo import OrderedDictDemo
from module03_collections.defaultdict_demo import DefaultDictDemo
from module03_collections.chainmap_demo import ChainMapDemo

if __name__ == "__main__":
    print("=== NamedTuple Demo ===")
    NamedTupleDemo().demo()

    print("\n=== Deque Demo ===")
    DequeDemo().demo()

    print("\n=== Counter Demo ===")
    CounterDemo().demo()

    print("\n=== OrderedDict Demo ===")
    OrderedDictDemo().demo()

    print("\n=== DefaultDict Demo ===")
    DefaultDictDemo().demo()

    print("\n=== ChainMap Demo ===")
    ChainMapDemo().demo()
