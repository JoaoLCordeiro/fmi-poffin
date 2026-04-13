from PyQt6.QtWidgets import QComboBox
from PyQt6.QtCore import QStringListModel, QSortFilterProxyModel, Qt
from PyQt6.QtCore import QRegularExpression


class CardSelector(QComboBox):
    def __init__(self, parent):
        super().__init__(parent=parent)

        self.setEditable(True)
        self.setInsertPolicy(QComboBox.InsertPolicy.NoInsert)

    def setAllCards(self, all_cards):
        # Model base
        self.model_base = QStringListModel(all_cards)

        # Filter
        self.proxy = QSortFilterProxyModel(self)
        self.proxy.setSourceModel(self.model_base)
        self.proxy.setFilterCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)

        # Filter on combobox
        self.setModel(self.proxy)

        # Connects input to filter
        self.lineEdit().returnPressed.connect(self.aplicar_filtro)

    def aplicar_filtro(self):
        texto = self.currentText()
        regex = QRegularExpression(texto)
        pttrn_opt = QRegularExpression.PatternOption
        regex.setPatternOptions(pttrn_opt.CaseInsensitiveOption)
        self.proxy.setFilterRegularExpression(regex)
        self.showPopup()
