# Audio module - sound effects using pygame
import pygame   
import os

# Initialize pygame mixer
def init_audio():
    pygame.mixer.init()

# Load and play sound effect
def play_sound(filename):
    try:
        sound = pygame.mixer.Sound(filename)
        sound.play()
    except pygame.error as e:
        print(f"Error loading sound: {e}")

#Keeping audio errors in check
def play_music(filename, loop=True):
    try:
        pygame.mixer.music.load(filename)
        pygame.mixer.music.play(loops=-1 if loop else 0)
    except pygame.error as e:
        print(f"Error loading music: {e}")

# Stop background music
def stop_music():
    pygame.mixer.music.stop()

# Stop audio
def stop_all():
    pygame.mixer.music.stop()
    pygame.mixer.stop()
"""
# Set volume
def set_volume(volume):
    pygame.mixer.music.set_volume(volume)

# Pause and resume music
def pause_music():
    pygame.mixer.music.pause()

def resume_music():
    pygame.mixer.music.unpause()
"""
# Quit pygame mixer
def quit_audio():
    pygame.mixer.quit()
