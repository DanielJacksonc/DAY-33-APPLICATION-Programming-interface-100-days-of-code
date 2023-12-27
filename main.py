from tkinter import *
import requests



def get_quote():
    api_link = requests.get(url="https://api.kanye.rest")

    try:
        api_link.raise_for_status()
        data = api_link.json()
        quotes = data["quote"]
        canvas.itemconfig(quote_text, text=quotes)

    except api_link.status_code != 200:
        raise Exception("Bad Response")






window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text=" ", width=250, font=("Arial", 17, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)
get_quote()


window.mainloop()