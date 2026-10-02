from engine import Engine
from feature import feat
if '__name__' == '__main__':
    print("This is the main module.")
    engine = Engine(bot_settings={"name": "MyBot", "version": "1.0"})
    a, b = 9, 10
    res = feat(a, b)
    print(res)