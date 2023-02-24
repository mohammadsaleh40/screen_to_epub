import tkinter as tk
from awesometkinter.bidirender import add_bidi_support, render_text , derender_bidi_text
# create the Tkinter window
last_text = ""
window = tk.Tk()
window.title("File Viewer")

# create a label to display the file contents
file_contents = tk.StringVar()

label = tk.Text(window , )
label.pack()

# define a function to update the label with the file contents
def update_contents():
    global last_text
    with open("file.txt", "r") as f:
        contents = f.read()
        #file_contents.set(contents)
        if last_text != contents:
            last_text = contents
            label.delete('1.0', tk.END)
        
            label.insert(tk.END, render_text(contents))
        
        #file_contents.set(render_text(contents))
    # schedule the function to run again in 1 second
    window.after(1000, update_contents)
def save_text():
    f = open("file.txt" , "w")
    f.write(derender_bidi_text(label.get("1.0", "end-1c")))
    
    f.close()
    
def send_text():
    f = open("f_file.txt" , "a")
    f.write(derender_bidi_text(label.get("1.0", "end-1c")))
    
    f.close()
    label.delete('1.0', tk.END)
def update_text():
    with open("file.txt", "r") as f:
        contents = f.read()
        label.insert(tk.END, render_text(contents))
# call the function to start displaying the file contents
update_contents()
button = tk.Button(text="Save", command=save_text)
button.pack()
update = tk.Button(text="update", command=update_text)
update.pack()
button_send = tk.Button(text="Send", command=send_text)
button_send.pack()
# run the Tkinter event loop
window.mainloop()
