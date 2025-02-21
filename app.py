import tkinter as tk
import customtkinter as ctk
from PIL import ImageTk
from authtoken import auth_token

from torch import autocast
from diffusers import StableDiffusionKDiffusionPipeline

# Create the app
app = tk.Tk()
app.geometry("532x632")
app.title("Stable Bud")
ctk.set_appearance_mode("dark")

prompt = ctk.CTkEntry(app, height=40, width=512, font=("Arial", 20), text_color="black", fg_color="white")
prompt.place(x=10, y=10)

lmain = ctk.CTkLabel(app, height=512, width=512)
lmain.place(x=10, y=110)

modelid = "CompVis/stable-diffusion-v1-4"
device = "cpu"  # Change to CPU instead of GPU
pipe = StableDiffusionKDiffusionPipeline.from_pretrained(modelid, use_auth_token=auth_token)
pipe.to(device)

def generate():
    with autocast(device):  # CPU doesn't require autocast, but it's harmless here
        image = pipe(prompt.get(), guidance_scale=8.5)["sample"][0]

    image.save('generatedimage.png')
    img = ImageTk.PhotoImage(image)
    lmain.configure(image=img)

trigger = ctk.CTkButton(app, height=40, width=120, font=("Arial", 20), text_color="white", fg_color="blue")
trigger.place(x=206, y=60)
trigger.configure(text="Generate")

app.mainloop()
