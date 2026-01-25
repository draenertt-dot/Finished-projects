from turtle import *


def schneeflocke(stufe, länge):
    if stufe == 0:
        forward(länge)
    else:
        schneeflocke(stufe - 1, länge / 3)
        left(60)
        schneeflocke(stufe - 1, länge / 3)
        right(120)
        schneeflocke(stufe - 1, länge / 3)
        left(60)
        schneeflocke(stufe - 1, länge / 3)

speed(-12)

color("blue", "red")

begin_fill()

schneeflocke(4, 500)
right(120)
schneeflocke(4, 500)
right(120)
schneeflocke(4, 500)

end_fill()


done()