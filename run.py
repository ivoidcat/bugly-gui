import tkinter as tk
from subprocess import call

class GuiApp:
    def __init__(self, master):
        self.master = master
        master.title("BuglyQQ Upload Symbol GUI")

        self.appid_label = tk.Label(master, text="App ID:")
        self.appkey_label = tk.Label(master, text="App Key:")
        self.bundleid_label = tk.Label(master, text="Bundle ID:")
        self.platform_label = tk.Label(master, text="Platform:")
        self.symbol_label = tk.Label(master, text="Input Symbol:")
        self.version_label = tk.Label(master, text="Version:")

        self.appid = tk.Entry(master)
        self.appkey = tk.Entry(master)
        self.bundleid = tk.Entry(master)
        self.platform = tk.Entry(master)
        self.symbol = tk.Entry(master)
        self.version = tk.Entry(master)

        self.execute_button = tk.Button(master, text="Execute", command=self.execute_command)

        self.appid_label.grid(row=0, column=0)
        self.appid.grid(row=0, column=1)
        self.appkey_label.grid(row=1, column=0)
        self.appkey.grid(row=1, column=1)
        self.bundleid_label.grid(row=2, column=0)
        self.bundleid.grid(row=2, column=1)
        self.platform_label.grid(row=3, column=0)
        self.platform.grid(row=3, column=1)
        self.symbol_label.grid(row=4, column=0)
        self.symbol.grid(row=4, column=1)
        self.version_label.grid(row=5, column=0)
        self.version.grid(row=5, column=1)

        self.execute_button.grid(row=6, columnspan=2)

    def execute_command(self):
        command = f"java -jar buglyqq-upload-symbol.jar -appid {self.appid.get()} -appkey {self.appkey.get()} -bundleid {self.bundleid.get()} -platform {self.platform.get()} -inputSymbol {self.symbol.get()} -version {self.version.get()}"
        call(command, shell=True)
root = tk.Tk()
app = GuiApp(root)
root.mainloop()
