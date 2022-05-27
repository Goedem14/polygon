import turtle

t = turtle.Turtle()

def polygon (n,length):
    """Zeichnet ein n-seitiges polygon mit der seiten länge length"""
    for _ in range(n):
        t.fd(length)
        t.lt(360/n)

def main ():
    """Draw polygon with 3-9 sides."""
    t.up()
    t.goto(-150,-140)
    t.down()
    for n in range (3,15):
        polygon(n,80)
    turtle.exitonclick()

main ()
