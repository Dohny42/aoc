"""
simple script to generate folder structure for current year of AoC with python files
including code for data fetching
"""

from datetime import datetime
import os

# get current year
current_year = datetime.now().year

# create parent folder
current_dir = os.getcwd()

current_year_folder_path = os.path.join(current_dir, str(current_year))

try:
    os.mkdir(current_year_folder_path)
except OSError as e:
    print(e)

# create folders and python files for each day
for i in range(1, 26):
    try:
        current_day_folder = os.path.join(
            current_year_folder_path, f"day_{i}")
        os.mkdir(current_day_folder)

        # data fetching code lines
        import_line = "from aocd import get_data\n\n"
        data_line = f"data = get_data(day={i}, year={current_year})"

        with open(os.path.join(current_day_folder, "part_A.py"), "w") as part_file:
            part_file.write(import_line)
            part_file.write(data_line)

        with open(os.path.join(current_day_folder, "part_B.py"), "w") as part_file:
            part_file.write(import_line)
            part_file.write(data_line)
    except OSError as e:
        print(e)
