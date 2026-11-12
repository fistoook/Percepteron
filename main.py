from Pixie import Pixie
from Goey import Goey
from Macey import Macey

def main():
    model = Pixie()
    gui = Goey()

    macey = Macey(gui, model)

    macey.run()

if __name__ == "__main__":
    main()