from typing import Any


class singleton:
    def __init__(self, cls):
        self._cls = cls

    def __call__(self, *args, **kwargs):
        if not hasattr(self, "_instance"):
            self._instance = self._cls(*args, **kwargs)
        return self._instance

    def __instancecheck__(self, instance):
        return isinstance(instance, self._cls)


class singleton_args:
    def __init__(self, cls):
        self._cls = cls
        self._instances: dict[tuple, Any] = {}

    def __call__(self, *args, **kwargs):
        # 获取函数的参数默认值，不然无法提取默认值的情况
        import inspect

        sig = inspect.signature(self._cls.__init__)
        bound_args = sig.bind_partial(*args, **kwargs)
        bound_args.apply_defaults()

        # 创建包含默认值的完整参数键
        key = tuple(sorted(bound_args.arguments.items()))

        if key not in self._instances:
            self._instances[key] = self._cls(*args, **kwargs)
        return self._instances[key]

    def __instancecheck__(self, instance):
        return isinstance(instance, self._cls)


if __name__ == "__main__":

    @singleton
    class A:
        def __init__(self, a):
            self.a = a

    a1 = A(1)
    a2 = A(2)
    a3 = A(1)
    print(a1.a, a2.a, a3.a)
    print(a1 is a2, a1 is a3)

    @singleton_args
    class B:
        def __init__(self, x, y=0):
            self.x = x
            self.y = y

    a1 = B(1)  # 创建新实例
    a2 = B(1)  # 返回相同实例
    a3 = B(2)  # 创建新实例
    a4 = B(1, y=0)  # 返回与a1相同的实例
    a5 = B(1, y=1)  # 创建新实例

    print(a1 is a2)  # True
    print(a1 is a3)  # False
    print(a1 is a4)  # True
    print(a1 is a5)  # False
