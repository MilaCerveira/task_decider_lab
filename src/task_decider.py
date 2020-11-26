def get_preferred_option(task1, task2):
    if task1.description == "wash dishes" and task2.description == "cook dinner":
        return "wash dishes"
    else:
        if task1.description == "clean windows" and task2.description == "wash dishes":
            return "clean windows"

# if clean window, wash dishes return clean windows
# elif wash dishes, cook dinner return wash dishes
#  else cook diner clean windows return cook dinner
