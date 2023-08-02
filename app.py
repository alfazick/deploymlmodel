from flask import Flask, render_template, request, url_for

app = Flask(__name__, static_url_path='/images', static_folder='images')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/show_image', methods=['POST'])
def show_image():
    image_number = request.form['image_number']

    if image_number == '1':
        image_url = url_for('static', filename='image1.jpg')
        return render_template('show_image.html', image_url=image_url)

    return "Invalid number!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

