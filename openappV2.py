import os
import subprocess


logo = """
 █████    ██████   ██████    ███████████      ███████████
░░███    ░░██████ ██████    ░░███░░░░░███    ░█░░░███░░░█
 ░███     ░███░█████░███     ░███    ░███    ░   ░███  ░ 
 ░███     ░███░░███ ░███     ░██████████         ░███    
 ░███     ░███ ░░░  ░███     ░███░░░░░███        ░███    
 ░███     ░███      ░███     ░███    ░███        ░███    
 █████ ██ █████     █████ ██ █████   █████ ██    █████   
░░░░░ ░░ ░░░░░     ░░░░░ ░░ ░░░░░   ░░░░░ ░░    ░░░░░         

I made random tool
version2

--made by justme1231234--

"""

choice = "0"

def get_mac_installed_programs():
    applications_path = "/Applications"
    programs = [app for app in os.listdir(applications_path) if app.endswith(".app")]
    return programs

def open_program(program_number, programs):
    if 0 < program_number <= len(programs):
        program_name = programs[program_number - 1]
        program_path = os.path.join("/Applications", program_name)
        subprocess.run(["open", program_path])
    else:
        print("wrong number")

while True:
    print(logo)
    print("1. Run a program")
    print("2. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        installed_programs = get_mac_installed_programs()
        sorted_programs = sorted(installed_programs)

        print("")
        for idx, program in enumerate(sorted_programs, start=1):
            print(f"{idx}. {program}")


        try:
            choice = int(input("Enter your choice: "))
            open_program(choice, sorted_programs)
        except ValueError:
            print("wrong input. Please enter a number.")
    elif choice == "2":
        break
