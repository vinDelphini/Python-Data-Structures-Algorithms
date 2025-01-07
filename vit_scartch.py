from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES
import threading
import time
import speech_recognition as sr

# Initialize the main application window
Screen = Tk()
Screen.title("Language Translator")
Screen.attributes("-fullscreen", True)

# Function to create gradient background
def create_gradient(canvas, color1, color2, width, height):
    for i in range(height):
        ratio = i / height
        r = int((1 - ratio) * color1[0] + ratio * color2[0])
        g = int((1 - ratio) * color1[1] + ratio * color2[1])
        b = int((1 - ratio) * color1[2] + ratio * color2[2])
        color = f"#{r:02x}{g:02x}{b:02x}"
        canvas.create_line(0, i, width, i, fill=color)

# Set screen dimensions and apply background gradient
width = Screen.winfo_screenwidth()
height = Screen.winfo_screenheight()

canvas = Canvas(Screen, width=width, height=height, highlightthickness=0)
canvas.pack(fill="both", expand=True)
create_gradient(canvas, (255, 255, 255), (173, 216, 230), width, height)

# Initialize Translator and language choices dynamically
translator = Translator()
language_codes = LANGUAGES
LanguageChoices = list(language_codes.values())

# Set up language selection variables and initial selections
InputLanguageChoice = StringVar()
TranslateLanguageChoice = StringVar()
InputLanguageChoice.set('english')
TranslateLanguageChoice.set('hindi')

# Variable for auto-detect checkbox
auto_detect = BooleanVar()
auto_detect.set(False)  # Default is False

# Variables for loading spinner
is_loading = False
loading_text = StringVar(value="")

# Loading animation function
def show_loading_animation():
    symbols = ["|", "/", "-", "\\"]
    idx = 0
    while is_loading:
        loading_text.set(f"Translating {symbols[idx % len(symbols)]}")
        idx += 1
        time.sleep(0.2)
        Screen.update_idletasks()

# Start translation with loading animation
def start_translation():
    global is_loading
    is_loading = True
    threading.Thread(target=show_loading_animation, daemon=True).start()
    threading.Thread(target=Translate, daemon=True).start()

# Translation function with auto-detection
def Translate():
    global is_loading
    try:
        text_to_translate = TextVar.get()

        # Determine source language
        if auto_detect.get():
            detected_lang = translator.detect(text_to_translate).lang
            from_lang_code = detected_lang
            detected_lang_name = language_codes.get(detected_lang, "Unknown Language").capitalize()
            InputLanguageChoice.set(detected_lang_name)
        else:
            from_lang_code = list(language_codes.keys())[list(language_codes.values()).index(InputLanguageChoice.get())]

        to_lang_code = list(language_codes.keys())[list(language_codes.values()).index(TranslateLanguageChoice.get())]

        # Perform translation
        Translation = translator.translate(text_to_translate, src=from_lang_code, dest=to_lang_code)
        translated_text = Translation.text
        OutputVar.set(translated_text)

    except Exception as e:
        OutputVar.set(f"Translation Error: {str(e)}. Please check your connection and try again.")
    finally:
        is_loading = False
        loading_text.set("")

# Function to capture audio and convert it to text
def capture_audio():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        OutputVar.set("Listening...")
        Screen.update_idletasks()
        try:
            audio = recognizer.listen(source, timeout=5)
            detected_text = recognizer.recognize_google(audio)
            TextVar.set(detected_text)  # Set the recognized text to the TextVar
            OutputVar.set("")  # Clear any previous output
            start_translation()  # Automatically start translation
        except sr.UnknownValueError:
            OutputVar.set("Could not understand audio.")
        except sr.RequestError as e:
            OutputVar.set(f"Could not request results; {e}")
        except Exception as e:
            OutputVar.set(f"Error: {str(e)}")

# Function to toggle auto-detect feature
def toggle_auto_detect():
    if auto_detect.get():
        InputLanguageChoiceMenu.config(state='disabled')
    else:
        InputLanguageChoiceMenu.config(state='readonly')

# Function to filter language choices based on search query
def filter_languages(event, choice_menu, search_var):
    search_term = search_var.get().lower()
    filtered_languages = [lang for lang in LanguageChoices if search_term in lang.lower()]
    choice_menu["values"] = filtered_languages

# GUI Layout
header = Label(canvas, text="Language Translator", font=("Helvetica", 36, "bold"), fg="#2D3142", bg="#ADD8E6")
header.place(relx=0.5, rely=0.1, anchor=CENTER)

