import tkinter
import tkintermapview
import phonenumbers
import tkinter as tk
from key import key
from phonenumbers import geocoder
from phonenumbers import carrier
from tkinter import *
from opencage.geocoder import OpenCageGeocode

def close_window():
    root.destroy()


def wel_page():
    global root
    welcome_text = "Welcome to Phone Tracking System"
    root = tk.Tk()
    root.title("Welcome Page")
    root.geometry("600x600")
    label = tk.Label(root, text=welcome_text, font=("Arial", 20))
    label.pack(padx=50, pady=50)
    welcome_text1 = "Click Next to Know the Location"
    label = tk.Label(root, text=welcome_text1, font=("Arial", 11))
    label.pack(padx=5, pady=5)

    button = tk.Button(root, text="Next",width=4,height=2, command=close_window)
    button.pack(pady=30)
    root.mainloop()

wel_page()

root = tkinter.Tk()
root.geometry("600x600")
label1 = Label(text="Phone Number Tracker ")
label1.pack()

def getResult():
    num = number.get("1.0", END)
    num1 = phonenumbers.parse(num)
    location = geocoder.description_for_number(num1, "en")
    service_provider = carrier.name_for_number(num1, "en")
    ocg = OpenCageGeocode(key)
    query = str(location)
    results = ocg.geocode(query)
    lat = results[0]['geometry']['lat']
    lng = results[0]['geometry']['lng']
    my_label = LabelFrame(root)
    my_label.pack(pady=20)
    map_widget = tkintermapview.TkinterMapView(my_label, width=450, height=450, corner_radius=0)
    map_widget.set_position(lat, lng)
    map_widget.set_marker(lat, lng, text = "Phone Location")
    map_widget.set_zoom(4)
    map_widget.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
    map_widget.pack()

    adr = tkintermapview.convert_coordinates_to_address(lat, lng )
    result.insert(END, "The country of this number is: " + location)
    result.insert(END, "\nThe sim card of this number is: " + service_provider)
    result.insert(END, "\nLatitude is: " + str(lat))
    result.insert(END, "\nLongitude is:" + str(lng))
number = Text(height=1)
number.pack()
button = Button(text="search", command=getResult)
button.pack(pady=10, padx=100)
result = Text(height=7)
result.pack()

root.mainloop()