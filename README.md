# Product Hunter

Product Hunter is a GUI application built with Python, which allows users to search for products on Bazos.sk, a popular Slovak classifieds website. It scrapes and displays product names and prices based on a search keyword, making it easier to browse items directly from the application.

## Table of Contents
- Features
- Technologies Used
- Installation
- Usage
- License

## Features
- **Search Functionality**: Users can search for products on Bazos.sk by entering keywords.
- **BeautifulSoup Web Scraping**: Scrapes product names and prices directly from Bazos.sk.
- **Tkinter GUI**: Provides a simple graphical interface with a search field, button, and scrollable listbox to display results.
- **Real-Time Updates**: Results are displayed in real time based on the user’s search query.

## Technologies Used
- **Python**: Core programming language used.
- **Tkinter**: For creating the graphical interface.
- **BeautifulSoup**: For web scraping the product data.
- **Requests**: To send HTTP requests to the Bazos.sk website.

## Installation

### Prerequisites
- Python 3.6 or later
- Internet connection for accessing Bazos.sk

### Setup Instructions
1. **Clone this repository**:
   ```bash
   git clone https://github.com/your-username/product-hunter.git
   cd product-hunter
   ```

2. **Install the required libraries**:
   ```bash
   pip install requests beautifulsoup4
   ```

3. **Run the Application**:
   ```bash
   python product_hunter.py
   ```

4. **Add Background Image**:
   - Place an image named `background.png` inside the `images` folder in the project directory.

## Usage

1. Run the program. 
2. Enter a keyword in the search field (e.g., "bicycle") and press **Enter** or click **Search**.
3. Results matching the keyword, including product names and prices, will display in the listbox below.
4. Use the scrollbar to browse through the list of results.

## Code Overview

- **`search()`**: This function takes the user’s input keyword, fetches the HTML from Bazos.sk, and parses it to find product details.
- **Tkinter Widgets**: Used to create input fields, buttons, listbox, and scrollbar.
  
## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
