from travailJSON import *

def main():
    jsonTravail = jsonWork("testFile/test.json")
    var = 0
    while (var < 19) :
        verifSortie = False
        while verifSortie == False :
            sortieUser = input("1.getContenuJSON\n2.lectureJSON\n3.lectureJSONMultiFlag\n"
                               "4.lectureJSONList\n5.lectureJSONDict\n6.EcritureJSON\n"
                               "7.EcritureJSONList\n8.EcritureJSONDictionnaire\n9.supprJSONList\n"
                               "10.suppressionJson\n11.uppressionJsonList\n12.dictJson\n"
                               "13.ompteurFlagJSON\n14.supprDictReorg\n15.creerFlagDictionnaire\n"
                               "16.ajouterFlagDict\n17.supprDictByFlag\n18.writeDictOnJson\n"
                               "19.Quit\n$ ")
            verifSortie = sortieUser.isdigit()
        var = int(sortieUser)
        match var :
            case 1 :
                jsonTravail
            case 2 :
                jsonTravail
            case 3 :
                jsonTravail
            case 4:
                jsonTravail
            case 5:
                jsonTravail
            case 6:
                jsonTravail
            case 7:
                jsonTravail
            case 8:
                jsonTravail
            case 9:
                jsonTravail
            case 10:
                jsonTravail
            case 11:
                jsonTravail
            case 12:
                jsonTravail
            case 13:
                jsonTravail
            case 14:
                jsonTravail
            case 15:
                jsonTravail
            case 16:
                jsonTravail
            case 17:
                jsonTravail
            case 18:
                jsonTravail

    print("Au revoir")


if __name__ == "__main__":
    main()