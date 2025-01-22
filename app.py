import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
from model import ModelHandler

# Initialize the ModelHandler
model_handler = ModelHandler()

# Create the main Tkinter application window
app = tk.Tk()
app.title("Predictive Analysis for Manufacturing Operations")
app.geometry("500x400")


# Function to upload data
def upload_data():
    file_path = filedialog.askopenfilename(
        title="Select a CSV File",
        filetypes=(("CSV files", "*.csv"), ("All files", "*.*"))
    )
    if not file_path:
        messagebox.showerror("Error", "No file selected!")
        return

    try:
        data = pd.read_csv(file_path)
        model_handler.load_data(data)
        messagebox.showinfo("Success", "Data uploaded successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to load data: {e}")


# Function to train the model
def train_model():
    if not model_handler.data_loaded:
        messagebox.showerror("Error", "No data uploaded!")
        return

    try:
        metrics = model_handler.train_model()
        metrics_str = "\n".join([f"{key}: {value:.2f}" for key, value in metrics.items()])
        messagebox.showinfo("Training Complete", f"Model trained successfully!\n\n{metrics_str}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to train the model: {e}")


# Function to make predictions
def predict():
    try:
        # Retrieve user inputs
        coolant_temperature = float(temp_entry.get())
        torque = float(torque_entry.get())
        input_data = {"Coolant_Temperature": coolant_temperature, "Torque": torque}

        prediction = model_handler.predict(input_data)

        if prediction:
            downtime = prediction.get("Downtime", "Unknown")
            confidence = prediction.get("Confidence", "Unknown")
            result = f"Downtime: {downtime}\nConfidence: {confidence:.2f}"
            messagebox.showinfo("Prediction", result)
        else:
            messagebox.showerror("Error", "Model not trained!")
    except ValueError:
        messagebox.showerror("Error", "Invalid input! Please enter numerical values.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to make a prediction: {e}")


# Create GUI elements
tk.Label(app, text="Predictive Analysis", font=("Arial", 16)).pack(pady=10)

# Upload Data Section
tk.Button(app, text="Upload Dataset", command=upload_data, width=20).pack(pady=10)

# Train Model Section
tk.Button(app, text="Train Model", command=train_model, width=20).pack(pady=10)

# Prediction Section
tk.Label(app, text="Enter Coolant Temperature:").pack()
temp_entry = tk.Entry(app)
temp_entry.pack(pady=5)

tk.Label(app, text="Enter Torque:").pack()
torque_entry = tk.Entry(app)
torque_entry.pack(pady=5)

tk.Button(app, text="Predict", command=predict, width=20).pack(pady=10)

# Run the Tkinter event loop
app.mainloop()
