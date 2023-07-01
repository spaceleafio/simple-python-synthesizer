
import tkinter as tk
from tkinter import ttk
from functools import partial
from synthesizer import Synthesizer

class GUI:
    def __init__(self, root, synthesizer):
        self.root = root
        self.synthesizer = synthesizer
        self.frequency = tk.DoubleVar()
        self.volume = tk.DoubleVar()

    def create_gui(self):
        self.root.title("Synthesizer")
        self.root.configure(bg="black")

        frequency_label = ttk.Label(self.root, text="Frequency", foreground="white", background="black")
        frequency_label.pack()

        frequency_knob = ttk.Scale(self.root, from_=0, to=100, variable=self.frequency, command=self.update_frequency_knob)
        frequency_knob.pack()

        volume_label = ttk.Label(self.root, text="Volume", foreground="white", background="black")
        volume_label.pack()

        volume_slider = ttk.Scale(self.root, from_=0, to=1, variable=self.volume, command=self.update_volume_slider)
        volume_slider.pack()

        start_button = ttk.Button(self.root, text="Start", command=self.start_synthesizer)
        start_button.pack()

        stop_button = ttk.Button(self.root, text="Stop", command=self.stop_synthesizer)
        stop_button.pack()

    def update_frequency(self, frequency: float):
        self.synthesizer.set_frequency(frequency)

    def update_volume(self, volume: float):
        self.synthesizer.set_volume(volume)

    def start_synthesizer(self):
        self.synthesizer.start()

    def stop_synthesizer(self):
        self.synthesizer.stop()

    def update_frequency_knob(self, value):
        frequency = float(value) * 1000.0
        self.frequency.set(frequency)
        self.update_frequency(frequency)

    def update_volume_slider(self, value):
        volume = float(value)
        self.volume.set(volume)
        self.update_volume(float(value))