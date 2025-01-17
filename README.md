# Network-Speed-Test

This is a network speed tester project , made from Python,flask,html/css/js which is used to test the speed of the internet and provide you with the details of your internet speed.
It is a simple yet helps you to understand how the internet speed is measured and on what basis.

# File Structure
static
   style.css
   script.js
templates
   index.html
app.py

# How did I make this project

1.Firstly it is important to understand the python logic implemented in this project. 
I create 2 main functions get_ip_details(to get the ip address and location of the user in order to locate the user and the device) and perform_speed_test(yo test the speed of network).

2. By importing the urlib and request methods we can be able to send and get requests from the user.
    Here is the function to get the IP details of user
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

   3.Now in the speed function the main logic to calculate the speed is by importing the speedtest module from python library which helps us to test the speed. Then it is also importanto to locate the best server near the user  . Now to calculate the speed we need to have 2 variables : download and upload which will check what is the time taken to download the file and what is the time taken to uplaod the file divided by 1,000,000 bytes to convert the numbers into mbps .
4.  Now after the main python logic is completed we have to focus on integrating flask to create a proper backend API . Add the flask functions to the file:

from flask import Flask, jsonify, render_template

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/speedtest', methods=['GET'])
def api_speedtest():
    try:
        ip_details = get_ip()
        speed_results = perform_speed_test()
        return jsonify({
            "ip_details": ip_details,
            "speed_results": speed_results
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

->The first line imports necessary components: Flask for creating the web app, jsonify for sending JSON responses, and render_template for rendering HTML templates.

->@app.route('/') defines the main route (URL path) for the home page. When someone visits the root URL (/), it will return an HTML file called index.html.

->@app.route('/api/speedtest', methods=['GET']) defines an API route at /api/speedtest. This route listens for GET requests, and when it receives one, it runs the api_speedtest() function.

->Inside api_speedtest(), the code first tries to get the user's IP details using get_ip() and performs a speed test using perform_speed_test(). After getting both results, it returns them in a JSON format using jsonify(), which sends structured data to the client.

->If there's an error (like if the get_ip() or perform_speed_test() functions fail), the code catches the exception and returns an error message in JSON format with a 500 status code to indicate a server error.

->Finally, if __name__ == '__main__': ensures that the Flask app runs in debug mode when the script is executed directly. This means you can see detailed error messages in case something goes wrong.




