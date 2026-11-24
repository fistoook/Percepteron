from Pixie import Pixie
from Goey import Goey
from Macey import Macey
from Alan import Alan

def main():
    pixie = Pixie()
    goey = Goey()
    alan = Alan(pixie.percy.bias, pixie.percy.weights)

    macey = Macey(goey, pixie, alan)

    macey.run()

if __name__ == "__main__":
    main()