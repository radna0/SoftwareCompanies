import time
from EdmondsKarp import EdmondsKarp
from pushRelabel import PushRelabel
from Dijkstra import Dijkstra
from BFS import BFS

testcase1 = {
    'names': ["topcoder", "doodle", "nasa", "ninny", "idm", "noname", "kintel"],
    'process': ["doodle nasa noname", "idm ninny noname", "idm ninny noname", "kintel", "kintel", "", ""],
    'cost': [1, 2, 7, 4, 6, 1, 2],
    'amount': [50, 10, 11, 9, 14, 11, 23],
    'company1': 'topcoder',
    'company2': 'kintel',
}
testcase2 = {
    'names': ["b", "bz", "ba", "d", "z", "ca", "y", "a", "x"],
    'process': ["bz ba z ca", "ba", "d", "", "ca", "d", "a", "x", ""],
    'cost': [5, 5, 5, 10, 6, 6, 3, 0, 3],
    'amount': [10, 7, 10, 9, 6, 9, 23, 13, 11],
    'company1': "b",
    'company2': "d",
}
testcase3 = {
    'names': ["b", "bz", "ba", "d", "z", "ca", "y", "a", "x"],
    'process': ["bz ba z ca", "ba", "d", "", "ca", "d", "a", "x", ""],
    'cost': [5, 5, 5, 10, 6, 6, 3, 1, 3],
    'amount': [10, 7, 10, 9, 6, 9, 23, 13, 11],
    'company1': "b",
    'company2':  "d",
}
testcase4 = {
    'names': ["coma", "comb", "comc", "comd"],
    'process': ["comb", "coma", "comd", "comc"],
    'cost': [10, 54, 18, 93],
    'amount': [10, 10, 10, 10],
    'company1': "comb",
    'company2': "comc",
}
testcase5 = {
    'names': ["c", "b", "a"],
    'process': ["b", "c", ""],
    'cost': [1, 1, 0],
    'amount': [1, 1, 22],
    'company1': "c",
    'company2': "b",
}
testcase6 = {
    'names': ["x", "y", "z", "t", "u", "w", "s", "r", "q", "p", "o", "k"],
    'process': ["y", "z", "t", "u", "w", "s", "r", "q", "p", "o", "k", ""],
    'cost': [1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000],
    'amount': [1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000],
    'company1': "x",
    'company2': "k",
}


# EdmondsKarp
if True:
    s1 = EdmondsKarp()
    start = time.time()
    print(s1.produceData(**testcase1) ==
          ["doodle", "idm", "kintel", "nasa", "ninny", "topcoder"])
    print(s1.produceData(**testcase2) == ["a", "b", "ba", "d"])
    print(s1.produceData(**testcase3) == ["b", "ba", "d"])
    print(s1.produceData(**testcase4) == [])
    print(s1.produceData(**testcase5) == ["a", "b", "c"])
    print(s1.produceData(**testcase6) ==
          ["k", "o", "p", "q", "r", "s", "t", "u", "w", "x", "y", "z"])
    end = time.time()
    print("EdmondsKarp: ", end - start)

# PushRelabel
if False:
    s2 = PushRelabel()
    start = time.time()

    print(s2.produceData(**testcase1) ==
          ["doodle", "idm", "kintel", "nasa", "ninny", "topcoder"])
    print(s2.produceData(**testcase2) == ["a", "b", "ba", "d"])
    print(s2.produceData(**testcase3) == ["b", "ba", "d"])
    print(s2.produceData(**testcase4) == [])
    print(s2.produceData(**testcase5) == ["a", "b", "c"])
    print(s2.produceData(**testcase6) ==
          ["k", "o", "p", "q", "r", "s", "t", "u", "w", "x", "y", "z"])

    end = time.time()
    print("PushRelabel: ", end - start)

# Dijkstra
if True:
    s2 = Dijkstra()
    start = time.time()

    print(s2.produceData(**testcase1) ==
          ["doodle", "idm", "kintel", "nasa", "ninny", "topcoder"])
    print(s2.produceData(**testcase2) == ["a", "b", "ba", "d"])
    print(s2.produceData(**testcase3) == ["b", "ba", "d"])
    print(s2.produceData(**testcase4) == [])
    print(s2.produceData(**testcase5) == ["a", "b", "c"])
    print(s2.produceData(**testcase6) ==
          ["k", "o", "p", "q", "r", "s", "t", "u", "w", "x", "y", "z"])

    end = time.time()
    print("Dijkstra: ", end - start)

# BFS
if True:
    s2 = BFS()
    start = time.time()

    print(s2.produceData(**testcase1) ==
          ["doodle", "idm", "kintel", "nasa", "ninny", "topcoder"])
    print(s2.produceData(**testcase2) == ["a", "b", "ba", "d"])
    print(s2.produceData(**testcase3) == ["b", "ba", "d"])
    print(s2.produceData(**testcase4) == [])
    print(s2.produceData(**testcase5) == ["a", "b", "c"])
    print(s2.produceData(**testcase6) ==
          ["k", "o", "p", "q", "r", "s", "t", "u", "w", "x", "y", "z"])

    end = time.time()
    print("BFS: ", end - start)