frame = Frame(canvas, bg="#FFFFFF", highlightbackground="#C2E2FF", highlightthickness=2, bd=5, relief="solid")
frame.place(relx=0.5, rely=0.3, anchor=CENTER, width=width * 0.6, height=height * 0.25)

# From Language Selection with Search
Label(frame, text="From:", font=("Helvetica", 16), bg="#FFFFFF").grid(row=0, column=0, padx=10, pady=10, sticky=E)
InputLanguageChoiceMenu = ttk.Combobox(frame, textvariable=InputLanguageChoice, values=LanguageChoices, state="readonly", font=("Helvetica", 12))
InputLanguageChoiceMenu.grid(row=0, column=1, padx=15, pady=10, sticky=W)

InputSearchVar = StringVar()
InputSearchBox = Entry(frame, textvariable=InputSearchVar, font=("Helvetica", 12))
InputSearchBox.grid(row=0, column=2, padx=10, pady=10, sticky=W)
InputSearchBox.bind("<KeyRelease>", lambda event: filter_languages(event, InputLanguageChoiceMenu, InputSearchVar))

# Auto-Detect Checkbox
AutoDetectCheck = Checkbutton(frame, text="Auto-Detect Language", variable=auto_detect, command=toggle_auto_detect, font=("Helvetica", 12), bg="#FFFFFF")
AutoDetectCheck.grid(row=0, column=3, padx=10, pady=10, sticky=W, columnspan=2)

# To Language Selection with Search
Label(frame, text="To:", font=("Helvetica", 16), bg="#FFFFFF").grid(row=1, column=0, padx=10, pady=10, sticky=E)
TranslateLanguageChoiceMenu = ttk.Combobox(frame, textvariable=TranslateLanguageChoice, values=LanguageChoices, state="readonly", font=("Helvetica", 12))
TranslateLanguageChoiceMenu.grid(row=1, column=1, padx=15, pady=10, sticky=W)

TranslateSearchVar = StringVar()
TranslateSearchBox = Entry(frame, textvariable=TranslateSearchVar, font=("Helvetica", 12))
TranslateSearchBox.grid(row=1, column=2, padx=10, pady=10, sticky=W)
TranslateSearchBox.bind("<KeyRelease>", lambda event: filter_languages(event, TranslateLanguageChoiceMenu, TranslateSearchVar))

# Spacer to align elements
Label(frame, text="", bg="#FFFFFF").grid(row=1, column=2, columnspan=2)

text_frame = Frame(canvas, bg="#FFFFFF", highlightbackground="#C2E2FF", highlightthickness=2, bd=5, relief="solid")
text_frame.place(relx=0.5, rely=0.6, anchor=CENTER, width=width * 0.6, height=height * 0.3)

# Enter Text
Label(text_frame, text="Enter Text:", font=("Helvetica", 16), bg="#FFFFFF").grid(row=0, column=0, padx=10, pady=15, sticky=E)
TextVar = StringVar()
TextBox = Entry(text_frame, textvariable=TextVar, width=40, font=("Helvetica", 14), relief="solid", bd=2)
TextBox.grid(row=0, column=1, padx=10, pady=15)

# Loading indicator
Label(text_frame, textvariable=loading_text, font=("Helvetica", 12, "italic"), fg="#6D8299", bg="#FFFFFF").grid(row=1, column=1, padx=5, pady=5)

# Output Text
OutputVar = StringVar()
Label(text_frame, text="Output:", font=("Helvetica", 16), bg="#FFFFFF").grid(row=2, column=0, padx=10, pady=15, sticky=E)
OutputBox = Entry(text_frame, textvariable=OutputVar, width=40, font=("Helvetica", 14), relief="solid", bd=2)
OutputBox.grid(row=2, column=1, padx=10, pady=15)

# Buttons for Translate and Audio Input
button_frame = Frame(canvas, bg="#ADD8E6")
button_frame.place(relx=0.5, rely=0.9, anchor=CENTER)

Button(button_frame, text="Translate", command=start_translation, font=("Helvetica", 14, "bold"), bg="#4682B4", fg="white", width=15).grid(row=0, column=0, padx=10)
Button(button_frame, text="Speak", command=capture_audio, font=("Helvetica", 14, "bold"), bg="#4682B4", fg="white", width=15).grid(row=0, column=1, padx=10)
Button(button_frame, text="Exit", command=Screen.destroy, font=("Helvetica", 14, "bold"), bg="#FF6347", fg="white", width=15).grid(row=0, column=2, padx=10)

Screen.mainloop()