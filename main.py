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

def buildConfig(file_mode):
    config = open(path, "{0}".format(file_mode))
    config.write("echo \"autoexec.cfg has been loaded!\"")
    config.close()
    
    try:
        get_fps_max = float(fps_max.get())
        get_sensitivity = float(sensitivity.get())
    except ValueError as e:
        messagebox.showerror("Only numeric allowed!", "Only numeric values allowed in FPS and Sensitivity!")
    else:
        config = open(path, "a")
        if get_fps_max != "":
            config.write("\n\nfps_max \"{0}\"".format(get_fps_max))
        
        if get_sensitivity < 0 or get_sensitivity > 10:
            messagebox.showerror("Value Error", "Only values between 0-10 allowed!")
        elif get_sensitivity != "":
            config.write("\n\nsensitivity \"{0}\"".format(get_sensitivity))
            
        if bhop.get() == True:
            config.write("""\n\nbind "mwheelup" "exec jump"\nbind "mwheeldown" "exec jump" """)
        
        if auto_buy.get() == True:
            config.write("""\n\nalias custom1 "autobuy"\nalias custom2 "buy flashbang; buy smokegrenade; buy molotov; buy hegrenade; buy defuser"\nalias custom3 "buy flashbang; buy smokegrenade; buy molotov; buy flashbang; buy defuser"\nalias +secondarycommand "key1; key2; key3;"\nalias -secondarycommand "def1; def2; def3;"\nbind mouse4 +secondarycommand """)
        
        if nade_binds.get() == True:
            config.write("""\n\nalias customC "slot10"\nalias customQ "slot7"\nalias customE "slot6"\nalias customF "slot8"\nalias customG "slot9"\nalias +secondarycommand "keyC; keyQ; keyE; keyF; keyG;"\nalias -secondarycommand "defC; defQ; defE; defF; defG;"\nbind mouse4 +secondarycommand """)
            
        config.close()

def generate():
    if checkDirectory() == True:
        try:
            buildConfig("x")
        except FileExistsError:
            answer = messagebox.askquestion("File already exists!", "Are you sure you want to over-write the file.")
            
            if answer == "yes":
                buildConfig("w")

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

lbl_fps_max = Label(left_frame, text="Max FPS", bg="#0F0F0F", fg="#008170")
fps_max = StringVar()
ent_fps_max = Entry(left_frame, textvariable=fps_max)
lbl_fps_max.grid(row=1, column=1)
ent_fps_max.grid(row=1, column=3)

lbl_sensitivity = Label(left_frame, text="Sensitivity", bg="#0F0F0F", fg="#008170")
sensitivity = StringVar()
ent_sensitivity = Entry(left_frame, textvariable=sensitivity)
lbl_sensitivity.grid(row=2, column=1)
ent_sensitivity.grid(row=2, column=3)

right_frame = Frame(window, bg="#0F0F0F")
right_frame.grid(row=1, column=2, padx=15, pady=15)

bhop = IntVar()
chk_bhop = Checkbutton(right_frame, variable=bhop, text="Set scroll-wheel bunny hop keybinds", bg="#0F0F0F", fg="#008170", activebackground="#0F0F0F", activeforeground="#008170")
chk_bhop.grid(row=1, column=3)

auto_buy = IntVar()
chk_auto_buy = Checkbutton(right_frame, variable=auto_buy, text="Set auto-buy keybinds", bg="#0F0F0F", fg="#008170", activebackground="#0F0F0F", activeforeground="#008170")
chk_auto_buy.grid(row=2, column=3)

nade_binds = IntVar()
chk_nade_binds= Checkbutton(right_frame, variable=nade_binds, text="Set nade shortcut keybinds", bg="#0F0F0F", fg="#008170", activebackground="#0F0F0F", activeforeground="#008170")
chk_nade_binds.grid(row=3, column=3)

btn_generate = Button(master=window, text="Generate", bg="#0F0F0F", fg="#008170", activebackground="#008170", activeforeground="#0F0F0F", bd=1, padx=5, pady=5, command=generate)
btn_generate.grid(row=3, column=0, columnspan=3)

window.mainloop()