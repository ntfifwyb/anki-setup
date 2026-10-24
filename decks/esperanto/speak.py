"""Speak the deck's audio clips into audio/ with eSpeak NG's Esperanto voice, skipping clips already there.

uv run --no-project -p 3.13 --with genanki==0.13.1 --with espeakng-loader==0.2.4 --with soundfile==0.13.1 --with numpy python speak.py

None of Psittacus's engines (Kokoro, Piper, Edge) has an Esperanto voice, so this deck has its own
engine: eSpeak NG, from the espeakng-loader package (its library and voice data, no system install).
It reads Esperanto by its own rules (ĉ, ĝ, ĥ, ĵ, ŝ, ŭ, stress on the next-to-last syllable), in a
robotic voice. It goes through Psittacus's Speaker, so clips get the names build.py expects.
"""
import ctypes
from pathlib import Path

from build import rows
from common import AUDIO, ENGINE, LANG, VOICE, clip, psittacus

RATE = 150  # words per minute; eSpeak's default is 175


class Espeak:
    """A Psittacus engine (core.Engine) for eSpeak NG, driven through its C library."""

    def __init__(self):
        import espeakng_loader
        import numpy

        self.np = numpy
        self.lib = ctypes.CDLL(espeakng_loader.get_library_path())
        # AUDIO_OUTPUT_SYNCHRONOUS: samples come back through the callback.
        self.rate = self.lib.espeak_Initialize(2, 0, espeakng_loader.get_data_path().encode(), 0)
        self.chunks = []
        callback = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_short), ctypes.c_int, ctypes.c_void_p)
        self.callback = callback(self.collect)  # kept on self, or it is garbage-collected
        self.lib.espeak_SetSynthCallback(self.callback)

    def collect(self, wav, n, events):
        if n > 0:
            self.chunks.append(self.np.ctypeslib.as_array(wav, (n,)).copy())
        return 0

    def synth(self, text, voice, speed, out):
        assert self.lib.espeak_SetVoiceByName(voice["voice"].encode()) == 0, voice
        self.lib.espeak_SetParameter(1, int(RATE * speed), 0)  # espeakRATE
        data = text.encode()
        self.chunks = []
        # espeakCHARS_UTF8; then wait for the whole text
        assert self.lib.espeak_Synth(data, len(data) + 1, 0, 0, 0, 1, None, None) == 0, text
        self.lib.espeak_Synchronize()
        psittacus("engines").write_mp3(out, self.np.concatenate(self.chunks), self.rate)


def main():
    core = psittacus()
    data = {"order": [ENGINE], "voices": {ENGINE: {LANG: VOICE}}}
    speaker = core.Speaker({ENGINE: Espeak()}, data, Path(AUDIO))
    todo = dict(clip(source)[::-1] for *_, sources in rows() for source in sources.values())
    todo = {name: text for name, text in todo.items() if not (Path(AUDIO) / name).exists()}
    for i, (name, text) in enumerate(todo.items(), 1):
        print(f"{i}/{len(todo)} {text}")
        path = speaker.speak(text, LANG)
        assert path.name == name, (path.name, name)


if __name__ == "__main__":
    main()
