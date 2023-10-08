from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)

# Initialize an empty list to store contact form submissions
contact_data = []

# Define the path to the JSON file
json_file_path = 'contact_data.json'

# Define your routes and other app logic below

@app.route('/')
def home():
    return render_template('product.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Get the form data
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        mobile_no = request.form['mobile_no']
        message = request.form['message']

        # Create a dictionary to store the form data
        contact_entry = {
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'mobile_no': mobile_no,
            'message': message
        }

        # Append the entry to the contact_data list
        contact_data.append(contact_entry)

        # Save the contact data to the JSON file
        with open(json_file_path, 'w') as json_file:
            json.dump(contact_data, json_file)


    return render_template('contact.html')


@app.route('/faq')
def faq():
    return render_template('faq.html')


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
