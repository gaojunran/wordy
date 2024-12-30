import sys

from youdao import main as youdao_main
from questionary import confirm

def run_yd_with_args(*args):
    sys.argv = sys.argv[:1]
    sys.argv.extend(args)
    youdao_main.main()
    sys.argv = sys.argv[:1]

def to_csv():
    pass

def main():
    while True:
        word = input(">>> ").strip()
        if word.startswith("-"):
            run_yd_with_args(word)
        elif word == "csv":
            to_csv()
        elif word:
            run_yd_with_args(word)
            if not confirm("Save?").ask():
                run_yd_with_args("-d", word)


if __name__ == "__main__":
    main()
