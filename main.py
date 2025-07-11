

from PyQt5 import QtWidgets
from executor import Execute
from movielogics import Database

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Execute(Database())
    window.show()
    sys.exit(app.exec_())