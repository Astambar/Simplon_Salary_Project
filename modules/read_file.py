
def _read_file(filename:str):
    with open(filename) as f:
        return f.read()

if __name__ == '__main__':
    print(_read_file('__init__.py'))