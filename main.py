from bs4 import BeautifulSoup
import requests
from tkinter import *

# FUNCTIONS
def search(event=None):
    keyword = user_input.get()
    # Deletes any previous results from the Listbox (output)
    output.delete(0, END)        
    # URL of the page you want to search
    url = f"https://www.bazos.sk/search.php?hledat={keyword}&rubriky=www&hlokalita=&humkreis=25&cenaod=&cenado=&Submit=H%C4%BEada%C5%A5&order=&kitx=ano"
    # Get the content of the page
    response = requests.get(url)
    if response.status_code == 200:
        # Load the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Identify the target elements (e.g., for product name and price)
        product_list = soup.find_all('div', class_='inzeraty')
        
        # Loop through the results and extract the information
        for product in product_list:
            name_element = product.find('h2', class_='nadpis')
            price_element = product.find('div', class_='inzeratycena')
            
            # Check if the elements exist
            if name_element and price_element:
                name = name_element.text.strip()
                price = price_element.text.strip()
                output.insert(END,f"{name}, Price: {price}")
                output.insert(END, '\n') 
                
    user_input.delete(0, END)

# ROOT - window
window =  Tk()
window.title("Product Hunter")
window.minsize(966,996)
window.resizable(width=False,height=False)

# BACKGROUND - add image
background = PhotoImage(file="images/background.png")
canvas = Canvas(window, width=966, height=996)
canvas.pack()
canvas.create_image(0,0, anchor=NW, image=background)

# FONT
big_font = font=("Helvetica",22)
small_font = font=("Helvetica",13,"italic")
mini_font = font=("Helvetica",11,"bold")

# INPUT - search field
user_input = Entry(window, bg="#ED820E",fg="#28231D",font=big_font,width=28)
user_input.focus()
user_input.place(x=385,y=35)
user_input.bind("<Return>", search)

# BUTTON - search
search_button = Button(window,text="Search",font=mini_font,bg="#FC6A03",fg="black",activebackground="orange",activeforeground="gray", borderwidth=5,relief="raised", command=search)
search_button.place(x=845,y=35)

# SCROLLBAR - add to listbox
scrollbar = Scrollbar(window, cursor="hand2", bg="#FC6A03")
scrollbar.place(x=910,y=101, width=20, height=861)

# OUTPUT - listbox
output = Listbox(window,bg="#28231D",fg="white",font=small_font,width=87, height=39, yscrollcommand=scrollbar.set)
output.place(x=35,y=100)
scrollbar.config(command=output.yview)

window.mainloop()
