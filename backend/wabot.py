import json
import requests

# Classe do Bot de Whatsapp em Python
class WABot():
  def __init__(self, options):
    self.APIUrl = options["APIUrl"]
    self.token = options["token"]

  def send_requests(self, method, data):
    url = f"{self.APIUrl}{method}?token={self.token}"
    headers = {'Content-type': 'application/json'}
    answer = requests.post(url, data=json.dumps(data), headers=headers)
    return answer.json()

  def send_file(self, chatId, filename, url):
    response = self.send_requests("sendFile", {"chatId": chatId, "body": url, "filename": filename})
    print("[SENDFILE]")
    print(response)

  def send_fileBase64(self, chatId, filename, fileBase64):
    response = self.send_requests("sendFile", {"chatId": chatId, "body": fileBase64, "filename": filename})
    print("[SENDFILE][BASE64]")
    print(response)

  def send_audio(self, chatID, audioFileBase64):
    response = self.send_requests("sendPTT", {"audio": audioFileBase64, "chatId": chatID})
    print("[SENDAUDIO]")
    print(response)
