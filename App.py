from flask import Flask, request, Response

app = Flask(__name__)
stored_text = ""  # Переменная для хранения текста

@app.route('/save', methods=['POST'])
def save_text():
    global stored_text
    stored_text = request.data.decode('utf-8')  # Обрабатываем текст в UTF-8
    return "OK"

@app.route('/load', methods=['GET'])
def load_text():
    global stored_text
    response = Response(stored_text, content_type="text/plain; charset=utf-8")
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    return response  # Отключаем кэширование

@app.route('/clear', methods=['POST'])
def clear_text():
    global stored_text
    stored_text = ""  # Очищаем текст
    return "OK"

@app.route('/')
def index():
    response = Response(open("index.html", encoding="utf-8").read(), content_type="text/html; charset=utf-8")
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)
