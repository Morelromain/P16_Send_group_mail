import pyodbc


def display_nb_line_SQL():
    """ Recuperation du nombre de ligne total à traité """

    baseDeDonnees = pyodbc.connect('DRIVER={SQL Server};SERVER=srvsql\HVUP00; DATABASE=hvup00; Trusted_Connection=yes;' )
    cursor = baseDeDonnees.cursor()
    cursor.execute("SELECT [NOM], [CODE_SEXE], [mail] FROM [hvup00].[hvup00].[Effectifs_MHV] WHERE TYPE_ASS = 'ASSPRI' AND mail <> '' AND DATE_RAD = '' GROUP BY [NOM], [CODE_SEXE], [mail]")
    count_line = cursor.fetchall()
    return str(len(count_line))


def recup_SQL(ligne_depart, nombre_ligne):
    """ Recuperation donnee sous forme liste d'une requete SQL """

    baseDeDonnees = pyodbc.connect('DRIVER={SQL Server};SERVER=srvsql\HVUP00; DATABASE=hvup00; Trusted_Connection=yes;' )
    cursor = baseDeDonnees.cursor()

    # Récupère une plage de mails
    cursor.execute("SELECT [NOM], [CODE_SEXE], [mail] \
        FROM [hvup00].[hvup00].[Effectifs_MHV] \
            WHERE TYPE_ASS = 'ASSPRI' AND mail <> '' AND DATE_RAD = '' \
                GROUP BY [NOM], [CODE_SEXE], [mail] \
                    ORDER BY [NOM], [CODE_SEXE], [mail] \
                        OFFSET "+ligne_depart+" ROWS FETCH NEXT "+nombre_ligne+" ROWS ONLY") 

    liste_b = cursor.fetchall()
    return [line for line in liste_b]
