def check_filename(name):
    no_in_filename = r'\/:*?"<>|'
    for i in no_in_filename:
        if i in name:
            name = name.replace(i, '+')
    return name