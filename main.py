import os

os.makedirs("logs", exist_ok=True)

with open("logs/logs.log", "a") as log_file:
    os.dup2(log_file.fileno(), 2)


from Pixie import Pixie
from Goey import Goey
from Macey import Macey
from Alan import Alan

def main():
    pixie = Pixie()
    goey = Goey()
    alan = Alan(pixie.get_models())

    macey = Macey(goey, pixie, alan)

    macey.run()

if __name__ == "__main__":
    main()