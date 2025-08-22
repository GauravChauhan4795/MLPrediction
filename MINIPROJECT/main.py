from PyQt6.QtWidgets import (
    QApplication, QWidget, QMainWindow, QVBoxLayout,
    QHBoxLayout, QStackedWidget, QLabel, QPushButton
)
from PyQt6.QtGui import QPixmap, QPainter
from PyQt6.QtCore import Qt
import sys

class BackgroundWidget(QWidget):
    def __init__(self, image_path, parent=None):
        super().__init__(parent)
        self.image = QPixmap(image_path)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(self.rect(), self.image)

class DatasetUploadWidget(QWidget):
    def __init__(self):
        super().__init__()
        dataset_layout = QVBoxLayout(self)
        self.info = QLabel("Upload your dataset here.")
        self.datasetupload_btn = QPushButton("Upload Dataset")

        dataset_layout.addWidget(self.info)
        dataset_layout.addWidget(self.datasetupload_btn)
        self.datasetupload_btn.clicked.connect(self.upload_dataset)

        self.dataset = None
    
    def upload_dataset(self):
        pass

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Machine Learning Prediction")
        self.setMinimumSize(800, 500)

        self.stacked_widgets = QStackedWidget(self)
        self.setCentralWidget(self.stacked_widgets)
        self.start_widget = BackgroundWidget("MINIPROJECT/resources/start_bg.jpg")
        hlayout = QHBoxLayout(self.start_widget)
        vlayout = QVBoxLayout()
        vlayout.addStretch(1)

        label = QLabel("Welcome!")
        label.setStyleSheet("color: white; font-size: 28px; font-weight: bold;")
        label.setAlignment(Qt.AlignmentFlag.AlignVCenter)

        start_btn = QPushButton("Let's Go!")
        vlayout.addStretch(1)
        vlayout.addWidget(label)
        vlayout.addSpacing(20)
        vlayout.addWidget(start_btn)
        vlayout.addStretch(2)
        hlayout.addStretch(1)
        hlayout.addLayout(vlayout)
        hlayout.addStretch(2)

        self.stacked_widgets.addWidget(self.start_widget)
        self.dataset_upload_page = DatasetUploadWidget()
        self.stacked_widgets.addWidget(self.dataset_upload_page)

        start_btn.clicked.connect(lambda: self.stacked_widgets.setCurrentWidget(self.dataset_upload_page))


app = QApplication(sys.argv)
Window = MainWindow()
Window.show()
sys.exit(app.exec())