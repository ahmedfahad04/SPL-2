from PyQt5.QtWidgets import QWidget

from Frontend.Teacher_UI import ui_sound_recorder

custom_widget = QWidget()
audio_recorder_widget = ui_sound_recorder.Ui_audioRecorderWidget()
audio_recorder_widget.setupUi(custom_widget)
custom_widget.show()

