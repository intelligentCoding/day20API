from tkinter import *
import requests

QUOTE = "Click button to get Kanye Quote"
quote_text = ""

def get_quote():

    response = requests.get(url="https://api.kanye.rest")
    response.raise_for_status()

    data = response.json()
    canvas.itemconfig(quote_text, text=data["quote"])


window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=708.77, height=496.14)
background_img = PhotoImage(file="background.png")
canvas.create_image(354, 248, image=background_img)
quote_text = canvas.create_text(354, 248, text="Click button to get Kanye quote", width=250, font=("Arial", 15, "bold"),
                                fill="black")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)

window.mainloop()
