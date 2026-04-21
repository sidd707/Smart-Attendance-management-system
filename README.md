# Smart Attendance Management System

My **first-ever coding project** — built during my 1st year at Bennett University. This QR code-based attendance system won the **intra-college hackathon** organized during our college fest, and became the inspiration that got me hooked on building things with code.

![Site QR](site.png)

## The Story

As a first-year student, I noticed how inefficient the manual attendance process was — teachers calling out names, students marking proxies, and the whole thing eating into lecture time. I wanted to fix that with something simple: **scan a QR code on your phone, and you're marked present.**

This project was my answer. Built it from scratch learning Python, Flask, and Tkinter along the way. It wasn't perfect, but it worked — and it won us the hackathon. That win is what made me realize I wanted to keep building software.

## How It Works

```
Teacher launches Tkinter GUI
        │
        ▼
  Login / Sign Up (MySQL)
        │
        ▼
  Flask server starts on local network
        │
        ▼
  QR Code auto-generated with server URL
        │
        ▼
  Students scan QR on their phones
  (any device on same WiFi network)
        │
        ▼
  Attendance form opens in browser
  (enter name + email)
        │
        ▼
  Record saved to SQLite database
        │
        ▼
  Teacher views attendance list on dashboard
```

## Features

- **QR Code Scanning** — auto-generates a QR code pointing to the Flask server's local IP address, students scan with any phone camera
- **Teacher Desktop App** — Tkinter-based login/signup GUI with MySQL authentication
- **Password Recovery** — security question-based password reset flow
- **Web-based Attendance** — Flask server serves an attendance form accessible to any device on the local network
- **Attendance Records** — view all submitted attendance entries in a table
- **WiFi QR Code** — also generates a QR code for connecting to the WiFi network
- **Local Network** — runs entirely on the local network, no internet required

## Tech Stack

| Technology | Purpose |
|-----------|---------|
| Python | Core language |
| Flask | Web server for attendance form |
| Tkinter | Desktop GUI for teachers |
| SQLite | Attendance record storage |
| MySQL (PyMySQL) | Teacher authentication database |
| qrcode | QR code generation |
| wifi-qrcode-generator | WiFi connection QR code |
| Pillow (PIL) | Image handling |

## Project Structure

```
Smart-Attendance-management-system/
├── hello.py              # Flask server — attendance form, view records
├── login_page.py         # Tkinter login GUI with MySQL auth
├── signup_page.py        # Tkinter signup GUI with security questions
├── credentials.py        # MySQL connection config
├── employee.db.py        # SQLite database initialization
├── qr.py                 # QR code generator (WiFi + site URL)
├── site.png              # Generated QR code image
├── templates/
│   ├── index.html        # Home page — login + view attendance
│   ├── add.html          # Attendance submission form
│   ├── success.html      # Confirmation page
│   ├── view.html         # Attendance records table
│   ├── delete.html       # Delete record form
│   ├── delete_record.html
│   ├── style.css
│   └── images/
│       └── logo.png      # Bennett University logo
└── Python College Project 1sem/
    └── Presentation files
```

## Getting Started

### Prerequisites
- Python 3.x
- MySQL server (for teacher authentication)

### Install Dependencies
```bash
pip install flask pymysql qrcode pillow wifi-qrcode-generator
```

### Setup MySQL Database
Create a database and table for teacher registration:
```sql
CREATE DATABASE student;
USE student;
CREATE TABLE teacher_register (
    id INT AUTO_INCREMENT PRIMARY KEY,
    f_name VARCHAR(50),
    l_name VARCHAR(50),
    email VARCHAR(100) UNIQUE,
    question VARCHAR(200),
    answer VARCHAR(200),
    password VARCHAR(100)
);
```

Update `credentials.py` with your MySQL credentials.

### Run the Application

1. **Start the teacher GUI:**
```bash
python login_page.py
```

2. **After login, the Flask server starts automatically and a QR code is displayed**

3. **Students scan the QR code** on their phones to open the attendance form

4. **Teacher views attendance** through the web dashboard

## What I Learned

This was my introduction to:
- Building GUIs with Tkinter
- Web servers with Flask
- Working with databases (both SQLite and MySQL)
- Networking basics (local IP, ports, QR codes)
- Integrating multiple systems into one project

Looking back, the code is rough around the edges — but it was the starting point for everything that followed.
