from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/products')
def products():
    return render_template('products.html')


@app.route('/services')
def services():
    return render_template('services.html')


@app.route('/news')
def news():
    return render_template('news.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Handle form submission
        pass
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True)
