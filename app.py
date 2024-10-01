from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def password_check():
    result = None
    if request.method == 'POST':
        password = request.form['password']
        response = requests.post('http://localhost:7071/api/password_strength', json={"password": password})
        if response.status_code == 200:
            result = response.json()
        else:
            result = {'error': 'Error communicating with the password strength service'}
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
