from platform import architecture


def get_arch() -> int:
    return 64 if architecture()[0] == "64bit" else 32
