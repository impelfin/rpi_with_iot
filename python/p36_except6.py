def division_function(a, b):
    try:
        return a / b
    except TypeError as e:
        return -1
    except ZeroDivisionError as e:
        return -2
    except Exception as e:
        return -3
    finally:
        print("finally!")

ret = division_function("a", 1)
print(ret)
ret = division_function(1, 0)
print(ret)
ret = division_function(4, 2)
print(ret)
