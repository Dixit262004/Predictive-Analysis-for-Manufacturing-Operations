Predictive Analysis for Manufacturing Operations
This project is a desktop application built using Tkinter and scikit-learn to predict machine downtime
or production defects based on manufacturing data. The app allows users to upload datasets, 
train a machine learning model, and make predictions interactively.
________________________________________
Features
•	Upload Dataset: Load a CSV file containing manufacturing data.
•	Train Model: Train a Logistic Regression model on the uploaded data.
•	Make Predictions: Predict machine downtime based on input features (Coolant Temperature and Torque).
•	Interactive GUI: Easy-to-use interface built with Tkinter.
________________________________________
Installation
1.	Clone the repository:
bash
CopyEdit
git clone https://github.com/Dixit262004/Predictive-Analysis-for-Manufacturing-Operations.git
cd predictive-analysis
2.	Install dependencies:
bash
CopyEdit
pip install -r requirements.txt
3.	Run the application:
bash
CopyEdit
python app.py
________________________________________
Usage
1.	Upload Dataset:
o	Click the "Upload Dataset" button.
o	Select a CSV file with the following columns:
	Coolant_Temperature
	Torque
	Downtime (target column: 1 for downtime, 0 for no downtime).
2.	Train Model:
o	After uploading, click the "Train Model" button.
o	The app will display the training metrics (e.g., accuracy and F1-score).
3.	Make Predictions:
o	Enter Coolant Temperature and Torque values in the input fields.
o	Click "Predict" to see the downtime prediction and confidence score.
________________________________________
File Structure
.
├── app.py                 # Main Tkinter application
├── model.py               # Contains ModelHandler for ML operations
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
└── example_dataset.csv    # Example manufacturing dataset
________________________________________

Example Dataset
The dataset should include the following columns:
Coolant_Temperature	  Torque	  Downtime
75	    120	      1
65	      80	      0
Place your dataset in .csv format and load it via the "Upload Dataset" button.
________________________________________
Dependencies
The project uses the following Python libraries:
•	pandas
•	numpy
•	scikit-learn
•	tkinter
Install all dependencies with:
bash
CopyEdit
pip install -r requirements.txt

![image](https://github.com/user-attachments/assets/4c7e9e67-b91b-4096-839a-0b4d4d287c6b)


![image](https://github.com/user-attachments/assets/b7c4e8f1-231b-465f-8606-77ab11ed4c78)


![image](https://github.com/user-attachments/assets/0c5c03ff-32d9-410c-a054-e366e5ca26bf)


![image](https://github.com/user-attachments/assets/f77f903f-12ed-4e31-bb37-3457422d7b03)


![image](https://github.com/user-attachments/assets/60385a0a-6227-4fb1-8400-098eb47bc47a)


![image](https://github.com/user-attachments/assets/5e64cb02-165b-43aa-8eb1-aa61560dd880)


![image](https://github.com/user-attachments/assets/25ebbd85-3e4a-431a-810e-6a099e2bc0b3)


![image](https://github.com/user-attachments/assets/da5b33cf-71d9-4ade-9d89-81ad202154a8)


Contact
For questions or suggestions, feel free to contact:
•	Name: Dixit
•	Email: mail4udixit46@gmail.com

