from travailJSON import *

def main():
    jsonTravail = jsonWork("testFile/test.json")
    var = 0
    while (var < 18) :
        verifSortie = False
        while verifSortie == False :
            sortieUser = input("1.getContenuJSON\n2.lectureJSON\n3.lectureJSONMultiFlag\n"
                               "4.lectureJSONList\n5.lectureJSONDict\n6.EcritureJSON\n"
                               "7.EcritureJSONList\n8.EcritureJSONDictionnaire\n9.supprJSONDict\n"
                               "10.suppressionJson\n11.suppressionJsonList\n"
                               "12.compteurFlagJSON\n13.supprDictReorg\n14.creerFlagDictionnaire\n"
                               "15.ajouterFlagDict\n16.supprDictByFlag\n17.writeDictOnJson\n"
                               "18.Quit\n$ ")
            verifSortie = sortieUser.isdigit()
        var = int(sortieUser)
        match var :
            case 1 :
                print(jsonTravail.getContenuJSON())
            case 2 :
                print(jsonTravail.lectureJSON("test"))
            case 3 :
                print(jsonTravail.lectureJSONMultiFlag("testM","test1"))
            case 4:
                print(jsonTravail.lectureJSONList("testList"))
            case 5:
                print(jsonTravail.lectureJSON("testM"))
            case 6:
                flag = input("Entrer le flag : ")
                valeur = input("Enter la valeur :")
                jsonTravail.EcritureJSON(flag,valeur)
            case 7:
                flag = input("Entrer le flag : ")
                valeur = input("Enter la valeur :")
                jsonTravail.EcritureJSONList(flag,valeur)
            case 8:
                flag = input("Entrer le flag : ")
                valeur = input("Enter la valeur :")
                jsonTravail.EcritureJSONDictionnaire("testM",flag,valeur)
            case 9:
                flag = input("Entrer le flag : ")
                jsonTravail.supprJSONDict("testM",flag)
            case 10:
                flag = input("Entrer le flag : ")
                jsonTravail.suppressionJson(flag)
            case 11:
                flag = input("Entrer le flag : ")
                valeur = input("Enter la valeur :")
                jsonTravail.suppressionJsonList(flag,valeur)
            case 12:
                print(jsonTravail.compteurFlagJSON())
            case 13:
                flag = input("Entrer le flag : ")
                jsonTravail.supprDictReorg(flag)
            case 14:
                flag = input("Entrer le flag : ")
                jsonTravail.creerFlagDictionnaire(flag)
            case 15:
                flag = input("Entrer le flag : ")
                cles = input("Entrer la cles : ")
                valeur = input("Enter la valeur :")
                jsonTravail.ajouterFlagDict(flag,cles,valeur)
            case 16:
                flag = input("Entrer le flag : ")
                name = input("Entrer le nom : ")
                jsonTravail.supprDictByFlag(flag,name)
            case 17:
                dict = {"a":"b","b":"b","c":"b","d":"b","e":"b","f":"b"}
                jsonTravail.writeDictOnJson(dict)

        if (var != 18):
            input("Press enter")

    print("Au revoir")


if __name__ == "__main__":
    main()