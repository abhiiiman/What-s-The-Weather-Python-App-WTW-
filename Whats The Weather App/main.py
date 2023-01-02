# importing the libs here.
from pathlib import Path
from tkinter import *
from tkinter import messagebox
from gtts import gTTS
import time
import requests
import os
import webbrowser

# creating the path variable.
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./bright_assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

# collecting the api data here.
def get_data():
    try:
        global condition, temp, feels_like, temp_min, temp_max, pressure, humidity, wind_speed, sunrise, sunset, city
        city = entry_1.get()
        if city.isdigit():
            messagebox.showwarning("Invalid Data", "Only Alphabets Are Allowed !")
        else:
            api = "http://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=0aa1585fe404fe991c26a0ecb44364bd"
            json_data = requests.get(api).json()

            # getting these weather props here.
            condition = json_data["weather"][0]["main"]
            temp = int(json_data["main"]["temp"] - 273.15)
            feels_like = int(json_data["main"]["feels_like"] - 273.15)
            temp_min = int(json_data["main"]["temp_min"] - 273.15)
            temp_max = int(json_data["main"]["temp_max"] - 273.15)
            pressure = json_data["main"]["pressure"]
            humidity = json_data["main"]["humidity"]
            wind_speed = json_data["wind"]["speed"]
            sunrise = time.strftime("%I:%M:%S", time.gmtime(json_data["sys"]["sunrise"] - 21600))
            sunset = time.strftime("%I:%M:%S", time.gmtime(json_data["sys"]["sunset"] - 21600))

            # updating the values here.
            feels_like_text.configure(text=f"Feels Like {feels_like}°C")
            temp_text.configure(text=f"{temp}°C")
            min_text.configure(text=f"{temp_min}°C")
            max_text.configure(text=f"{temp_max}°C")
            sunrise_text.configure(text=f"{sunrise} AM")
            sunset_text.configure(text=f"{sunset} PM")
            condition_text.configure(text=f"Overall : {condition}")
            humidity_text.configure(text=f"{humidity}")
            wind_speed_text.configure(text=f"{wind_speed} Mph")
            pressure_text.configure(text=f"{pressure} Pa")

            if condition == "Rain":
                image_data.configure(file=relative_to_assets("bright_rain.png"))
            elif condition == "Clouds":
                image_data.configure(file=relative_to_assets("bright_clouds.png"))
            elif condition == "Thunderstorm":
                image_data.configure(file=relative_to_assets("bright_thunderstorm.png"))
            elif condition == "Mist":
                image_data.configure(file=relative_to_assets("bright_mist.png"))
            elif condition == "Drizzle":
                image_data.configure(file=relative_to_assets("bright_drizzle.png"))
            elif condition == "Snow":
                image_data.configure(file=relative_to_assets("bright_snow.png"))
            elif condition == "Clear":
                image_data.configure(file=relative_to_assets("bright_clear.png"))
            else:
                image_data.configure(file=relative_to_assets("bright_default.png"))

    # handling the exception here.
    except Exception as city_not_found_error:
        print(city_not_found_error)
        messagebox.showerror("CityNotFound", "Invalid City!\nTry Again With Different Name.")
        entry_1.delete(0, END)

def call_back(event):
    get_data()

def speak():
    mytext = f"hi there, i am your weather assistant, here is your weather details.As you searched for the city {city}, so let me tell you that the temperature here is {temp} degree celcius, but it feels like {feels_like} degree celcius only, the minimum temperature of {city} is {temp_min} degree celcius and the maximum is {temp_max} degree celcius. just to add on, if you want to do your early morning yoga exercise then the time {sunrise[1]}:{sunrise[3:5]} AM is just perfect for you, cause it's the sunrise time ! and if you want to enjoy the sunset today, then just be ready before {sunset[1]}:{sunset[3:5]} PM. now moving on to the another section, so today's humidity level is {humidity}.and the wind will blow with the speed of {wind_speed} miles per hour, i don't know you will feel or not but The pressure you are going to feel today will be of {pressure} pascals. so that's all about today's weather details. have a great day. thank you. "
    language = 'en'
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save("weather.mp3")
    os.system("weather.mp3")

def contact():
    yt = "https://www.youtube.com/channel/UC1uhivO7SmNr4I5KwJufW4A"
    webbrowser.open(yt)


def about():
    messagebox.showinfo("About App", "You Are About To PLay A Video !")
    yt_video_link = "https://youtu.be/6v_jf6pKBaQ"
    webbrowser.open(yt_video_link)

