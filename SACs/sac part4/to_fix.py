from tkinter import Tk, Frame, Label, Entry, Button, PhotoImage, StringVar, Radiobutton
from tkinter.ttk import Combobox
from datetime import datetime
import csv


def write_report():
    team = name_entry.get()
    bottom_age = lower_age.get()
    top_age = upper_age.get()
    type = team_type.get()
    data = []
    with open('data.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            if row[2] == type and int(bottom_age) < int(row[4]) < int(top_age) and row[3] == team:
                data.append(row)
    now = datetime.now().strftime("%d-%m-%y")
    filename = f"{team} {type} Under {top_age} {now}.txt"
    with open(filename, 'w') as f:
        title = f"{team} {type} Under {top_age} Team      {now}\n"
        f.write(title)
        f.write("-"*len(title)+"\n")
        f.write(f"{"Player":17} | {"Age":3} | {"Role"}\n")
        f.write("-"*len(title)+"\n")
        for player in data:
            f.write(f'{player[1]:20} {player[4]:4} {player[5]}\n')
        f.write("-"*len(title)+"\n")


# Create the main window
root = Tk()
root.title("Cricket Teams")

# Get screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Window width and height
window_width = 650
window_height = 300

# Calculate position x and y coordinates
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)

# Center window on screen
root.geometry(f"650x300+{x}+{y}")

# Frame 1: Personal Details and Contact Details
frame1 = Frame(root, width=400, height=400)
frame1.grid(column=1, row=1, sticky='nesw')
age_frame = Frame(frame1)
# List of data entry boxes in frame1
name_entry = Combobox(
    frame1,
    values=[
        "Stars",
        "Strikers",
        "Hurricanes",
        "Scorchers",
        "Renegades",
        "Sixers"
        ],
    state='readonly'
    )
lower_age = Entry(
    age_frame,
    width=5
    )
upper_age = Entry(
    age_frame,
    width=5
)


# Displaying widgets in personal details frame
Label(frame1, text="Report Detail", font=("Arial", 14)).pack(pady=10)
Label(frame1, text="Team Name:").pack(anchor="w", padx=10)
name_entry.pack(anchor="w", padx=10)
Label(frame1, text="Age Range:").pack(anchor="w", padx=10)
age_frame.pack(anchor="w", padx=10)
lower_age.pack(side='left', anchor="w", padx=10)
Label(age_frame, text='-').pack(side='left')
upper_age.pack(side="left", anchor="w", padx=10)

# Frame 2: Team Details
frame2 = Frame(root, width=400, height=400)
frame2.grid(column=2, row=1, sticky="nesw")

# List of data entry boxes in frame2
team_type = StringVar(value="Women's")  # default value

# Displaying widgets in Team Details frame
Label(frame2, text=" ", font=("Arial", 14)).pack(pady=10)
Label(frame2, text="Team Type:").pack(anchor="w", padx=10)
radio_frame = Frame(frame2)
radio_frame.pack(anchor='w', padx=10, pady=2)
Radiobutton(
    radio_frame,
    text="Men's",
    variable=team_type,
    value="Men's"
    ).pack(side='left', anchor="w", padx=5)
Radiobutton(
    radio_frame,
    text="Women's",
    variable=team_type,
    value="Women's"
    ).pack(side='left', anchor="w", padx=5)
export_button = Button(
    frame2,
    text="Export",
    command=write_report
    ).pack(anchor="w", pady=10, padx=50)


# Frame 3: Logo Display
frame3 = Frame(root, width=150, height=150)
frame3.grid(column=3, row=1, sticky="nesw")

# Load and display the logo image
image_path = "cricket-logo.gif"
logo_image = PhotoImage(file=image_path)

logo_label = Label(frame3, image=logo_image)
logo_label.pack(pady=20)

# Frame 4: Submit Frame
frame4 = Frame(root, width=200, height=50)
frame4.grid(column=3, row=2, sticky="nesw")


# Frame 5: Error Message Frame
frame5 = Frame(root, height=50)
frame5.grid(column=1, row=2, columnspan=2, sticky="nesw")
error_label = Label(
    frame5,
    text="",
    justify="center",
    font=('Arial', 12),
    fg="red"
    )
error_label.pack()


# Run the application
root.mainloop()
