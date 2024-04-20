from elevenlabs import Voice, VoiceSettings, play
from elevenlabs.client import ElevenLabs

client = ElevenLabs(
  api_key="7cca14c36c31fb428b03c649e3ae352e", # Defaults to ELEVEN_API_KEY
)

audio = client.generate(
    text="Juliana cara di banana",
    voice=Voice(
        voice_id='tS45q0QcrDHqHoaWdCDR',
        settings=VoiceSettings(stability=0.71, similarity_boost=0.5, style=0.0, use_speaker_boost=True)
    )
)

play(audio)





# *********************


# import pyttsx3

# # Crie um objeto da classe pyttsx3
# engine = pyttsx3.init()

# # Texto a ser convertido em áudio
# texto = "Vai tomar banho"

# # Defina a propriedade de voz, se necessário
# voices = engine.getProperty('voices')  # Obtenha todas as vozes disponíveis
# # Você pode imprimir voices para ver todas as vozes disponíveis e escolher a que deseja usar
# # Por exemplo, para usar a voz feminina, você pode definir engine.setProperty('voice', voices[1].id)
# # Por padrão, a voz masculina é usada
# # engine.setProperty('voice', voices[1].id)

# # Converta o texto em fala e reproduza o áudio
# engine.say(texto)
# engine.runAndWait()



# ***************************

# import requests
# import pygame
# from io import BytesIO

# pygame.init()

# url = "https://api.elevenlabs.io/v1/text-to-speech/tS45q0QcrDHqHoaWdCDR"

# headers = {
#   "Accept": "audio/mpeg",
#   "Content-Type": "application/json",
#   "xi-api-key": "a0aab2987f2437fcd3954ea9ce1c8a5f"
# }

# data = {
#   "text": "esses caras são muito vagabundos",
#   "model_id": "eleven_monolingual_v1",
#   "voice_settings": {
#     "stability": 0.3,
#     "similarity_boost": 0.5
    
#   }
# }

# response = requests.post(url, json=data, headers=headers)
# if response.status_code == 200:
#     audio_data = BytesIO(response.content)
#     pygame.mixer.music.load(audio_data)
#     pygame.mixer.music.play()
#     while pygame.mixer.music.get_busy():
#         pygame.time.Clock().tick(10)  # Verifique a cada 10 milissegundos se a música parou de tocar
# else:
#     print("Falha ao recuperar o áudio. Código de status:", response.status_code)


