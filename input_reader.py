import numpy as np
MAIN_DATA_FILE_PATH = "sample-input.txt"


def read_input_file():
    with open(MAIN_DATA_FILE_PATH, 'r') as f:

        index = 1
        for line in f.readlines():
            if line[0] == "#":
                continue
            if line[0] == "\n":
                continue

            read_one_good_line(line, index)
            index += 1


def read_one_good_line(line, ifile):
    start = 0
    end = 6
    initial_config = ""
    initial_params = ""
    for index in range(6):
        initial_config += line[start:end]
        initial_config += "\n"
        start += 6
        end += 6

    file_name = "datatxt/game" + str(ifile) + ".txt"
    with open(file_name, "w") as file:
        file.write(initial_config)
        file.close()

    initial_params = line[37:]
    initial_params.strip()
    file_name = "datatxt/params" + str(ifile) + ".txt"
    if initial_params:
        with open(file_name, "w") as file:
            file.write(initial_params)
            file.close()






