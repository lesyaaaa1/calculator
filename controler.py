from functools import partial # часткова передача параметрів


class CalculatorController:
    def __init__(self, model, view):
        self._model = model  # func elevate_expression
        self._view = view  # class Ui_MainWindow

        self._connect_signals()

    def _calculate_result(self):
        result = self._model(expression=self._view.displayText())
        self._view.setText(result)

    def _build_expression(self, sub_exp):
        if self._view.displayText() == 'ERROR':
            self._view.clearText()

        expression = self._view.displayText() + sub_exp
        self._view.setText(expression)

    def _connect_signals(self):
        for buttons_value, buttons in self._view.buttons.items():
            if buttons_value not in ['=', 'C']:
                buttons.clicked.connect(partial(self._build_expression, buttons_value))

        self._view.equal.clicked.connect(self._calculate_result)
        self._view.input.returnPressed.connect(self._calculate_result)
        self._view.clear.clicked.connect(self._view.clearText)
