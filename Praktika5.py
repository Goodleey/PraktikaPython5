import time
# декаратор времени
def time_this(NUM_RUNS=n): # число прогонов функции(n)
    def decorator(func): # декаратор, который принимает в значение другую функцию
        def func(*args, **kwargs): # нам не известно, сколько и какие будут аргументы у функции
            avg = 0
            for i in range(NUM_RUNS):
                t0 = time.time() # начальное время
                func(*args, **kwargs) # тут выполняется наша функция(или полезный код функции)
                t1 = time.time() # конечное время
                avg += (t1 - t0) # конечное - начальное 
            avg /= NUM_RUNS
            fn = func.__name__
            print("среднее время выполнения", fn)
            print("Количество запусков ", NUM_RUNS)
            print(avg)
        return func

    return decorator