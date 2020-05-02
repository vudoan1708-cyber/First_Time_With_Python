# setup the GUI
import tkinter as tk;

# to access users file directory, pick apps, and display some texts
from tkinter import filedialog, Text;

# allow us to run the app
import os;
# print("Package Loaded");

root = tk.Tk();

# create an empty array
apps = [];

if os.path.isfile('save.txt'):
    # r means read
    with open('D:\DesignWork\Programming\Python\Works\Apps\save.txt', 'r') as f:
        tempApps = f.read();
        # print(tempApps);
        # split them into an array
        tempApps = tempApps.split(',');
        apps = [x for x in tempApps if x.strip()];

# functions
def addApp() :
    # print('HEY')
    # pass;
    filename = filedialog.askopenfilename(initialdir='/', title='Select File',
                                        filetypes=( ('executables', '*.exe'), ('all files', '*.*') ));  
    # work like push in js
    apps.append(filename);     
    # print(filename);
    # print(apps);

    # loop through the app files
    for app in apps:
        # add labels to them and show them on the app
        # if the length of apps is larger than 1 (2, 3, 4, ...)
        if len(apps) > 1:
            # get the last item (by getting the total length and subtracting it by 1)
            # 3 files => apps[3-1] = apps[2] (0, 1, 2)
            last_item = apps[len(apps) - 1];
            label_added = tk.Label(frame, text=last_item, bg='gray');
            label_added.pack();
            break;
            
        label = tk.Label(frame, text=app, bg='gray');
        label.pack();

def runApps() :
    for app in apps:
        os.startfile(app);

def deleteApp():
    # if there is one or more apps stored in the text file
    if len(apps) > 0:
        # itereate through the array
        for app in apps:
            # find the last item
            last_item = len(apps) - 1;
            # use pop function to get rid of it
            poppedApp = apps.pop(last_item);
            # print(poppedApp);
            # print(apps);
            label_popped = tk.Label(frame, text=apps, bg='gray');
            label_popped.pack();

# create canvas
width = 700;
height = 700;
colour = '#263d42';
canvas = tk.Canvas(root, width = width, height = height, bg = colour);

# attach canvas to the root
canvas.pack();

# add a frame (similar to adding a html tag)
frame = tk.Frame(root, bg = 'white');

# attach frame to the root, set its width, height, x, y
# rel means relative
frame.place(relwidth = 0.8, relheight = 0.8, relx = 0.1, rely = 0.1);

# add buttons
# fg means foreground (applying colour to the text)
openFile_btn = tk.Button(root, text = 'Open File',
                            padx = 10, pady = 5, fg = 'white', bg = colour, command = addApp);
openFile_btn.pack();

runApps_btn = tk.Button(root, text = 'Run',
                            padx = 10, pady= 5, fg = 'white', bg = colour, command = runApps);
runApps_btn.pack();

deleteApps_btn = tk.Button(root, text='Delete', padx = 10, pady = 5,
                                fg = 'white', bg = colour, command = deleteApp);
deleteApps_btn.pack();

for app in apps:
    # only get the name of the apps
    # if (len(apps) > 0):
    #     tempApp_Name = app.split('/');
    #     app = (x for x in tempApp_Name);
    #     print(app);
    label = tk.Label(frame, text=app);
    label.pack();

root.mainloop();

# save all the apps into a text file
# 'w' means write
with open('D:\DesignWork\Programming\Python\Works\Apps\save.txt', 'w') as f:
    for app in apps:
        # in a scenario where users close the directory without adding any file
        # it will put in a white space
        if (app == '' or app == None):
            print(app);
            break;
        else: f.write(app + ',');