import requests
import tkinter as tk
from tkinter import font

#Size of window
HEIGHT=300
WIDTH = 400

def bottom_display(weather):
    name =weather['name']
    country = weather ['sys']['country']
    descrip=weather['weather'][0]['description']
    temp =weather['main']['temp']
    feels = weather ['main']['feels_like']
    final_display= 'City: %s \n Country: %s \n Conditions: %s \n ' \
                   'Temperature (°F) :  %s \n Feels Like (°F) : %s'% (name,country,descrip,temp,feels)
    return final_display

#api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}

def weather_check(city):
    weather_key ='bf3aa022e712505b7ecedd9a80810f60'
    url='http://api.openweathermap.org/data/2.5/weather?id=2172797&appid=bf3aa022e712505b7ecedd9a80810f60'
    params={'APPID': weather_check,'q': city,'units': 'imperial'}
    response = requests.get(url,params=params)
    print(response.json())

#take out comment once done with JSON
    weather = response.json()
    label_bottom['text'] = bottom_display(weather)
root = tk.Tk()

canvas = tk.Canvas(root,height=HEIGHT, width=WIDTH)
canvas.pack()

#frame for search bar

#frame color & height & border line for top search bar
frame = tk.Frame(root, bg='light pink', bd=3)
frame.place(relx=0.5,rely=0.1,relwidth=.75,relheight=.1,anchor = 'n')

#Searching to display on textbox
search = tk.Entry(frame, font =('Gabriola',20))
search.place(relwidth=.65,relheight=1)

#Button to press
#lambda temportary memory to redefine for searchbox
button = tk.Button(frame,text="Search",font = ('Gabriola',20), bg="white",fg="black",command =lambda:weather_check(search.get()))
button.place(relx=0.7,relheight=1,relwidth =0.3)

#Display feather to show weather requested

#Bottom frame for display
bottom_frame = tk.Frame(root, bg="light blue", bd =7)
bottom_frame.place(relx=.5, rely=.25,relwidth=.75,relheight=.6, anchor='n')

#label the inside of the bottom frame
label_bottom= tk.Label(bottom_frame,bg="white",font=('Gabriola', 14))
label_bottom.place(relwidth=1, relheight=1)

#Display background pgn
root.mainloop()