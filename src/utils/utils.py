import os

def read_file(path: str):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def get_files(path: str) -> list[str]:
    list_files = []
    for file in os.listdir(path):
        list_files.append(file)
    return list_files
