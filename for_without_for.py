def for_loop(iterable, loop_body_func):
    iterator = iter(iterable)
    while True:
        try:
            element_from_iterator = next(iterator)
            loop_body_func(element_from_iterator)
        except StopIteration:
            break

def loop(i):
    print(i+6)

for_loop([1,2,3], loop)
