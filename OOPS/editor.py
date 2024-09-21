class Editor:

    name:str

    vendor:str

    def __init__(self,name,vendor):

        self.name=name

        self.vendor=vendor

    def open(self):

        print(f"{self.name} open")

    def execute(self):

        print(f"{self.name} execute")


class Vscode(Editor):

    def __init__(self, name, vendor):
        super().__init__(name, vendor)

class PyCharm(Editor):

    def __init__(self, name, vendor):
        super().__init__(name, vendor)

Vscode_instance=Vscode("visualStudioCode","vsvendor")

Vscode_instance.open()

PyCharm_instance=PyCharm("pycharm","jetbrains")

PyCharm_instance.open()