import os
import shutil

medium_project_files_to_remove = ["docs", ".env", "Makefile"]

small_project_files_to_remove = medium_project_files_to_remove + [
    os.path.join("data", "raw"),
    os.path.join("data", "interim"),
    os.path.join("data", "processed"),
    os.path.join("notebooks", "draft"),
    os.path.join("notebooks"),
    os.path.join("src", "data"),
    os.path.join("src", "models"),
    os.path.join("src", "visualization"),
    os.path.join("tests"),
]

project_size = "{{ cookiecutter.project_size }}"

paths = []

if project_size == "Medium":
    paths = medium_project_files_to_remove
elif project_size == "Small":
    paths = small_project_files_to_remove

for path in paths:
    if path and os.path.exists(path):
        if os.path.isdir(path):
            shutil.rmtree(path, ignore_errors=True)
        else:
            os.remove(path)
