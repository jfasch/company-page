g = 1

def create_f():
    def f():
        g = 2
        print('inner f called, g =', g)
    return f

inner = create_f()
inner()
print('global g =', g)
