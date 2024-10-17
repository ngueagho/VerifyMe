# VerifyMe
projet de cybert-securite

---

# 🎓 (VerifyMe) Système de Vérification d'Identité et du paiment des Étudiant  

![facial_recognition](https://img.shields.io/badge/Reconnaissance-Faciale-green) ![fingerprint](https://img.shields.io/badge/Identification-Empreinte%20Digitale-blue) ![database](https://img.shields.io/badge/Base%20de%20données-PostgreSQL-orange) ![python](https://img.shields.io/badge/Backend-Python%20%7C%20Django-yellow)

## 📖 Description  
Ce projet est un **système de vérification d’identité automatisé** pour les étudiants, combinant la reconnaissance faciale et l'empreinte digitale. Le but est d'authentifier un étudiant et de vérifier s'il est à jour dans ses paiements, avec une **réponse vocale en temps réel**.  

---

## 🎯 Fonctionnalités  
- **Capture d'image** via la webcam.  
- **Identification faciale** avec OpenCV.  
- **Lecture d'empreinte digitale** via un capteur biométrique.  
- **Vérification du statut de paiement** dans PostgreSQL.  
- **Synthèse vocale** avec l'API Web Speech.  
- **Interface d’administration** développée avec Django pour gérer les étudiants.  

---

## 🛠️ Architecture du Système  
1. **Module de Capture d'Image** : Utilise une webcam pour capturer l’image de l’étudiant.  
2. **Module de Reconnaissance Faciale** : Identifie l’étudiant à partir des données préenregistrées.  
3. **Module de Vérification des Empreintes** : Compare les empreintes avec celles en base de données.  
4. **Module de Vérification des Paiements** : Effectue une requête sur PostgreSQL.  
5. **Synthèse Vocale** : Fournit une réponse selon le statut de l’étudiant.  
6. **Interface Django** : Permet de gérer la base d’étudiants et leurs statuts.

---

## ⚙️ Prérequis  
- **Python 3.x**  
- **Django**  
- **PostgreSQL**  
- **OpenCV**  
- **Fingerprint SDK** (du fabricant)  
- **pyttsx3 / gTTS** pour la synthèse vocale

```bash
# Installer les dépendances
pip install django opencv-python-headless psycopg2-binary pyttsx3
```

---

## 🚀 Installation et Lancement  
1. **Cloner le dépôt** :  
```bash
git clone https://github.com/votre-utilisateur/projet-verification-etudiant.git
cd projet-verification-etudiant
```

2. **Configurer PostgreSQL** :  
Crée une base de données avec les champs nécessaires (id, nom, empreinte, paiement).

3. **Lancer le serveur Django** :  
```bash
python manage.py migrate
python manage.py runserver
```

4. **Exécuter le Module de Capture et Reconnaissance Faciale** :  
```bash
python modules/recognition.py
```

---

## 🧪 Tests et Validation  
- **Tests Unitaires** : Vérification individuelle de chaque module (reconnaissance faciale, empreintes, synthèse vocale).  
- **Scénarios Réels** : Simulation avec plusieurs étudiants pour tester l’exactitude du système.  

---

## 🛠️ Répartition des Tâches  
- **Membre 1** : Capture d’image et Reconnaissance Faciale  
- **Membre 2** : Capture et Vérification d’Empreintes Digitales  
- **Membre 3** : Base de données, Génération Vocale, et Intégration  

---

## 📚 Documentation et Maintenance  
- Prévoir une **documentation détaillée** pour chaque module.  
- Planifier des **mises à jour régulières** pour la base de données et le logiciel de reconnaissance.  

---

## 🎨 Design  
- **Couleurs Utilisées** : Bleu, Noir, Blanc et Orange pour une interface moderne et intuitive.  
- **Interface Django** : Gestion simple des utilisateurs avec des notifications d’état de paiement.

---

## 📞 Contact  
- Suivez l’avancement du projet sur [LinkedIn](https://www.linkedin.com/in/roberto-landry-ngueagho-tiodong-7a0989223/)  
- Pour toute question, contactez-nous à : support@projet-verification.com  

---

## 📝 Licence  
Ce projet est sous licence MIT. Consultez le fichier [LICENSE](LICENSE) pour plus d'informations.

---

## 📷 Aperçu  
![Aperçu Interface](https://via.placeholder.com/800x400?text=Interface+de+Capture+et+Paiement)

---

## ⭐ Contributions  
Les contributions sont les bienvenues ! Veuillez lire le fichier [CONTRIBUTING.md](CONTRIBUTING.md) pour plus de détails.

---

