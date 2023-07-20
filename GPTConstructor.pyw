import os

try:
 import pyperclip
except:
    print("Module not found! Installing...")
    os.system("python -m pip install pyperclip")
    import pyperclip
import time
try:
  import threading
except:
    print("Module not found! Installing...")
    os.system("python -m pip install threading")
    import threading
try:
  import openai
except:
    print("Module not found! Installing...")
    os.system("python -m pip install openai")
    import openai
try:
  import customtkinter
except:
    print("Module not found! Installing...")
    os.system("python -m pip install customtkinter")
    import customtkinter
model = "gpt-3.5-turbo-0613"

class App():
    def __init__(self):
     self.app = customtkinter.CTk()
     self.api = ""
     self.Tlabel = customtkinter.CTkLabel(master=self.app)
     self.model = "gpt-3.5-turbo-0613"
     self.mode = "system"
     self.messages = []
     self.r = 2
     self.r2 = 2
    def rev(self,box2):
        self.Chat(box2)

    def Chat(self,box2):
        global Entry2
        Entry2 = customtkinter.CTkEntry(master=self.app)
        Entry2.place(relx=0.35, rely=0.9, anchor=customtkinter.CENTER)
        def send():
            global llabel
            llabel = customtkinter.CTkLabel(master=self.app, text="Loading...")
            llabel.place(relx=0.5, rely=0.8, anchor=customtkinter.CENTER)
            msg1 = Entry2.get()
            box2.insert(index=f"{self.r2}.0", text="\n" + "You: " + msg1)
            self.r2 += 1
            def thr1():
                global messages
                global r
                global model
                entrbutton2.destroy()
                Entry2.destroy()
                progress = customtkinter.CTkProgressBar(master=self.app)
                progress.place(relx=0.5, rely=0.9, anchor=customtkinter.CENTER)
                progress.set(0.1)
                llabel.configure(text="Saving msg...")
                self.messages.append({"role": "user", "content": msg1})
                progress.set(0.3)
                llabel.configure(text="Creating completion...")
                completion = openai.ChatCompletion.create(
                    model=model,
                    messages=self.messages
                )
                progress.set(0.7)
                llabel.configure(text="Writing response...")
                chat_response = completion.choices[0].message.content
                progress.set(0.8)
                llabel.configure(text="Box writing...")
                box2.insert(index=f"{self.r2}.0", text="\n" + "ChatGPT: " + chat_response)
                progress.set(0.9)
                llabel.configure(text="Saving response...")
                self.messages.append({"role": "assistant", "content": chat_response})
                pyperclip.copy(chat_response)
                progress.set(1)
                llabel.configure(text="complete!", text_color=("green"))
                time.sleep(0.1)
                self.r2 += chat_response.count('\n') + 1

                progress.destroy()
                llabel.destroy()
                self.rev(box2)
            if __name__ == "__main__":
                thr1 = threading.Thread(target=thr1)
                thr1.start()
        global entrbutton2
        entrbutton2 = customtkinter.CTkButton(master=self.app, text="Enter", command=send)
        entrbutton2.place(relx=0.65, rely=0.9, anchor=customtkinter.CENTER)
    def Constructor(self):
        try:
            entrbutton2.destroy()
            box2.destroy()
            Entry2.destroy()
            backbutton.destroy()
        except:
            pass
        self.app.geometry("600x500")
        self.Tlabel.configure(text=f"Constructor: {self.mode}")
        def check(s):
            option = s
            if option == "System":
                self.mode = "system"
            if option == "Assistant":
                self.mode = "assistant"
            if option == "User":
                self.mode = "user"
        def Send():
            msg1 = Entry.get()
            box.insert(index=f"{self.r}.0", text="\n" + f"{self.mode}: " + msg1)
            self.messages.append({"role": f"{self.mode}", "content": msg1})
            self.r += 1
        def reset():
            box.insert(index=f"{self.r}.0", text="\nHistory cleared")
            self.r += 1
            self.messages = []
        openai.api_key = self.api
        global menu
        menu = customtkinter.CTkOptionMenu(master=self.app, values=["System", "Assistant", "User"], command=check)
        menu.place(relx=0.51, rely=0.05, anchor=customtkinter.CENTER)
        global Entry
        global continuebutton
        global entrbutton
        entrbutton = customtkinter.CTkButton(master=self.app, text="Enter", command=Send)
        box.configure(width=500, height=300)
        box.place(relx=0.5, rely=0.45, anchor=customtkinter.CENTER)
        Entry = customtkinter.CTkEntry(master=self.app)
        continuebutton = customtkinter.CTkButton(master=self.app, text="continue", command=self.Prechatting)
        resetbutton = customtkinter.CTkButton(master=self.app, text="Reset", command=reset)
        resetbutton.place(relx=0.15, rely=0.05, anchor=customtkinter.CENTER)
        Entry.place(relx=0.35, rely=0.9, anchor=customtkinter.CENTER)
        entrbutton.place(relx=0.65, rely=0.9, anchor=customtkinter.CENTER)
        continuebutton.place(relx=0.85, rely=0.05, anchor=customtkinter.CENTER)
    def Prechatting(self):
        Entry.destroy()
        menu.destroy()
        entrbutton.destroy()
        continuebutton.destroy()
        self.Tlabel.configure(text="ChatGPT chat")
        box.configure(width=200, height=300)
        box.place(relx=0.2, rely=0.5, anchor=customtkinter.CENTER)
        global box2
        box2 = customtkinter.CTkTextbox(master=self.app, width=200, height=300)
        box2.place(relx=0.8, rely=0.5, anchor=customtkinter.CENTER)
        box2.insert(index="0.0", text="this is a chat textbox. Here you can see your messages with chatGPT")
        global backbutton
        backbutton = customtkinter.CTkButton(master=self.app, text="Back", command=self.Constructor)
        backbutton.place(relx=0.15, rely=0.05, anchor=customtkinter.CENTER)
        self.Chat(box2)
    def Main(self):
        customtkinter.set_appearance_mode("System")
        customtkinter.set_default_color_theme("green")
        self.app.geometry("400x240")
        self.Tlabel.configure(text="API")
        self.Tlabel.place(relx=0.5, rely=0.11, anchor=customtkinter.CENTER)
        self.app.title("GPTConstructor")
        global box
        box = customtkinter.CTkTextbox(master=self.app)
        box.insert(index="0.0", text="This is a constructor textbox. Here you can see your messages")
        def api():
         dialog = customtkinter.CTkInputDialog(title="API", text="type your api key.")
         key = dialog.get_input()
         if key == None:
              api()
         else:
             self.api = key
        api()
        self.Constructor()
    def loop(self):
        self.app.mainloop()
app = App()
app.Main()
app.loop()
