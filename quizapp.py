from tkinter import *
import random
x, y, count = 0, 0, 0
list1 = ["+", "-", "*", "//"]
color = ""

root = Tk()
root.geometry("720x720")
root.minsize(720, 720)
root.maxsize(720, 720)


def game():

    # Level Function
    def level(diff):
        global x, y, color
        if diff == 1:
            x, y = 1, 10
            color = "#7BFF57"
        elif diff == 2:
            x, y = 10, 20
            color = "#FFEC47"
        elif diff == 3:
            x, y = 20, 100
            color = "#FF4747"
        elif diff == 4:
            x, y = 100, 1000
            color = "#9157FF"
        for widgets in root.winfo_children():
            widgets.destroy()
        first_question()

    # MENU
    root.configure(bg="#F0F0F0")
    text1 = Label(root, text='MATH QUIZ', font='Calibri 64')
    text1.place(x=150, y=150)

    easy = Button(root, text="Easy", font="Calibri 24", width=9, bg="#7BFF57", relief="flat", command=lambda: level(1))
    easy.place(x=272, y=300)

    medium = Button(root, text="Medium", font="Calibri 24", width=9, bg="#FFEC47", relief="flat", command=lambda: level(2))
    medium.place(x=272, y=400)

    hard = Button(root, text="Hard", font="Calibri 24", width=9, bg="#FF4747", relief="flat", command=lambda: level(3))
    hard.place(x=272, y=500)

    impossible = Button(root, text="Impossible", font="Calibri 24", width=9, bg="#9157FF", relief="flat", command=lambda: level(4))
    impossible.place(x=272, y=600)

    # QUIZ
    def first_question():
        global count, color, levelnum
        x1, y1, total = 0, 0, 0,
        question = ''
        list2 = []
        x1 = random.randint(x, y)
        y1 = random.randint(x, y)
        count += 1

        if y1 > x1:
            y1 = random.randint(x, y)
        r = random.choice(list1)

        question += str(x1) + r + str(y1)

        if r == "//":
            r = "÷"
        if r == "*":
            r = "x"
        question_text = str(x1) + " " + str(r) + " " + str(y1)
        total = str(eval(question))
        print(total)
        list2.append(int(total))
        while len(list2) < 4:
            k = random.randint(int(total) - x1, int(total) + y1)
            if k != int(total) or k not in list2:
                list2.append(k)

        random.shuffle(list2)
        question_label = Label(root, text=question_text, font="Calibri 64")
        question_label.place(x=300, y=150)

        choice1 = Button(root, text=list2[0], font="Calibri 24", width=7, command=lambda num=list2[0]: check(num, 1))
        choice1.place(x=100, y=300)

        choice2 = Button(root, text=list2[1], font="Calibri 24", width=7, command=lambda num=list2[1]: check(num, 2))
        choice2.place(x=250, y=300)

        choice3 = Button(root, text=list2[2], font="Calibri 24", width=7, command=lambda num=list2[2]: check(num, 3))
        choice3.place(x=400, y=300)

        choice4 = Button(root, text=list2[3], font="Calibri 24", width=7, command=lambda num=list2[3]: check(num, 4))
        choice4.place(x=550, y=300)

        levelnum = Label(root, text=count, font='Calibri 24', width=2, bg=color, relief=FLAT)
        levelnum.place(x=680, y=0)

        def destroy():
            choice1.destroy(), choice2.destroy(), choice3.destroy(), choice4.destroy(), question_label.destroy(),

        def disable_buttons():
            choice1.configure(state=DISABLED), choice2.configure(state=DISABLED),
            choice3.configure(state=DISABLED), choice4.configure(state=DISABLED)

        def restart():
            global congrats, reset, levelnum
            destroy(), congrats.destroy(), reset.destroy(), levelnum.destroy(), game()

        def check(n, m):
            global count, congrats, reset
            if str(n) != str(total) and m == 1:
                choice1.configure(bg="red")
                root.after(1000, first_question)
                root.after(1000, destroy)
                disable_buttons()
                count = 0
            elif str(n) != str(total) and m == 2:
                choice2.configure(bg="red")
                root.after(1000, first_question)
                root.after(1000, destroy)
                disable_buttons()
                count = 0
            elif str(n) != str(total) and m == 3:
                choice3.configure(bg="red")
                root.after(1000, first_question)
                root.after(1000, destroy)
                disable_buttons()
                count = 0
            elif str(n) != str(total) and m == 4:
                choice4.configure(bg="red")
                root.after(1000, first_question)
                root.after(1000, destroy)
                disable_buttons()
                count = 0

            else:
                destroy()
                levelnum.configure(text=count)
                if count != 20:
                    first_question()
                elif count == 20:
                    root.configure(bg=color)
                    congrats = Label(root, text="CONGRATULATIONS", font="Calibri 48", width=20)
                    congrats.place(x=25, y=300)

                    reset = Button(root, text="Restart", font='Calibri 24', width=10, relief=FLAT, command=restart)
                    reset.place(x=300, y=400)



game()
root.mainloop()
