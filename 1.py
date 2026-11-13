# import tkinter as tk
# from random import choices
# from string import ascii_uppercase
# from audioplayer import AudioPlayer
# from PIL import Image, ImageTk, ImageSequence
#
# music = AudioPlayer("8bit.mp3")
# music.volume = 10
# music.play(block=False)
#
# label1 = tk.Tk()
# label1.title("keygen activator")
#
# WIDTH = 676
# HEIGHT = 954
# label1.geometry(f"{WIDTH}x{HEIGHT}")
# label1.resizable(False, False)
#
#
# gif_file = 'neon_borders.gif'
# img = Image.open(gif_file)
#
#
# gif_frames = [ImageTk.PhotoImage(frame.resize((WIDTH, HEIGHT))) for frame in ImageSequence.Iterator(img)]
# frame_index = 0
#
# def update_bg():
#     global frame_index
#     frame = gif_frames[frame_index]
#     canvas.itemconfig(gif_bg_id, image=frame)
#     frame_index = (frame_index + 1) % len(gif_frames)
#     label1.after(50, update_bg)
#
#
# canvas = tk.Canvas(label1, width=WIDTH, height=HEIGHT)
# canvas.pack(fill="both", expand=True)
#
#
# gif_bg_id = canvas.create_image(WIDTH // 2, HEIGHT // 2, image=gif_frames[0])
#
#
# bg_image = tk.PhotoImage(file='the-witcher-3.png')
# canvas.create_image(WIDTH // 2, HEIGHT // 2, image=bg_image)
#
# def generate_key(user_input):
#     word = user_input.upper()
#     alf = ascii_uppercase
#     letters = choices(word, k=6)
#     l = ''.join(letters)
#     nums = ''
#     for i in range(len(letters)):
#         nums += str((alf.index(letters[i])) % 10)
#     return f'{l[:3]}-{nums}-{l[-3:]}'
#
# def show_text():
#     user_input = entry.get()
#     label_output.config(text=f"key={generate_key(user_input)}")
#
#
# entry = tk.Entry(label1, font=("Consolas", 14), width=25, justify="center")
# button = tk.Button(label1, text="GENERATE", font=("Consolas", 13), command=show_text)
# label_output = tk.Label(label1, text="ваш ключ", font=("Consolas", 15), bg="white")
#
# canvas.create_window(WIDTH // 2, HEIGHT // 2 - 50, window=entry)
# canvas.create_window(WIDTH // 2, HEIGHT // 2, window=button)
# canvas.create_window(WIDTH // 2, HEIGHT // 2 + 60, window=label_output)
#
# label1.after(0, update_bg)
# label1.mainloop()
