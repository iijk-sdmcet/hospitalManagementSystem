# Hospital Management System

## Project Overview

The **Hospital Management System (HMS)** is a simple web application developed using **Python** and the **Flask** framework. It is designed to help manage hospital-related tasks, such as:

- **Patient registration**
- **Doctor listing**
- **Appointment booking**

This system uses **SQLite** as the database for storing information about patients, doctors, and appointments. The frontend is built using **HTML** with **Jinja2 templates**.

## Features

- **Patient Management**: Register patients and view their details.
- **Doctor Management**: View a list of doctors and their specializations.
- **Appointment Booking**: Patients can book appointments with doctors.
- **Database**: Uses SQLite to store patient, doctor, and appointment data.

## Tech Stack

- **Backend**: Python, Flask
- **Frontend**: HTML, Jinja2 (Flask templating engine)
- **Database**: SQLite
- **CSS**: Custom styles

## Setup Instructions

Follow these steps to run the project locally:

### 1. Install Dependencies

First, ensure that you have Python installed on your system. Then, create a virtual environment and install the required packages.

```bash
# Install Flask and SQLAlchemy
pip install flask flask_sqlalchemy
