import wabot
import speech
import soundfile
import base64

# Get user speech text and save to a file
speechBot = speech.SpeechBot({"region": "brazilsouth", "key": "5c1267517689495aacddb9eb154a01c0"})
speechBot.run("teste-karine-2.wav")

# TODO: change to use Opus Codec (maybe using ffmpeg lib)
data, samplerate = soundfile.read("teste-karine-2.wav")
soundfile.write("teste-karine-final.ogg", data, samplerate)

# Instantiate a WP bot
bot = wabot.WABot({
  "token": "eckcxyz6ilztk3kp",
  "APIUrl": "https://api.chat-api.com/instance138610/"})

# Transform file content to a Base64 file string
data = open("teste-karine-final.ogg","rb").read()
dataBase64Binary = base64.b64encode(data)
dataBase64 = str(dataBase64Binary, "ascii", "ignore")
dataAudioBase64 = "data:audio/ogg;base64," + dataBase64

# Send audio file base64 string as a file
bot.send_fileBase64("5511984281584@c.us", "teste.ogg", dataAudioBase64)

# Send audio file base64 string as an audio
bot.send_audio("5511984281584@c.us", dataAudioBase64)
