import azure.cognitiveservices.speech as speechsdk

class SpeechBot():
  def __init__(self, options):
    self.region = options["region"]
    self.speechKey = options["key"]
    self.config = speechsdk.SpeechConfig(subscription=self.speechKey, region=self.region)

  def saveAudioFile(self, result, filename):
    audioStream = speechsdk.AudioDataStream(result)
    audioStream.save_to_wav_file(filename)

  def getUserInput(self):
    print("Type some text that you want to speak...")
    text = input()
    return text

  def run(self, filename):
    synthesizer = speechsdk.SpeechSynthesizer(speech_config=self.config)
    userInput = self.getUserInput()
    result = synthesizer.speak_text_async(userInput).get()
    self.saveAudioFile(result, filename)
