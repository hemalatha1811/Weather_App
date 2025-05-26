from tkinter import *
import requests
import json
import datetime
from PIL import ImageTk, Image


root=Tk()
root.title("Weather App")
root.geometry("650x680")
#root.iconbitmap("C:/Users/Lenovo/OneDrive/Desktop/PROJECTS/WEATHER PROJECT[PYTHON]/images/weathericon.png")
root.resizable(0,0)

bg = PhotoImage(file = "C:/Users/Lenovo/OneDrive/Desktop/PROJECTS/WEATHER PROJECT[PYTHON]/images/weather.png")


canvas1 = Canvas( root, width = 500,height = 400) 
canvas1.pack(fill = "both", expand = True) 
  
# Display image
canvas1.create_image( 0, 0, image = bg,anchor = "nw")

city_entry=StringVar()
city_name=Entry(root,textvariable=city_entry,width=30,borderwidth=5,bg=None)
city_name.place(x=140,y=30)

def func():
    # API Call
    api_key='d0f4215f39312e5de368ee8edad554b8'
    api_request = requests.get("https://api.openweathermap.org/data/2.5/weather?q="
                                                            + city_entry.get() + "&units=metric&appid="+api_key)

    api = json.loads(api_request.content)

    # Weather data
    A = api['main']
    temperature = A['temp']
    humidity = A['humidity']
    pressure=A['pressure']
    windspeed=api['wind']['speed']
    groundlevel=A['grnd_level']


    # Country
    z = api['sys']
    country = z['country']
    city = api['name']
    # Adding the received info into the screen
    img1_label.configure(text=f"temperature:{temperature} c")
    img2_label.configure(text=f"pressure:{pressure} hpa")
    img3_label.configure(text=f"humidity:{humidity} %")
    img4_label.configure(text=f"windspeed:{windspeed} m/s")
    img5_label.configure(text=f"ground level:{groundlevel} hpa")
    country_label.configure(text=country)
    city_label.configure(text=city)
    
search=Button(root,width=10,height=1,text="search",command=func)
search.place(x=350,y=31)

city_label=Label(root,text=" ",width=20)
city_label.place(x=170,y=70)

country_label=Label(root,text=" ",width=20)
country_label.place(x=320,y=70)

dt = datetime.datetime.now()
date=Label(root,text=dt.strftime('%m %B %Y || %A'),width=20)
date.place(x=250,y=100)

time=Label(root,text=dt.strftime('%I : %M %p'),width=20)    #dt.strftime('%m %B')
time.place(x=250,y=130)

img1 = ImageTk.PhotoImage(Image.open('C:/Users/Lenovo/OneDrive/Desktop/PROJECTS/WEATHER PROJECT[PYTHON]/images/temperatureee.png'))
panel1 = Label(root, image=img1)
panel1.place(x=50, y=200)

img1_label=Label(root,text="temperature ",width=15)
img1_label.place(x=70,y=380)


img2 = ImageTk.PhotoImage(Image.open("C:/Users/Lenovo/OneDrive/Desktop/PROJECTS/WEATHER PROJECT[PYTHON]/images/pressure.png"))
panel2 = Label(root, image=img2)
panel2.place(x=250, y=200)

img2_label=Label(root,text="pressure ",width=15)
img2_label.place(x=270,y=380)

img3 = ImageTk.PhotoImage(Image.open('C:/Users/Lenovo/OneDrive/Desktop/PROJECTS/WEATHER PROJECT[PYTHON]/images/humidity.png'))
panel3 = Label(root, image=img3)
panel3.place(x=450, y=200)

img3_label=Label(root,text="humidty ",width=15)
img3_label.place(x=470,y=380)

img4 = ImageTk.PhotoImage(Image.open('C:/Users/Lenovo/OneDrive/Desktop/PROJECTS/WEATHER PROJECT[PYTHON]/images/windspeed.png'))
panel4 = Label(root, image=img4)
panel4.place(x=150, y=450)

img4_label=Label(root,text="windspeeed ",width=15)
img4_label.place(x=170,y=630)

img5 = ImageTk.PhotoImage(Image.open('C:/Users/Lenovo/OneDrive/Desktop/PROJECTS/WEATHER PROJECT[PYTHON]/images/grndlevel.png'))
panel5 = Label(root, image=img5)
panel5.place(x=350, y=450)

img5_label=Label(root,text="ground level ",width=15)
img5_label.place(x=370,y=630)



root.mainloop()

