import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, \
    QSlider, QStyle, QSizePolicy, QFileDialog, QFrame 
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtGui import QIcon, QPalette, QPixmap
from PyQt5.QtCore import Qt, QUrl, QRect, QPoint, QFile, QSize


class ImageCaptureWidget(QWidget):

    def __init__(self, ui_object):
        super().__init__()

        self.ui_obj = ui_object
        self.current_saved_file = None

        self.setWindowTitle("PyQt5 Media Player")
        self.setGeometry(350, 100, 800, 800)
        self.setWindowIcon(QIcon('player.png'))

        p = self.palette()
        p.setColor(QPalette.Window, Qt.white)
        self.setPalette(p)

        self.init_ui()

        self.show()

    def init_ui(self):

        # create media player object
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)

        # create videowidget object
        self.videowidget = QVideoWidget()
        
        video_frame = QFrame()
        video_frame.setStyleSheet("border: 2px solid #002B5B;")
        video_layout = QVBoxLayout(video_frame)
        video_layout.addWidget(self.videowidget)

        # create open button
        openBtn = QPushButton('ফাইল খুলুন')
        openBtn.setFixedSize(100, 50)
        openBtn.setIcon(QIcon('Frontend\Images\open_folder_v2.png'))
        openBtn.setIconSize(QSize(20, 20))
        openBtn.clicked.connect(self.open_file)
        openBtn.setStyleSheet("QPushButton {\n"
"border: 3px solid rgb(43, 72, 101);\n"
"border-radius: 10px;\n"
"background-color: rgb(43, 72, 101);\n"
"color: rgb(137, 218, 199)\n"
"}\n"
"\n"
"QPushButton::hover:!pressed {\n"
"background-color: rgb(0, 43, 91);\n"
"border: 3px solid rgb(0, 43, 91); \n"
"}")

        # create button for playing
        self.playBtn = QPushButton()
        self.playBtn.setEnabled(False)
        self.playBtn.setFixedSize(50, 50)
        self.playBtn.setIcon(QIcon('Frontend\Images\play_btn.png'))
        self.playBtn.clicked.connect(self.play_video)
        self.playBtn.setStyleSheet("QPushButton {\n"
"border: 3px solid rgb(43, 72, 101);\n"
"border-radius: 10px;\n"
"background-color: rgb(43, 72, 101);\n"
"color: rgb(137, 218, 199)\n"
"}\n"
"\n"
"QPushButton::hover:!pressed {\n"
"background-color: rgb(0, 43, 91);\n"
"border: 3px solid rgb(0, 43, 91); \n"
"}")

        # create slider
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setRange(0, 0)
        self.slider.sliderMoved.connect(self.set_position)
        self.slider.setStyleSheet("QSlider::handle:horizontal {background-color:#002B5B;}")

        # create volume slider
        self.volume_slider = QSlider(Qt.Horizontal)
        self.volume_slider.setRange(0, 100)
        self.volume_slider.setFixedSize(100, 30)
        self.volume_slider.sliderMoved.connect(self.set_volume)
        self.volume_slider.setStyleSheet("QSlider::handle:horizontal {background-color:#002B5B;}")

        # create label
        self.label = QLabel()
        self.label.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)

        # create volume label
        self.volume_lbl = QLabel("ভলিউম")
        self.volume_lbl.setStyleSheet("color: black")
        self.volume_lbl.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.volume_lbl.setMinimumSize(250, 0)
        self.volume_lbl.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)

        # create button for taking a snapshot
        snapshotBtn = QPushButton('স্ক্রিনশট নিন') 
        snapshotBtn.setFixedSize(100, 50)
        snapshotBtn.clicked.connect(self.take_snapshot)
        snapshotBtn.setIcon(QIcon('Frontend\Images\screenshot.png'))
        snapshotBtn.setIconSize(QSize(30, 30))
        snapshotBtn.setStyleSheet("QPushButton {\n"
"border: 3px solid rgb(43, 72, 101);\n"
"border-radius: 10px;\n"
"background-color: rgb(43, 72, 101);\n"
"color: rgb(137, 218, 199)\n"
"}\n"
"\n"
"QPushButton::hover:!pressed {\n"
"background-color: rgb(0, 43, 91);\n"
"border: 3px solid rgb(0, 43, 91); \n"
"}")

        # create hbox layout
        hboxLayout = QHBoxLayout()
        hboxLayout.setContentsMargins(0, 0, 0, 0)

        # set widgets to the hbox layout
        hboxLayout.addWidget(self.slider)

        hbox2 = QHBoxLayout()
        hbox2.addWidget(openBtn)
        hbox2.addWidget(self.playBtn)
        hbox2.addWidget(snapshotBtn)  # Add the snapshot button here
        hbox2.addWidget(self.volume_lbl)
        hbox2.addWidget(self.volume_slider)

        # create vbox layout
        vboxLayout = QVBoxLayout()
        vboxLayout.addWidget(video_frame)  # Use the wrapped video widget
        vboxLayout.addLayout(hboxLayout)
        vboxLayout.addLayout(hbox2)
        vboxLayout.addWidget(self.label)

        self.setLayout(vboxLayout)

        self.mediaPlayer.setVideoOutput(self.videowidget)

        self.mediaPlayer.stateChanged.connect(self.mediastate_changed)
        self.mediaPlayer.positionChanged.connect(self.position_changed)
        self.mediaPlayer.durationChanged.connect(self.duration_changed)
        self.mediaPlayer.volumeChanged.connect(self.volume_changed)
        self.mediaPlayer.setVolume(50)

    def open_file(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Open Video")

        if filename != '':
            self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(filename)))
            self.playBtn.setEnabled(True)
            self.play_video()

    def play_video(self):

        print('Playing...')

        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()

        else:
            self.mediaPlayer.play()

    def mediastate_changed(self, state):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.playBtn.setIcon(QIcon('Frontend\Images\pause_btn.png'))

        else:
            self.playBtn.setIcon(
                self.style().standardIcon(QStyle.SP_MediaPlay)

            )

    def position_changed(self, position):
        self.slider.setValue(position)

    def duration_changed(self, duration):
        self.slider.setRange(0, duration)

    def set_position(self, position):
        self.mediaPlayer.setPosition(position)

    def handle_errors(self):
        self.playBtn.setEnabled(False)
        self.label.setText("Error: " + self.mediaPlayer.errorString())

    def volume_changed(self, volume):
        self.volume_slider.setValue(volume)

    def set_volume(self, volume):
        self.mediaPlayer.setVolume(volume)

    def take_snapshot(self):
        # Get the video widget's position and size
        video_pos = self.videowidget.mapToGlobal(QPoint(0, 0))
        video_size = self.videowidget.size()

        # Calculate the coordinates and size for grabbing the video widget only
        grab_x = video_pos.x()
        grab_y = video_pos.y()
        grab_width = video_size.width()
        grab_height = video_size.height()

        # Grab the contents of the video widget
        pixmap = QApplication.primaryScreen().grabWindow(0, grab_x, grab_y, grab_width, grab_height)
        
        # Save the pixmap as an image file
        # Set the initial directory to the Desktop
        
        
        initial_directory = "Lessons\Sequence_Images"  # Replace with the path to your desktop

        # Open the save file dialog
        snapshot_path, _ = QFileDialog.getSaveFileName(self, "Save Snapshot", initial_directory, "PNG Image (*.png)")

        if snapshot_path:
            # Save the pixmap as a PNG image
            pixmap.save(snapshot_path, "PNG")
            QFile(snapshot_path).flush()
            print("Screenshot saved successfully")
                        
        # scale the image to fit the label
        self.ui_obj.task_seq_img_view_lbl.setScaledContents(True)
        self.ui_obj.task_seq_img_view_lbl.setPixmap(QPixmap(snapshot_path))
        self.current_saved_file = snapshot_path
        print("Snap: ", snapshot_path)


# app = QApplication(sys.argv)
# window = ImageCaptureWidget()
# sys.exit(app.exec_())