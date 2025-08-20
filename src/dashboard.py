# dashboard.py
from flask import Flask, render_template_string
import threading

app = Flask(__name__)

# Store alerts in memory
alerts = []

# Simple HTML template
template = """
<!DOCTYPE html>
<html>
<head>
    <title>Ransomware Detector Dashboard</title>
    <style>
        body { font-family: Arial, sans-serif; background: #f4f4f4; }
        h1 { color: #c0392b; }
        .alert {
            background: #fff;
            border: 1px solid #ddd;
            margin: 10px;
            padding: 15px;
            border-left: 5px solid #e74c3c;
        }
    </style>
</head>
<body>
    <h1>🚨 Ransomware Alerts</h1>
    {% if alerts %}
        {% for alert in alerts %}
            <div class="alert">
                <strong>{{ alert['time'] }}</strong>: {{ alert['message'] }}
            </div>
        {% endfor %}
    {% else %}
        <p>No alerts yet.</p>
    {% endif %}
</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(template, alerts=alerts)

def add_alert(message, timestamp):
    alerts.append({"message": message, "time": timestamp})

def run_dashboard():
    thread = threading.Thread(target=lambda: app.run(host="127.0.0.1", port=5000, debug=False, use_reloader=False))
    thread.daemon = True
    thread.start()
