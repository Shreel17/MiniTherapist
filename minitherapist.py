import tkinter as tk
from textblob import TextBlob
import random
import pyttsx3
import speech_recognition as sr

# Tips based on mood
positive_tips = [
    "Keep shining! You're doing amazing.",
    "Celebrate your wins, big or small!",
    "Stay grateful — it multiplies happiness.",
    "Your smile can brighten someone’s day.",
    "Keep spreading positivity like confetti!",
    "Your energy is contagious — use it well!",
    "Believe in your magic, always.",
    "Keep doing what makes your soul happy!",
    "You're on the right track. Keep going!",
    "Happiness looks so good on you!"
]


negative_tips = [
    "Take a deep breath, everything will be okay.",
    "It’s okay to feel low sometimes. Be kind to yourself.",
    "Try listening to your favorite music or take a short walk.",
    "Talk to someone — you're not alone.",
    "Breathe. This feeling will pass.",
    "Your feelings are valid — don’t suppress them.",
    "Self-care is not selfish. Rest, reflect, recover."
]

neutral_tips = [
    "Maintain balance and take short breaks.",
    "Stay mindful and focused!",
    "Do something today that makes you smile.",
    "A short walk can refresh your mind.",
    "Try journaling to connect with your thoughts.",
    "Listen to your favorite music for 5 minutes.",
    "Make a cup of tea and relax for a bit.",
    "Check in with yourself: How are you really feeling?",
    "Read a quote or book that inspires you.",
    "Silence is okay. Use it to recharge.",
    "Try something new — even if it's small."
]

# Initialize text-to-speech engine
engine = pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Speech-to-text input
recognizer = sr.Recognizer()
def listen_to_user():
    try:
        with sr.Microphone() as source:
            speak("I'm listening. Tell me how you're feeling today.")
            audio = recognizer.listen(source, timeout=5)
            text = recognizer.recognize_google(audio)
            entry.delete(0, tk.END)
            entry.insert(0, text)
            check_mood()
    except Exception as e:
        speak("Sorry, I couldn't understand you. Please try typing instead.")

# Analyze mood and display results
def check_mood():
    text = entry.get()
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity > 0.1:
        mood = "Positive"
        tip = random.choice(positive_tips)
        root.config(bg='#d4fcdc')  # Light green
    elif polarity < -0.1:
        mood = "Negative"
        tip = random.choice(negative_tips)
        root.config(bg='#f8d7da')  # Light red
    else:
        mood = "Neutral"
        tip = random.choice(neutral_tips)
        root.config(bg='#dbefff')  # Light blue

    result_label.config(text=f"Mood: {mood}")
    tip_label.config(text=tip)
    speak(tip)

# GUI setup
root = tk.Tk()
root.title("Mini Virtual Therapist")
root.geometry("400x450")
root.config(bg='#ffffff')

# Title label
title = tk.Label(root, text="Mood Checker", font=("Helvetica", 18, "bold"))
title.pack(pady=10)

# Entry for user input
entry = tk.Entry(root, font=("Helvetica", 14), width=40)
entry.pack(pady=10)

# Result label
result_label = tk.Label(root, text="", font=("Helvetica", 14), bg='#ffffff')
result_label.pack(pady=10)

# Tip label
tip_label = tk.Label(root, text="", font=("Helvetica", 12), wraplength=350, bg='#ffffff', fg='gray')
tip_label.pack(pady=10)

# Buttons
button_frame = tk.Frame(root, bg='#ffffff')
button_frame.pack(pady=10)

analyze_btn = tk.Button(button_frame, text="Analyze Mood", command=check_mood, bg="#4CAF50", fg="white", font=("Helvetica", 12))
analyze_btn.grid(row=0, column=0, padx=10)

listen_btn = tk.Button(button_frame, text="🎙️ Speak Mood", command=listen_to_user, bg="#2196F3", fg="white", font=("Helvetica", 12))
listen_btn.grid(row=0, column=1, padx=10)



# Emoji buttons
emoji_frame = tk.Frame(root, bg='#ffffff')
emoji_frame.pack(pady=20)

tk.Label(emoji_frame, text="Or choose your mood:", font=("Helvetica", 12), bg='#ffffff').pack(pady=5)

emoji_row = tk.Frame(emoji_frame, bg='#ffffff')
emoji_row.pack()

def on_enter(e):
    e.widget.config(bg="#e0e0e0")

def on_leave(e):
    e.widget.config(bg="#ffffff")

btn_happy = tk.Button(emoji_row, text="😄", font=("Helvetica", 20), command=lambda: set_mood("Positive"), bg="#ffffff", bd=0)
btn_happy.pack(side=tk.LEFT, padx=10)
btn_happy.bind("<Enter>", on_enter)
btn_happy.bind("<Leave>", on_leave)

btn_neutral = tk.Button(emoji_row, text="😐", font=("Helvetica", 20), command=lambda: set_mood("Neutral"), bg="#ffffff", bd=0)
btn_neutral.pack(side=tk.LEFT, padx=10)
btn_neutral.bind("<Enter>", on_enter)
btn_neutral.bind("<Leave>", on_leave)

btn_sad = tk.Button(emoji_row, text="😞", font=("Helvetica", 20), command=lambda: set_mood("Negative"), bg="#ffffff", bd=0)
btn_sad.pack(side=tk.LEFT, padx=10)
btn_sad.bind("<Enter>", on_enter)
btn_sad.bind("<Leave>", on_leave)

def set_mood(mood):
    if mood == "Positive":
        tip = random.choice(positive_tips)
        root.config(bg='#d4fcdc')
    elif mood == "Negative":
        tip = random.choice(negative_tips)
        root.config(bg='#f8d7da')
    else:
        tip = random.choice(neutral_tips)
        root.config(bg='#dbefff')

    result_label.config(text=f"Mood: {mood}")
    tip_label.config(text=tip)
    speak(tip)

# Hover effect functions
def on_enter_analyze(e):
    analyze_btn['bg'] = '#45a049'
def on_leave_analyze(e):
    analyze_btn['bg'] = '#4CAF50'

def on_enter_listen(e):
    listen_btn['bg'] = '#1976D2'
def on_leave_listen(e):
    listen_btn['bg'] = '#2196F3'

# Bind hover events
analyze_btn.bind("<Enter>", on_enter_analyze)
analyze_btn.bind("<Leave>", on_leave_analyze)

listen_btn.bind("<Enter>", on_enter_listen)
listen_btn.bind("<Leave>", on_leave_listen)

# Start GUI
root.mainloop()

