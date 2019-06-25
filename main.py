from UI import Ui_MainWindow

import gc

from PyQt5 import QtWidgets
from PyQt5.QtCore import QCoreApplication, pyqtSlot
from PyQt5.QtWidgets import QDialog, QFileDialog, QMessageBox

from copy import deepcopy
from UI import Ui_MainWindow


class GramarUI(Ui_MainWindow):
    def __init__(self, root):
        Ui_MainWindow.__init__(root)
        self.root = root
        self.setupUi(root)
        # vars
        self.current_filename = None
        #
        self.associate_actions()

    def associate_actions(self):
        self.actionLoadCode.triggered.connect(self.load_code)
        self.actionNewCode.triggered.connect(self.new_code)
        self.actionSaveCode.triggered.connect(self.save_code)
        self.actionSaveCodeAs.triggered.connect(self.save_code_as)
        self.actionAnalyse.triggered.connect(self.analyse)
        # self.buttonAskBelongs.clicked.connect(self.ask_belongs)

    def _load_code(self, file_name: str):
        self.current_filename = file_name
        with open(file_name, "r") as file:
            try:
                self.textEditCode.setPlainText(file.read())
                    
                if self.tabs:
                    self._close_adicional_tabs()

            except:
                self.dialog_warning("Ocurrió un error al cargar el archivo.")
        return

    def load_code(self):
        import os

        grm_path, _ = QFileDialog.getOpenFileName(
            self.root, "Cargar código...", "./", "archivo de texto... (*.txt )"
        )
        if not grm_path or not os.path.exists(grm_path):
            return
        # print(grm_path)
        self._load_code(grm_path)

    def _save_code_at(self, file_name):
        if not self.get_code:
            return
        with open(file_name, "w") as file:
            file.write(self.get_code)
        return

    def save_code_as(self):
        if not self.get_code:
            return

        file_name, _ = QFileDialog.getSaveFileName(
            self.root, "Salvar código...", "./", "Archivos... (*.txt)"
        )

        if not file_name:
            # If dialog is cancelled, will return ''
            return

        self.current_filename = file_name
        return self._save_code_at(self.current_filename)

    def save_code(self):
        if not self.get_code:
            return

        if self.current_filename is None:
            self.save_code_as()
        else:
            self._save_code_at(self.current_filename)

    def new_code(self):
        self.grammar = None
        self.current_filename = None
        # clear results and grammar
        self.textAST.setPlainText("")
        self.textChecker.setPlainText("")
        self.textCollector.setPlainText("")
        self.textCollector.setPlainText("")
        self.textEditCode.setText("")

        self.tabWidget.setCurrentIndex(0)
        self._close_adicional_tabs()
        return

    def analyse(self):
        if not self.get_code:
            return
        if self.tabs:
            self._close_adicional_tabs()

        self.code = self._code
        self.set_results()
        self.tabWidget.setCurrentIndex(1)

        # for parser_name, svg_str in self.svg_imgs:
        #     assert isinstance(svg_str, str), parser_name
        #     self.create_slot(parser_name, svg_str)

    ############## Word Belongs ##############
    def ask_belongs(self):
        word = self.textEdit_input_belongs.toPlainText().strip("\n \t").split(" ")
        _word = "" if not self.grammar else self.grammar.tokenize(word)
        res_belongs, derivation = self.get_belongs_info(_word)
        self.label_belong_result.setText(res_belongs)
        if derivation:
            derivation = derivation._repr_svg_()
            if derivation:
                self.create_svg_slot(f"Derivación({','.join(word)})", derivation)

    ############## Parser Results ##############
    def set_results(self):
        if not self.get_code:
            return
        
        Header = "RESULTADOS:\n\n"
        
        res = Header + self.get_AST_info()
        self.textAST.setPlainText(res)
        
        res = Header + self.get_Collector_info()
        self.textCollector.setPlainText(res)

        res = Header + self.get_Builder_info()
        self.textBuilder.setPlainText(res)

        res = Header + self.get_Checker_info()
        self.textChecker.setPlainText(res)

        res = Header + self.get_Inferer_info()
        self.textInferer.setPlainText(res)
        
        return
    
    def get_AST_info(self) -> str:# TODO: all down here
        res = ""
        # Insert your code here!!!
        return res

    def get_Collector_info(self) -> str:
        res = ""
        # Insert your code here!!!
        return res

    def get_Builder_info(self) -> str:# TODO: all down here
        res = ""
        # Insert your code here!!!
        return res
    
    def get_Checker_info(self) -> str:
        res = ""
        # Insert your code here!!!
        return res

    def get_Inferer_info(self) -> str:
        res = ""
        # Insert your code here!!!
        return res


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = GramarUI(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
