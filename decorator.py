import time


def cache_decorator(func):
    cache_dict = {}

    def wrapper(*args, **kwargs):
        if not cache_dict.get(args):
            wrapper_function = func(*args, **kwargs)
            cache_dict[args] = wrapper_function
            return wrapper_function
        else:
            return cache_dict[args]

    return wrapper


@cache_decorator
def multiplier(number: int) -> int:
    return number * 2


def re_execution(call_count=1, start_sleep_time=0, factor=1, border_sleep_time=0):
    def decorator(func):
        def wrapper(*args, **kwargs):
            sleep_time = start_sleep_time

            for i in range(1, call_count + 1):
                result = func(*args, **kwargs)
                time.sleep(sleep_time)
                print(f'Запуск номер {i}. Ожидание: {sleep_time} секунд(ы).'
                      f' Результат декорируемой функций = {result}.')
                sleep_time *= factor
                if sleep_time >= border_sleep_time:
                    sleep_time = border_sleep_time
            return 'Конец работы'

        return wrapper

    return decorator


@re_execution(call_count=5, start_sleep_time=1, factor=2, border_sleep_time=200)
def add_ten(number: int) -> int:
    return number + 10


print(add_ten(2))
