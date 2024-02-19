import turtle

bob = turtle.Turtle()

def polyline(t,n,length,angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)
def polyline2(t,n,length,angle):
    for i in range(n):
        t.fd(length)
        t.rt(angle)

polyline(bob,10,10,10)
polyline2(bob,10,10,10)

turtle.done()
