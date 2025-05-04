import tkinter as tk
from tkinter import messagebox
from user_management import register_user, login_user
from voice_translator import load_languages, take_command, translate_and_speak

class TranslatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("LinguaBridge")
        self.root.geometry("400x500")
        self.login_ui()

    def login_ui(self):
        self.clear_window()
        tk.Label(self.root, text="LinguaBridge", font=("Times New Roman", 30, "bold")).pack(pady=10)
        tk.Label(self.root, text="Email").pack()
        self.email = tk.Entry(self.root)
        self.email.pack()
        tk.Label(self.root, text="Password").pack()
        self.password = tk.Entry(self.root, show="*")
        self.password.pack()
        tk.Button(self.root, text="Login", command=self.login).pack(pady=5)
        tk.Button(self.root, text="Register", command=self.register_ui).pack()

    def register_ui(self):
        self.clear_window()
        tk.Label(self.root, text="Register", font=("Times New Roman", 30, "bold")).pack(pady=10)
        tk.Label(self.root, text="Name").pack()
        self.name = tk.Entry(self.root)
        self.name.pack()
        tk.Label(self.root, text="Email").pack()
        self.email = tk.Entry(self.root)
        self.email.pack()
        tk.Label(self.root, text="Password").pack()
        self.password = tk.Entry(self.root, show="*")
        self.password.pack()
        tk.Button(self.root, text="Register", command=self.register).pack(pady=5)
        tk.Button(self.root, text="Back to Login", command=self.login_ui).pack()

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def login(self):
        email = self.email.get()
        password = self.password.get()
        if login_user(email, password):
            self.voice_translator_ui()
        else:
            messagebox.showerror("Login Failed", "Invalid credentials")

    def register(self):
        name = self.name.get()
        email = self.email.get()
        password = self.password.get()
        if register_user(name, email, password):
            messagebox.showinfo("Success", "Registered successfully")
            self.login_ui()
        else:
            messagebox.showerror("Error", "Registration failed")

    def voice_translator_ui(self):
        self.clear_window()
        tk.Label(self.root, text="Voice Translator", font=("Times New Roman", 25)).pack(pady=10)

        self.lang_dict = load_languages()
        self.input_text = None

        tk.Button(self.root, text="Speak Sentence", command=self.capture_sentence).pack(pady=5)
        self.input_display = tk.Text(self.root, height=3, width=40, wrap=tk.WORD)
        self.input_display.pack(pady=5)
        self.input_display.insert(tk.END, "Your spoken sentence will appear here...")

        tk.Button(self.root, text="Speak Target Language", command=self.set_language_by_voice).pack(pady=5)

        self.language_var = tk.StringVar()
        tk.Label(self.root, text="Selected Language:").pack()
        self.language_label = tk.Label(self.root, textvariable=self.language_var, font=("Arial", 12))
        self.language_label.pack(pady=2)

        tk.Button(self.root, text="Translate", command=self.translate_sentence).pack(pady=10)

        self.output_text = tk.Text(self.root, height=5, width=45, wrap=tk.WORD)
        self.output_text.pack(pady=10)

    def capture_sentence(self):
        self.input_text = take_command()
        self.input_display.delete("1.0", tk.END)
        if self.input_text == "None":
            self.input_display.insert(tk.END, "Could not understand your speech.")
        else:
            self.input_display.insert(tk.END, self.input_text)

    def set_language_by_voice(self):
        spoken_lang = take_command().lower()
        if spoken_lang in self.lang_dict:
            self.language_var.set(spoken_lang)
        else:
            messagebox.showerror("Error", f"'{spoken_lang}' not supported. Try again.")

    def translate_sentence(self):
        if not self.input_text or self.input_text == "None":
            messagebox.showerror("Error", "Please speak a sentence first.")
            return

        to_lang = self.language_var.get().lower()
        if to_lang not in self.lang_dict:
            messagebox.showerror("Error", "Please speak a valid target language.")
            return

        self.output_text.delete("1.0", tk.END)
        try:
            translated = translate_and_speak(self.input_text, self.lang_dict[to_lang])
            self.output_text.insert(tk.END, f"{translated}")
        except Exception as e:
            self.output_text.insert(tk.END, f"Error: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = TranslatorApp(root)
    root.mainloop()