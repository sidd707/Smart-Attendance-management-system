# Smart Attendance Management System

### Overview
The **Smart Attendance Management System** is a project designed to automate the process of recording attendance using **QR codes**. The system integrates **Flask** as the backend framework and **Tkinter** for the GUI. It captures attendance by scanning QR codes and storing the data securely on a local host server. This solution is ideal for **educational** and **professional institutions** looking to streamline their attendance processes.

---

## ✨ Features
- **Automated Attendance**: Uses QR code-based scanning to mark attendance, eliminating manual effort.
- **GUI Integration**: A user-friendly interface built with **Tkinter** for real-time attendance management.
- **Local Host Operation**: Runs on a local server, ensuring data security and real-time processing.
- **QR Code Scanning**: Leverages QR codes to uniquely identify and record attendance.
- **Data Storage**: Attendance data is captured and stored efficiently using the **local hotspot server**.

---

## 🛠️ Tech Stack
- **Backend**: Flask (Python)
- **Frontend/GUI**: Tkinter (Python)
- **Database**: SQLite / MySQL (optional for future scalability)
- **QR Code Integration**: Python libraries (qrcode, OpenCV)

---

## 🚀 Installation & Setup

### Prerequisites
- Python 3.x
- Flask
- Tkinter
- OpenCV (for QR code scanning)
- SQLite / MySQL (optional for extended data handling)

### Step-by-Step Setup
1. Clone this repository:

   bash
   git clone https://github.com/sidd707/Smart-Attendance-management-system.git

   

2. Install the dependencies:

  pip install -r requirements.txt

     
3.Run the Flask backend:

  python app.py

4. Launch the Tkinter GUI:

   python gui.py

