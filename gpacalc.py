import tkinter

from customtkinter import *
from PIL import Image

# Set the image of the illustrated moon
moonimg = Image.open("free-half-moon-inverted.png")
sunimg = Image.open("free-sun-inverted.png")

# Creates the application's window
app = CTk()
app.geometry("550x750")
app.title("GPA Calculator")

# Disable the Maximize button of the window
app.resizable(0,0)

set_appearance_mode("light")

# Creates the frame
frame = CTkFrame(master=app, height=500, width=500, fg_color="#D3D3D3", border_color="#BFBFBF", border_width=3)
frame.pack(expand=True)

#
def lightmode():
    lightbtn.place_forget()
    darkbtn.place(relx=0.1, rely=0.95, anchor="center")
    set_appearance_mode("light")
    frame.configure(fg_color="#D3D3D3", border_color="#BFBFBF",)

#
def darkmode():
    darkbtn.place_forget()
    lightbtn.place(relx=0.1, rely=0.95, anchor="center")
    set_appearance_mode("dark")
    frame.configure(fg_color="#262626", border_color="#191919")

darkbtn = CTkButton(master=app, text="Dark", corner_radius=16, fg_color="#0080FF", hover_color="#00CC00", height=35, width=65, command=darkmode, image=CTkImage(moonimg))

darkbtn.place(relx=0.1, rely=0.95, anchor="center")

lightbtn = CTkButton(master=app, text="Light", corner_radius=16, fg_color="#0080FF", hover_color="#00CC00", height=35, width=65, command=lightmode, image=CTkImage(sunimg))



# These four lines of code create the text above the drop-down boxes
gradetextlabel = CTkLabel(master=frame, text="Grade", font=('Arial', 20))

gradetextlabel.place(relx=0.5, rely=0.07, anchor="center")

coursetypetextlabel = CTkLabel(master=frame, text="Course Type", font=('Arial', 20))

coursetypetextlabel.place(relx=0.8, rely=0.07, anchor="center")

# This list assigns numerical values to the grades
gpa = {
    'A+':4.3,
    'A': 4,
    'A-':3.7,
    'B+':3.3,
    'B':3,
    'B-':2.7,
    'C+':2.3,
    'C':2,
    'C-':1.7,
    'D+':1.3,
    'D':1,
    'D-':0.7,
    'F':0
}

# This list assigns numerical values to the course type. This will get added on the grade later on.
coursetype = {
    'Regular':0,
    'AP/IB/College': 1,
    'Honors':0.50,
}

# This list assigns a value of zero to all blank drop-down boxes
firstgpainteger = 0
firstgpaweight = 0
secondgpainteger = 0
secondgpaweight = 0
thirdgpainteger = 0
thirdgpaweight = 0
fourthgpainteger = 0
fourthgpaweight = 0
fifthgpainteger = 0
fifthgpaweight = 0
sixthgpainteger = 0
sixthgpaweight = 0
seventhgpainteger = 0
seventhgpaweight = 0

# This function retrieves the numerical value of the grade that was inputted for the first class's drop-down box.
def firstgrade(value):
    global firstgpainteger
    if value in gpa:
        firstgpainteger = gpa[value]

# This function retrieves the numerical value of the course type that was inputted for the first class's drop-down box.
def firstclasstype(value):
    global firstgpaweight
    if value in coursetype:
        firstgpaweight = coursetype[value]

# This function retrieves the numerical value of the grade that was inputted for the second class's drop-down box.
def secondgrade(value):
    global secondgpainteger
    if value in gpa:
        secondgpainteger = gpa[value]

# This function retrieves the numerical value of the course type that was inputted for the second class's drop-down box.
def secondclasstype(value):
    global secondgpaweight
    if value in coursetype:
        secondgpaweight = coursetype[value]

# This function retrieves the numerical value of the grade that was inputted for the third class's drop-down box.
def thirdgrade(value):
    global thirdgpainteger
    if value in gpa:
        thirdgpainteger = gpa[value]

