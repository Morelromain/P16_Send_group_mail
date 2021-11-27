import smtplib
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
import time
import configparser

from prototype_mail import prototype


def send_mail(liste_all, titre_mail, corp_mail):
    """ Envoi mail à chaque contact de la liste """
    
    config = configparser.RawConfigParser()
    config.read('smtp.config')
    conf_mssg_add = config.get('MAIL','mssg_add')
    conf_real_add = config.get('MAIL','real_add')
    conf_sender_pass = config.get('MAIL','sender_pass')
    conf_session = config.get('MAIL','session')
    conf_session_port = config.get('MAIL','session_port')
    conf_session_port_nb = int(conf_session_port)

    for count, contact in enumerate(liste_all, start=1):
        if count%50 == 0:
            print(str(count)+ " mails envoyés")
            time.sleep(2) 

        try:
            #CREATION DES VARIABLES CONTACT
            nom = contact[0].rstrip()
            if contact[1] == 'F':
                sexe = "Madame"
            elif contact[1] == 'M':
                sexe = "Monsieur"
            else :
                sexe = ""
            adresse = contact[2].rstrip()

            #CONFIGURATION MAIL
            strTo = adresse
            msgRoot = MIMEMultipart('related')
            msgRoot['Subject'] = 'Mutuelle actualités'
            msgRoot['From'] = conf_mssg_add
            msgRoot['To'] = strTo
            msgRoot.preamble = 'Multi-part message in MIME format.'
            msgAlternative = MIMEMultipart('alternative')
            msgRoot.attach(msgAlternative)
            msgText = MIMEText('Alternative plain text message.')
            msgAlternative.attach(msgText)

            #STYLE ET CORP DU MAIL
            corp = prototype(nom, sexe, corp_mail)

            # AJOUT IMAGE DANS CORP MAIL
            msgText = MIMEText(corp, 'html')
            msgAlternative.attach(msgText)
            with open('pied_mail.png', 'rb') as fp:
                msgImage = MIMEImage(fp.read())
            msgImage.add_header('Content-ID', '<image1>')
            msgRoot.attach(msgImage)

            msgText1 = MIMEText(corp, 'html')
            msgAlternative.attach(msgText1)
            with open('actu_titre.png', 'rb') as fp2:
                msgImage2 = MIMEImage(fp2.read())
            msgImage2.add_header('Content-ID', '<image2>')
            msgRoot.attach(msgImage2)

            # FICHIER JOIN
            # part = MIMEBase('application', "octet-stream")
            # part.set_payload(open(fichier_joint, "rb").read())
            # encoders.encode_base64(part)
            # part.add_header('Content-Disposition', 'attachment; filename='+fichier_joint+'')
            # msgRoot.attach(part)

            # CONFIGURATION ENVOI MAIL
            session = smtplib.SMTP(conf_session, conf_session_port_nb)
            session.starttls()
            session.login(conf_real_add, conf_sender_pass)
            text = msgRoot.as_string()
            toaddrs = [strTo ] 
            session.sendmail(conf_real_add, toaddrs, text)
            session.quit()

        except Exception as e:
            print("error"+ str(e))
