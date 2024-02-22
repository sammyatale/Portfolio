from flask import Flask, render_template, request
from data_handler import save_data

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about/')
def about():
    return "About Myself"

@app.route('/submit_form', methods=['POST'])
def submit_form():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        
        save_data(name, email, message)  # Save the form data
        
        return "Form submitted successfully!"
    else:
        return "Method Not Allowed"

if __name__ == '__main__':
    app.run(debug=True)
