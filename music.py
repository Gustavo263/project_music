from tkinter import *
from PIL import Image, ImageTk
from pygame import mixer
import os

janela = Tk()
janela.title("")
janela.geometry("460x255")
janela.configure(background="#feffff")
janela.resizable(width=FALSE, height=FALSE)

# Configurando Interface

left = Frame(janela, width=150, height=150, bg="#2e2d2c")
left.grid(row=0, column=0, pady=1, padx=1, sticky=NSEW)

right = Frame(janela, width=250, height=200, bg="#2e2d2c")
right.grid(row=0, column=1, pady=1, padx=0, sticky=NSEW)

underside = Frame(janela, width=404, height=100, bg="#2e2d2c")
underside.grid(row=1, column=0, columnspan=3, pady=1, padx=0, sticky=NSEW)

# Configurando o frame left

img_1 = Image.open("image/icon_spotify.png")
img_1 = img_1.resize((130, 130))
img_1 = ImageTk.PhotoImage(img_1)

l_logo = Label(left, height=130, image=img_1, compound=LEFT, padx=10, anchor="nw",
               font="ivy 16 bold", bg="#2e2d2c", fg="#2e2d2c")
l_logo.place(x=6, y=15)


# funções

def play_music():
    rodando = listbox.get(ACTIVE)
    l_rodando["text"] = rodando
    mixer.music.load(rodando)
    mixer.music.play()


def pause_music():
    frase = ["Música pausada..."]
    for f in frase:
        l_rodando["text"] = f
        mixer.music.pause()


def resume_music():
    rodando = listbox.get(ACTIVE)
    l_rodando["text"] = rodando
    mixer.music.unpause()


def stop_music():
    rodando = listbox.get(ACTIVE)
    l_rodando["text"] = "Música..."
    mixer.music.load(rodando)
    mixer.music.stop()


def next_music():
    tocando = l_rodando["text"]
    index = musicas.index(tocando)

    novo_index = index + 1
    tocando = musicas[novo_index]

    mixer.music.load(tocando)
    mixer.music.play()

    listbox.delete(0, END)
    mostrar()

    listbox.select_set(novo_index)
    listbox.config(selectmode=SINGLE)
    l_rodando["text"] = tocando


def previous_music():
    tocando = l_rodando["text"]
    index = musicas.index(tocando)

    novo_index = index - 1
    tocando = musicas[novo_index]

    mixer.music.load(tocando)
    mixer.music.play()

    listbox.delete(0, END)
    mostrar()

    listbox.select_set(novo_index)
    listbox.config(selectmode=SINGLE)
    l_rodando["text"] = tocando


def plus_volume():
    if plus == plus:
        mixer.music.set_volume(+0.2)


def minus_volume():
    mixer.music.set_volume(0.1)


lista = ["Melhor Dia 7 - Sossego", "Poesia Acústica 12 - Pra Sempre", "Sigo sozinho"]
# Configurando o frame right

listbox = Listbox(right, width=41, height=10, selectmode=SINGLE, font="arial 9 bold",
                  bg="#2e2d2c", fg="#feffff")
listbox.grid(row=0, column=0)

s = Scrollbar(right)
s.grid(row=0, column=1, sticky=NSEW)
listbox.config(yscrollcommand=s.set)
s.config(command=listbox.yview)

# Configurando o frame underside

l_rodando = Label(underside, text="Música...", width=58, justify=LEFT,
                  anchor="nw", font="ivy 10", bg="#feffff", fg="#2e2d2c")
l_rodando.place(x=0, y=1)

img_2 = Image.open("image/icon_rewind.png")
img_2 = img_2.resize((30, 30))
img_2 = ImageTk.PhotoImage(img_2)
rewind = Button(underside, command=previous_music, width=40, height=40, image=img_2,
                font="ivy 10 bold", relief=RAISED, overrelief=RIDGE,
                bg="#2e2d2c", fg="#feffff")
rewind.place(x=38, y=35)

img_3 = Image.open("image/icon_play.png")
img_3 = img_3.resize((30, 30))
img_3 = ImageTk.PhotoImage(img_3)
play = Button(underside, command=play_music, width=40, height=40, image=img_3,
              font="ivy 10 bold", relief=RAISED, overrelief=RIDGE,
              bg="#2e2d2c", fg="#feffff")
play.place(x=84, y=35)

img_4 = Image.open("image/icon_next.png")
img_4 = img_4.resize((30, 30))
img_4 = ImageTk.PhotoImage(img_4)
next = Button(underside, command=next_music, width=40, height=40, image=img_4,
              font="ivy 10 bold", relief=RAISED, overrelief=RIDGE,
              bg="#2e2d2c", fg="#feffff")
next.place(x=130, y=35)

img_5 = Image.open("image/icon_pause.png")
img_5 = img_5.resize((30, 30))
img_5 = ImageTk.PhotoImage(img_5)
pause = Button(underside, command=pause_music, width=40, height=40, image=img_5,
               font="ivy 10 bold", relief=RAISED, overrelief=RIDGE,
               bg="#2e2d2c", fg="#feffff")
pause.place(x=176, y=35)

img_6 = Image.open("image/icon_resume.png")
img_6 = img_6.resize((30, 30))
img_6 = ImageTk.PhotoImage(img_6)
resume = Button(underside, command=resume_music, width=40, height=40, image=img_6,
                font="ivy 10 bold", relief=RAISED, overrelief=RIDGE,
                bg="#2e2d2c", fg="#feffff")
resume.place(x=222, y=35)

img_7 = Image.open("image/icon_stop.png")
img_7 = img_7.resize((30, 30))
img_7 = ImageTk.PhotoImage(img_7)
stop = Button(underside, command=stop_music, width=40, height=40, image=img_7,
              font="ivy 10 bold", relief=RAISED, overrelief=RIDGE,
              bg="#2e2d2c", fg="#feffff")
stop.place(x=268, y=35)

img_8 = Image.open("image/icon_plus.png")
img_8 = img_8.resize((30, 30))
img_8 = ImageTk.PhotoImage(img_8)
plus = Button(underside, command=plus_volume, width=40, height=40, image=img_8,
              font="ivy 10 bold", relief=RAISED, overrelief=RIDGE,
              bg="#2e2d2c", fg="#feffff")
plus.place(x=340, y=35)

img_9 = Image.open("image/icon_minus.png")
img_9 = img_9.resize((30, 30))
img_9 = ImageTk.PhotoImage(img_9)
minus = Button(underside, command=minus_volume, width=40, height=40, image=img_9,
               font="ivy 10 bold", relief=RAISED, overrelief=RIDGE,
               bg="#2e2d2c", fg="#feffff")
minus.place(x=387, y=35)

os.chdir(r"C:\Users\Gustavo\Downloads\musicas_python")
musicas = os.listdir()


def mostrar():
    for m in musicas:
        listbox.insert(END, m)


mostrar()

mixer.init()

janela.mainloop()
