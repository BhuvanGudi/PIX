import tkinter as tk
import customtkinter as ctk

from PIL import ImageTk
from authtoken import auth_token

import torch
from torch import autocast
from diffusers import StableDiffusionKDiffusionPipeline

# Create the app
app = tk.Tk()
app.geometry("532x622")
app.title("Stable Bud")
ctk.set_appearance_mode("dark")

prompt = ctk.CTkEntry(app, height=40, width=512, font=("Arial", 20), text_color="black", fg_color="white")
prompt.place(x=10, y=10)

lmain = ctk.CTkLabel(app, height=512, width=512)
lmain.place(x=10, y=110)

modelid = "CompVis/stable-diffusion-v1-4"
device = "cuda"
pipe = StableDiffusionKDiffusionPipeline.from_pretrained(modelid, revision="fp16", torch_dtype=torch.float16, use_auth_token= auth_token)
pipe.to(device)

def generate():
    with autocast(device):
        image = pipe(prompt.get(), guidance_scale=8.5)["sample"][0]

    image.save('generatedimage.png')
    img = ImageTk.PhotoImage(image)
    lmain.configure(image=img)

trigger = ctk.CTkButton(app, height=40, width=120, font=("Arial", 20), text_color="white", fg_color="blue")
trigger.place(x=206, y=60)
trigger.configure(text="Generate")

app.mainloop()