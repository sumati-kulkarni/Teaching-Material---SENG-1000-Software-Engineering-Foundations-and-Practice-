class B(Exception):
    pass

class C(B):
    pass

class D(C):
    pass

for cls in [B, C, D]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")

print('.........................')

for cls in [D, C, B]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")


print('.........................')

for cls in [D, B, C]:
    try:
        raise cls()
    except (D,C):
        print("D or C")
    except B:
        print("B")