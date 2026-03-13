# Brain Tumor MRI Classification Competition

## Description
Cette compétition porte sur la classification de tumeurs cérébrales à partir d'images IRM. Les quatre classes sont : Glioma, Meningioma, No Tumor, et Pituitary.

## Structure du Répertoire
- `train.csv` : Données d'entraînement.
- `test.csv` : Données de test (sans les labels pour les participants).
- `solution.csv` : Vérité terrain (privée).
- `sample_submission.csv` : Exemple de format de soumission.
- `leaderboard.csv` : Classement actuel des participants.

## Comment Soumettre
1. Préparez un fichier CSV avec deux colonnes : `ImageId` et `Expected`.
2. Assurez-vous que les IDs correspondent à ceux du fichier `test.csv`.
3. Soumettez votre fichier en le nommant `submission.csv`.

## Évaluation
La métrique d'évaluation est l'**Accuracy** (Précision globale).
