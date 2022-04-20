# Créer un programme qui demandera à l’utilisateur de renseigner un mot et un seul, sans
# espace ni aucun autre caractère que les 26 lettres de l’alphabet (sans accent ni
# majuscule).
# Votre programme devra modifier ce mot, en y changeant de place certains caractères
# (ou tous) afin de donner un mot plus “loin” dans l’ordre alphabétique que le mot
# renseigné par l'utilisateur.
# Attention: Le nouveau mot doit être le mot le plus proche possible, dans l’ordre
# alphabétique, du mot original !
# Par exemple, “abcde” donnerait “abced”. “acedb” est aussi “valide” mais n’est PAS le
# plus proche du mot original dans l’ordre alphabétique.

def triDeMot():
    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

    result = input('ecrivez une suite de lettre')
    temp = ""
    new = ""
    # for letter in range(1,len(result), -1):
    for letter in reversed(result):
    #     print(letter)    
        i = 0
        bool = true
        for alph in alphabet: 
            if letter == alph:

                temp = letter
               #flemme sans internet 
            i += 1
            # new += 
        # print(key + " " + alph)
        # temp = 
        

triDeMot()