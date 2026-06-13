import psutil
from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Route 1: Serves the main HTML dashboard page
@app.route('/')
def index():
    return render_template('index.html')

# Route 2: The REST API that fetches live system data in background
@app.route('/api/metrics')
def get_metrics():
    cpu_metric = psutil.cpu_percent(interval=None)
    mem_metric = psutil.virtual_memory().percent
    
    return jsonify(
        cpu=cpu_metric,
        memory=mem_metric
    )

if __name__ == '__main__':
    # Runs the application locally on http://127.0.0.1:5000
    app.run(debug=True, host='0.0.0.0', port=5000)