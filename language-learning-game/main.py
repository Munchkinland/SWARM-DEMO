from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QPushButton, QComboBox, QWidget, QTextEdit, QGridLayout
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from functions.handoff_functions import HandoffManager, HandoffLogger
from agents.english_expert import EnglishExpert
from agents.spanish_expert import SpanishExpert
from agents.game_master import GameMaster
import sys

class LogHandler:
    """Class to handle logging output to the GUI."""
    def __init__(self, log_widget):
        self.log_widget = log_widget

    def write(self, message):
        """Redirects the output to the QTextEdit log widget."""
        self.log_widget.append(message)

    def flush(self):
        """Flush function for compatibility with Python's print()."""
        pass

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Idiom Bot Manager")
        
        # Set the favicon (optional)
        self.setWindowIcon(QIcon('pikachu_glasses.png'))

        # Create bots
        self.english_expert = EnglishExpert()
        self.spanish_expert = SpanishExpert()
        self.game_master = GameMaster()

        # Handoff Manager and Logger
        self.handoff_manager = HandoffManager()
        self.logger = HandoffLogger()

        # GUI Elements
        layout = QVBoxLayout()

        # Add GameMaster introduction and rules
        layout.addWidget(QLabel(self.game_master.introduce_game()))
        layout.addWidget(QLabel(self.game_master.explain_rules()))

        # Idiom Selector (no language selector needed)
        self.idiom_selector = QComboBox()
        self.idiom_selector.addItems(["break the ice", "hit the nail on the head", "spill the beans",
                                      "dar en el clavo", "romper el hielo", "tirar la toalla"])
        layout.addWidget(QLabel("Select an Idiom:"))
        layout.addWidget(self.idiom_selector)

        # Explanation Output
        self.explanation_output = QTextEdit()
        self.explanation_output.setReadOnly(True)
        layout.addWidget(QLabel("Explanation:"))
        layout.addWidget(self.explanation_output)

        # Add a section for showing bot statuses
        self.status_layout = QGridLayout()

        # Bot status labels
        self.english_status = QLabel("English Expert: idle")
        self.spanish_status = QLabel("Spanish Expert: idle")
        self.gamemaster_status = QLabel("Game Master: idle")

        # Add status labels to grid
        self.status_layout.addWidget(QLabel("Agent Status"), 0, 0, 1, 2, alignment=Qt.AlignmentFlag.AlignCenter)
        self.status_layout.addWidget(self.english_status, 1, 0)
        self.status_layout.addWidget(self.spanish_status, 2, 0)
        self.status_layout.addWidget(self.gamemaster_status, 3, 0)

        # Add status layout to main layout
        layout.addLayout(self.status_layout)

        # Submit Button
        self.submit_button = QPushButton("Get Explanation")
        self.submit_button.clicked.connect(self.handle_explanation_request)
        layout.addWidget(self.submit_button)

        # Reset Button to set all bot statuses to idle
        self.reset_button = QPushButton("Reset Bot Statuses")
        self.reset_button.clicked.connect(self.reset_bot_statuses)
        layout.addWidget(self.reset_button)

        # Button to show the handoff history
        self.handoff_history_button = QPushButton("Show Handoff History")
        self.handoff_history_button.clicked.connect(self.show_handoff_history)
        layout.addWidget(self.handoff_history_button)

        # Log output area
        self.log_output = QTextEdit()
        self.log_output.setReadOnly(True)
        layout.addWidget(QLabel("Log Output:"))
        layout.addWidget(self.log_output)

        # Set layout
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # Redirect stdout to log output
        sys.stdout = LogHandler(self.log_output)
        print("Initializing the functions package.")

    def handle_explanation_request(self):
        """Handles the explanation request from the selected idiom."""
        idiom = self.idiom_selector.currentText()

        # Step 1: GameMaster coordinates the task
        explanation = self.delegate_task_to_expert(idiom)

        # Display explanation
        self.explanation_output.setText(explanation)

    def delegate_task_to_expert(self, idiom):
        """GameMaster decides which expert can handle the idiom and passes the task."""
        
        # Try the English Expert first
        if self.english_expert.can_help_with(idiom):
            self.english_status.setText("English Expert: working")
            self.gamemaster_status.setText("Game Master: assigned to English Expert")
            explanation = self.english_expert.explain_idiom(idiom)
            self.handoff_manager.add_handoff(idiom, self.english_expert.name)
            self.logger.log_handoff(idiom, self.english_expert.name)
            print(f"Task assigned to English Expert for topic '{idiom}'.")  # Log message
            self.update_bot_status(self.english_expert.name, "Task assigned")
            return explanation
        
        # If English Expert can't help, try Spanish Expert
        elif self.spanish_expert.can_help_with(idiom):
            self.spanish_status.setText("Spanish Expert: working")
            self.gamemaster_status.setText("Game Master: assigned to Spanish Expert")
            explanation = self.spanish_expert.explain_idiom(idiom)
            self.handoff_manager.add_handoff(idiom, self.spanish_expert.name)
            self.logger.log_handoff(idiom, self.spanish_expert.name)
            print(f"Task assigned to Spanish Expert for topic '{idiom}'.")  # Log message
            self.update_bot_status(self.spanish_expert.name, "Task assigned")
            return explanation
        
        # If no expert can help, GameMaster provides a fallback explanation
        else:
            self.gamemaster_status.setText("Game Master: fallback")
            explanation = f"No expert could explain the idiom '{idiom}'."
            explanation += "\n" + self.game_master.introduce_game()  # GameMaster provides further context
            return explanation

    def update_bot_status(self, bot_name, status):
        """Update the visual status of the bot."""
        if bot_name == "English Expert":
            self.english_status.setText(f"English Expert: {status}")
        elif bot_name == "Spanish Expert":
            self.spanish_status.setText(f"Spanish Expert: {status}")
        elif bot_name == "Game Master":
            self.gamemaster_status.setText(f"Game Master: {status}")

    def reset_bot_statuses(self):
        """Reset all bot statuses back to idle when the reset button is clicked."""
        self.english_status.setText("English Expert: idle")
        self.spanish_status.setText("Spanish Expert: idle")
        self.gamemaster_status.setText("Game Master: idle")

    def show_handoff_history(self):
        """Display the history of task handoffs."""
        handoff_history = self.handoff_manager.list_handoffs()

        # Convert list to a formatted string for display
        handoff_history_str = "\n".join(handoff_history)
    
        # Display the history in the log output
        self.log_output.append("\nHandoff History:")
        self.log_output.append(handoff_history_str)

# Entry point for the application
if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
