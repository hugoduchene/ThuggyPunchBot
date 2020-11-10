from gtts import gTTS
from data.punchline import PUNCHLINE

for i, content in enumerate(PUNCHLINE['punch_content']):
    tts = gTTS(content[i], lang='fr')
    tts.save('../assets/mp3/' + str(i) + '.mp3')
