import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/calculate-scores', methods=['POST'])
def calculate_scores():
    try:
        # Récupérer les données de la requête
        data = request.get_json()
        reponses = data.get('reponses', [])

        # Initialiser les scores par dimension
        dimensions = {"DOM": 0, "SUB": 0, "SWI": 0, "AUT": 0, "EXP": 0}

        # Calculer les scores
        for reponse in reponses:
            scores = reponse.get('scores', {})
            for dim, value in scores.items():
                if dim in dimensions:
                    dimensions[dim] += value

        # Interpréter les scores
        interpretations = {
            "DOM": "Vous avez une forte capacité à diriger." if dimensions["DOM"] > 10 else "Votre dominance est modérée.",
            "SUB": "Vous êtes réceptif(ve) au lâcher-prise." if dimensions["SUB"] > 10 else "Votre soumission est modérée.",
            "SWI": "Vous montrez une certaine flexibilité." if dimensions["SWI"] > 10 else "Vous êtes plus orienté(e) vers un rôle fixe.",
            "AUT": "Vous préférez une gestion indépendante." if dimensions["AUT"] > 10 else "Vous préférez déléguer.",
            "EXP": "Vous êtes curieux(se) et ouvert(e) aux nouvelles expériences." if dimensions["EXP"] > 10 else "Vous êtes prudent(e) face à l'inconnu."
        }

        # Synthèse générale
        synthesis = "Votre profil montre une forte inclination dominante avec une curiosité notable."

        # Retourner la réponse
        return jsonify({
            "scores": dimensions,
            "interpretations": interpretations,
            "synthesis": synthesis
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 400


@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Bienvenue dans l'API Labyrinthe. Utilisez POST /calculate-scores pour soumettre vos données."})


if __name__ == "__main__":
    # Récupérer le port dynamique pour Railway
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