def toggle_theme():
    window.destroy()
    # creating the path variable here.
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path("./dark_assets")

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)
    
    # collecting the api data here.
    def get_data():
        try:
            global condition, temp, feels_like, temp_min, temp_max, pressure, humidity, wind_speed, sunrise, sunset, city
            city = entry_1.get()
            if city.isdigit():
                messagebox.showwarning("Invalid Data", "Only Alphabets Are Allowed !")
            else:
                api = "http://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=0aa1585fe404fe991c26a0ecb44364bd"
                json_data = requests.get(api).json()

                # getting these weather props here.
                condition = json_data["weather"][0]["main"]
                temp = int(json_data["main"]["temp"] - 273.15)
                feels_like = int(json_data["main"]["feels_like"] - 273.15)
                temp_min = int(json_data["main"]["temp_min"] - 273.15)
                temp_max = int(json_data["main"]["temp_max"] - 273.15)
                pressure = json_data["main"]["pressure"]
                humidity = json_data["main"]["humidity"]
                wind_speed = json_data["wind"]["speed"]
                sunrise = time.strftime("%I:%M:%S", time.gmtime(json_data["sys"]["sunrise"] - 21600))
                sunset = time.strftime("%I:%M:%S", time.gmtime(json_data["sys"]["sunset"] - 21600))

                # updating the values here.
                feels_like_text.configure(text=f"Feels Like {feels_like}°C")
                temp_text.configure(text=f"{temp}°C")
                min_text.configure(text=f"{temp_min}°C")
                max_text.configure(text=f"{temp_max}°C")
                sunrise_text.configure(text=f"{sunrise} AM")
                sunset_text.configure(text=f"{sunset} PM")
                condition_text.configure(text=f"Overall : {condition}")
                humidity_text.configure(text=f"{humidity}")
                wind_speed_text.configure(text=f"{wind_speed} Mph")
                pressure_text.configure(text=f"{pressure} Pa")

                if condition == "Rain":
                    image_data.configure(file=relative_to_assets("dark_rain.png"))
                elif condition == "Clouds":
                    image_data.configure(file=relative_to_assets("dark_clouds.png"))
                elif condition == "Thunderstorm":
                    image_data.configure(file=relative_to_assets("dark_thunderstorm.png"))
                elif condition == "Mist":
                    image_data.configure(file=relative_to_assets("dark_mist.png"))
                elif condition == "Drizzle":
                    image_data.configure(file=relative_to_assets("dark_drizzle.png"))
                elif condition == "Snow":
                    image_data.configure(file=relative_to_assets("dark_snow.png"))
                elif condition == "Clear":
                    image_data.configure(file=relative_to_assets("dark_clear.png"))
                else:
                    image_data.configure(file=relative_to_assets("dark_default.png"))

        # handling the exception here.
        except Exception as city_not_found_error:
            print(city_not_found_error)
            messagebox.showerror("CityNotFound", "Invalid City!\nTry Again With Different Name.")
            entry_1.delete(0, END)

    def call_back(event):
        get_data()
    
    def toggle_dark():
        choice = messagebox.askyesnocancel("Restart Required !", "Theme Applied Successfully\nRestart the Application Now !")
        if choice:
            dark_window.destroy()
        elif choice == False:
            messagebox.showinfo("Theme Not Changed", "You Are Now Using Dark Theme !")
        else:
            messagebox.showinfo("Theme Not Changed", "No, Action has been taken !")

    # creating the dark themed window here.
    dark_window = Tk()
    width = 850
    height = 650
    # placing the dark_window at the center of the screen here.
    screen_width = dark_window.winfo_screenwidth()
    screen_height = dark_window.winfo_screenheight()
    x_coordinate = (screen_width / 2) - (width / 2)
    y_coordinate = (screen_height / 2) - (height / 2)
    dark_window.geometry("%dx%d+%d+%d" % (width, height, x_coordinate, y_coordinate))
    dark_window.title("WTW : What's The Weather")
    dark_window.iconbitmap(relative_to_assets("icon.ico"))
    dark_window.configure(bg="#2F3542")
    dark_window.resizable(False, False)

    canvas = Canvas(dark_window, bg="#2F3542", height=650, width=850, bd=0, highlightthickness=0, relief="ridge")
    canvas.place(x=0, y=0)
    image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(425.0, 320.0, image=image_image_1)

    # creating the dynamic image here.
    image_file_name = "dark_default.png"
    image_data = PhotoImage(file=relative_to_assets(image_file_name))
    imagedata = canvas.create_image(125.0, 285.0, image=image_data)

    # creating text in the canvas here.
    feels_like_text = Label(dark_window, text="---", background="#485460", font=("Ubuntu Regular", 15), fg="#A8ABC3")
    temp_text = Label(dark_window, text="---", background="#485460", font=("Ubuntu Regular", 35), fg="white")
    min_text = Label(dark_window, text="---", background="#485460", font=("Ubuntu Regular", 18), fg="white")
    max_text = Label(dark_window, text="---", background="#485460", font=("Ubuntu Regular", 18), fg="white")
    sunrise_text = Label(dark_window, text="---", background="#485460", font=("Ubuntu Regular", 15), fg="white")
    sunset_text = Label(dark_window, text="---", background="#485460", font=("Ubuntu Regular", 15), fg="white")
    condition_text = Label(dark_window, text="---", background="white", font=("Sans-Serif", 23), fg="#130F40")
    humidity_text = Label(dark_window, text="---", background="#485460", font=("Sans-Serif", 25), fg="white")
    wind_speed_text = Label(dark_window, text="---", background="#485460", font=("Sans-Serif", 25), fg="white")
    pressure_text = Label(dark_window, text="---", background="#485460", font=("Sans-Serif", 25), fg="white")

    # placing the labels acc to the coordinates.
    feels_like_text.place(x=248.0, y=249.0, anchor="nw")
    temp_text.place(x=264.0, y=194.0, anchor="nw")
    min_text.place(x=240.0, y=292.0, anchor="nw")
    max_text.place(x=335.0, y=292.0, anchor="nw")
    sunrise_text.place(x=80.0, y=463.0, anchor="nw")
    sunset_text.place(x=225.0, y=463.0, anchor="nw")
    condition_text.place(x=90.0, y=555.0, anchor="nw")
    humidity_text.place(x=603.0, y=188.0, anchor="nw")
    wind_speed_text.place(x=603.0, y=359.0, anchor="nw")
    pressure_text.place(x=603.0, y=553.0, anchor="nw")

    entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(213.0, 151.5, image=entry_image_1)
    entry_1 = Entry(bd=0, bg="#FFFFFF", highlightthickness=0, font="Sans-Serif 20 bold")
    entry_1.place(x=43.0, y=132.0, width=340.0, height=39.0)
    entry_1.focus_set()
    entry_1.focus()

    button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))  # about app
    button_1 = Button(image=button_image_1, borderwidth=0, highlightthickness=0, command=about,
                    relief="flat", background="#485460", activebackground="#485460")
    button_1.place(x=503.0, y=34.0, width=112.0, height=32.0)

    button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))  # contact
    button_2 = Button(image=button_image_2, borderwidth=0, highlightthickness=0, command=contact,
                    relief="flat", background="#485460", activebackground="#485460")
    button_2.place(x=632.0, y=36.0, width=86.0, height=25.0)

    button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))  # toggle
    button_3 = Button(image=button_image_3, borderwidth=0, highlightthickness=0, command=toggle_dark, relief="flat",
                    background="#2F3542", activebackground="#2F3542")
    button_3.place(x=746.0, y=28.0, width=30.0, height=30.0)

    button_image_4 = PhotoImage(file=relative_to_assets("button_4.png"))  # search
    button_4 = Button(image=button_image_4, borderwidth=0, highlightthickness=0, relief="flat", background="white",
                    activebackground="white", command=get_data)
    button_4.place(x=353.0, y=136.0, width=30.0, height=30.0)
    dark_window.bind("<Return>", call_back)

    button_image_5 = PhotoImage(file=relative_to_assets("button_5.png"))  # sound
    button_5 = Button(image=button_image_5, borderwidth=0, highlightthickness=0, relief="flat", background="#A8ABC3",
                    activebackground="#A8ABC3", command=speak)
    button_5.place(x=336.0, y=557.0, width=45.0, height=45.0)
    dark_window.mainloop()

