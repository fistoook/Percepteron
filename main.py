from Pixie import Pixie
from Goey import Goey
from Macey import Macey
from Alan import Alan

def main():
    model = Pixie()
    gui = Goey()
    terminal = Alan(model.brain.bias, model.brain.weights)

    macey = Macey(gui, model, terminal)

    macey.run()

if __name__ == "__main__":
    main()