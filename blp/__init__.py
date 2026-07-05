try:
    from .BLP2PNG.BLP2PNG import BlpConverter as BLP2PNG
except Exception as exc:
    class BLP2PNG:
        def __init__(self, *args, **kwargs):
            raise ImportError(f"BLP2PNG native binding is unavailable: {exc}")

try:
    from .PNG2BLP.PNG2BLP import BlpFromPng as PNG2BLP
except Exception as exc:
    class PNG2BLP:
        def __init__(self, *args, **kwargs):
            raise ImportError(f"PNG2BLP native binding is unavailable: {exc}")
