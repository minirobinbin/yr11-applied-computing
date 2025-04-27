# 12d6f5cd001d2ed789d13036fe8fbc3f
API_key= "12d6f5cd001d2ed789d13036fe8fbc3f"
import requests
import tkinter as tk

#getting weather
zip_code = "3084"
country_code = "au" 

url1 = f'https://api.openweathermap.org/data/2.5/weather?zip={zip_code},{country_code}&appid={API_key}&units=metric'
url2 = f"https://api.openweathermap.org/data/2.5/forecast?zip={zip_code},{country_code}&appid={API_key}&units=metric"

response1 = requests.get(url1)
data1 = response1.json()
response2 = requests.get(url2)
data2 = response2.json()
print(f" Weather is {data1["weather"][0]['description']}")
print(f"Current temperature is {data1["main"]['temp']}°c")
print(f"{data2['list'][11]['dt_txt']} {data2['list'][11]['main']['temp']}")


def changelocation():
    city_name = changesuburbentry.get()
    global country_code
    global API_key

    url1 = f"https://api.openweathermap.org/data/2.5/weather?q={city_name},{country_code}&appid={API_key}&units=metric"
    url2 = f"https://api.openweathermap.org/data/2.5/forecast?q={city_name},{country_code}&appid={API_key}&units=metric"

    response1 = requests.get(url1)
    data1 = response1.json()
    response2 = requests.get(url2)
    data2 = response2.json()
    if response1.status_code == 200:
        location.config(text=data1['name'])
        temp.config(text=f"{data1["main"]['temp']}°")
        templow.config(text=f"L:{data1['main']['temp_min']}°")
        weatherdesc.config(text=data1['weather'][0]['main'])
        temphigh.config(text=f"H:{data1['main']['temp_max']}°")
        date = data2['list'][10]['dt_txt']
        date = date.split()
        date = date[1]
        date1 = date.split(':')
        hour = date1[0]
        min = date1[1]
        tmrtemp.config(text=f"Tmr temp @ {hour}:{min}: {data2['list'][10]['main']['temp']}°C")
        root.title(f"Weather in {data1['name']}")
    else:
        errors.config(text='city not found')
        root.after(1000, lambda: errors.config(text=''))


def add_placeholder(entry, placeholder):
    # Function to add the placeholder if the entry is empty
    if not entry.get():
        entry.insert(0, placeholder)
        entry.config(fg='grey')

def remove_placeholder(entry, placeholder):
    # Function to remove the placeholder if it's currently displayed
    if entry.get() == placeholder:
        entry.delete(0, tk.END)
        entry.config(fg='white')

#creating window
root = tk.Tk()
root.geometry("300x300")
root.title(f"Weather in {data1['name']}")


location = tk.Label(root, text=data1['name'])
location.pack() 
temp = tk.Label(root, text=f"{data1["main"]['temp']}°")
temp.pack()
weatherdesc = tk.Label(root, text=data1['weather'][0]['main'])
weatherdesc.config(fg="grey")
weatherdesc.pack()
templow = tk.Label(root, text=f"L:{data1['main']['temp_min']}°")
templow.pack()
temphigh = tk.Label(root, text=f"H:{data1['main']['temp_max']}°")
temphigh.pack()



date = data2['list'][11]['dt_txt'] #2025-03-24 21:00:00
date = date.split() #['2025-03-24', '21:00:00']
date = date[1] #'21:00:00'
date1 = date.split(':') #['21', '00', '00']
hour = date1[0] # '21'
min = date1[1] # '00'


tmrtemp = tk.Label(root, text=f"Tmr temp @ {hour}:{min}: {data2['list'][11]['main']['temp']}°C")
tmrtemp.pack()

errors = tk.Label(root, text="")
errors.pack()

changesuburbentry = tk.Entry(root)
changesuburbentry.insert(0, 'Suburb in Australia')
changesuburbentry.pack()
changelocationbutton = tk.Button(root, text='change location', command=changelocation)
changelocationbutton.pack()


changesuburbentry.bind("<FocusIn>", lambda e: remove_placeholder(changesuburbentry, "Suburb in Australia"))
changesuburbentry.bind("<FocusOut>", lambda e: add_placeholder(changesuburbentry, "Suburb in Australia"))
root.mainloop()