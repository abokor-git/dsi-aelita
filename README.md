# <p align="center">Direction System d'Information (DSI) - Agent Conversationnel alimenter par Bing (Aelita) </p>

Cette application est une API qui permet de conversé avec l'ia Bing de Microsoft basé sur GPT-4. Elle est basée sur la bibliothèque EdgeGPT, FastAPI et l'interface utilisateur Gradio pour une utilisation facile et intuitive.

# Utilisation

L'API accepte un texte en entrée. Pour utiliser l'API, envoyez une requête avec le texte et l'API renverra le texte générer par bing sous forme d'une réponse JSON.

Pour exécuter l'application, vous pouvez utiliser Docker ou exécuter le script Python api.py directement sur votre machine. Si vous utilisez Docker, vous pouvez créer l'image Docker en exécutant la commande suivante à partir du répertoire racine du projet :

```
docker build -t nom-de-l-image .
```

Vous pouvez ensuite exécuter l'image Docker en utilisant la commande suivante :

```
docker run -p 8000:8000 nom-de-l-image
```

Ou directement utiliser l'image disponible sur le hub docker :

```
docker run -p 8000:8000 abokor16/dsi-aelita:1.0
```

L'application sera alors accessible à l'adresse http://localhost:8000/gradio dans votre navigateur.

# Documentation

L'API d'Aelita est accessible via l'URL http://localhost:8000/gradio. Elle accepte les requêtes HTTP POST avec les images au format PNG, JPEG ou BMP.

## Exemple de requête

```
POST /run/predict
http://localhost:8000/gradio/run/predict
```

## Payload d'entrée

Le payload d'entrée doit être un objet JSON avec une clé "data" contenant un tableau d'éléments représentant le texte d'entrée :

```
{
  "data": [
    "Salut !", 
  ]
}
```

## Exemple de payload d'entrée

```
{
  "data": [
    "Salut !",
  ]
}
```

## Exemple de réponse

La réponse renvoie un objet JSON contenant un tableau d'élément, qui représentent le résultat de la reconnaissance de caractères pour l'image en question :

```
{
  "data": [" Salut c'est bing :) "],
  "duration": 2.5
}
```

La clé "duration" représente le temps de traitement en secondes.

# Utilisation de l'API

Vous pouvez tester l'API en envoyant une requête POST avec un texte. Vous pouvez utiliser des outils comme cURL ou Postman pour tester l'API.

```
curl -X POST \
  http://localhost:8000/gradio/run/predict \
  -H 'Content-Type: application/json' \
  -d '{
    "data": [
        "Salut !", 
    ]
}'
```

# Contact

N'hésitez pas à nous contacter si vous avez des questions ou des commentaires.

Mail : abokor.ahmed.kadar.nour@outlook.com
