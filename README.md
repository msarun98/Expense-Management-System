# Expense Management System (EMS)

This project helps users with tracking daily expenses by enabling storage and retrieval of date-wise expense data with an SQL server through FastAPI with the help of a streamlit based frontend.

## Project Structure
- **frontend/** : contains streamlit application code.
- **backend/** : contains FastAPI backend server code.
- **tests/** : contains test cases for both frontend and backend.
- **requirements.txt/** : Lists the required python packages.
- **README.md/** : Provides an overview and instructions for the project.

## Functionality
- Get user inputs and Add/update expenses to database
- Remove expenses from database
- retrieve expenses from database for a selected date
- analyze the spread of expenses across categories between selected dates
- presenting the expenses in a visual format.

## Setup Instructions
1. **Clone the repository:**
    ```bash
    git clone https://github.com/msarun98/expense_management_system
    cd expense_management_system
    ```
1. **Install dependencies:**
    ```commandline
    pip install -r requirements.txt
    ```
1. **Run the FastAPI server:**
    ```commandline
    uvicorn server.server:app --reload
    ```
1. **Run the Streamlit app:**
    ```commandline
    streamlit run frontend/app.py
    ```
