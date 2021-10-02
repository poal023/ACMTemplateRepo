def eggs():
    print("eggs")
def spam():
    print("spam")

def spamNeggs(s, e):
    s()
    e()



if __name__ == "__main__":
    eggs()
    spam()
    spamNeggs()


