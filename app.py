from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for session management

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')

    # Basic validation
    if not username:
        flash('Username required', 'error')
        return redirect(url_for('home'))
    if '@' not in email:
        flash('Invalid email', 'error')
        return redirect(url_for('home'))
    if len(password) < 6:
        flash('Password too short', 'error')
        return redirect(url_for('home'))

    # Here you would typically save the user data to a database
    flash('Registration Successful!', 'success')
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
