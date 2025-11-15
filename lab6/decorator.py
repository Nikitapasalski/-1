def limit_calls(max_calls):
    def decorator(func):
        calls = 0

        def wrapper(*args, **kwargs):
            nonlocal calls
            if calls >= max_calls:
                raise Exception(f"Функція '{func.__name__}' більше не може бути викликана. Досягнуто ліміт: {max_calls}")
            calls += 1
            return func(*args, **kwargs)
        return wrapper
    return decorator
