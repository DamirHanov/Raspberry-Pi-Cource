import wave
import random

with wave.open('test.wav', 'wb') as file:
    file.setnchannels(1)
    file.setsampwidth(1)
    file.setframerate(256)
    for x in range(256 * 10):
        file.writeframes(b'10101110')
