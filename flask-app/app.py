from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <html>
        <head><title>Flask Image Example</title></head>
        <body style="text-align:center;">
            <h1>Hello from Flask inside Docker!</h1>
            <img src="https://images.unsplash.com/photo-1637124041953-d3fbd25d3ea6" 
                 alt="Concept car in the dark" 
                 style="max-width:80%; height:auto; border-radius:10px;">
        </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
