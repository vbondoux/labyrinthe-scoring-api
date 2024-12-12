from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Dict

app = FastAPI()

class Response(BaseModel):
    scores: Dict[str, int]

class RequestBody(BaseModel):
    reponses: List[Response]

@app.post("/calculate-scores")
def calculate_scores(body: RequestBody):
    # Calcul des scores
    dimensions = {"DOM": 0, "SUB": 0, "SWI": 0, "AUT": 0, "EXP": 0}
    for reponse in body.reponses:
        for dim, value in reponse.scores.items():
            dimensions[dim] += value

    # Interprétation
    interpretations = {
        "DOM": "Vous avez une forte capacité à diriger." if dimensions["DOM"] > 10 else "Votre dominance est modérée.",
        "SUB": "Vous êtes réceptif(ve) au lâcher-prise." if dimensions["SUB"] > 10 else "Votre soumission est modérée.",
        "SWI": "Vous montrez une certaine flexibilité." if dimensions["SWI"] > 10 else "Vous êtes plus orienté(e) vers un rôle fixe.",
        "AUT": "Vous préférez une gestion indépendante." if dimensions["AUT"] > 10 else "Vous préférez déléguer.",
        "EXP": "Vous êtes curieux(se) et ouvert(e) aux nouvelles expériences." if dimensions["EXP"] > 10 else "Vous êtes prudent(e) face à l'inconnu."
    }

    # Synthèse
    synthesis = "Votre profil montre une forte inclination dominante avec une curiosité notable."

    return {"scores": dimensions, "interpretations": interpretations, "synthesis": synthesis}
