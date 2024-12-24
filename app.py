from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Classe Personnage
class Personnage:
    def __init__(self, nom, x=0, y=0):
        self.nom = nom
        self.x = x
        self.y = y

    def deplacer(self, direction):
        if direction == "haut":
            self.y += 1
        elif direction == "bas":
            self.y -= 1
        elif direction == "gauche":
            self.x -= 1
        elif direction == "droite":
            self.x += 1

    def get_position(self):
        return {"x": self.x, "y": self.y}

# Initialisation du personnage
personnage = Personnage("Héros")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/deplacer", methods=["POST"])
def deplacer():
    data = request.json
    direction = data.get("direction", "")
    personnage.deplacer(direction)
    return jsonify(personnage.get_position())

if __name__ == "__main__":
    app.run(debug=True)
