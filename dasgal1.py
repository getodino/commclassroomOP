def printSpring():
    print("Хавар болж цэцэгс цэцэглэлээ.")


def printSummer():
    print("Зун болж халуун боллоо.")


def printFall():
    print("Намар болж навч уналаа")


def printWinter():
    print("Өвөл болж цас орлоо.")


season = int(input("Улиралаа оруулна уу 1-хавар 2-зун 3-намар 4-өвөл:"))
if season == 1:
    printSpring()
elif season == 2:
    printSummer()
elif season == 3:
    printFall()
elif season == 4:
    printWinter()
else:
    print("Буруу утга оруулсан байна")