# This function retrieves the numerical value of the course type that was inputted for the third class's drop-down box.
def thirdclasstype(value):
    global thirdgpaweight
    if value in coursetype:
        thirdgpaweight = coursetype[value]

# This function retrieves the numerical value of the grade that was inputted for the fourth class's drop-down box.
def fourthgrade(value):
    global fourthgpainteger
    if value in gpa:
        fourthgpainteger = gpa[value]

# This function retrieves the numerical value of the course type that was inputted for the fourth class's drop-down box.
def fourthclasstype(value):
    global fourthgpaweight
    if value in coursetype:
        fourthgpaweight = coursetype[value]

# This function retrieves the numerical value of the grade that was inputted for the fifth class's drop-down box.
def fifthgrade(value):
    global fifthgpainteger
    if value in gpa:
        fifthgpainteger = gpa[value]

# This function retrieves the numerical value of the course type that was inputted for the fifth class's drop-down box.
def fifthclasstype(value):
    global fifthgpaweight
    if value in coursetype:
        fifthgpaweight = coursetype[value]

# This function retrieves the numerical value of the grade that was inputted for the sixth class's drop-down box.
def sixthgrade(value):
    global sixthgpainteger
    if value in gpa:
        sixthgpainteger = gpa[value]

# This function retrieves the numerical value of the course type that was inputted for the sixth class's drop-down box.
def sixthclasstype(value):
    global sixthgpaweight
    if value in coursetype:
        sixthgpaweight = coursetype[value]

# This function retrieves the numerical value of the grade that was inputted for the seventh class's drop-down box.
def seventhgrade(value):
    global seventhgpainteger
    if value in gpa:
        seventhgpainteger = gpa[value]

# This function retrieves the numerical value of the course type that was inputted for the seventh class's drop-down box.
def seventhclasstype(value):
    global seventhgpaweight
    if value in coursetype:
        seventhgpaweight = coursetype[value]

gradecombobox = CTkComboBox(master=frame, values=[' ', 'A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D', 'D-', 'F'], command=firstgrade,)

gradecombobox.place(relx=0.5, rely=0.16, anchor="center")

coursecombobox = CTkComboBox(master=frame, values=['Regular', 'AP/IB/College', 'Honors'], command=firstclasstype,)

coursecombobox.place(relx=0.8, rely=0.16, anchor="center")

courseonelabel= CTkLabel(master=frame, text="1st Class", font=('Arial', 20))

courseonelabel.place(relx=0.2, rely=0.16, anchor="center")

# This list is used when calculating GPA
class2enabled = 0
class3enabled = 0
class4enabled = 0
class5enabled = 0
class6enabled = 0
class7enabled = 0


def class2():

    global class2enabled

    class2enabled = 0

    class2enabled += 1

    courseonelabel = CTkLabel(master=frame, text="2nd Class", font=('Arial', 20))

    courseonelabel.place(relx=0.2, rely=0.24, anchor="center")

    cls2btn.place(relx=2, rely=2, anchor="center",)

    gradecombobox = CTkComboBox(master=frame, values=[' ', 'A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D', 'D-', 'F'], command=secondgrade,)

    gradecombobox.place(relx=0.5, rely=0.24, anchor="center")

    coursecombobox = CTkComboBox(master=frame, values=['Regular', 'AP/IB/College', 'Honors'], command=secondclasstype,)

    coursecombobox.place(relx=0.8, rely=0.24, anchor="center")

    cls3btn.place(relx=0.2, rely=0.32, anchor="center",)

def class3():

    global class3enabled

    class3enabled = 0

    class3enabled += 1

    courseonelabel = CTkLabel(master=frame, text="3rd Class", font=('Arial', 20))

    courseonelabel.place(relx=0.2, rely=0.32, anchor="center")

    cls3btn.place(relx=2, rely=2, anchor="center")

    gradecombobox = CTkComboBox(master=frame, values=[' ', 'A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D', 'D-', 'F'], command=thirdgrade,)

    gradecombobox.place(relx=0.5, rely=0.32, anchor="center")

    coursecombobox = CTkComboBox(master=frame, values=['Regular', 'AP/IB/College', 'Honors'], command=thirdclasstype,)

    coursecombobox.place(relx=0.8, rely=0.32, anchor="center")

    cls4btn.place(relx=0.2, rely=0.40, anchor="center")

