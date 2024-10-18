from flask import Flask, request, jsonify

app = Flask(__name__)

# Ruta para el Webhook de 17Track
@app.route('/webhook', methods=['POST'])
def webhook():
    # Obtén los datos enviados por 17Track
    data = request.get_json()
    print(f"Datos recibidos del Webhook: {data}")

    # Aquí puedes procesar los datos y guardarlos en tu base de datos
    # Por ejemplo, podrías conectar con tu base de datos Railway y actualizar el estado del envío

    return jsonify({'status': 'ok'}), 200

if __name__ == '__main__':
    app.run(debug=True)