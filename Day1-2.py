def print_twice(n):
    print(n)
    print(n)

def do_twice(f,n):
    f(n)
    f(n)

do_twice(print_twice,'spam')

def do_four(f,n):
    do_twice(f,n)
    do_twice(f,n)

do_four(print_twice,'spam')
