"""Main TUI implementation for {{ cookiecutter.project_name }}

Author: {{ cookiecutter.full_name }}  
Created: 
"""


import py_cui


class {{ cookiecutter.project_name|title }}App:

    def __init__(self, master):

        self.master = master
        self.master.add_label('Hello py_cui!!!', 1, 1)


def main():
    root = py_cui.PyCUI(3, 3)
    wrapper =  {{ cookiecutter.project_name|title }}App(root)
    root.start()