def class4():

    global class4enabled

    class4enabled = 0

    class4enabled += 1

    courseonelabel = CTkLabel(master=frame, text="4th Class", font=('Arial', 20))

    courseonelabel.place(relx=0.2, rely=0.40, anchor="center")

    cls4btn.place(relx=2, rely=2, anchor="center")

    gradecombobox = CTkComboBox(master=frame, values=[' ', 'A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D', 'D-', 'F'], command=fourthgrade,)

    gradecombobox.place(relx=0.5, rely=0.40, anchor="center")

    coursecombobox = CTkComboBox(master=frame, values=['Regular', 'AP/IB/College', 'Honors'], command=fourthclasstype, )

    coursecombobox.place(relx=0.8, rely=0.40, anchor="center")

    cls5btn.place(relx=0.2, rely=0.48, anchor="center")

def class5():

    global class5enabled

    class5enabled = 0

    class5enabled += 1

    courseonelabel = CTkLabel(master=frame, text="5th Class", font=('Arial', 20))

    courseonelabel.place(relx=0.2, rely=0.48, anchor="center")

    cls5btn.place(relx=2, rely=2, anchor="center")

    gradecombobox = CTkComboBox(master=frame, values=[' ', 'A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D', 'D-', 'F'], command=fifthgrade, )

    gradecombobox.place(relx=0.5, rely=0.48, anchor="center")

    coursecombobox = CTkComboBox(master=frame, values=['Regular', 'AP/IB/College', 'Honors'], command=fifthclasstype, )

    coursecombobox.place(relx=0.8, rely=0.48, anchor="center")

    cls6btn.place(relx=0.2, rely=0.56, anchor="center")

def class6():

    global class6enabled

    class6enabled = 0

    class6enabled += 1

    courseonelabel = CTkLabel(master=frame, text="6th Class", font=('Arial', 20))

    courseonelabel.place(relx=0.2, rely=0.56, anchor="center")

    cls6btn.place(relx=2, rely=2, anchor="center")

    gradecombobox = CTkComboBox(master=frame, values=[' ', 'A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D', 'D-', 'F'], command=sixthgrade, )

    gradecombobox.place(relx=0.5, rely=0.56, anchor="center")

    coursecombobox = CTkComboBox(master=frame, values=['Regular', 'AP/IB/College', 'Honors'], command=sixthclasstype, )

    coursecombobox.place(relx=0.8, rely=0.56, anchor="center")

    cls7btn.place(relx=0.2, rely=0.64, anchor="center")

def class7():

    global class7enabled

    class7enabled = 0

    class7enabled += 1

    courseonelabel = CTkLabel(master=frame, text="7th Class", font=('Arial', 20))

    courseonelabel.place(relx=0.2, rely=0.64, anchor="center")

    cls7btn.place(relx=2, rely=2, anchor="center")

    gradecombobox = CTkComboBox(master=frame, values=[' ', 'A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D', 'D-', 'F'], command=seventhgrade, )

    gradecombobox.place(relx=0.5, rely=0.64, anchor="center")

    coursecombobox = CTkComboBox(master=frame, values=['Regular', 'AP/IB/College', 'Honors'], command=seventhclasstype, )

    coursecombobox.place(relx=0.8, rely=0.64, anchor="center")

