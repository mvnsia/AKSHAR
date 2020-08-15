# Import the required module for text
# to speech conversion
from gtts import gTTS

# This module is imported so that we can
# play the converted audio
import os

# The text that you want to convert to audio
mytext = ' KISAH DESA GLOBAL proyek seni relasional Deskripsi: 128 cerita pendek berbahasa Inggris (maksimal 4 baris) dipamerkan di ruang galeri di Sekolah Menengah Seni Rakyat, Denmark. Mereka dibingkai dalam 20 bingkai A4 sekitar 6-7 cerita per frame. Mereka dikumpulkan melalui internet dalam periode Februari-April 2009. Mereka akan datang dari lebih dari 50 negara yang berbeda. Beberapa kontributor telah mengirimkan lebih dari satu story. Beberapa terlalu panjang maka saya telah mempersingkat; yang lain tidak dalam bahasa Inggris maka saya harus menerjemahkan mereka.'

# Language in which you want to convert
language = 'id'

# Passing the text and language to the engine,
# here we have marked slow=False. Which tells
# the module that the converted audio should
# have a high speed
myobj = gTTS(text=mytext, lang=language, slow=False)

# Saving the converted audio in a mp3 file named
# welcome
myobj.save("converted.mp3")

# Playing the converted file
os.system("mpg321 welcome.mp3") 