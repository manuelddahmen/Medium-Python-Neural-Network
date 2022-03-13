def jour(date1):  # date est sous la forme 'jj/mm/aaaa'
    jours = ['Dimanche', 'Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi']
    # nombre de jours cumulÃ©s des mois prÃ©cÃ©dents modulo 7
    # sur la base d'une annÃ©e non bissextile
    code_mois = [0, 3, 3, 6, 1, 4, 6, 2, 5, 0, 3, 5]
    # Extraction du jour, mois et annÃ©e de la date 'jj/mm/aaaa'
    j, m, a = date1.split("/")
    j = int(j)
    m = int(m)
    a = int(a)
    # annÃ©e de rÃ©fÃ©rence : 1900
    a = a - 1900
    # eps=1 si l'annÃ©e est bissextile (=0 sinon)
    eps = 1 if (a % 400 == 0 or (a % 4 == 0 and a % 100 != 0)) else 0
    # Calcul du numÃ©ro du jour
    # r=(j%7)+(code_mois[m-1]%7)+((a+a//4)%7)-int(m<=2)*eps
    r = (j + code_mois[m - 1] + (a + a // 4) - int(m <= 2) * eps) % 7
    return jours[r]


if __name__ == "__main__":
    for date1 in ['28/02/2014', '01/03/2014', '31/12/2014', '01/01/2015', '11/03/2022', '13/03/2022']:
        print(date1 + ' : ' + jour(date1))
