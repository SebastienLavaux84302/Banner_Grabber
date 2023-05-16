# ScannerGrabber
## Description
ScannerGrabber est un outil Python simple et efficace qui permet de scanner les ports ouverts d'un hôte spécifié et d'obtenir des informations sur ces ports. Il utilise les sockets Python pour se connecter à chaque port de l'hôte et affiche les résultats directement à l'écran.

## Fonctionnalités

    Scan des ports ouverts d'un hôte.
    Affiche le nom du service correspondant à chaque port ouvert.
    Tente d'envoyer un message à chaque port ouvert et d'afficher la réponse, si disponible.

## Utilisation

Pour utiliser ScannerGrabber, il suffit de lancer le script Python et de lui fournir l'adresse IP ou le nom d'hôte de la cible. Les ports à scanner sont définis dans le script et peuvent être personnalisés selon vos besoins.

```python
def main():
    ScannerGrabber("123.123.123.123")

if (__name__ == '__main__'):
    main()
```
Dans l'exemple ci-dessus, l'hôte cible est 123.123.123.123. Vous pouvez le remplacer par l'adresse IP ou le nom d'hôte de votre choix.

## Note
Ce script est à des fins éducatives et de recherche seulement. Ne l'utilisez pas pour des activités illégales. Il est de la responsabilité de l'utilisateur final de respecter toutes les lois locales, nationales et internationales applicables. Les développeurs n'assument aucune responsabilité et ne sont pas responsables de toute mauvaise utilisation ou dommage causé par ce programme.
