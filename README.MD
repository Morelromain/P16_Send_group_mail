# Send_Group_Mail

Programme d'automatisation d'envoi de mail en masse

## 1. configuration fichier smtp.config

configuration de l'envoi de mail par le fichier smtp.config dans auto_group_mail  

Exemple :  
[MAIL]  
mssg_add: adresse_visible@domaine.fr  
real_add: adresse_envoi@domaine.fr  
sender_pass: Mdp 
session: smtp.office365.com  
session_port: 587  

## 2. configuration fichier main  

### Création du mail

Modification du titre et du corp du mail

### Ligne SQL / mails envoyés

Choisi la ligne SQL de départ et le nombre de lignes selectionnées

### Envoi mail

Configurer de base sur liste_test, remplacer par liste_GO pour envoyer vraiment mail

## 3. configuration Base de donnée SQL SERVER  

Information adresse récupéré dans une base de donnée SQL SERVER, sous forme :  
`NOM;PRENOM;EMAIL`  
Information de connection à votre base de donnée à adapter dans SQL_to_list.py

### Ligne SQL / mails envoyés

Choisi la ligne SQL de départ et le nombre de lignes selectionnées

### Envoi mail

Configurer de base sur liste_test, remplacer par liste_GO pour envoyer vraiment mail

## 4. Utilisation auto_group_mail

Creer un environnement virtuel:  
`python -m venv env`  

Activer cet environnement virtuel:  
`env/Scripts/activate.bat`  

Configuration environnement virtuel:  
`pip install -r requirements.txt`  

rentrer dans auto_group_mail  
`cd auto_group_mail`  

lancer auto_group_mail  
`python send_group_mail` 