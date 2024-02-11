from flask import Flask, render_template, request

app = Flask(__name__)

# Определение маршрута для главной страницы
@app.route('/')
def index():
    return render_template('index.html')

# Обработка данных из формы
@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        # Здесь можно обработать данные из формы, например, сохранить их в базу данных
        return render_template('submit.html', name=name, email=email)

if __name__ == '__main__':
    app.run(debug=True)