import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QLabel, QComboBox, QPushButton
from PyQt6.QtGui import QFont, QIcon
from PyQt6.QtCore import Qt
from functions.idioms import IdiomManager
from agents.english_expert import EnglishExpert
from agents.spanish_expert import SpanishExpert

class IdiomGameApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Idiom Game")
        self.setWindowIcon(QIcon('pikachu_glasses.png'))  # Replace with your icon path
        self.setStyleSheet("""
            QMainWindow {
                background-color: #f0f0f0;
            }
            QLabel {
                font-size: 14px;
                margin-bottom: 5px;
            }
            QComboBox {
                font-size: 14px;
                padding: 5px;
                border: 1px solid #ccc;
                border-radius: 3px;
            }
            QPushButton {
                font-size: 14px;
                padding: 8px 15px;
                background-color: #4CAF50;
                color: white;
                border: none;
                border-radius: 3px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        self.setup_ui()

        # Create expert instances
        self.english_expert = EnglishExpert()
        self.spanish_expert = SpanishExpert()

        # Get all idioms
        self.idioms = list(self.english_expert.known_idioms.keys()) + list(self.spanish_expert.known_idioms.keys())
        self.idiom_combobox.addItems(self.idioms)

    def setup_ui(self):
        title_label = QLabel("Idiom Game")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_label.setFont(QFont("Arial", 20, QFont.Weight.Bold))
        self.layout.addWidget(title_label)

        self.layout.addSpacing(20)

        instruction_label = QLabel("Select an idiom:")
        self.layout.addWidget(instruction_label)

        self.idiom_combobox = QComboBox()
        self.layout.addWidget(self.idiom_combobox)

        self.submit_button = QPushButton("Submit")
        self.submit_button.clicked.connect(self.run_idiom_game)
        self.layout.addWidget(self.submit_button)

        self.layout.addSpacing(20)

        self.output_label = QLabel()
        self.output_label.setWordWrap(True)
        self.layout.addWidget(self.output_label)

        self.layout.addSpacing(20)

        expert_status_layout = QHBoxLayout()
        self.english_status = QLabel("English Expert: Idle")
        self.spanish_status = QLabel("Spanish Expert: Idle")
        expert_status_layout.addWidget(self.english_status)
        expert_status_layout.addWidget(self.spanish_status)
        self.layout.addLayout(expert_status_layout)

    def run_idiom_game(self):
        idiom = self.idiom_combobox.currentText().strip()
        if idiom.lower() == 'exit':
            self.close()
            return

        self.output_label.setText("")
        self.english_status.setText("English Expert: Idle")
        self.spanish_status.setText("Spanish Expert: Idle")

        # Check if the English expert can help
        if self.english_expert.can_help_with(idiom):
            self.english_status.setText("English Expert: Active")
            explanation = self.english_expert.explain_idiom(idiom)
            self.output_label.setText(explanation)
        # Check if the Spanish expert can help
        elif self.spanish_expert.can_help_with(idiom):
            self.spanish_status.setText("Spanish Expert: Active")
            explanation = self.spanish_expert.explain_idiom(idiom)
            self.output_label.setText(explanation)
        else:
            self.output_label.setText("Sorry, I can't help with that idiom (modismo).")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = IdiomGameApp()
    window.setGeometry(100, 100, 400, 300)
    window.show()
    sys.exit(app.exec())