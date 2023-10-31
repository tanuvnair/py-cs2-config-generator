from tkinter import *
from tkinter import messagebox
import os

path = "./generated-configs/autoexec.cfg"

def checkDirectory():
    if os.path.exists("./generated-configs"):
        return True
    else:
        os.mkdir("generated-configs")
        return True

def addConfigStart(file_mode):
    config = open(path, "{0}".format(file_mode))
    config.write("echo \"autoexec.cfg has been loaded!\"")
    config.close()
    
    config = open(path, "a")
    if max_fps.get() != "":
        config.write("\n\nfps_max \"{0}\"".format(max_fps.get()))
    
    if sensitivity.get() != "":
        config.write("\n\nsensitivity \"{0}\"".format(sensitivity.get()))
        
    if bhop.get() == True:
        config.write("""
                     \nbind "mwheelup" "exec jump"\nbind "mwheeldown" "exec jump"
                     """)
    
    if auto_buy.get() == True:
        config.write("""\nalias custom1 "autobuy"\nalias custom2 "buy flashbang; buy smokegrenade; buy molotov; buy hegrenade; buy defuser"\nalias custom3 "buy flashbang; buy smokegrenade; buy molotov; buy flashbang; buy defuser"\nalias +secondarycommand "key1; key2; key3;"\nalias -secondarycommand "def1; def2; def3;"\nbind mouse4 +secondarycommand
                     """)
        
    config.close()

def createConfig():
    if checkDirectory() == True:
        try:
            addConfigStart("x")
        except FileExistsError:
            answer = messagebox.askquestion("File already exists!", "Are you sure you want to over-write the file.")
            
            if answer == "yes":
                addConfigStart("w")

def generate():
    createConfig()

window = Tk()
window.title("Counter-Strike 2 Config Generator")
window.geometry("+850+350")
window.resizable(False, False)
window.configure(bg="#0F0F0F")
window['padx'] = 2
window['pady'] = 5

lbl_title = Label(master=window, text="Counter-Strike 2 Config Generator", font = "80", padx=5, pady=5, bg="#0F0F0F", fg="#008170")
lbl_title.grid(row=0, column=0, columnspan=3)

left_frame = Frame(window, padx=5, bg="#0F0F0F")
left_frame.grid(row=1, column=0)

lbl_max_fps = Label(left_frame, text="Max FPS", bg="#0F0F0F", fg="#008170")
max_fps = StringVar()
ent_max_fps = Entry(left_frame, textvariable=max_fps)
lbl_max_fps.grid(row=1, column=1)
ent_max_fps.grid(row=1, column=3)

lbl_sensitivity = Label(left_frame, text="Sensitivity", bg="#0F0F0F", fg="#008170")
sensitivity = StringVar()
ent_sensitivity = Entry(left_frame, textvariable=sensitivity)
lbl_sensitivity.grid(row=2, column=1)
ent_sensitivity.grid(row=2, column=3)

right_frame = Frame(window, bg="#0F0F0F")
right_frame.grid(row=1, column=2, padx=15, pady=15)

bhop = IntVar()
chk_bhop = Checkbutton(right_frame, variable=bhop, text="Set scroll-wheel bunny hop binds", bg="#0F0F0F", fg="#008170", activebackground="#0F0F0F", activeforeground="#008170")
chk_bhop.grid(row=1, column=3)

auto_buy = IntVar()
chk_auto_buy = Checkbutton(right_frame, variable=auto_buy, text="Set auto-buy binds", bg="#0F0F0F", fg="#008170", activebackground="#0F0F0F", activeforeground="#008170")
chk_auto_buy.grid(row=2, column=3)

btn_generate = Button(master=window, text="Generate", bg="#0F0F0F", fg="#008170", activebackground="#008170", activeforeground="#0F0F0F", bd=1, padx=5, pady=5, command=generate)
btn_generate.grid(row=3, column=0, columnspan=3)

window.mainloop()