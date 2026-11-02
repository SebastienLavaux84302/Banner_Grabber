# Banner Grabber

Prototype Python d'exploration réseau : il teste une liste fixe de ports TCP sur un hôte, puis tente de récupérer une réponse des services accessibles. Ce projet permet d'expérimenter les sockets et les délais réseau.

Cette version est un fork de [Groot-me/Banner_Grabber](https://github.com/Groot-me/Banner_Grabber).

## Fonctionnement

1. Le script tente une connexion TCP sur les ports définis dans `Useful_ports`.
2. Il associe aux ports ouverts les noms figurant dans `Description_ports` : ce sont des étiquettes statiques, pas une identification certaine du service.
3. Il ouvre une nouvelle connexion vers chaque port détecté, envoie `a\r\n\r\n` et tente de lire une réponse.

## Utilisation dans un lab autorisé

Prérequis : Python 3 ; le script utilise uniquement la bibliothèque standard.

1. Ouvrir `ScannerGrabber.py` et remplacer `X.X.X.X` dans `main()` par l'adresse IPv4 ou le nom d'une machine de test autorisée.
2. Adapter au besoin les listes `Useful_ports` et `Description_ports` en conservant la correspondance entre leurs éléments.
3. Lancer :

   ```bash
   python3 ScannerGrabber.py
   ```

L'hôte est actuellement renseigné dans le code : le script ne prend pas encore d'argument en ligne de commande. Le fichier `TCP_PORT.txt` est informatif et n'est pas lu par le script.

## Limites

- Connexions IPv4 et TCP uniquement ; la liste de ports est prédéfinie.
- Le message envoyé est générique : certains services ne répondront pas ou peuvent le rejeter. Les protocoles applicatifs et TLS ne sont pas négociés.
- Les délais sont courts et le script est séquentiel ; un port non détecté n'est pas nécessairement fermé.
- C'est un prototype pédagogique, pas un scanner complet ni un outil de diagnostic de production.

Tester uniquement des systèmes pour lesquels une autorisation explicite a été obtenue : le script établit des connexions et envoie des données aux services détectés.

## Documentation

Cette présentation du projet existant a été clarifiée avec l'assistance de **Codex (OpenAI)**. Le code reste à améliorer et à tester davantage.
