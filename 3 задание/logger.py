
from datetime import datetime


def logger(path):
    def __logger(old_function):
        def new_function(*args, **kwargs):
            call_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            result = old_function(*args, **kwargs)
            args_repr = [repr(arg) for arg in args]
            kwargs_repr = [f"{k}={repr(v)}" for k, v in kwargs.items()]
            signature = ", ".join(args_repr + kwargs_repr)
            log_line = f"{call_time} - {old_function.__name__}({signature}) -> {repr(result)}"
            with open(path, 'a', encoding='utf-8') as log_file:
                log_file.write(log_line + '\n')
            return result
        return new_function
    return __logger


