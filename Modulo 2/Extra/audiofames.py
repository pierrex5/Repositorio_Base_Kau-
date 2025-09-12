from gtts import gTTS
import pygame
import os

texto = input("Digite o texto que deseja ouvir: ")
tts = gTTS(text=texto, lang='pt')
arquivo = "saida.mp3"
tts.save(arquivo)

pygame.mixer.init()
pygame.mixer.music.load(arquivo)
pygame.mixer.music.play()

# Aguarda até que a música termine
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)
