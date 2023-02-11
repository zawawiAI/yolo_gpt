import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import openai
from ultralytics.yolo.engine.model import YOLO

def open_image(event):
    file_path = filedialog.askopenfilename()
    im1 = Image.open(file_path)
    model = YOLO("yolov8n.pt")
    results = model.predict(source=im1, save=True)  # save plotted images

    detected_obj_names = []
    for r in results:
        for c in r.boxes.cls:
            detected_obj_names.append(model.names[int(c)])

    detected_obj_names_string = ', '.join(detected_obj_names)
    print(detected_obj_names_string)
    
    # Set up the OpenAI API client
    openai.api_key = "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"

    # Set up the model and prompt
    model_engine = "text-davinci-003"

    prompt = f"Suggest 5 simple recipes based on {detected_obj_names_string} and include the estimated calorie per meal"

    # Generate a response
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        temperature=0.7,
        top_p=1,
        frequency_penalty=0.52,
        presence_penalty=0.5,
        stop=["11."]
    )

    response = completion.choices[0].text
    result_text.config(state="normal")
    result_text.delete("1.0", tk.END)
    result_text.insert(tk.END, response)
    result_text.config(state="disabled")
    
    # Show input image
    im1 = im1.resize((400, 300), Image.ANTIALIAS) #auto-resize function
    image = ImageTk.PhotoImage(im1)
    global image_label
    image_label = tk.Label(image=image)
    image_label.image = image
    image_label.pack(in_=drag_drop_frame)


def clear_input_and_results():
    result_text.config(state="normal")
    result_text.delete("1.0", tk.END)
    result_text.config(state="disabled")
    try:
        image_label.pack_forget()
    except NameError:
        pass


root = tk.Tk()
root.geometry("800x600")
root.title("OpenAI YOLOv8- A Playground to test integration between GPT3 and Object Recognition")


# Drag and drop window
drag_drop_frame = tk.Frame(root)
drag_drop_frame.pack(side="left", fill="both", expand=True)

label = tk.Button(drag_drop_frame, text="Input Image") #Label to Button
label.pack(pady=10)

label.bind("<Button-1>", open_image)

# Show input image
try:
    im1 = im1.resize((400, 300), Image.ANTIALIAS) #auto-resize function
    image = ImageTk.PhotoImage(im1)
    global image_label
    image_label = tk.Label(drag_drop_frame, image=image)
    image_label.image = image
    image_label.pack()
except NameError:
    pass


# Clear input and results window
def clear_input_and_results():
    result_text.config(state="normal")
    result_text.delete("1.0", tk.END)
    result_text.config(state="disabled")
    try:
        image_label.pack_forget()
    except NameError:
        pass

# Results window
results_frame = tk.Frame(root)
results_frame.pack(side="right", fill="both", expand=True)

result_label = tk.Label(results_frame, text="Recipes:")
result_label.pack(pady=10)

result_text = tk.Text(results_frame, height=40, width=80, state="disabled")
result_text.pack(pady=30)#changed 10 to 20

clear_button = tk.Button(results_frame, text="Clear Input and Results", command=lambda: clear_input_and_results())
clear_button.pack(pady=10)

root.mainloop()
