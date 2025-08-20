# 🛡️ Ransomware Detector

A real-time ransomware detection and prevention system that monitors filesystem activity, detects suspicious behavior (like mass file modifications/encryptions), and automatically alerts the user.  
The project also includes a **web dashboard** for monitoring alerts in real-time.

---

## 📌 Features
- 🔍 **Real-time monitoring** of file modifications.
- 🚨 **Suspicious activity detection** (e.g., rapid file writes/renames).
- 🧩 **Process analysis** — identifies which process is touching sensitive files.
- ❌ **Process termination** — kills suspicious ransomware-like processes.
- 🌐 **Web Dashboard (Flask + Dash)** for visual monitoring of alerts.
- 📊 **Alert logging** to both **terminal and dashboard**.
- 🖥️ Lightweight & runs in the background.

---

## 🛠️ Tech Stack
- **Python 3.9+**
- [watchdog](https://pypi.org/project/watchdog/) – File system monitoring  
- [psutil](https://pypi.org/project/psutil/) – Process monitoring & management  
- [Flask](https://flask.palletsprojects.com/) – Web server  
- [Dash](https://dash.plotly.com/) – Real-time dashboard for alerts  

---

## ⚙️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/dilli1605/ransomware-detector.git
   cd ransomware-detector
Create a virtual environment (recommended):

python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows


Install dependencies:

pip install -r requirements.txt

🚀 Usage

Run the detector:

python src/main.py


Open the dashboard in your browser:

http://127.0.0.1:8050


The terminal and dashboard will both show real-time ransomware alerts.

📸 Demo Screenshots
<img width="1896" height="1022" alt="Screenshot 2025-08-20 114012" src="https://github.com/user-attachments/assets/0063015c-bfc7-42a9-b004-46fb66d4f2c0" />


📂 Project Structure  
ransomware-detector/
│── src/
│   ├── main.py            # Entry point (runs detector + dashboard)
│   ├── monitor.py         # File monitoring logic
│   ├── process_manager.py # Process management utilities
│   ├── dashboard.py       # Flask + Dash dashboard
│── requirements.txt       # Python dependencies
│── README.md              # Project documentation

⚠️ Disclaimer

This project is for educational and research purposes only.
Do NOT rely on this tool as your only protection against ransomware. Always use a professional antivirus/antimalware solution.

👨‍💻 Author

Dilli Raj
GitHub: dilli1605
