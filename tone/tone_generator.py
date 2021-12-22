from enum import IntEnum

from tone.base_wave import BaseWave


class Sides(IntEnum):
    LEFT = 1
    RIGHT = 2


class ToneGenerator:
    def __init__(self, side: Sides):
        self.side = side
        self.current_wave = None
        self.current_amplitude = 0
        self.current_frequency = 0

    def create_wave(self, wave: BaseWave):
        pass
