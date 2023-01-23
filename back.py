import sys;
# Hard Coded Values to start out with #
summonerElo = {

        "BUDDA69" : ("Gold", "1", "94"),
        "Sean954" : ("Platinum", "4", "0"),
        "Come2peace" : ("Platinum", "3", "12"),
        "ybsruin" : ("Bronze", "3", "94")

}

def sortElo(eloDict):

    final = {
        
        "BUDDA69" : 0,
        "Sean954" : 0,
        "Come2peace" : 0,
        "ybsruin" : 0
    
    }


    bronzeWeight = 400 
    silverWeight = 800
    goldWeight = 1200
    platWeight = 1600
    diamondWeight = 2000


    for entry in eloDict:


        match eloDict[entry][0]:
            case "Iron":
                final[entry] += int(eloDict[entry][1])*100
                final[entry] += int(eloDict[entry][2])
            case "Bronze":

                final[entry] += bronzeWeight

                match eloDict[entry][1]:
                    case "3":
                        final[entry] += 100
                    case "2":
                        final[entry] += 200
                    case "1":
                        final[entry] += 300

                final[entry] += int(eloDict[entry][2])

            case "Silver":
                final[entry] += silverWeight
                match eloDict[entry][1]:
                    case "3":
                        final[entry] += 100
                    case "2":
                        final[entry] += 200
                    case "1":
                        final[entry] += 300
                final[entry] += int(eloDict[entry][2])                
            case "Gold":
                final[entry] += goldWeight
                match eloDict[entry][1]:
                    case "3":
                        final[entry] += 100
                    case "2":
                        final[entry] += 200
                    case "1":
                        final[entry] += 300
                final[entry] += int(eloDict[entry][2])                
            case "Platinum":
                final[entry] += platWeight
                match eloDict[entry][1]:
                    case "3":
                        final[entry] += 100
                    case "2":
                        final[entry] += 200
                    case "1":
                        final[entry] += 300
                final[entry] += int(eloDict[entry][2])                
            case "Diamond":
                final[entry] += diamondWeight
                match eloDict[entry][1]:
                    case "3":
                        final[entry] += 100
                    case "2":
                        final[entry] += 200
                    case "1":
                        final[entry] += 300
                final[entry] += int(eloDict[entry][2])

    for i in final:
        print(final[i])                

                


sortElo(summonerElo)
