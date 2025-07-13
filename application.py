from flask import Flask, request
from HelloWorldProgram.HelloWorldProgram import main as console_main

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def hello():
    # jeśli GET, wyświetl prosty formularz
    if request.method == "GET":
        return """
          <form method="post">
            Imię: <input name="name"><br>
            Miasto: <input name="city"><br>
            <button type="submit">Wyślij</button>
          </form>
        """
    # jeśli POST, pobierz dane
    name = request.form.get("name", "")
    city = request.form.get("city", "")
    # zamiast stdout konsoli – zadzwoń do logiki programu
    greeting = f"Witaj, {name} z {city}!"
    return f"<h1>{greeting}</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
