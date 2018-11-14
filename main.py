# This function will install and upgrade status

import Get_proceses, Choose_best_process, Forminate_string
import vk_api


def main_function():
    login, password = "89832095427", "misha2013MISHA"
    print(login, password)

    processes = Get_proceses.get_proc()

    Using_Pocesses = Choose_best_process.find_best(processes)

    print(Forminate_string.do_it(Using_Pocesses))

    


main_function()