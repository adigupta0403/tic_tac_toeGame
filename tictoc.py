from tkinter import *
import random

def next_turn(row, column):

    global player

    if buttons[row][column]['text'] == "" and check_winner() is False:

        if player == players[0]:

            buttons[row][column]['text'] = player

            if check_winner() is False:
                player = players[1]
                label.config(text=(players[1]+" Turn"))

            elif check_winner() is True:
                label.config(text=(players[0]+" Wins"))

            elif check_winner() == "Tie":
                label.config(text="Tie!")

        else:

            buttons[row][column]['text'] = player

            if check_winner() is False:
                player = players[0]
                label.config(text=(players[0]+" Turn"))

            elif check_winner() is True:
                label.config(text=(players[1]+" Wins"))

            elif check_winner() == "Tie":
                label.config(text="Tie!")

def check_winner():

    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            buttons[row][0].config(bg="red")
            buttons[row][1].config(bg="red")
            buttons[row][2].config(bg="red")
            return True

    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
            buttons[0][column].config(bg="red")
            buttons[1][column].config(bg="red")
            buttons[2][column].config(bg="red")
            return True

    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        buttons[0][0].config(bg="red")
        buttons[1][1].config(bg="red")
        buttons[2][2].config(bg="red")
        return True

    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        buttons[0][2].config(bg="red")
        buttons[1][1].config(bg="red")
        buttons[2][0].config(bg="red")
        return True

    elif empty_spaces() is False:

        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg="green")
        return "Tie"

    else:
        return False


def empty_spaces():

    spaces = 9

    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] != "":
                spaces -= 1

    if spaces == 0:
        return False
    else:
        return True

def new_game():

    global player

    player = random.choice(players)

    label.config(text=player+" Turn")

    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="",bg="#F0F0F0")


window = Tk()
window.title("Tic-Tac-Toe")
window.configure(bg="grey")
window.geometry("1000x700")
window.resizable(False, False)
players = ["X","O"]
player = random.choice(players)
buttons = [[0,0,0],
           [0,0,0],
           [0,0,0]]


top_frame = Frame(
    window,
    bg='#5D6D7E',
    width=1000,
    height=250
)
top_frame.place(x=0, y=0)



game_title = Label(
    top_frame,
    bg='#5D6D7E',
    fg='white',
    text='Tic Tac Toe using Python',
    font=('', 48)
)
game_title.place(x=135, y=0)


label = Label(top_frame, text=player + " Turn", font=('arial',30), bg = "#5D6D7E", fg ="white")
label.place(x=440,y= 200)

reset_button = Button(top_frame, text="Restart Game", font=('arial',30),bg = "#5D6D7E", fg ="white", command=new_game)
reset_button.place(x=360, y=95)

bottom_frame = Frame(
    window,
    bg='#FFFFFF',
    width=400,
    height=400
)
bottom_frame.place(x=265, y=300)
# frame = Frame(window)
# frame.pack()

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(bottom_frame, text="",font=('consolas',40), width=5, height=1,
                                      command= lambda row=row, column=column: next_turn(row,column))
        buttons[row][column].grid(row=row,column=column)
