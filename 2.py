import tkinter as tk
import random
from string import ascii_uppercase
from audioplayer import AudioPlayer
from PIL import Image, ImageTk, ImageSequence

# --- Настройка музыки ---
music = AudioPlayer("8bit.mp3")
music.volume = 4
music.play(block=False)

# --- Настройка главного окна ---
root = tk.Tk()
root.title("keygen activator")

WIDTH = 864
HEIGHT = 1152
root.geometry(f"{WIDTH}x{HEIGHT}")
root.resizable(False, False)


gif_file = 'neon_border.gif'
img = Image.open(gif_file)

gif_frames = [ImageTk.PhotoImage(frame.resize((WIDTH, HEIGHT))) for frame in ImageSequence.Iterator(img)]
frame_index = 0


def update_bg():
    global frame_index
    frame = gif_frames[frame_index]
    canvas.itemconfig(gif_bg_id, image=frame)
    frame_index = (frame_index + 1) % len(gif_frames)
    root.after(50, update_bg)


canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)
canvas.pack(fill="both", expand=True)

gif_bg_id = canvas.create_image(WIDTH // 2, HEIGHT // 2, image=gif_frames[0])

bg_image = tk.PhotoImage(file='Dark_souls.png')
canvas.create_image(WIDTH // 2, HEIGHT // 2, image=bg_image)



def get_letter_weight(char):
    return ascii_uppercase.index(char) + 1


def generate_valid_block(length):
    while True:
        block = random.choices(ascii_uppercase, k=length)
        total_sum = sum(get_letter_weight(char) for char in block)
        average = total_sum / length
        if 10 <= average <= 15:
            return ''.join(block)


def generate_key():
    block1 = generate_valid_block(5)
    block2 = generate_valid_block(4)
    block3 = generate_valid_block(4)

    return f'{block1}-{block2}-{block3}'


def show_text():
    label_output.config(text=f"key={generate_key()}")


button = tk.Button(root, text="GENERATE", font=("Consolas", 11), command=show_text)
label_output = tk.Label(root, text="your keys", font=("Consolas", 12), bg="white")

canvas.create_window(WIDTH // 2, HEIGHT // 2 - 20, window=button)
canvas.create_window(WIDTH // 2, HEIGHT // 2 + 40, window=label_output)


root.after(0, update_bg)
root.mainloop()