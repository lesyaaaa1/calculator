from design import Ui_MainWindow


class MainWindow(Ui_MainWindow):

    def retranslateUi(self, MainWindow):
        super().retranslateUi(MainWindow)

        self.buttons = {
            '1': self.one,
            '2': self.two,
            '3': self.three,
            '4': self.four,
            '5': self.five,
            '6': self.six,
            '7': self.seven,
            '8': self.eight,
            '9': self.nine,
            '0': self.zero,
            '00': self.double_zero,
            '.': self.point,
            ')': self.right_bracket,
            '(': self.left_bracket,
            '+': self.plus,
            '-': self.minus,
            '/': self.div,
            '*': self.mul,
            '=': self.equal,
            'C': self.clear,
        }

    def displayText(self):   # виведення значень
        return self.input.text()

    def setText(self, text): # задання тексту
        self.input.setText(text)
        self.input.setFocus() # переводить каретку в кінець

    def clearText(self): # очищення тексту
        self.input.clear()