# This calculates your weighted and unweighted GPA and displays it. This action will only happen if you click on the "Calculate GPA" button.
def calculate():
    global weightedlabel
    global unweightedlabel
    weightedlabel = CTkLabel(master=frame, fg_color="transparent", font=("Arial", 22), text=("Your weighted GPA is {:.2f}".format((firstgpainteger + firstgpaweight + secondgpainteger + secondgpaweight + thirdgpainteger + thirdgpaweight + fourthgpainteger + fourthgpaweight + fifthgpainteger + fifthgpaweight + sixthgpainteger + sixthgpaweight + seventhgpainteger + seventhgpaweight)/(1 + class2enabled + class3enabled + class4enabled + class5enabled + class6enabled + class7enabled))),)
    weightedlabel.place(relx=0.5, rely=0.88, anchor="center")
    unweightedlabel = CTkLabel(master=frame, fg_color="transparent", font=("Arial", 22), text=("Your unweighted GPA is {:.2f}".format((firstgpainteger + secondgpainteger + thirdgpainteger + fourthgpainteger + fifthgpainteger + sixthgpainteger + seventhgpainteger)/(1 + class2enabled + class3enabled + class4enabled + class5enabled + class6enabled + class7enabled))))
    unweightedlabel.place(relx=0.5, rely=0.78, anchor="center")

# This creates the "Calculate GPA" button seen near the bottom of the window
calculatebtn = CTkButton(master=app, text="Calculate GPA", corner_radius=32, fg_color="#0080FF", hover_color="#00CC00", height=50, width=175, command=calculate,)

calculatebtn.place(relx=0.5, rely=0.88, anchor="center")

# This creates the button that allows you to add a second class
cls2btn = CTkButton(master=frame, text="Add Class", corner_radius=32, fg_color="#0080FF", hover_color="#00CC00", height=35, width=100, command=class2, )

cls2btn.place(relx=0.2, rely=0.24, anchor="center")

# This creates the button that allows you to add a third class
cls3btn = CTkButton(master=frame, text="Add Class", corner_radius=32, fg_color="#0080FF", hover_color="#00CC00", height=35, width=100, command=class3,)

cls3btn.place(relx=2, rely=2, anchor="center")

# This creates the button that allows you to add a fourth class
cls4btn = CTkButton(master=frame, text="Add Class", corner_radius=32, fg_color="#0080FF", hover_color="#00CC00", height=35, width=100, command=class4,)

cls4btn.place(relx=2, rely=2, anchor="center")

# This creates the button that allows you to add a fifth class
cls5btn = CTkButton(master=frame, text="Add Class", corner_radius=32, fg_color="#0080FF", hover_color="#00CC00", height=35, width=100, command=class5,)

cls5btn.place(relx=2, rely=2, anchor="center")

# This creates the button that allows you to add a sixth class
cls6btn = CTkButton(master=frame, text="Add Class", corner_radius=32, fg_color="#0080FF", hover_color="#00CC00", height=35, width=100, command=class6,)

cls6btn.place(relx=2, rely=2, anchor="center")

# This creates the button that allows you to add a seventh class
cls7btn = CTkButton(master=frame, text="Add Class", corner_radius=32, fg_color="#0080FF", hover_color="#00CC00", height=35, width=100, command=class7,)

cls7btn.place(relx=2, rely=2, anchor="center")

gpacalculatequestion = CTkLabel(master=app, text="Add your grades to drop-down boxes accordingly,\n then if you have a class that a different course type,\n input that into its own drop-down box.", font=('Arial', 20))

plusminusquestion = CTkLabel(master=app, text="The GPA calculator supports the usage of +/- grades.", font=('Arial', 20))

zerogpaquestion = CTkLabel(master=app, text="When the drop-down boxes are empty.\n It registers as a zero when calculating GPA.\n When ever you input your grades,\n please make sure that none of the boxes are empty\n to ensure that the results are accurate.", font=('Arial', 20))

colormodequestion = CTkLabel(master=app, text="Yes, you can.\n Near the bottom left side of the application's window\n there is a button that will either display the text Dark or Light\n depending on the color mode you are already on.\n By default, it is set to light.", font=('Arial', 20))

def question1():
    question1btn.pack_forget()
    question1btn.place_forget()
    question2btn.pack_forget()
    question2btn.place_forget()
    question3btn.pack_forget()
    question3btn.place_forget()
    question4btn.pack_forget()
    question4btn.place_forget()
    backbtn.place(relx=0.1, rely=0.045, anchor="center")
    gpacalculatequestion.place(relx=0.5, rely=0.2, anchor="center")

