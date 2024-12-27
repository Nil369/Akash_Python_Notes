import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import pyshorteners

def shorten_url():
    # Get the URL from the user input
    original_url = url_entry.get()
    if not original_url:
        messagebox.showerror("Input Error", "Please enter a URL!")
        return
    
    try:
        # Shorten the URL using tinyurl
        shortener = pyshorteners.Shortener()
        shortened_url = shortener.tinyurl.short(original_url)

        # Display the shortened URL in the output field & clear any existing text
        output_entry.delete(0, tk.END)  
        output_entry.insert(0, shortened_url)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to shorten URL: {e}")

# Create the Tkinter window
app = tk.Tk()
app.title("URL Shortener")
app.geometry("500x350")
app.resizable(False, False)

# Load and set the background image using Pillow
bg_image = Image.open("background.jpg") 
bg_image = bg_image.resize((500, 350), Image.Resampling.LANCZOS)  
bg_photo = ImageTk.PhotoImage(bg_image)

canvas = tk.Canvas(app, width=500, height=350)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=bg_photo, anchor="nw")

# Add widgets on top of the canvas
url_label = tk.Label(app, text="Enter URL:", font=("Arial", 12,"bold"), bg="#ffffff", fg="black")
url_label.place(x=50, y=50)

url_entry = tk.Entry(app, width=40, font=("Arial", 12,"bold"))
url_entry.place(x=150, y=50)

shorten_button = tk.Button(
    app, text="Shorten URL", font=("Arial", 12,"bold"), command=shorten_url,
    bg="green", fg="white", relief="raised", borderwidth=0,
    highlightbackground="green", highlightthickness=2
)
shorten_button.place(x=200, y=100)

output_label = tk.Label(app, text="Shortened URL:", font=("Arial", 12,"bold"), bg="#ffffff", fg="black")
output_label.place(x=15, y=150)

output_entry = tk.Entry(app, width=40, font=("Arial", 10,"bold"), fg="blue")
output_entry.place(x=150, y=150)
output_entry.config(state="normal")
output_entry.bind("<FocusIn>", lambda event: output_entry.select_range(0, tk.END))  # Auto-select text

# Run the app
app.mainloop()