# creating the splash screen window here.
splash_window = Tk()
w = 515
h = 358
# placing the window at the center of the screen here.
screen_width = splash_window.winfo_screenwidth()
screen_height = splash_window.winfo_screenheight()
x_coordinate = (screen_width / 2) - (w / 2)
y_coordinate = (screen_height / 2) - (h / 2)
splash_window.geometry("%dx%d+%d+%d" % (w, h, x_coordinate, y_coordinate))
splash_window.resizable(False, False)
# creating the image elements here in canvas.
canvas = Canvas(splash_window, bg="#7ED6DF", height=358, width=515, bd=0, highlightthickness=0, relief="ridge")
canvas.place(x=0, y=0)
image_image_1 = PhotoImage(file=relative_to_assets("splashimage.png"))
image_1 = canvas.create_image(257.0, 180.0, image=image_image_1)

def main():
    # creating the UI here.
    window = Tk()
    width = 850
    height = 650
    # placing the window at the center of the screen here.
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x_coordinate = (screen_width / 2) - (width / 2)
    y_coordinate = (screen_height / 2) - (height / 2)
    window.geometry("%dx%d+%d+%d" % (width, height, x_coordinate, y_coordinate))
    window.configure(bg="#7ED6DF")
    window.title("WTW : What's The Weather")
    window.resizable(False, False)
    window.iconbitmap(relative_to_assets("icon.ico"))

    # creating the image elements here in canvas.
    canvas = Canvas(window, bg="#7ED6DF", height=650, width=850, bd=0, highlightthickness=0, relief="ridge")
    canvas.place(x=0, y=0)
    image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(425.0, 322.0, image=image_image_1)

    # creating the dynamic image here.
    image_file_name = "bright_default.png"
    image_data = PhotoImage(file=relative_to_assets(image_file_name))
    imagedata = canvas.create_image(125.0, 285.0, image=image_data)

    # creating the entry text feild here.
    entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(213.0, 151.5, image=entry_image_1)
    entry_1 = Entry(bd=0, bg="#FFFFFF", highlightthickness=0, font="Ubuntu 20 bold")
    entry_1.place(x=43.0, y=132.0, width=340.0, height=39.0)
    entry_1.focus()

    # creating text in the canvas here.
    feels_like_text = Label(window, text="---", background="#1289A7", font=("Ubuntu Regular", 15), fg="#130F40")
    temp_text = Label(window, text="---", background="#1289A7", font=("Ubuntu Regular", 35), fg="white")
    min_text = Label(window, text="---", background="#1289A7", font=("Ubuntu Regular", 18), fg="white")
    max_text = Label(window, text="---", background="#1289A7", font=("Ubuntu Regular", 18), fg="white")
    sunrise_text = Label(window, text="---", background="#1289A7", font=("Ubuntu Regular", 15), fg="white")
    sunset_text = Label(window, text="---", background="#1289A7", font=("Ubuntu Regular", 15), fg="white")
    condition_text = Label(window, text="---", background="white", font=("Sans-Serif", 23), fg="#130F40")
    humidity_text = Label(window, text="---", background="#7ED6DF", font=("Sans-Serif", 25), fg="black")
    wind_speed_text = Label(window, text="---", background="#7ED6DF", font=("Sans-Serif", 25), fg="black")
    pressure_text = Label(window, text="---", background="#7ED6DF", font=("Sans-Serif", 25), fg="black")

    # placing the labels acc to the coordinates.
    feels_like_text.place(x=248.0, y=249.0, anchor="nw")
    temp_text.place(x=264.0, y=194.0, anchor="nw")
    min_text.place(x=240.0, y=294.0, anchor="nw")
    max_text.place(x=335.0, y=294.0, anchor="nw")
    sunrise_text.place(x=80.0, y=463.0, anchor="nw")
    sunset_text.place(x=225.0, y=463.0, anchor="nw")
    condition_text.place(x=90.0, y=555.0, anchor="nw")
    humidity_text.place(x=603.0, y=188.0, anchor="nw")
    wind_speed_text.place(x=603.0, y=359.0, anchor="nw")
    pressure_text.place(x=603.0, y=553.0, anchor="nw")

    # creating buttons in the canvas here.
    # button-1 - toggle button
    button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
    button_1 = Button(image=button_image_1, borderwidth=0, highlightthickness=0, command=toggle_theme, relief="flat",
                    background="#7ED6DF", activebackground="#7ED6DF")
    button_1.place(x=744.0, y=28.0, width=30.0, height=30.0)

    # button-2 - about app button
    button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
    button_2 = Button(image=button_image_2, borderwidth=0, highlightthickness=0, command=about,
                    relief="flat", background="#1289A7", activebackground="#1289A7")
    button_2.place(x=503.0, y=34.0, width=112.0, height=32.0)

    # button-3 - contact button
    button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
    button_3 = Button(image=button_image_3, borderwidth=0, highlightthickness=0, command=contact,
                    relief="flat", background="#1289A7", activebackground="#1289A7")
    button_3.place(x=632.0, y=36.0, width=86.0, height=25.0)

    # button-4 - sound button
    button_image_4 = PhotoImage(file=relative_to_assets("button_4.png"))
    button_4 = Button(image=button_image_4, borderwidth=0, highlightthickness=0, command=speak, relief="flat",
                    background="#7ED6DF", activebackground="#7ED6DF")
    button_4.place(x=336.0, y=554.0, width=45.0, height=45.0)
    window.bind("<Return>", call_back)

    # button-5 - search button
    button_image_5 = PhotoImage(file=relative_to_assets("button_5.png"))
    button_5 = Button(image=button_image_5, borderwidth=0, highlightthickness=0, command=get_data, relief="flat",
                    background="white", activebackground="white")
    button_5.place(x=358.0, y=136.0, width=30.0, height=30.0)

# running over the loop here.
mainloop()