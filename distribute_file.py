from tkinter import *
from tkinter import filedialog
from openpyxl import load_workbook

def select_student_list():
    root.class_list = filedialog.askopenfilename(initialdir = ".", title = "Select Student List")

def select_source_file():
    root.source_file = filedialog.askopenfilename(initialdir = ".", title = "Select Source File")

def select_destination():
    root.destination = filedialog.askdirectory(initialdir = ".", title = "Select Desintation Folder")

def go():
    # create student list
    workbook = load_workbook(filename=root.class_list)
    sheet = workbook.active
    row_count = 3
    while sheet.cell(row=row_count, column=1).value != None:
        print(sheet.cell(row=row_count, column=1).value)
        row_count += 1

root = Tk()
root.geometry("600x400")
root.title("CaRAF")

# create file variables
root.class_list = ""
root.source_file = ""
root.destination = ""


Label(root, text="Copy and Rename Assessment Files", font=("Arial",20)).grid(row=0,column=0)
Button(root, text="Select student list", command=select_student_list).grid(row=1,column=0)
Button(root, text="Select source file", command=select_source_file).grid(row=2,column=0)
Button(root, text="Select destination folder", command=select_destination).grid(row=3,column=0)
Button(root,text="Go", command=go).grid(row=4,column=0)


root.mainloop()