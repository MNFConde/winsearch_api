class singleton:
    def __init__(self, cls):
        self._cls = cls

    def __call__(self, *args, **kwargs):
        if not hasattr(self, "_instance"):
            self._instance = self._cls(*args, **kwargs)
        return self._instance

    def __instancecheck__(self, instance):
        return isinstance(instance, self._cls)

if __name__ == '__main__':
    @singleton
    class A:
        def __init__(self, a):
            self.a = a

    a1 = A(1)
    a2 = A(2)
    a3 = A(1)
    print(a1.a, a2.a, a3.a)
    print(a1 is a2, a1 is a3)