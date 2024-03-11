#генератор range

def m_range(arg1, arg2=None, step=1):
    if arg2 is None:
        arg1, arg2 = 0, arg1
    current = arg1
    while True:
        yield current
        next_value = current + step
        if (step > 0 and next_value >= arg2) or (step < 0 and next_value <= arg2):
            break
        current = next_value

for num in m_range(1, 10, 2):
    print(num)