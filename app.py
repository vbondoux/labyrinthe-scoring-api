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
@app.route('/privacy-policy', methods=['GET'])
def privacy_policy():
    return """
   <html>
    <head>
        <title>Politique de Confidentialité</title>
    </head>
    <body>
        <h1>Politique de Confidentialité</h1>
        <p><strong>Dernière mise à jour :</strong> [date]</p>

        <h2>1. Introduction</h2>
        <p>
            Cette application respecte votre vie privée et s'engage à protéger les données que vous partagez. 
            Nous ne collectons que les informations nécessaires pour fournir les fonctionnalités du labyrinthe.
        </p>

        <h2>2. Données collectées</h2>
        <p>Lorsque vous utilisez cette application, les données suivantes peuvent être collectées :</p>
        <ul>
            <li>Réponses fournies aux questions posées dans le labyrinthe.</li>
            <li>Scores générés par l'API en fonction de vos choix.</li>
        </ul>

        <h2>3. Utilisation des données</h2>
        <p>Les données collectées sont utilisées uniquement dans le cadre suivant :</p>
        <ul>
            <li>Calculer et interpréter les scores pour vous fournir une expérience personnalisée.</li>
            <li>Améliorer les fonctionnalités et les performances de l'application.</li>
        </ul>

        <h2>4. Partage des données</h2>
        <p>
            Vos données ne seront jamais partagées avec des tiers, sauf si cela est requis par la loi 
            ou pour protéger nos droits légaux.
        </p>

        <h2>5. Sécurité des données</h2>
        <p>
            Nous mettons en œuvre des mesures standard pour protéger vos données contre les accès non autorisés 
            ou les pertes accidentelles. Cependant, aucune méthode de transmission sur Internet ou de stockage 
            électronique n'est totalement sécurisée.
        </p>

        <h2>6. Conservation des données</h2>
        <p>
            Les données collectées sont conservées uniquement pendant la durée nécessaire pour fournir le service.
            Une fois le labyrinthe terminé, aucune donnée personnelle identifiable n'est stockée.
        </p>

        <h2>7. Vos droits</h2>
        <p>
            Vous avez le droit de demander des informations sur les données collectées, de demander leur suppression, 
            ou de signaler toute préoccupation concernant leur utilisation. Contactez-nous via l'email ci-dessous.
        </p>

        <h2>8. Contact</h2>
        <p>
            Si vous avez des questions concernant cette politique de confidentialité, vous pouvez nous contacter à :
            <a href="mailto:votre-email@example.com">votre-email@example.com</a>
        </p>

        <footer>
            <p>
                Cette politique peut être mise à jour périodiquement. Veuillez consulter cette page pour 
                rester informé(e) des modifications.
            </p>
        </footer>
    </body>
</html>
    """


@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Bienvenue dans l'API Labyrinthe. Utilisez POST /calculate-scores pour soumettre vos données."})


if __name__ == "__main__":
    # Récupérer le port dynamique pour Railway
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
