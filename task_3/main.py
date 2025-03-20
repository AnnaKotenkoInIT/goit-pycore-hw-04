import sys
from pathlib import Path
from colorama import init, Fore

# start colorama and reseting styles automatically
init(autoreset=True)

def show_directory_structure(directory_path, indent=0):
    path = Path(directory_path)    #path creation

    if not path.exists() or not path.is_dir():
        print(Fore.RED + f"Шлях '{directory_path}' відсутній або не є директорією.")
        return

    print(" " * indent + Fore.YELLOW + f"{path.name}/")

    # checking inside the the main folder 
    for item in path.iterdir():
        if item.is_dir():
            print(" " * (indent + 2) + Fore.GREEN + f"{item.name}/")
            show_directory_structure(item, indent + 4)

        elif item.is_file():
            print(" " * (indent + 2) + Fore.MAGENTA + f"{item.name}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(Fore.RED + "Вкажіть шлях до директорії.")
        sys.exit(1)

    directory_path = sys.argv[1]

# Example of function use
    show_directory_structure(directory_path)

# Check the task_3 separately
# py task_3/main.py task_3/picture