from flask import Flask, jsonify, render_template
import speedtest
import json
from urllib.request import urlopen

app = Flask(__name__)

def get_ip_details():

    url = 'http://ipinfo.io/json'
    response = urlopen(url)
    data = json.load(response)

    return {
        "ip": data.get('ip', 'N/A'),
        "org": data.get('org', 'N/A'),
        "city": data.get('city', 'N/A'),
        "country": data.get('country', 'N/A'),
        "region": data.get('region', 'N/A')
    }

def perform_speed_test():

    st = speedtest.Speedtest()
    st.get_best_server()
    download_speed = st.download() / 1_000_000 
    upload_speed = st.upload() / 1_000_000  
    ping = st.results.ping

    return {
        "ping": round(ping, 2),
        "download_speed": round(download_speed, 2),
        "upload_speed": round(upload_speed, 2)
    }

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/speedtest', methods=['GET'])
def api_speedtest():
    try:
        ip_details = get_ip_details()
        speed_results = perform_speed_test()
        return jsonify({
            "ip_details": ip_details,
            "speed_results": speed_results
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
