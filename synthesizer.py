import math

class Synthesizer:
    def __init__(self):
        self.frequency = 440.0
        self.volume = 0.5
        self.is_playing = False

    def start(self):
        self.is_playing = True

    def stop(self):
        self.is_playing = False

    def set_frequency(self, frequency: float):
        self.frequency = frequency

    def set_volume(self, volume: float):
        self.volume = volume

    def generate_wave(self):
        if self.is_playing:
            amplitude = 0.3
            sample_rate = 44100
            duration = 10.0
            num_samples = int(sample_rate * duration)
            samples = []
            for i in range(num_samples):
                t = float(i) / sample_rate
                value = amplitude * math.sin(2.0 * math.pi * self.frequency * t)
                samples.append(value * self.volume)
            return samples
        else:
            return []