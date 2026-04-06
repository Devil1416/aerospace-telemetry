import random
def run():
    print('module: aerospace-telemetry')
    data = [random.random() for _ in range(10)]
    print('avg:', sum(data)/len(data))
