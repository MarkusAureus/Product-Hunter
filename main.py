# --- Third-party Library Imports ---
from bs4 import BeautifulSoup
import requests
from tkinter import *
from tkinter import font # Explicitly import font module for clarity

# --- Core Functions ---

def search(event=None):
    """
    Performs the web scraping when the user clicks the search button or presses Enter.
    It fetches data from bazos.sk, parses the HTML, and displays the results.
    The 'event=None' parameter allows this function to be bound to a key press event.
    """
    keyword = user_input.get()
    if not keyword:
        return # Do nothing if the input is empty

    # Deletes any previous results from the Listbox (output) before a new search.
    output.delete(0, END)
    
    # Construct the URL for the search query on bazos.sk.
    url = f"https://www.bazos.sk/search.php?hledat={keyword}&rubriky=www&hlokalita=&humkreis=25&cenaod=&cenado=&Submit=H%C4%BEada%C5%A5&order=&kitx=ano"
    
    try:
        # Send an HTTP GET request to the URL.
        response = requests.get(url)
        # Raise an exception for bad status codes (like 404 or 500).
        response.raise_for_status()
        
        # Load the HTML content into BeautifulSoup for parsing.
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all 'div' elements with the class 'inzeraty', which contain the listings.
        product_list = soup.find_all('div', class_='inzeraty')
        
        if not product_list:
            output.insert(END, "No results found for your query.")
            return

        # Loop through the results and extract the desired information.
        for product in product_list:
            name_element = product.find('h2', class_='nadpis')
            price_element = product.find('div', class_='inzeratycena')
            
            # Check if both the name and price elements were found to avoid errors.
            if name_element and price_element:
                name = name_element.text.strip()
                price = price_element.text.strip()
                # Insert the formatted product name and price into the output Listbox.
                output.insert(END, f"{name}, Price: {price}")
                output.insert(END, '') # Add a blank line for better readability
                
    except requests.exceptions.RequestException as e:
        # Handle network-related errors (e.g., no internet connection).
        output.delete(0, END)
        output.insert(END, f"Network Error: {e}")
    except Exception as e:
        # Handle other potential errors during scraping.
        output.delete(0, END)
        output.insert(END, f"An error occurred: {e}")
    finally:
        # Clear the user input field after the search is complete.
        user_input.delete(0, END)


# --- GUI Initialization ---

# Create the main application window (root).
window = Tk()
window.title("Product Hunter")
window.minsize(966, 996)
window.resizable(width=False, height=False) # Lock the window size.

# Set up the background image using a Canvas widget.
# This allows other widgets to be placed on top of the image.
try:
    background = PhotoImage(file="images/background.png")
    canvas = Canvas(window, width=966, height=996)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, anchor=NW, image=background)
except TclError:
    print("Warning: Could not load background image 'images/background.png'.")


# --- Font Definitions ---
big_font = font.Font(family="Helvetica", size=22)
small_font = font.Font(family="Helvetica", size=13, slant="italic")
mini_font = font.Font(family="Helvetica", size=11, weight="bold")

# --- UI Widget Creation and Placement ---

# Input field for the user's search query.
user_input = Entry(window, bg="#ED820E", fg="#28231D", font=big_font, width=28)
user_input.focus() # Set initial focus to this entry field.
user_input.place(x=385, y=35)
# Bind the <Return> (Enter) key to the search function.
user_input.bind("<Return>", search)

# Search button to trigger the scraping process.
search_button = Button(window, text="Search", font=mini_font, bg="#FC6A03", fg="black",
                       activebackground="orange", activeforeground="gray", borderwidth=5,
                       relief="raised", command=search)
search_button.place(x=845, y=35)

# Scrollbar for the output listbox.
scrollbar = Scrollbar(window, cursor="hand2", bg="#FC6A03")
scrollbar.place(x=910, y=101, width=20, height=861)

# Output Listbox to display the scraped results.
output = Listbox(window, bg="#28231D", fg="white", font=small_font, width=87, height=39,
                 yscrollcommand=scrollbar.set)
output.place(x=35, y=100)

# Link the scrollbar to the listbox's y-view.
scrollbar.config(command=output.yview)


# --- Main Event Loop ---
# Starts the Tkinter event loop, which listens for user actions.
window.mainloop()
