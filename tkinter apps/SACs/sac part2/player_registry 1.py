from tkinter import Tk, Frame, Label, Entry, Button, StringVar, Radiobutton, END
from tkinter.ttk import Combobox
# from PIL import Image, ImageTk

teams = {}


# ============= DEFINE YOUR VALIDATION functions =================== #
def is_mobile():
    # if the input starts with 04 and is 10 digits long
    testing04 = mobile_entry.get()
    if testing04[:2] == '04':
        testing10 = mobile_entry.get()
        test = len(testing10)
        if test == 10:
            return True
        else:
            error_label.config(text="Mobile Number not recongised")
            return False
    else:
        error_label.config(text="Enter Mobile Phone Number")
        return False


def is_email():
    # if the input has exactly 1 '@' and contains '.'
    email = email_entry.get()
    print(email)
    if "@" in email and "." in email:
        print("@.")
        return True
    else:
        error_label.config(text="Enter a correct email")
        return False


def not_empty():
    # if name, age, contact_number, email, and team_name exist

    # widgets = {
    #         "": ,
    #         "age":  age_entry.get(),
    #         "mobile": mobile_entry.get(),
    #         "email": email_entry.get(),
    #         "team name": team_entry.get()
    # }
    # for widget in widgets:
    #     print(widget)
    #     if widget == "":
    #         error_label.config(text=f"{widget} missing")
    #         return False
    # return True    
    if name_entry.get():
        if age_entry.get():
            if mobile_entry.get():
                if email_entry.get():
                    if team_entry.get():
                        return True
                    else:
                        error_label.config(text="Team name missing")
                else:
                    error_label.config(text="email missing")
            else:
                error_label.config(text="mobile missing")
        else:
            error_label.config(text="age missing")
    else:
        error_label.config(text="name missing")
    


def age_is_number():
    # if age is numeric
    age = age_entry.get()
    try:
        age = int(age)
        return True
    except:
        error_label.config(text="Incompatible age")
        return False
# ================================================================== #


# Defining Command for Submit Button
def submit_data():
    if not_empty() and is_mobile() and is_email() and age_is_number():
        personal = {
            "name": name_entry.get(),
            "age":  age_entry.get(),
            "mobile": mobile_entry.get(),
            "email": email_entry.get(),
            "preferences": {
                'role': primary_entry.get(),
                'position': position_entry.get()}
        }
        team = {
            "name": team_entry.get() + " " + team_type.get(),
            "members": {}
        }
        if team["name"] not in teams:
            team["members"].update({personal["name"]: personal})
            teams.update({team['name']: team})
        else:
            teams[team["name"]]["members"].update({personal["name"]: personal})
        for team in teams:
            team_members = [x for x in teams[team]['members']]
            print(f'{teams[team]["name"]}: {", ".join(team_members)}')
        print('\n\n')
        clear()
        name_entry.focus()
        error_label.config(text='Data Successfully Added')
        root.after(3000, lambda: error_label.config(text=""))


def clear():
    widgets = [
        name_entry,
        age_entry,
        mobile_entry,
        email_entry,
        team_entry,
    ]
    for entry in widgets:
        entry.delete(0, END)
    primary_entry.set('')
    position_entry.set('')


# Create the main window
root = Tk()
root.title("Cricket Player Registration")
root.geometry("650x300+150+150")

# Frame 1: Personal Details and Contact Details
frame1 = Frame(root, width=400, height=400)
frame1.grid(column=1, row=1, sticky='nesw')

# List of data entry boxes in frame1
name_entry = Entry(frame1)
age_entry = Entry(frame1)
mobile_entry = Entry(frame1)
email_entry = Entry(frame1)

# Displaying widgets in personal details frame
Label(frame1, text="Personal Details", font=("Arial", 14)).pack(pady=10)
Label(frame1, text="Name:").pack(anchor="w", padx=10)
name_entry.pack(anchor="w", padx=10)
Label(frame1, text="Age:").pack(anchor="w", padx=10)
age_entry.pack(anchor="w", padx=10)
Label(frame1, text="Contact Number:").pack(anchor="w", padx=10)
mobile_entry.pack(anchor="w", padx=10)
Label(frame1, text="Email:").pack(anchor="w", padx=10)
email_entry.pack(anchor='w', padx=10)
# Frame 2: Team Details
frame2 = Frame(root, width=400, height=400)
frame2.grid(column=2, row=1, sticky="nesw")

# List of data entry boxes in frame2
team_entry = Entry(frame2)
gender_entry = Entry(frame2)
primary_entry = Combobox(
    frame2,
    values=[
        "Batter",
        "Bowler",
        "Fielder",
        "Wicket-Keeper"
        ],
    state='readonly'
    )
position_entry = Combobox(
    frame2,
    values=[
        'slips',
        'gully',
        'point',
        'cover',
        'mid-off',
        'mid-on',
        'mid-wicket',
        'square leg',
        'fine leg',
        'wicketkeeper'],
    state='readonly')
team_type = StringVar(value="Women's")  # default value

# Displaying widgets in Team Details frame
Label(frame2, text="Team Details", font=("Arial", 14)).pack(pady=10)
Label(frame2, text="Team Name:").pack(anchor="w", padx=10)
team_entry.pack(anchor="w", padx=10)
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
Label(frame2, text="Primary Role:").pack(anchor="w", padx=10)
primary_entry.pack(anchor="w", padx=10, pady=2)
Label(frame2, text="Fielding Position Preference:").pack(anchor="w", padx=10)
position_entry.pack(anchor="w", padx=10, pady=2)

# Frame 3: Logo Display
frame3 = Frame(root, width=150, height=150)
frame3.grid(column=3, row=1, sticky="nesw")

# Load and display the logo image
# image_path = "cricket-logo.gif"
# logo_image = Image.open(image_path)
# logo_image = logo_image.resize((200, 200))  # Resize the image for better fit
# logo_photo = ImageTk.PhotoImage(logo_image)

# logo_label = Label(frame3, image=logo_photo)
# logo_label.pack(pady=20)

# Frame 4: Submit Frame
frame4 = Frame(root, width=200, height=50)
frame4.grid(column=3, row=2, sticky="nesw")
submit_button = Button(frame4, text="Submit", command=submit_data)
submit_button.pack(anchor="center")

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

# Sample acceptable data input
name_entry.insert(0, 'Georgia Voll')
age_entry.insert(0, "21")
mobile_entry.insert(0, "0455123456")
email_entry.insert(0, 'voll.georgia@cricketaustralia.com.au')
team_entry.insert(0, "Thunder")
primary_entry.current(0)
position_entry.current(0)

# Run the application
root.mainloop()