def question2():
    question1btn.pack_forget()
    question1btn.place_forget()
    question2btn.pack_forget()
    question2btn.place_forget()
    question3btn.pack_forget()
    question3btn.place_forget()
    question4btn.pack_forget()
    question4btn.place_forget()
    backbtn.place(relx=0.1, rely=0.045, anchor="center")
    plusminusquestion.place(relx=0.5, rely=0.2, anchor="center")

def question3():
    question1btn.pack_forget()
    question1btn.place_forget()
    question2btn.pack_forget()
    question2btn.place_forget()
    question3btn.pack_forget()
    question3btn.place_forget()
    question4btn.pack_forget()
    question4btn.place_forget()
    backbtn.place(relx=0.1, rely=0.045, anchor="center")
    zerogpaquestion.place(relx=0.5, rely=0.2, anchor="center")

def question4():
    question1btn.pack_forget()
    question1btn.place_forget()
    question2btn.pack_forget()
    question2btn.place_forget()
    question3btn.pack_forget()
    question3btn.place_forget()
    question4btn.pack_forget()
    question4btn.place_forget()
    backbtn.place(relx=0.1, rely=0.045, anchor="center")
    colormodequestion.place(relx=0.5, rely=0.2, anchor="center")

question1btn = CTkButton(master=app, text="How do I calculate my GPA?", corner_radius=0, fg_color="#0080FF", hover_color="#00CC00", height=35, width=500, command=question1)

question2btn = CTkButton(master=app, text="How do I handle GPA calculation if my school uses +/- grading?", corner_radius=0, fg_color="#0080FF", hover_color="#00CC00", height=35, width=500, command=question2)

question3btn = CTkButton(master=app, text="Why does it say that my GPA is 0.00 when all the drop-down boxes are empty?", corner_radius=0, fg_color="#0080FF", hover_color="#00CC00", height=35, width=500, command=question3)

question4btn = CTkButton(master=app, text="Can I change the color modes?", corner_radius=0, fg_color="#0080FF", hover_color="#00CC00", height=35, width=500, command=question4)

def helppage():
     frame.place_forget()
     frame.pack_forget()
     calculatebtn.place_forget()
     helpbtn.place_forget()
     homebtn.place(relx=0.9, rely=0.045, anchor="center")
     question1btn.place(relx=0.5, rely=0.15, anchor="center")
     gpacalculatequestion.place_forget()
     plusminusquestion.place_forget()
     zerogpaquestion.place_forget()
     colormodequestion.place_forget()
     backbtn.place_forget()
     question2btn.place(relx=0.5, rely=0.22, anchor="center")
     question3btn.place(relx=0.5, rely=0.29, anchor="center")
     question4btn.place(relx=0.5, rely=0.36, anchor="center")
def homepage():
    frame.pack()
    frame.place(relx=0.5, rely=0.5, anchor="center")
    calculatebtn.place(relx=0.5, rely=0.88, anchor="center")
    helpbtn.place(relx=0.9, rely=0.95, anchor="center")
    homebtn.place_forget()
    gpacalculatequestion.place_forget()
    plusminusquestion.place_forget()
    zerogpaquestion.place_forget()
    colormodequestion.place_forget()
    question1btn.place_forget()
    question1btn.pack_forget()
    question2btn.place_forget()
    question2btn.pack_forget()
    question3btn.place_forget()
    question3btn.pack_forget()
    question4btn.place_forget()
    question4btn.pack_forget()
    backbtn.place_forget()

backbtn = CTkButton(master=app, text="Back", corner_radius=16, fg_color="#0080FF", hover_color="#00CC00", height=35, width=65, command=helppage,)

homebtn = CTkButton(master=app, text="Exit", corner_radius=16, fg_color="#0080FF", hover_color="#00CC00", height=35, width=65, command=homepage,)

# This creates the help button.
helpbtn = CTkButton(master=app, text="?  Help", corner_radius=16, fg_color="#0080FF", hover_color="#00CC00", height=35, width=65, command=helppage,)

helpbtn.place(relx=0.9, rely=0.95, anchor="center")

# This allows the application to not immediately close.
app.mainloop()