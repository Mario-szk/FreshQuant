import threading
import importlib


def lock(func):
    """
    线程锁的装饰器
    :param func:
    :return:
    """
    func.__lock__ = threading.Lock()

    def wrapper(*args, **kwargs):
        with func.__lock__:
            return func(*args, **kwargs)
    return wrapper


def Singleton(cls):
    """
    线程安全的单例装饰器
    :param cls:
    :return:
    """
    __instances = {}

    @lock
    def wrapper(*args, **kw):
        if cls not in __instances:
            __instances[cls] = cls(*args, **kw)
        return __instances[cls]
    return wrapper


def load_clz_from_file(module_name, clz_name, path):
    module = importlib.machinery.SourceFileLoader(module_name, path).load_module()
    return getattr(module, clz_name)
