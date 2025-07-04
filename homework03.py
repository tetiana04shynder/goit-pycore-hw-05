import sys
from pathlib import Path
from colorama import init, Fore, Style

def print_tree(path: Path, prefix=""):
    if not path.exists():
        print(Fore.RED + f"Шлях {path} не існує." + Style.RESET_ALL)
        return
    if not path.is_dir():
        print(Fore.RED + f"Шлях {path} не є директорією." + Style.RESET_ALL)
        return

    items = sorted(path.iterdir(), key=lambda x: (x.is_file(), x.name.lower()))
    for index, item in enumerate(items):
        connector = "┗━━" if index == len(items) - 1 else "┣━━"
        if item.is_dir():
            print(prefix + connector + Fore.BLUE + item.name + "/" + Style.RESET_ALL)
            extension = "    " if index == len(items) - 1 else "┃   "
            print_tree(item, prefix + extension)
        else:
            print(prefix + connector + Fore.GREEN + item.name + Style.RESET_ALL)


def main():
    init(autoreset=True)  

    if len(sys.argv) != 2:
        print(Fore.YELLOW + "Використання: python hw03.py /шлях/до/директорії" + Style.RESET_ALL)
        sys.exit(1)

    directory = Path(sys.argv[1])

    if not directory.exists():
        print(Fore.RED + f"Шлях {directory} не існує." + Style.RESET_ALL)
        sys.exit(1)

    if not directory.is_dir():
        print(Fore.RED + f"Шлях {directory} не є директорією." + Style.RESET_ALL)
        sys.exit(1)

    print(Fore.MAGENTA + f"Структура директорії: {directory}" + Style.RESET_ALL)
    print_tree(directory)


if __name__ == "__main__":
    main()
