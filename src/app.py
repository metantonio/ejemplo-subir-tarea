from flask import Flask
app = Flask(__name__) #instancia del servidor Flask


@app.route('/todos', methods=['GET']) #decorador
def hello_world():
    return "<h1>Hello, World!</h1>"
#se mostraria en gitpod en: https://3245-c181d190-54dc-4dba-a45a-442802d9cead.ws-us03.gitpod.io/todos



# These two lines should always be at the end of your app.py file.
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)
