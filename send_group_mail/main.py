from send_mail import send_mail
from SQL_to_list import recup_SQL, display_nb_line_SQL
from datetime import datetime


def lancement():

    # Création de liste de test :
    liste_test = [('MOREL        ', 'M', 'romain.morel@mhv86.fr      ')]
    liste_test2 = [('MOREL', 'M', 'romain.morel@mhv86.fr'), ('ITMHV', 'M', 'it.mhv@mhv86.fr')]
    liste_test3 = [('MEMIN', 'M', 'frederic.memin@mhv86.fr')]

    # Création du mail
    titre_mail = "Mutuelle actualités n°74"
    corp_mail = "<br> Nous avons le plaisir de vous adresser votre nouveau <br>« Mutuelle Actualités ».<br>\
        Pour en prendre connaissance, <a href='https://www.mhv.fr/files/pack/contenu/PDF/mhv74.pdf'> cliquez ici </a>  <br> <br>\
            Bonne lecture ! "

    # ligne SQL / mails envoyés
    ligne_depart = "0"
    nombre_ligne = "50"

    # Envoie mail
    print("Debut à : "+str(datetime.today().strftime('%Hh%Mm%Ss')))
    nb_line = display_nb_line_SQL()
    print("nombre de ligne total : " + nb_line)
    liste_GO = recup_SQL(ligne_depart, nombre_ligne)
    send_mail(liste_test, titre_mail, corp_mail)
    print("Fin à : "+str(datetime.today().strftime('%Hh%Mm%Ss')))
